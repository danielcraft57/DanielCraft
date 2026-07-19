---
title: "Docker : bien l'installer et le garder propre"
date: 2024-11-07
excerpt: "Installation, droits, contextes et nettoyage : l'hygiène locale qui évite les surprises."
type: article
tags: [Docker, installation, Linux, WSL, macOS]
series: docker-serie
series_order: 2
og_image: docker-installation-1200x630.jpg
---

# Docker : bien l'installer et le garder propre

Avant de jouer avec les boites Docker, il faut un **garage propre**. Une mauvaise install, c'est des bugs bizarres, des droits qui bloquent tout, ou un WSL qui rale.

Tu as deja vu [images et conteneurs](/blog/articles/docker-fondamentaux-images-conteneurs.html) ? Bien. Maintenant on installe Docker **simplement** sur Linux, macOS et Windows.

---

## Linux (Ubuntu, Debian...)

Sur Linux, le plus sain : installer **Docker Engine** directement. Pas besoin de Docker Desktop.

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

Par defaut, il faut `sudo` pour tout. En dev, ca fatigue vite.

```bash
sudo usermod -aG docker "$USER"
newgrp docker
docker ps
```

Si `docker ps` marche **sans sudo**, c'est bon. Tu as les cles du garage.

---

## macOS

Sur Mac, le plus simple reste **Docker Desktop** :

- telecharge depuis le site officiel,
- installe,
- verifie que `docker ps` marche dans le terminal.

<figure class="schema-figure">
  <img src="/assets/images/blog/schemas/docker-install-hygiene.svg" alt="Schema bonnes pratiques installation Docker" class="schema-inline" width="640" />
  <figcaption>Installer ne suffit pas : user, contextes et prune font l'hygiene.</figcaption>
</figure>

Avec Homebrew :

```bash
brew install --cask docker
```

Lance Docker depuis le Dock. Attends que le moteur demarre. Puis :

```bash
docker run hello-world
```

Si tu vois un message de succes, le garage est ouvert. Pour aller plus loin sans Desktop (licence, perf), il y a Colima ou Rancher Desktop - mais pour commencer, Desktop suffit.

---

## Windows : passe par WSL2

Sous Windows, deux mondes :

- Docker Desktop qui utilise **WSL2** sous le capot (WSL = un petit Linux dans Windows).
- Une install "pure" dans WSL2, comme sur un vrai Linux.

Pour du dev moderne : **travaille dans WSL2**.

### Etapes rapides

1. Active WSL2 et installe Ubuntu depuis le Microsoft Store.
2. Dans Ubuntu, suis la procedure Linux ci-dessus.
3. Verifie :

```bash
wsl -l -v          # Ubuntu en version 2
docker ps          # depuis Ubuntu
```

Tu es dans un environnement proche d'un serveur Linux. Le jour ou tu passes en prod, tu seras moins perdu.

---

## Reglages utiles au quotidien

- **Limiter les ressources** (surtout sur laptop). Dans Docker Desktop : onglet Resources. Mets un plafond CPU/RAM raisonnable. Sinon ton PC devient une friteuse.
- **Nettoyer regulierement** :

```bash
docker ps -a
docker image ls
docker volume ls
docker system prune
```

`prune`, c'est le balai. Ca jette les boites et images inutiles. Attention : ca ne touche pas aux volumes nommes (tes donnees).

- **Activer la completion shell** (bash/zsh) pour taper `docker` plus vite.

---

## Checklist

Coche ca, et tu es pret :

- [x] `docker ps` sans sudo (en dev)
- [x] `docker run hello-world` OK
- [x] Tu sais ou Docker tourne (Linux / WSL / Mac)
- [x] Tu as limite CPU/RAM sur ta machine principale

Ensuite : [volumes et reseaux](/blog/articles/docker-volumes-reseaux.html) pour que tes conteneurs gardent des donnees et se parlent. Puis [Docker Compose](/blog/articles/docker-compose-environnements-local.html) pour tout lancer d'une commande.
