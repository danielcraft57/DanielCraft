# Chapitre 14 - Atelier : configurer un wallet test

Atelier **sans fonds** (ou dust minime explicitement acceptee perdue). L'objectif n'est pas de "devenir self-custody expert" en une heure. C'est d'apprendre le **geste** : creer, noter la seed, verrouiller, restaurer, puis jeter la seed de test. Chez DanielCraft, on pratique a froid pour ne pas decouvrir la panique le jour ou un montant compte.

Disclaimer pedagogique : cet atelier n'est pas un conseil d'installation d'un editeur precis. Verifie toujours l'editeur officiel, l'URL, les avis de securite a jour. Les cryptos peuvent tout perdre ; une seed mal gardee aussi. Ne reutilise **jamais** une seed de test pour de vrais fonds.

Nora veut "voir a quoi ca ressemble". Max a peur de se tromper et c'est sain. Sam veut une checklist anti-phishing avant le premier clic. Parfait : l'atelier est fait pour les trois.

## Avant de commencer (cadre)

Travaille sur un appareil que tu controles. Ferme les onglets douteux. Refuse les DM "je t'aide a setup". Prepare papier + stylo (pas de photo cloud de la seed). Decide a l'avance : **zero depot** pendant l'atelier, sauf si tu acceptes explicitement de perdre un dust - et meme alors, ce n'est pas necessaire pour apprendre.

Rappel : wallet chaud (extension / mobile) = pratique et expose. Hardware vient plus tard, quand les montants le justifient. Ici, on apprend la grammaire des cles, pas la collection de gadgets.

## Etapes detaillees

**1. Choisir et verifier l'editeur.** Installe un wallet reputable (extension navigateur ou application mobile) en passant par le site / store officiel de l'editeur. Compare le nom de l'editeur, l'orthographe, le nombre de telechargements avec mefiance (les copies existent). Si un lien arrive par Discord, Twitter, Telegram : stop. Bookmark le vrai site apres verification.

**2. Creer un wallet neuf.** Lance la creation. Lis les ecrans sans survoler. Tu vas rencontrer des mots sur la sauvegarde de phrase de recuperation : c'est normal. Ce n'est pas un tutoriel pour la coller dans un Google Doc.

**3. Noter la seed sur papier (test).** Ecris les mots dans l'ordre, lisiblement. Verifie deux fois. Ne les tape pas dans un gestionnaire cloud "temporaire". Ne les envoie pas a toi-meme par email "pour backup". Pour un wallet de test, le papier suffit - et sera detruit a la fin.

**4. Verifier les mots.** Beaucoup d'apps te demandent de reselectionner des mots. Fais-le sans tricher. L'exercice entraine la patience que le phishing essaie de casser avec l'urgence.

**5. Lock / unlock.** Verrouille le wallet. Rouvre-le avec le mot de passe / biometrie local. Confirme que tu comprends la difference : mot de passe local != seed. Le mot de passe protege l'acces sur cet appareil ; la seed recupere le compte ailleurs (et donc vole aussi le compte ailleurs si elle fuit).

**6. Option - restore sur un second appareil de test.** Si tu as un vieux telephone ou un profil navigateur de test, restaure avec la seed papier. Objectif : sentir que "qui a la seed a les fonds". Puis verrouille. Si tu n'as qu'un appareil, saute cette etape sans culpabilite - visualise-la quand meme.

**7. Nettoyage.** Efface / desinstalle le wallet de test selon ton aise. Detruise le papier de la seed de test (dechire). Note dans ton carnet : "seed test = morte, jamais reutilisee". Si tu gardes l'app pour plus tard, cree plus tard une **nouvelle** seed pour de vrais fonds - ne "promouvois" pas la seed d'atelier.

## Checklist anti-phishing (a cocher a voix haute)

- URL / editeur / store corrects (pas un lien DM)
- Pas de "support" qui demande la seed
- Pas de site "valider / sync / claim" avec champ seed
- Pas de capture d'ecran de seed envoyee a quiconque
- Zero depot (ou dust accepte perdu, clairement etiquete)
- Seed de test detruite ou clairement separee des fonds reels

## Petite histoire

Max installe depuis un lien Discord "aide wallet". L'icone est presque bonne. Sam lui fait comparer l'editeur caractere par caractere : faux. Ils desinstallent avant la seed. Nora, elle, cree correctement, note, restore sur un vieux telephone, sourit, puis dechire le papier. Elle n'a rien "gagne" en euros. Elle a gagne un reflexe. DanielCraft prefere ce reflexe a dix threads "meilleure seed metal".

## Erreur classique

Reutiliser la seed de test "puisque ca marche". Photographier la seed "au cas ou". La taper dans un notes synchronise. Accepter un DM pendant l'atelier. Deposer des fonds "pour voir le solde bouger". L'atelier devient alors un vrai risque pour de mauvaises raisons.

## En vrai

Fais les etapes 1 a 5 sans depot. Coche la checklist. Ecris "seed never online" et signe la date.

## A toi

Reponse ecrite : seed never online - oui/non. Si non, arrete l'atelier et relis securite / arnaques avant de continuer.

:::retenir
Le geste de restauration se pratique a froid, sans argent. Seed de test != seed de fonds.
:::

:::attention
Une seed de test compromise n'est grave que si tu la reutilises pour de vrai - ne le fais jamais.
:::

:::astuce
Hardware plus tard, quand les montants le justifient. D'abord le geste, ensuite le metal.
:::
