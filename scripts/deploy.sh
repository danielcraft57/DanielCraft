#!/bin/bash

# Script de déploiement pour DanielCraft V6
# Usage: ./deploy.sh [domaine]

set -e  # Arrêter en cas d'erreur

# Couleurs pour les messages
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Configuration
SERVER_USER="pi"
SERVER_HOST="node12.lan"
SERVER_PATH="/var/www/danielcraft.fr"
NGINX_SITES_AVAILABLE="/etc/nginx/sites-available"
NGINX_SITES_ENABLED="/etc/nginx/sites-enabled"
CONFIG_NAME="danielcraft.fr"
DOMAIN=""

# Vérifier si un domaine est passé en argument
if [ -z "$1" ]; then
    echo -e "${RED}Erreur: Nom de domaine requis${NC}"
    echo "Usage: ./deploy.sh ton-domaine.com"
    exit 1
fi

DOMAIN="$1"

echo -e "${GREEN}=== Déploiement DanielCraft V6 ===${NC}"
echo -e "Domaine: ${YELLOW}${DOMAIN}${NC}"
echo -e "Serveur: ${YELLOW}${SERVER_USER}@${SERVER_HOST}${NC}"
echo ""

# 1. Vérifier que nous sommes dans le bon répertoire
if [ ! -f "index.html" ]; then
    echo -e "${RED}Erreur: index.html non trouvé. Exécute ce script depuis le dossier V6.${NC}"
    exit 1
fi

# 2. Créer le répertoire sur le serveur si nécessaire
echo -e "${YELLOW}[1/6]${NC} Création du répertoire sur le serveur..."
ssh ${SERVER_USER}@${SERVER_HOST} "sudo mkdir -p ${SERVER_PATH} && sudo chown -R ${SERVER_USER}:www-data ${SERVER_PATH} && sudo chmod -R 755 ${SERVER_PATH}"

# 3. Transférer les fichiers
echo -e "${YELLOW}[2/6]${NC} Transfert des fichiers..."
rsync -avz --delete \
    --exclude 'node_modules' \
    --exclude '.git' \
    --exclude 'docs' \
    --exclude 'scripts' \
    --exclude 'src' \
    --exclude 'build.py' \
    --exclude '.gitignore' \
    --exclude 'README.md' \
    ./ ${SERVER_USER}@${SERVER_HOST}:${SERVER_PATH}/

# 4. Configurer les permissions (CRITIQUE pour nginx/www-data)
echo -e "${YELLOW}[3/6]${NC} Configuration des permissions (chown/chmod pour www-data)..."
ssh ${SERVER_USER}@${SERVER_HOST} "
    # Propriétaire : pi (pour pouvoir modifier), groupe : www-data (pour que nginx puisse lire)
    sudo chown -R ${SERVER_USER}:www-data ${SERVER_PATH}
    
    # Permissions : répertoires 755 (rwxr-xr-x), fichiers 644 (rw-r--r--)
    sudo find ${SERVER_PATH} -type d -exec chmod 755 {} \;
    sudo find ${SERVER_PATH} -type f -exec chmod 644 {} \;
    
    # Vérifier que nginx peut lire les fichiers
    sudo -u www-data test -r ${SERVER_PATH}/index.html && echo 'Permissions OK' || echo 'ERREUR: nginx ne peut pas lire les fichiers'
"

# 5. Préparer la config nginx
echo -e "${YELLOW}[4/6]${NC} Préparation de la configuration nginx..."
# Créer un fichier temporaire compatible Windows/Linux
TMP_FILE=$(mktemp 2>/dev/null || echo "./nginx-${CONFIG_NAME}.tmp.conf")

# Vérifier si les certificats SSL existent déjà
CERT_EXISTS=$(ssh ${SERVER_USER}@${SERVER_HOST} "test -f /etc/letsencrypt/live/${DOMAIN}/fullchain.pem && echo 'yes' || echo 'no'")

if [ "$CERT_EXISTS" = "yes" ]; then
    echo -e "${GREEN}Certificats SSL trouvés, utilisation de la config complète${NC}"
    # Copier nginx.conf avec SSL (déjà configuré pour danielcraft.fr)
    cp nginx.conf "${TMP_FILE}"
else
    echo -e "${YELLOW}Certificats SSL non trouvés, utilisation de la config sans SSL${NC}"
    echo -e "${YELLOW}Certbot ajoutera automatiquement le bloc SSL après création${NC}"
    # Copier nginx.conf sans SSL (pour permettre à Certbot de créer les certificats)
    cp nginx.conf.no-ssl "${TMP_FILE}"
fi

# Transférer la config sur le serveur
scp "${TMP_FILE}" ${SERVER_USER}@${SERVER_HOST}:/tmp/nginx-${CONFIG_NAME}.conf

# Installer la config
ssh ${SERVER_USER}@${SERVER_HOST} "sudo mv /tmp/nginx-${CONFIG_NAME}.conf ${NGINX_SITES_AVAILABLE}/${CONFIG_NAME}"

# Nettoyer le fichier temporaire local
rm -f "${TMP_FILE}"

# 6. Activer la configuration nginx
echo -e "${YELLOW}[5/6]${NC} Activation de la configuration nginx..."

