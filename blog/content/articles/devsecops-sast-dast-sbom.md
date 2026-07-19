---
title: "Sécurité dans le code : contrôler avant de publier"
date: 2025-12-02
excerpt: "Vérifier le code, les dépendances et les images avant la mise en ligne — sans freiner toute l'équipe."
type: article
tags: [DevSecOps, SAST, DAST, SBOM, CI/CD]
series: cybersecurite-secops-serie
series_order: 9
og_image: devsecops-sast-dast-sbom-1200x630.jpg
---

# Sécurité dans le code : contrôler avant de publier

Le **DevSecOps**, ce n'est pas "mettre un scanner et bloquer tout jusqu'a ce que l'equipe hurle". C'est integrer des controles au bon endroit, avec des regles pragmatiques, pour reduire le risque sans casser le delivery.

Si ton pipeline passe de 8 minutes a 45 et que tout le monde bypass les checks avec un label magique, tu as perdu.

L'idee est simple : feedback rapide sur la PR, portes ciblees sur ce qui fait vraiment mal, inventaire de ce que tu deploies (**SBOM**), et une boucle vers le runtime. Shift-left, oui - mais aussi "ne pas oublier la droite".

## Les controles qui comptent vraiment dans un pipeline

- **Secrets scanning** : attraper les cles API, jetons, mots de passe avant qu'ils partent sur GitHub
- **SCA** (analyse de composition) : dependances et [CVE](/blog/articles/gestion-vulnerabilites-cve-patching.html) connues
- **SAST** : analyse statique du code (injections, auth foireuse, SSRF, crypto faible)
- Scan d'**images** [conteneurs](/blog/articles/docker-fondamentaux-images-conteneurs.html)
- **DAST** : tests dynamiques sur un environnement qui ressemble a la vraie vie
- Scan **IaC** : Terraform, Kubernetes, CloudFormation - parce que la mauvaise config part souvent du repo

Tu n'as pas a tout activer le meme jour. Secrets + SCA, c'est deja un enorme progres pour une equipe qui n'avait rien. Ensuite SAST sur les chemins critiques. Ensuite images. Le DAST, plus tard, quand staging est stable.

<figure class="schema-figure">
  <img src="/assets/images/blog/schemas/devsecops-pipeline.svg" alt="Schéma pipeline DevSecOps : code, build, test, image, deploy, run avec gates sécurité" class="schema-inline" width="640" />
  <figcaption>Du code au runtime : secrets scan, SAST, deps, DAST, scan d'images, policy gates - puis feedback runtime vers le code.</figcaption>
</figure>

## SAST : utile si tu l'industrialises (sinon, c'est du bruit)

Le **SAST** (Static Application Security Testing), c'est "lire le code sans le lancer" pour trouver des failles. Il a mauvaise reputation parce qu'on le branche "out of the box" et qu'on noie l'equipe sous 500 alertes dont 480 sont des faux positifs ou du style.

Bon usage :

- Regles adaptees au **langage** et au framework
- Reduction agressive du **bruit**
- Focus sur les failles qui comptent (injection, auth, deserialisation, SSRF, path traversal)

Donne le feedback dans la **PR**, pas dans un PDF hebdo que personne ne lit. Un developpeur corrige plus volontiers un finding de 30 secondes apres son commit qu'un backlog de 200 items trois semaines plus tard.

Si une regle genere trop de faux positifs, desactive-la ou affine-la. Une regle bruyante tue la confiance dans tout le scanner. Moins de regles, mieux calibrees, ca passe mieux en equipe.

## DAST : tester comme un attaquant, au bon moment

Le **DAST** (Dynamic Application Security Testing) tape sur l'appli qui **tourne**. Pertinent sur un staging stable, avec une auth realiste, et des scenarios cibles : login, upload, zones admin, APIs authentifiees.

Un DAST "generique" sans compte, qui crawl la home page publique, donne souvent peu de valeur - sauf si tu cherches juste des misconfigs evidentes.

