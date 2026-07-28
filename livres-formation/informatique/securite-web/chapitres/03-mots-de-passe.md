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

## A toi

Ecris ta politique en quatre puces : longueur, unicite, stockage, 2FA. Coche ce qui est deja vrai. Planifie les trous cette semaine.
