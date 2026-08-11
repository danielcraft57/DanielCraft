#!/usr/bin/env bash
# shellcheck shell=bash
# Déploiement auto DanielCraft : clone git -> tests -> build -> rsync vers le webroot.
# Le site en prod (/var/www/...) n'est PAS un dépôt git ; seul REPO_DIR l'est.
#
# Usage (sur le serveur) :
#   ./scripts/prod-auto-deploy.sh              # déploie si origin/master a avancé
#   FORCE_DEPLOY=1 ./scripts/prod-auto-deploy.sh   # force build + rsync
#
# Variables optionnelles : REPO_DIR, WEB_ROOT, GIT_REMOTE, GIT_BRANCH, SITE_BASE, LOG_FILE

set -euo pipefail

REPO_DIR="${REPO_DIR:-/home/pi/danielcraft-src}"
WEB_ROOT="${WEB_ROOT:-/var/www/danielcraft.fr}"
GIT_REMOTE="${GIT_REMOTE:-https://github.com/danielcraft57/DanielCraft.git}"
GIT_BRANCH="${GIT_BRANCH:-master}"
SITE_BASE="${SITE_BASE:-https://danielcraft.fr}"
LOG_FILE="${LOG_FILE:-/home/pi/logs/danielcraft-deploy.log}"
LOCK_FILE="/tmp/danielcraft-deploy.lock"
FORCE_DEPLOY="${FORCE_DEPLOY:-0}"

mkdir -p "$(dirname "$LOG_FILE")"

log() {
  echo "[$(date -Iseconds)] $*" | tee -a "$LOG_FILE"
}

fail() {
  log "ERREUR: $*"
  exit 1
}

exec 200>"$LOCK_FILE"
if ! flock -n 200; then
  log "Déploiement déjà en cours — abandon."
  exit 0
fi

if [ ! -d "$WEB_ROOT" ]; then
  fail "Webroot introuvable : $WEB_ROOT"
fi

if [ ! -d "$REPO_DIR/.git" ]; then
  log "Clone initial dans $REPO_DIR"
  git clone --branch "$GIT_BRANCH" "$GIT_REMOTE" "$REPO_DIR"
fi

cd "$REPO_DIR"

# Secrets prod : jamais dans git, toujours lus depuis le webroot
if [ -f "$WEB_ROOT/.env" ]; then
  ln -sfn "$WEB_ROOT/.env" "$REPO_DIR/.env"
elif [ ! -f "$REPO_DIR/.env" ]; then
  log "ATTENTION: pas de .env dans $WEB_ROOT — build sans secrets API"
fi

git fetch origin "$GIT_BRANCH"
LOCAL="$(git rev-parse HEAD)"
REMOTE="$(git rev-parse "origin/$GIT_BRANCH")"

if [ "$LOCAL" = "$REMOTE" ] && [ "$FORCE_DEPLOY" != "1" ]; then
  log "Déjà à jour ($LOCAL)"
  exit 0
fi

if [ "$LOCAL" != "$REMOTE" ]; then
  log "Mise à jour git $LOCAL -> $REMOTE"
  git pull --ff-only origin "$GIT_BRANCH"
fi

COMPOSER="$REPO_DIR/bin/composer.phar"
if [ ! -f "$COMPOSER" ]; then
  log "Installation de Composer..."
  mkdir -p "$REPO_DIR/bin"
  curl -fsSL https://getcomposer.org/installer | php -- --install-dir="$REPO_DIR/bin" --filename=composer.phar
fi

log "Dépendances PHP..."
php "$COMPOSER" install --no-interaction --prefer-dist --no-progress --no-ansi

log "Vérification syntaxe PHP..."
find api -name '*.php' -print0 | xargs -0 -n1 php -l >/dev/null

log "Tests PHP..."
php vendor/bin/phpunit --testsuite php --colors=never

VENV="$REPO_DIR/.venv"
if [ ! -d "$VENV" ]; then
  log "Création venv Python..."
  python3 -m venv "$VENV"
fi
# shellcheck disable=SC1091
source "$VENV/bin/activate"
pip install -q -r blog/requirements.txt

log "Tests Python..."
python -m unittest discover -s tests -p 'test_*.py' -v

log "Build SITE_BASE=$SITE_BASE"
export SITE_BASE
python build.py --no-webp

test -f dist/index.html || fail "dist/index.html manquant"
test -f dist/api/send-contact.php || fail "dist/api/send-contact.php manquant"
grep -q '"price_eur": 199' dist/data/audits.json || fail "audits.json invalide"

log "Rsync vers $WEB_ROOT ( .env préservé )..."
# livres-formation/pdf : hors dist, ne pas supprimer (fulfillment livres)
# .well-known / assets email BIMI : parfois root-owned, eviter delete en erreur
rsync -av --delete \
  --exclude '.env' \
  --exclude 'api/.env' \
  --exclude 'livres-formation/' \
  --exclude '.well-known/' \
  --exclude 'assets/icons/mail/' \
  --exclude 'assets/images/email/' \
  dist/ "$WEB_ROOT/"

find "$WEB_ROOT" -type d -exec chmod 755 {} \;
find "$WEB_ROOT" -type f -exec chmod 644 {} \;

log "Déploiement terminé ($(git rev-parse --short HEAD))"
