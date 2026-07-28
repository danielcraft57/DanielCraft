# Chapitre 11 - Sessions et cookies

Une **session** dit "cet utilisateur est deja authentifie pour un temps". Un **cookie** est souvent le jeton que le navigateur renvoie pour retrouver cette session. Chez DanielCraft, on veut des sessions **courtes autant que possible**, transportees en **HTTPS**, avec **deconnexion** claire, sans laisser un poste partage "encore connecte". Lea se deconnecte sur les ordis d'atelier. Max a compris apres avoir laisse l'admin ouvert en bibliotheque. Sam explique HttpOnly / Secure comme idees : le framework serieux les active souvent pour toi.

:::retenir
Session = preuve temporaire. Cookie = jeton. HTTPS, duree, deconnexion : freins de base.
:::

## Gestes debutant

- Preferer HTTPS partout ou il y a login  
- Se deconnecter sur machine partagee  
- Ne pas cocher "rester connecte" sur un PC public  
- Invalider les sessions apres changement de mot de passe (si l'outil le permet)  
- Limiter les comptes admin ouverts en parallele  

Tu n'as pas a reecrire un moteur de session. Tu as a utiliser proprement celui du CMS / framework.

:::attention
Un cookie de session n'est pas un souvenir a partager. Ne l'envoie pas par mail "pour debug" sur un canal large.
:::

## Petite histoire

Max a demontre une feature admin sur le laptop d'un cafe, puis est parti sans logout. Lea a change le mot de passe et force la deconnexion depuis le panneau. Sam a ajoute "logout" a la fin de chaque atelier. Chez DanielCraft, le detail sauve.

## Erreur classique

Croire que fermer l'onglet = deconnexion complete partout. Autre piege : sessions admin qui ne meurent jamais.

:::astuce
Apres un voyage / PC prete : change le mdp admin et verifie les sessions actives si l'outil le montre.
:::

## En vrai

Sur ton CMS ou app, trouve ou se reglent duree de session / deconnexion / "se souvenir de moi". Note le reglage actuel.

## A toi

Ecris trois regles perso (ex. : pas d'admin en Wi-Fi cafe sans VPN/prudence, logout atelier, 2FA mail). Affiche-les.