# Créer le lien symbolique s'il n'existe pas
ssh ${SERVER_USER}@${SERVER_HOST} "if [ ! -L ${NGINX_SITES_ENABLED}/${CONFIG_NAME} ]; then sudo ln -s ${NGINX_SITES_AVAILABLE}/${CONFIG_NAME} ${NGINX_SITES_ENABLED}/${CONFIG_NAME}; echo 'Lien symbolique cree'; else echo 'Lien symbolique existe deja'; fi"

# Tester la configuration nginx
echo "Test de la configuration nginx..."
ssh ${SERVER_USER}@${SERVER_HOST} "sudo nginx -t"

NGINX_TEST_RESULT=$?
if [ $NGINX_TEST_RESULT -ne 0 ]; then
    echo -e "${RED}Erreur dans la configuration nginx.${NC}"
    echo -e "${YELLOW}Diagnostic des ports 80/443...${NC}"
    ssh ${SERVER_USER}@${SERVER_HOST} "echo '=== Port 80 ==='; sudo lsof -i:80 2>/dev/null || echo 'Libre'; echo ''; echo '=== Port 443 ==='; sudo lsof -i:443 2>/dev/null || echo 'Libre'; echo ''; echo '=== Sites actives ==='; ls -la ${NGINX_SITES_ENABLED}/"
    echo -e "${YELLOW}Note: Si les ports sont utilises par nginx lui-meme, c est normal.${NC}"
    echo -e "${YELLOW}Le probleme vient probablement d une configuration invalide. Verifie les logs ci-dessus.${NC}"
    exit 1
fi

# 7. Obtenir le certificat SSL avec Certbot
echo -e "${YELLOW}[6/6]${NC} Configuration du certificat SSL..."

# Si on a utilisé la config sans SSL, maintenant on peut créer les certificats
if [ "$CERT_EXISTS" = "no" ]; then
    echo -e "${YELLOW}Note:${NC} Certificats SSL non trouvés, Certbot va les créer."
    echo -e "${YELLOW}Note:${NC} Assure-toi que le DNS pointe vers ce serveur avant de continuer."
    
    read -p "Le DNS est-il configuré pour ${DOMAIN} ? (o/N) " -n 1 -r
    echo
    if [[ $REPLY =~ ^[Oo]$ ]]; then
        echo -e "${YELLOW}Création des certificats SSL avec Certbot...${NC}"
        ssh ${SERVER_USER}@${SERVER_HOST} "sudo certbot --nginx -d ${DOMAIN} -d www.${DOMAIN} --non-interactive --agree-tos --email loic5488@gmail.com --redirect"
    
        if [ $? -eq 0 ]; then
            echo -e "${GREEN}Certificat SSL configuré avec succès !${NC}"
            # Après création des certificats, on peut restaurer la config complète si souhaité
            echo -e "${YELLOW}Certbot a automatiquement configuré SSL. La config est prête !${NC}"
        else
            echo -e "${YELLOW}Attention: Erreur lors de la configuration du certificat SSL.${NC}"
            echo -e "${YELLOW}Vérifie que le DNS pointe bien vers ce serveur.${NC}"
            echo -e "${YELLOW}Tu peux réessayer manuellement avec:${NC}"
            echo "ssh ${SERVER_USER}@${SERVER_HOST} 'sudo certbot --nginx -d ${DOMAIN} -d www.${DOMAIN}'"
        fi
    else
        echo -e "${YELLOW}Configuration SSL ignorée. Configure le DNS puis exécute:${NC}"
        echo "ssh ${SERVER_USER}@${SERVER_HOST} 'sudo certbot --nginx -d ${DOMAIN} -d www.${DOMAIN}'"
    fi
else
    echo -e "${GREEN}Certificats SSL déjà présents, configuration OK.${NC}"
fi

# 8. Vérifier les permissions une dernière fois et recharger nginx
echo -e "${YELLOW}[Finalisation]${NC} Verification finale des permissions et rechargement de nginx..."

# S'assurer que les permissions sont correctes
ssh ${SERVER_USER}@${SERVER_HOST} "sudo chown -R ${SERVER_USER}:www-data ${SERVER_PATH}; sudo find ${SERVER_PATH} -type d -exec chmod 755 {} \; ; sudo find ${SERVER_PATH} -type f -exec chmod 644 {} \;"

# Recharger nginx et vérifier
ssh ${SERVER_USER}@${SERVER_HOST} "
    sudo systemctl reload nginx
    sleep 1
    if sudo systemctl is-active --quiet nginx; then
        echo 'OK: Nginx est actif et fonctionne correctement'
    else
        echo 'ERREUR: Nginx n est pas actif'
        sudo journalctl -u nginx -n 20 --no-pager
        exit 1
    fi
"

echo ""
echo -e "${GREEN}=== Déploiement terminé avec succès ! ===${NC}"
echo -e "Site disponible sur: ${GREEN}https://${DOMAIN}${NC}"
echo ""
echo -e "${YELLOW}Pour vérifier les logs:${NC}"
echo "ssh ${SERVER_USER}@${SERVER_HOST} 'sudo tail -f /var/log/nginx/${CONFIG_NAME}-error.log'"

