# Chapitre 7 - Sauvegardes

Une sauvegarde est un **plan B** decide avant le jour J. Panne disque, fausse manip, ransomware, hebergeur qui plante, maj qui casse : sans copie, tu negocies avec le vide. Chez DanielCraft, une sauvegarde qui n'a jamais ete **restauree en test** est un espoir, pas une assurance. Lea teste une restore tous les mois. Max a cru que "l'hebergeur sauvegarde" suffisait - jusqu'au jour ou la retention etait trop courte. Sam exige : copie hors machine + test.

:::retenir
Sauvegarde = copie + hors site + test de restauration. Sinon, illusion.
:::

## Quoi sauvegarder

Fichiers du site (code, media) et base de donnees si tu en as une. Configs critiques (sans coller les secrets dans un repo public). Pour un site simple : export CMS + telechargement fichiers, ou outil hebergeur documente.

## Ou et comment

Au moins une copie **ailleurs** que le serveur live (autre stockage, autre compte, disque offline selon le cas). Rotation : plusieurs points dans le temps si possible (hier, semaine derniere). Chiffre / protege l'acces a ces copies : une sauvegarde lisible par tout le monde est une fuite en attente.

:::attention
Ne publie jamais une archive de sauvegarde sur un lien public "temporaire".
:::

## Tester la restore

Une fois par mois (ou apres un gros changement) : restaure sur un environnement de test ou verifie que l'archive s'ouvre et que la base importe. Lea chronometre. Max note "OK restore" avec la date. Sam refuse "on verra le jour ou ca casse".

## Petite histoire

Max a ecrase une page importante. La sauvegarde de la veille l'a sauve en vingt minutes. Lea a sourit : "C'est pour ca qu'on teste." Chez DanielCraft, la sauvegarde n'est pas une slide. C'est un reflexe.

## Erreur classique

Une seule copie sur le meme disque que le site. Autre piege : sauvegarder mais jamais verifier.

:::astuce
Ajoute "test restore" dans le meme calendrier que les mises a jour.
:::

## En vrai

Verifie ou sont tes copies aujourd'hui. Si tu n'en as pas, cree la premiere (meme imparfaite) puis ameliore.

## A toi

Ecris ta regle 3-2-1 adaptee debutant : au moins une copie recente hors serveur live, et une date de prochain test restore.
