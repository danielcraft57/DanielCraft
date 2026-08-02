# Chapitre 2 - Menaces courantes

Avant les outils, il faut une carte mentale. Les menaces qui touchent le plus souvent un petit site ou un compte debutant ne sont pas des films. Ce sont du **phishing**, des **vols d'acces** (mots de passe reutilises, sessions laissees ouvertes), des **oublis** (pas de mise a jour, pas de sauvegarde), parfois des **formulaires** mal controles. Lea range ces risques en "humain" et "technique". Max pensait que seul le "hack" comptait. Sam lui a montre qu'un mail urgent et un plugin abandonne font plus de degats que le mythe du genie dans le noir.

Chez DanielCraft, on apprend a **reconnaitre** pour **freiner**. On ne detaille pas comment mener une attaque. On nomme le signal, on donne le geste sure.

:::retenir
Menace courante = signal a reconnaitre + frein simple. Reconnaitre bat paniquer.
:::

## Phishing et ingenierie sociale

Quelqu'un se fait passer pour un service (hebergeur, banque, collegue) et pousse a cliquer, a coller un secret, a transferer de l'argent ou des droits. Signaux : urgence, peur, cadeau trop beau, lien qui ne correspond pas au domaine attendu, piece jointe inattendue. Frein : ne pas cliquer, ouvrir le site en tapant l'adresse soi-meme, appeler par un numero connu. Lea lit l'expediteur deux fois. Max survole le lien sans cliquer. Sam refuse les "reponds en 5 minutes ou ton compte saute".

## Vol d'acces et reemploi de secrets

Si le meme mot de passe sert au mail et a l'admin WordPress, une fuite ailleurs ouvre deux portes. Les sessions laissees sur un ordi partage font la meme chose sans "piratage". Frein : secrets uniques, gestionnaire, deconnexion, 2FA quand c'est propose. On detaille au chapitre mots de passe.

## Oublis : maj et sauvegardes

Une faille publiee reste ouverte tant que tu n'as pas mis a jour CMS, plugins, themes, systeme. Une sauvegarde absente transforme un accident en catastrophe. Frein : calendrier de mises a jour, copie hors machine, test de restauration. Pas glamour. Efficace.

## Formulaires et entrees non filtrees

Tout ce que l'utilisateur envoie (champ, fichier, parametre d'URL) peut casser une page ou une requete si on le colle tel quel dans le code ou la base. L'idee - sans jamais montrer d'exploit - est : valider, separer donnees et instructions. Chapitres injections et formulaires.

:::attention
Ne cherche pas "comment faire" une attaque pour "mieux comprendre". Cherche comment la reconnaitre et quoi cocher pour la prevenir.
:::

## Petite histoire

Un artisan a recu un SMS "colis bloque, payez 1,90 EUR". Max a failli cliquer. Lea a dit : "On ouvre le site du transporteur depuis les favoris." Le vrai suivi montrait rien. Sam a note le motif : urgence + lien court. Chez DanielCraft, ce motif revient souvent.

## Erreur classique

Tout classer en "je suis trop petit pour etre vise". Les bots ne lisent pas ton chiffre d'affaires. Autre piege : collectionner des outils antivirus en ignorant mots de passe et mises a jour.

:::astuce
Fais une liste "mes trois portes" : mail, hebergeur, admin. Si elles tiennent, le reste devient gerable.
:::

## En vrai

Pour chaque type (phishing, vol d'acces, oubli maj/backup, formulaire), ecris un signal et un frein en une ligne. Tu reutiliseras cette grille au quiz.

## A toi

Choisis un mail ou SMS douteux recent (sans cliquer les liens). Decris en cinq lignes pourquoi tu freines. Si tu n'en as pas, invente un scenario "compte expire demain" et ecris le frein.
