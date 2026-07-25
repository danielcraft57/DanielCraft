# Chapitre 15 - Atelier : CNN et transfer learning (plan de projet)

Objectif : ecrire un plan de projet vision realiste. Duree visee : environ 40 minutes. Tu n'as pas besoin d'avoir entraine pour valider le plan. Chez DanielCraft, un plan honnete bat un notebook theatral.

Ines utilise exactement cette grille pour ses pieces detachees. Lea s'en sert pour cadrer un prestataire. Toi, tu l'adaptes a ton jeu d'images - meme imaginaire, du moment qu'il est concret.

:::retenir
Plan CNN = classes, donnees, conditions reelles, preentraine, augmentation, split, metriques, anti-overfitting, go/no-go, calcul.
:::

## Ce que ce n'est pas

Ce n'est pas un entrainement complet. Ce n'est pas une promesse de 99 %. Ce n'est pas non plus "collecter 50 images et deployer demain". Si tu as moins de 50 images au total, reste sur proof of concept et transfer learning agressif, ou reconsidere la faisabilite.

## Image mentale

Tu construis un dossier de decision. Chaque section empeche un mensonge courant : "on verra bien", "le modele saura", "les photos studio suffisent". Le go/no-go signe a l'avance te protege du deploiement par enthousiasme.

## Etapes (dans l'ordre)

1) Definir 3 a 10 classes d'images. Noms clairs, frontieres discutees (qu'est-ce qui est ambigu ?).

2) Estimer combien de photos par classe tu peux collecter cette semaine / ce mois.

3) Decrire les conditions reelles : eclairage, flou, telephone, angle, mains dans le cadre, huile, pluie.

4) Choisir un modele preentraine a adapter (famille CNN ou vision transformer, peu importe le detail : l'esprit transfer).

5) Plan d'augmentation de donnees : liste de transformations qui existent en production sans casser le label.

6) Split train / val / test. Qui touche au test ? Idealement presque personne jusqu'a la fin.

7) Metriques : accuracy si utile, mais surtout erreurs couteuses (faux positif vs faux negatif selon le metier).

8) Plan anti-overfitting : early stopping, dropout, moins de capacite, plus de diversite, gel de couches...

9) Critere go/no-go avant deploiement. Une phrase signee.

10) Idee GPU : local, cloud, ou seulement inference API.

:::idee
Ecris le go/no-go AVANT de regarder un premier score. Sinon tu deplaces la barre.
:::

## Petite histoire

Ines a ecrit : "si recall sur pieces critiques < seuil X sur test terrain, on n'automatise pas ; humain valide". Un premier modele a echoue sous le seuil. Elle a ameliore les donnees, pas le marketing. Max a applique la meme idee a un "detecteur de fuite sur photo" trop frele : abstention > fausse alerte permanente.

## Erreur classique

Remplir le plan avec des chiffres inventes pour faire serieux. Ou oublier les conditions terrain. Ou choisir from scratch par snobisme. Ou ne jamais ecrire le no-go.

:::attention
Sans critere d'arret metier, tu deploieras par fatigue ou par slide.
:::

## En vrai

Prends un timer 40 minutes. Remplis les 10 etapes au brouillon. Interdiction d'ouvrir un framework avant la fin du document.

## Livrable

Document "plan CNN" de 1 a 2 pages. Titre, classes, volumes, conditions, modele preentraine, augmentation, split, metriques, anti-overfitting, go/no-go, calcul. Envoie-le a un pair pour contradiction.

## A toi

Signe ton go/no-go. Formule type : "si la metrique X sur test terrain < Y, on n'automatise pas, on garde un humain dans la boucle". Date. Initiales.

## Conseil DanielCraft

Si les labels sont ambigus, arrete-toi a l'etape 1 et clarifie avec un expert metier. Aucun CNN ne sauve une taxonomie pourrie. Sam le fait dire a ses eleves avant tout telechargement de backbone.

## Exemple Ines (rempli partiellement)

Classes : 6 types de pieces. Volume vise : 80 photos / classe, telephone chantier. Conditions : neon, graisse, angle 30-60 degres. Modele : CNN preentraine ImageNet-like. Augmentation : rotation legere, luminosite, crop ; pas de flip si le sens compte. Split 70/15/15. Metrique : recall sur pieces critiques + revue humaine si score bas. Go/no-go : recall terrain < seuil => pas d'automatisation. GPU : cloud ponctuel. Copie la structure, change les chiffres.

## Revue par un pair

Envoie le plan a quelqu'un qui cherchera les trous : classes floues, volumes irrealistes, oubli du terrain, absence de no-go. Une contradiction amicale aujourd'hui evite un deploiement honteux demain.
