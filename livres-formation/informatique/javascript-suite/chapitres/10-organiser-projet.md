# Chapitre 10 - Organiser un petit projet

Un projet web, ce n'est pas seulement "du code qui marche une fois". C'est aussi un rangement que tu comprends dans une semaine, quand tu auras oublie les details, quand un client demandera une modification, ou quand tu reviendras apres des vacances. Voici une structure simple qui marche pour beaucoup de mini-apps JavaScript front. Pas de framework, pas de bundler obligatoire. Juste des fichiers avec des roles clairs.

Chez DanielCraft, on voit trop de debutants coller 300 lignes entre deux balises script dans index.html. Ca marche pour dix lignes. Au-dela, c'est une nasse. Passe tot aux fichiers separes, meme pour un exercice. Lea structure ainsi presque tous ses petits projets clients avant d'envisager React ou autre.

## La structure de base

```
mon-projet/
  index.html
  styles.css
  main.js
  api.js
  afficher.js
  data/   (optionnel)
```

index.html : la page, la structure, peu de logique. styles.css : l'habillage. main.js : le chef d'orchestre (ecoute les clics, lance les chargements, gere les erreurs). api.js : fetch et parsing reseau. afficher.js : creer des elements DOM a partir des donnees. data/ : fichiers JSON locaux pour les exercices.

## Responsabilites

Si api.js commence a manipuler le DOM, tu melanges les roles. Si afficher.js appelle fetch, pareil. Garde une regle : chaque fichier a une phrase pour se presenter. "Moi, je charge les donnees." "Moi, je dessine la liste." "Moi, je branche les boutons." Si tu ne trouves pas la phrase, le fichier n'est peut-etre pas necessaire, ou tu dois le renommer. Ton projet est une petite equipe. main.js est le chef : il donne les ordres, ne fait pas tout lui-meme. api.js est le messager : il va chercher les infos dehors. afficher.js est le graphiste : il met en forme a l'ecran. index.html est la scene. styles.css est le decor. Chacun son metier.

## Noms clairs

faireTruc.js n'aide personne six mois plus tard. chargerProduits, afficherErreur, viderListe : on comprend. Les noms longs et explicites battent les noms courts et mysterieux. Max a renomme tout.js en main.js et data.js en api.js un dimanche. Il a gagne une heure la semaine suivante.

## Une seule source de verite

Evite d'avoir le meme tableau de produits copie dans trois endroits. Charge une fois, stocke dans une variable (ou un petit etat simple), puis affiche. Si tu modifies, tu modifies a un seul endroit. Sam explique ca a ses eleves avec l'image du tableau au tableau : une seule copie officielle, pas trois versions divergentes.

## Petite histoire

Lea a repris le site d'un artisan (pas Max, un autre client). Tout etait dans index.html : HTML, CSS inline, JS melange. En une journee, elle a extrait CSS et JS, decoupe en trois modules. Le site faisait la meme chose pour l'utilisateur. Mais Lea pouvait enfin ajouter une feature sans peur. L'organisation, c'est de l'argent gagne en maintenance.

## Erreur classique

Creer vingt fichiers vides "pour faire pro" avant d'avoir vingt lignes qui marchent. Commence petit : trois fichiers suffisent. Autre piege : copier-coller le meme fetch dans main.js et api.js "temporairement" et oublier de supprimer le doublon. Ou melanger logique metier et affichage dans la meme fonction de 80 lignes.

## En vrai

Beaucoup de projets open source ou tutos melangent tout au debut. C'est normal. L'etape suivante, c'est ranger. Dessine sur papier les 4 fichiers de ton prochain mini-projet et une phrase de role pour chacun. Si une phrase est floue, simplifie.

## A toi

Dessine sur papier (ou dans un commentaire en tete de main.js) les fichiers de ton prochain mini-projet et le role de chacun. Si tu ne trouves pas la phrase en une ligne, le decoupage n'est pas encore clair. Ajuste avant de coder. Ce plan de dix minutes evite des heures de refactor plus tard.

## Versioning et sauvegarde

Meme pour un petit projet, un dossier Git ou une copie datee sauve du desespoir. Lea commit apres chaque feature qui marche ("formulaire ok", "fetch ok"). Max zippe son dossier le dimanche. Sam demande un export GitHub aux eleves motives. L'organisation, ce n'est pas que les noms de fichiers : c'est aussi pouvoir revenir en arriere quand tu casses fetch en "corrigeant" autre chose.

## Evolutivite sans sur-ingenerier

Tu n'as pas besoin de architecture hexagonale pour afficher dix produits. Tu as besoin de ne pas peindre dans un coin. Si tu sens que main.js depasse cent cinquante lignes, decoupe. Si api.js contient des selecteurs DOM, deplace. Si tu prevois d'ajouter une recherche plus tard, garde les donnees en memoire apres le premier fetch (atelier 15 bonus). Anticiper un peu, pas tout abstraire d'avance.

## Checklist avant de dire "c'est fini"

index.html minimal et lisible. CSS separe. fetch avec ok et catch. Formulaire avec preventDefault si present. Modules si plus de deux fichiers JS. Test en local avec serveur, pas file://. Message chargement et message erreur visibles. Console sans erreur rouge non geree. Si tu coches ca sur un mini-projet DanielCraft, tu es deja au-dessus de beaucoup de tutos abandonnes a mi-chemin.
