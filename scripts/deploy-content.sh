#!/bin/bash
# Script Bash de déploiement CONTENU UNIQUEMENT
# Ne touche PAS à nginx, SSL, ou configuration serveur
# Usage: ./scripts/deploy-content.sh

# Configuration (anonymisee)
# Surcharge possible via variables d'environnement:
#   SERVER_USER, SERVER_HOST, SERVER_PATH, SITE_BASE
SERVER_USER="${SERVER_USER:-deploy}"
SERVER_HOST="${SERVER_HOST:-server.local}"
SERVER_PATH="${SERVER_PATH:-/var/www/example.com}"
SITE_BASE="${SITE_BASE:-https://example.com}"

# Couleurs
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

echo -e "${GREEN}=== Deploiement CONTENU - DanielCraft V6 ===${NC}"
echo -e "${YELLOW}Serveur: ${SERVER_USER}@${SERVER_HOST}${NC}"
echo -e "${YELLOW}Chemin: ${SERVER_PATH}${NC}"
echo ""

# 1. Vérifier que nous sommes dans le bon répertoire (racine du repo)
if [ ! -f "build.py" ]; then
    echo -e "${RED}Erreur: build.py non trouvé. Exécute ce script depuis la racine du projet.${NC}"
    exit 1
fi

# 1.5. Build local dans dist/ (inclut pages + blog + sitemaps)
echo -e "${YELLOW}[0/4]${NC} Build du site dans dist/..."
export SITE_BASE

PYTHON_CMD="${PYTHON_CMD:-python3}"
if ! command -v "$PYTHON_CMD" >/dev/null 2>&1; then
  if command -v python >/dev/null 2>&1; then
    PYTHON_CMD="python"
  fi
fi

"$PYTHON_CMD" build.py

DIST_DIR="dist"
if [ ! -f "${DIST_DIR}/index.html" ]; then
    echo -e "${RED}Erreur: ${DIST_DIR}/index.html manquant. Le build a peut-être échoué.${NC}"
    exit 1
fi

echo -e "${GREEN}Build terminé. Déploiement depuis ${DIST_DIR}/...${NC}"

# 2. Lister les fichiers à déployer
echo -e "${YELLOW}[1/4] Verification des fichiers locaux...${NC}"
FILES_TO_DEPLOY=(
    "${DIST_DIR}/index.html"
    "${DIST_DIR}/processus.html"
    "${DIST_DIR}/metz.html"
    "${DIST_DIR}/portfolio.html"
    "${DIST_DIR}/projets.html"
    "${DIST_DIR}/statistiques.html"
    "${DIST_DIR}/mentions-legales.html"
    "${DIST_DIR}/cgv.html"
    "${DIST_DIR}/cgu.html"
    "${DIST_DIR}/politique-confidentialite.html"
    "${DIST_DIR}/robots.txt"
    "${DIST_DIR}/sitemap.xml"
    "${DIST_DIR}/sitemap-pages.xml"
    "${DIST_DIR}/assets"
    "${DIST_DIR}/api"
    "${DIST_DIR}/blog"
    "${DIST_DIR}/projets"
)

MISSING_FILES=()
for file in "${FILES_TO_DEPLOY[@]}"; do
    if [ ! -e "$file" ]; then
        MISSING_FILES+=("$file")
    fi
done

