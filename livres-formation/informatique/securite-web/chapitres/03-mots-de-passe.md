# Chapitre 3 - Mots de passe

Un mot de passe n'est pas un slogan cute. C'est une **cle**. Si la cle est courte, previsible, ou reutilisee partout, une seule fuite ouvre plusieurs portes. Chez DanielCraft, la regle debutant est simple a retenir et dure a tricher : **long**, **unique**, range dans un **gestionnaire**, avec **2FA** quand le service le propose. Lea a migre ses comptes critiques en un week-end. Max a arrete `PrenomAnnee!`. Sam refuse les post-it sous le clavier et les fichiers `mdp.txt` sur le bureau.

On ne te donne pas de listes de mots de passe a casser. On te donne une politique.

:::retenir
Long + unique + gestionnaire (+ 2FA si possible). Un secret reutilise = plusieurs portes ouvertes.
:::

## Long et imprevisible

La longueur aide. Une phrase de passe longue, ou un secret genere par le gestionnaire, bat un mot court "complexe" du type `A1b!`. Tu n'as pas a le memoriser pour chaque site : le gestionnaire le retient. Toi, tu memorises le maitre (tres solide) et tu actives le verrouillage de l'appareil.

## Unique par service

Mail, hebergeur, admin site, banque, reseaux : chacun son secret. Si un forum fuit, ton admin ne tombe pas avec. Lea tient un inventaire des comptes critiques. Max commence par les trois portes. Sam dit : "Pas de 'je change tout demain'. Trois aujourd'hui."

## Gestionnaire et 2FA

Un gestionnaire (application dedicatee) genere, stocke, remplit. La double authentification ajoute un second facteur (application, cle, parfois SMS avec limites). Ce n'est pas magique. Ca coupe beaucoup de vols d'acces apres fuite de mot de passe. Active-la d'abord sur le mail : c'est souvent la cle de reset de tout le reste.

:::attention
Ne stocke pas tes secrets dans un mail a toi-meme, un Drive partage, un Slack, un README du projet. Le depot Git n'est pas un coffre.
:::

## Petite histoire

Max a reutilise le meme secret "solide" sur boutique et mail. Une fuite boutique a permis une tentative de reset mail. Lea a freine avec la 2FA deja active. Sam a fait migrer Max vers un gestionnaire le soir meme. Chez DanielCraft, on celebre le frein, pas la peur.

## Erreur classique

Changer tous les mots de passe tous les 30 jours vers des variantes previsibles (`Hiver2024`, `Hiver2025`). Preferer unique + long + 2FA. Autre piege : partager un compte "equipe" avec un seul login admin.

:::astuce
Commence par mail + hebergeur + admin. Ensuite le reste au fil de l'eau quand tu te connectes.
:::

## En vrai

Ouvre (ou installe) un gestionnaire. Cree une entree pour un compte non critique en test. Note la regle que tu appliqueras aux trois comptes critiques.

## Gerer le secret maitre

Le gestionnaire a lui-meme un secret maitre. Il doit etre long, memorisable pour toi seul, jamais reutilise ailleurs. Active le verrouillage automatique de l'appareil et du coffre. Lea utilise une phrase de passe personnelle longue. Max a abandonne les quatre chiffres faciles. Sam rappelle : si le maitre fuit, le coffre fuit - d'ou l'interet de la 2FA sur le mail de recuperation et du soin porte a l'appareil.

Chez DanielCraft, on prefere un coffre un peu contraignant a vingt secrets ecrits dans un carnet perdu. Si tu partages un ordinateur familial, cree un profil separe ou verrouille systematiquement. Un gestionnaire ouvert sur une session partagee n'est plus un coffre.

## Reagir a une fuite suspecte

Si un service annonce une fuite, ou si tu as colle un secret au mauvais endroit : change ce secret depuis le vrai site, verifie les sessions actives, active la 2FA, regarde si le meme secret existait ailleurs (et change aussi). Lea chronometre ces gestes. Max ne panique plus : il execute la liste. Sam interdit d'attendre demain.

## A toi

Ecris ta politique en quatre puces : longueur, unicite, stockage, 2FA. Coche ce qui est deja vrai. Planifie les trous cette semaine.
