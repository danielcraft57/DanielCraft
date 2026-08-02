# Chapitre 10 - GitHub, c'est quoi ?

**GitHub** heberge tes depots Git sur internet. Sauvegarde distante, collaboration, issues, pull requests, vitrine README. Ce n'est pas Git lui-meme. C'est un hotel pour tes albums Git, avec des couloirs pour travailler a plusieurs. Chez DanielCraft, on separe bien les deux mots : tu peux maitriser Git sans GitHub, mais en 2026 tu croiseras GitHub (ou un cousin) tres vite. GitLab, Bitbucket, Forgejo : meme famille d'idee. On apprend avec GitHub parce que c'est partout. Les gestes se transferent.

Lea pousse ses projets clients en prive. Max met son carnet en prive aussi, puis invite Sam en lecture. Sam montre la page GitHub au tableau : fichiers, commits, README. La "preuve visuelle" rassure autant que la commande. Toi, tu vas creer un compte, un depot de test, lier `origin`, pousser. Quand tu rafraichiras la page et verras tes fichiers, tu sentiras le soulagement. C'est normal. C'est le but.

Ton ordi a l'album local. GitHub a une copie distante (**`origin`**). Tu lies les deux avec `remote add`. Tu envoies avec **`push`**. Tu recuperes avec `pull` (chapitre suivant). Le **README.md** est la vitrine : cinq lignes claires battent un roman vide. HTTPS ou SSH : deux portes d'entree. Choisis-en une et avance. Tu pourras changer plus tard. Chez DanielCraft, on veut que tu pousses, pas que tu te perdres dans un debat de porte.

:::retenir
Cree le depot GitHub sans cocher "Add a README" si tu as deja un historique local. Ca evite les premiers commits divergents au debut.
:::

## Ce que ce n'est pas

GitHub, ce n'est pas obligatoire pour versionner en local. Ce n'est pas non plus le seul hebergeur. Ce n'est pas "le cloud magique qui commit pour toi". Et ce n'est surtout pas un endroit pour coller des secrets. Avant le premier push public ou meme prive partage, relis `status` et ton `.gitignore`. Ce n'est pas non plus "finir le projet" : un README de cinq lignes claires bat un roman vide.

Ce n'est pas non plus "public par defaut pour tout". Prive existe. Utilise-le pour les projets clients, les notes perso, les exercices incomplets. Lea pousse en prive par defaut. Max aussi. Sam montre public seulement quand le contenu est volontairement partage.

## Compte et nouveau depot

Cree un compte sur github.com. Confirme l'email. Optionnel mais recommande : active la double authentification. Deux minutes qui evitent des sueurs froides.

Sur GitHub : New repository. Choisis un nom, par exemple `mon-carnet`. Public ou prive. Tu peux ne pas cocher "Add a README" si tu as deja un depot local - evite les histoires de premiers commits divergents au debut. Si GitHub cree un README et que toi aussi tu as un historique, tu auras deux debuts a fusionner. Faisable. Embettant pour un premier push. Evite-le.

## Lier ton depot local

Sur la page du depot vide, GitHub montre des commandes. En general :

```bash
git remote add origin https://github.com/TON_COMPTE/mon-carnet.git
git branch -M main
git push -u origin main
```

`origin` = surnom classique de ton remote principal.

```bash
git remote -v
```

Verifie que l'URL est la bonne. Max a pousse une fois vers le mauvais depot parce qu'il avait copie trop vite. `remote -v` avant le premier push, c'est pas cher.

## SSH ou HTTPS ?

HTTPS est simple au debut (parfois un token). SSH utilise des cles et devient tres confortable au quotidien. Les deux marchent. Lea est passee en SSH apres deux semaines. Max est reste en HTTPS avec token. Sam montre les deux sans dogme. Si l'auth rate, lis le message. Token expire ? Cle mal ajoutee ? Droits manquants ? Une cause. Une correction. Pas dix essais au hasard.

:::astuce
Lea pousse en prive par defaut. Max active la double authentification des qu'il cree son compte. Deux minutes qui evitent des sueurs froides.
:::

## README.md

Sur GitHub, `README.md` s'affiche en vitrine. Ecris 5 lignes : but du projet + comment lancer. Puis commit et push. Verifie le rendu. C'est ton premier "produit visible". Lea soigne le README autant que le code sur les petits projets. Max a compris le jour ou un ami a compris son carnet sans l'appeler. Sam refuse de "considerer le projet fini" tant que la page GitHub ne montre rien de comprehensible.

## Petite histoire

Lea a pousse, rafraichi la page, vu ses fichiers, souffle. Max a ajoute un vrai README clair le soir meme. Sam a refuse de valider un atelier tant que l'URL ne montrait pas un titre et deux phrases utiles. Trois standards, une meme idee : le distant existe pour etre lu. Chez DanielCraft, la page GitHub fait partie du livrable, pas du bonus.

## Erreur classique

Creer un README sur GitHub et un historique local divergent sans savoir merger. Pousser sans `.gitignore`. Oublier la double authentification sur un compte pro. Autre piege : deposer un projet perso public avec des emails clients dedans. Prive existe. Utilise-le. Encore un piege : croire que "c'est sur GitHub" egal "c'est sauvegarde pour toujours" sans jamais verifier le push. Rafraichis. Regarde. Confirme.

## En vrai

Apres le push, rafraichis la page GitHub. Tu dois voir tes fichiers. Soulagement. Puis ameliore le README. Commit. Push. Verifie le rendu. Sens la boucle locale -> distante. C'est cette boucle que tu rejoueras chaque jour utile.

## A toi

Cree un depot GitHub de test (prive OK). Branche `origin`. Fais `push` de ta branche `main`. Ajoute un vrai `README.md` clair. Commit. Push. Verifie. Note l'URL quelque part : tu en auras besoin pour le mini-projet.
