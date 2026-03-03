---
title: "Installer Docker correctement sur ta machine de dev"
date: 2025-12-07
excerpt: "Installer Docker Desktop ou Docker Engine sans te tirer une balle dans le pied : Linux, macOS, Windows/WSL, droits sudo et premiers réglages utiles."
type: article
tags: [Docker, installation, Linux, WSL, macOS]
series: docker-serie
series_order: 2
og_image: docker-installation-1200x630.jpg
---

# Installer Docker correctement sur ta machine de dev

Avant de jouer avec les conteneurs, il faut une base propre. Une mauvaise install de Docker, c'est des bugs bizarres, des permissions qui bloquent tout, ou un WSL qui hurle.

Voyons une installation **simple et propre** sur les trois cas principaux : Linux, macOS, Windows (WSL).

---

## Linux (Ubuntu, Debian, etc.)

Sur un poste Linux, le plus sain est d'installer **Docker Engine** directement, sans Docker Desktop.

### Installation rapide (Ubuntu/Debian)

```bash
sudo apt update
sudo apt install ca-certificates curl gnupg

sudo install -m 0755 -d /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg

echo \
  "deb [arch=\"$(dpkg --print-architecture)\" signed-by=/etc/apt/keyrings/docker.gpg] \
  https://download.docker.com/linux/ubuntu $(. /etc/os-release && echo \"$VERSION_CODENAME\") stable" \
  | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

sudo apt update
sudo apt install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
```

### Ajouter ton utilisateur au groupe docker

Par défaut, il faut `sudo` pour tout. Pour du dev, c'est vite insupportable.

```bash
sudo usermod -aG docker "$USER"
newgrp docker
docker ps
```

Si `docker ps` fonctionne sans sudo, c'est bon.

---

## macOS

Sur macOS, le plus simple reste **Docker Desktop** :

- Télécharge depuis le site officiel,  
- installe,  
- vérifie que `docker ps` fonctionne dans ton terminal.

Pour un usage pro ou si tu veux éviter Docker Desktop (licence, perf), tu peux passer par **Colima** ou **Rancher Desktop**, mais c'est un poil plus avancé. Pour commencer :

```bash
brew install --cask docker
```

Ensuite, lance Docker depuis le Dock, attends que le daemon démarre, puis :

```bash
docker run hello-world
```

---

## Windows : WSL2 obligatoire (ou presque)

Sous Windows, il y a deux mondes :

- Docker Desktop qui utilise **WSL2** sous le capot.
- Une install plus "pure" où tu travailles **directement dans WSL2** (Ubuntu, Debian, etc.) avec Docker Engine comme sur Linux.

Franchement, pour du dev moderne, **travaille dans WSL2**.

### Étapes rapides

1. Activer WSL2 et installer Ubuntu depuis le Microsoft Store.  
2. Dans WSL (Ubuntu), suivre la procédure Linux ci-dessus (install Docker Engine).  
3. Vérifier :

```bash
wsl -l -v          # tu dois voir Ubuntu en version 2
docker ps          # depuis Ubuntu
```

Tu restes dans un environnement proche d'un serveur Linux classique, ce qui te simplifiera la vie le jour où tu passeras en prod.

---

## Réglages utiles au quotidien

Quelques petits réglages qui changent la vie :

- **Limiter les ressources** (surtout sur laptop)  
  - Docker Desktop (macOS/Windows) → onglet Resources : limite CPU/RAM raisonnable.  
  - Sur Linux, pense à fermer les conteneurs que tu n'utilises plus.

- **Nettoyer régulièrement**  
  ```bash
  docker ps -a
  docker image ls
  docker volume ls
  docker system prune
  ```

- **Activer la complétion shell** (bash/zsh)  
  Permet d'avoir l'auto-complétion sur `docker run`, `docker image`, etc.

---

## Checklist installation

Si tu coches tout ça, tu es bien :

- [x] `docker ps` fonctionne sans sudo (sur ta machine de dev)  
- [x] `docker run hello-world` s'exécute correctement  
- [x] Tu sais où Docker est installé (Linux natif / WSL / macOS)  
- [x] Tu as limité l'usage CPU/RAM sur ta machine principale  

Dans le prochain article, on va commencer à **brancher des volumes et des réseaux** pour que les conteneurs deviennent vraiment utiles (bases de données, front + API, etc.).