Ne le mets pas sur chaque commit. Nightly ou sur main / pre-prod, c'est souvent le bon rythme. Et accepte qu'il ne remplace pas le SAST ni les tests d'auth manuels sur les flows critiques. Les deux se completent : SAST voit le **code**, DAST voit le **comportement**.

<figure class="schema-figure">
  <img src="/assets/images/blog/schemas/devsecops-shift-left.svg" alt="Schema des gates securite dans un pipeline DevSecOps" class="schema-inline" width="640" />
  <figcaption>Des gates progressives : signal tot, blocage seulement sur le critique.</figcaption>
</figure>

## SBOM : savoir ce que tu deploies (vraiment)

Le **SBOM** (Software Bill of Materials), c'est l'inventaire des composants d'un artefact. Libs, versions, parfois licences.

Interet concret : quand une CVE explose (Log4Shell, xz, etc.), tu reponds "suis-je expose ?" en minutes, pas en jours de grep panique. Tracabilite de la chaine d'outils. Exigences clients et audits qui demandent de plus en plus cet inventaire.

Genere le SBOM au build, attache-le a l'image / au release, stocke-le. Ce n'est pas sexy. Le jour ou tu en as besoin, tu es content de l'avoir. Sans SBOM, chaque crise CVE devient une chasse au tresor dans des repos mal indexes.

Petit bonus : le SBOM force aussi a regarder les dependances **transitives** - celles que tu n'as jamais choisies explicitement, mais qui sont dans ton image quand meme.

## Gates : bloquer intelligemment (pas tout, pas rien)

Ne bloque pas tout. Bloque ce qui est vraiment **dangereux** :

- Secrets detectes
- Vulnerabilites critiques exposees (surtout internet-facing ou deja exploitees)
- Erreurs IAM / IaC dangereuses (wildcard admin, stockage public)
- Images non signees si tu as une politique de signature

Le reste : ticket, delai, owner, exception temporaire avec date de fin. Un gate qui bloque pour une CVE medium sur une lib interne non exposee, ca cree des bypass. Et une fois que les gens ont goute au bypass, ton gate est mort.

Seuil different selon l'environnement. Sur une PR feature : **warn**. Sur main vers prod : **fail** sur le critique. Sur un hotfix de prod : process d'exception court et trace, pas "on coupe tout le pipeline". Documente les exceptions comme une dette technique - owner, raison, date d'expiration.

## Un workflow qui tient sur la duree

- Education et conventions : secure defaults, templates de repo, coffre a secrets des le jour 1
- Scans rapides en PR (secrets, SCA critique, SAST light)
- Scans plus lourds sur main / nightly (DAST, scan image complet)
- Dashboard de risque **reel** - pas un mur de findings - avec priorisation
- Feedback runtime ([CSPM / CWPP](/blog/articles/securite-cloud-cspm-cwpp.html), logs) qui remonte en tickets

Pour une TPE / petite agence : secrets scanning + Dependabot/Renovate + un SAST simple sur le langage principal, c'est deja serieux. Pour un SaaS : ajoute SBOM, scan d'images, gates sur main, et un owner "securite pipeline" qui tranche les exceptions.

## Demarrer sans paralyser l'equipe

Cette semaine :

1. Active le **secrets scanning** sur les repos critiques (et purge l'historique si besoin - rotation des cles, pas juste "on a delete le fichier")
2. Branche un SCA et traite uniquement les critical/high **exposes**
3. Genere un **SBOM** sur ton artefact de prod principal
4. Ecris **trois** regles de gate, pas trente

DevSecOps efficace = feedback rapide + gates cibles + SBOM + gestion des failles qui suit. Ca ne remplace pas un bon [IAM](/blog/articles/iam-mfa-principes-zero-trust.html) ni une reponse a [incident](/blog/articles/incident-response-runbook-postmortem.html). Mais ca ferme beaucoup de portes *avant* la prod.
