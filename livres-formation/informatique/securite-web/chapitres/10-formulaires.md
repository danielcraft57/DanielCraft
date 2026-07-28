# Chapitre 10 - Formulaires et entrees

Un **formulaire** est une porte. Contact, inscription, upload, recherche : tout ce qui entre doit etre **attendu**, **limite**, **controle cote serveur**. Chez DanielCraft, on ne fait pas confiance au seul navigateur. Lea valide email et longueur. Max a laisse un champ fichier sans type - mauvaise idee. Sam ajoute un token anti-CSRF quand le framework le propose, et un rate limit simple sur les spams.

:::retenir
Formulaire = porte. Controle serveur obligatoire. Client = aide, pas autorite.
:::

## Controles de base

- Champs requis vs optionnels clairs  
- Longueur max  
- Format (email, telephone, choix liste)  
- Types de fichiers autorises et taille max si upload  
- Messages d'erreur sans reveler trop d'interne  

Stocke le minimum. N'enregistre pas un numero de carte dans un champ contact "au cas ou".

## Spam et abus

Captcha raisonnable, limitation de debit, moderation : selon le contexte. Un formulaire contact ouvert sans frein devient une boite a spam. Lea a ajoute un delai simple et une validation email. Max filtre cote serveur les messages vides / liens en masse.

:::astuce
Liste les champs vraiment utiles. Chaque champ en moins est une surface en moins.
:::

## Petite histoire

Le formulaire "devis" demandait piece d'identite "pour aller plus vite". Lea a retire : hors finalite. Sam a rappele le chapitre RGPD. Max a garde nom, email, message. Le site respirait. Chez DanielCraft, minimiser est aussi de la securite.

## Erreur classique

Valider seulement en JavaScript. Autre piege : accepter n'importe quel upload "image" sans verifier type/taille.

:::attention
Un fichier uploade mal controle peut devenir une porte. Reste strict sur types et emplacement de stockage.
:::

## En vrai

Prends un formulaire de ton site. Pour chaque champ : type attendu, longueur, obligatoire, ou ca part (mail, base). Complecte les trous.

## A toi

Ecris la checklist formulaire (8 cases max) que tu recocheras a chaque nouveau form.