if [ ${#MISSING_FILES[@]} -gt 0 ]; then
    echo -e "${YELLOW}Attention: Fichiers manquants:${NC}"
    for file in "${MISSING_FILES[@]}"; do
        echo "  - $file"
    done
    read -p "Continuer quand meme ? (o/N) " response
    if [[ ! "$response" =~ ^[Oo]$ ]]; then
        exit 1
    fi
fi

# 3. Créer le répertoire sur le serveur si nécessaire
echo -e "${YELLOW}[2/4] Creation du repertoire sur le serveur (si necessaire)...${NC}"
ssh "${SERVER_USER}@${SERVER_HOST}" "mkdir -p $SERVER_PATH && mkdir -p $SERVER_PATH/assets && mkdir -p $SERVER_PATH/api && mkdir -p $SERVER_PATH/blog && mkdir -p $SERVER_PATH/projets"
if [ $? -eq 0 ]; then
    echo -e "${GREEN}Repertoire cree/verifie${NC}"
else
    echo -e "${RED}Erreur lors de la creation du repertoire${NC}"
    exit 1
fi

# 4. Transférer les fichiers avec rsync (ou scp en fallback)
echo -e "${YELLOW}[3/4] Transfert des fichiers...${NC}"

# Vérifier si rsync est disponible
if command -v rsync &> /dev/null; then
    echo -e "${YELLOW}Utilisation de rsync (transfert optimise)...${NC}"

    rsync -avz --delete \
        "${DIST_DIR}/" "${SERVER_USER}@${SERVER_HOST}:${SERVER_PATH}/"
    
    if [ $? -eq 0 ]; then
        echo -e "${GREEN}Transfert rsync reussi${NC}"
    else
        echo -e "${RED}Erreur lors du transfert rsync${NC}"
        exit 1
    fi
else
    echo -e "${YELLOW}rsync non trouve, utilisation de scp (plus lent)...${NC}"
    
    # Transfert fichier par fichier avec scp
    HTML_FILES=(
        "index.html" 
        "processus.html" 
        "metz.html" 
        "portfolio.html" 
        "projets.html" 
        "statistiques.html"
        "mentions-legales.html"
        "cgv.html"
        "cgu.html"
        "politique-confidentialite.html"
    )
    OTHER_FILES=("robots.txt" "sitemap.xml" "sitemap-pages.xml")
    
    for file in "${HTML_FILES[@]}"; do
        if [ -f "${DIST_DIR}/${file}" ]; then
            echo "  Transfert: $file"
            scp "${DIST_DIR}/${file}" "${SERVER_USER}@${SERVER_HOST}:${SERVER_PATH}/"
        fi
    done
    
    for file in "${OTHER_FILES[@]}"; do
        if [ -f "${DIST_DIR}/${file}" ]; then
            echo "  Transfert: $file"
            scp "${DIST_DIR}/${file}" "${SERVER_USER}@${SERVER_HOST}:${SERVER_PATH}/"
        fi
    done
    
    # Transfert du dossier assets
    if [ -d "${DIST_DIR}/assets" ]; then
        echo "  Transfert: assets/ (peut prendre du temps...)"
        scp -r "${DIST_DIR}/assets" "${SERVER_USER}@${SERVER_HOST}:${SERVER_PATH}/"
    fi

    # Transfert du dossier api (formulaire contact PHP)
    if [ -d "${DIST_DIR}/api" ]; then
        echo "  Transfert: api/"
        scp -r "${DIST_DIR}/api" "${SERVER_USER}@${SERVER_HOST}:${SERVER_PATH}/"
    fi

    # Transfert du blog
    if [ -d "${DIST_DIR}/blog" ]; then
        echo "  Transfert: blog/"
        scp -r "${DIST_DIR}/blog" "${SERVER_USER}@${SERVER_HOST}:${SERVER_PATH}/"
    fi

    # Transfert des pages projet (projets/<slug>.html)
    if [ -d "${DIST_DIR}/projets" ]; then
        echo "  Transfert: projets/"
        scp -r "${DIST_DIR}/projets" "${SERVER_USER}@${SERVER_HOST}:${SERVER_PATH}/"
    fi
    
    echo -e "${GREEN}Transfert scp termine${NC}"
fi

# 5. Configurer les permissions (sans sudo, juste les permissions de base)
echo -e "${YELLOW}[4/4] Configuration des permissions...${NC}"
ssh "${SERVER_USER}@${SERVER_HOST}" "chmod -R 755 $SERVER_PATH && find $SERVER_PATH -type f -exec chmod 644 {} \; && find $SERVER_PATH -type d -exec chmod 755 {} \;"
if [ $? -eq 0 ]; then
    echo -e "${GREEN}Permissions configurees${NC}"
else
    echo -e "${YELLOW}Attention: Erreur lors de la configuration des permissions${NC}"
    echo -e "${YELLOW}Si nginx ne peut pas lire les fichiers, execute manuellement:${NC}"
    echo "ssh ${SERVER_USER}@${SERVER_HOST} 'sudo chown -R ${SERVER_USER}:www-data $SERVER_PATH && sudo chmod -R 755 $SERVER_PATH'"
fi

# 6. Vérification finale
echo ""
echo -e "${YELLOW}=== Verification finale ===${NC}"

# Vérifier que index.html est accessible
ssh "${SERVER_USER}@${SERVER_HOST}" "test -f $SERVER_PATH/index.html && echo 'OK: index.html present' || echo 'ERREUR: index.html manquant'"

# Vérifier que api/send-contact.php est présent (formulaire contact)
ssh "${SERVER_USER}@${SERVER_HOST}" "test -f $SERVER_PATH/api/send-contact.php && echo 'OK: api/send-contact.php present' || echo 'ATTENTION: api/send-contact.php manquant (formulaire contact)'"

# Vérifier que le blog est déployé
ssh "${SERVER_USER}@${SERVER_HOST}" "test -f $SERVER_PATH/blog/index.html && echo 'OK: blog/index.html present' || echo 'ATTENTION: blog/index.html manquant'"

# Vérifier que les pages projet sont déployées
ssh "${SERVER_USER}@${SERVER_HOST}" "test -d $SERVER_PATH/projets && echo 'OK: projets/ present' || echo 'ATTENTION: projets/ manquant'"

# Lister les fichiers déployés
FILE_COUNT=$(ssh "${SERVER_USER}@${SERVER_HOST}" "ls -lh $SERVER_PATH/*.html 2>/dev/null | wc -l")
echo "Fichiers HTML deployes: $FILE_COUNT"

echo ""
echo -e "${GREEN}=== Deploiement contenu termine ! ===${NC}"
echo -e "${GREEN}Les fichiers ont ete transferes sur le serveur.${NC}"
echo ""
echo -e "${YELLOW}Note: Ce script ne touche PAS a nginx.${NC}"
echo -e "${YELLOW}Si tu veux recharger nginx (sans modifier la config):${NC}"
echo "ssh ${SERVER_USER}@${SERVER_HOST} 'sudo systemctl reload nginx'"
echo ""
echo -e "${YELLOW}Pour verifier les logs d'erreur nginx:${NC}"
NGINX_LOG_NAME="${NGINX_LOG_NAME:-example.com}"
echo "ssh ${SERVER_USER}@${SERVER_HOST} 'sudo tail -f /var/log/nginx/${NGINX_LOG_NAME}-error.log'"

