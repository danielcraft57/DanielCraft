# Chapitre 4 - HTTPS et le cadenas

**HTTPS** protege le **trajet** entre ton navigateur et le serveur : les donnees sont chiffrees en transit, plus difficiles a lire ou modifier sur le chemin. Le cadenas (ou l'indicateur equivalent) signale en general que cette protection de trajet est active. Chez DanielCraft, on enseigne HTTPS comme une brique necessaire - pas comme un certificat de saintete. Lea verifie le domaine autant que le cadenas. Max a cru qu'un cadenas rendait un site "sur a 100 %". Sam a corrige : "Sur le trajet, oui. Sur l'intention du site, non."

:::retenir
HTTPS = trajet protege. Utile et attendu. Ce n'est pas toute la securite, ni une preuve d'honnetete.
:::

## Ce que HTTPS fait

Il reduit le risque qu'un intermediaire lise ton mot de passe ou ta session sur un Wi-Fi douteux. Il aide aussi a eviter certaines modifications du contenu en transit. Pour un site qui demande login, paiement, ou donnees perso, HTTPS n'est plus optionnel : c'est le minimum.

## Ce que HTTPS ne fait pas

Il ne garantit pas que le site est le bon service (regarde le **domaine**). Il ne protege pas un serveur mal configure, un plugin abandonne, un mot de passe faible. Un faux site peut aussi avoir HTTPS. Lea tape l'URL connue. Max compare `boutique-exemple.fr` et une variante avec un caractere en trop. Sam refuse les raccourcis suspects meme avec cadenas.

## Certificat et hebergeur

Chez la plupart des hebergeurs modernes, activer HTTPS (Let's Encrypt ou equivalent) est un clic ou une option. Pour un petit site, l'objectif est simple : forcer HTTPS, rediriger HTTP vers HTTPS, verifier que le cadenas apparait sur les pages sensibles. Pas besoin de devenir expert certificats X.509 pour commencer.

:::astuce
Bookmark les sites critiques (banque, hebergeur, admin). Tu ouvres le favori, tu ne colles pas un lien recu.
:::

## Petite histoire

Lea a livre un site encore en HTTP "parce que c'est juste une vitrine". Le formulaire contact envoyait le message en clair sur le trajet. Elle a active HTTPS avant la mise en prod. Max a vu le cadenas et a sourit. Sam a ajoute : "Maintenant, verifie aussi les mots de passe admin." Chez DanielCraft, une brique apres l'autre.

## Erreur classique

Confondre "cadenas vert / present" et "je peux faire confiance aveuglement". Autre piege : ignorer l'avertissement du navigateur "connexion non privee" pour "avancer vite".

:::attention
Si le navigateur crie, tu t'arretes. Tu ne "continues quand meme" que si tu comprends vraiment pourquoi - et rarement sur un compte critique.
:::

## En vrai

Ouvre ton site (ou un site que tu geres). Note : HTTPS oui/non, redirection HTTP, domaine exact. Si non, planifie l'activation avec l'hebergeur.

## A toi

Explique a un ami, en trois phrases, ce que HTTPS protege et ce qu'il ne protege pas. Si tu peines, relis ce chapitre avant l'atelier HTTPS.
