# Chapitre 18 - Securite et phishing

La securite crypto n'est pas un antivirus miracle ni un badge "hardware = immortalite". C'est un **rituel** repete : verifier avant de signer, verifier apres avoir colle, tester petit, se mefier de l'urgence. Chez DanielCraft, on traite le phishing et le malware comme des risques de base, au meme niveau que la volatilite - parce qu'un clic peut vider un wallet plus vite qu'un bear market.

Disclaimer : pedagogie. Aucune checklist n'est complete face a des attaques qui evoluent. Perte totale possible. Ce chapitre ne remplace pas une veille securite ni un audit pro. Il te donne des gestes utilisables ce soir.

Nora a failli coller une adresse piegee. Max a clique un faux site presque parfait. Sam refuse les extensions "outils yield" inconnues. Le chapitre parle de leurs erreurs evitees - et des mechaniques derriere.

## Phishing : le theatre de la confiance

Le phishing crypto emprunte les decors que tu connais : logo d'exchange, ecran de wallet, ticket "support", page de claim. La difference se joue souvent sur l'URL, l'editeur, le canal d'arrivee. Un vrai service a des chemins connus ; un piege arrive par DM, pub, resultat de recherche empoisonne, typo-squatting (lettre proche), ou lien raccourci.

Le scenario classique : tu crois te connecter, tu signes une transaction ou tu colles une seed. Dans le cas seed, c'est souvent game over pour ce wallet. Dans le cas signature / approval, un contrat malveillant obtient le droit de deplacer des tokens. D'ou la lenteur volontaire : lire ce que tu signes, refuser les approvals eternelles quand tu peux les eviter, revoquer plus tard au calme si tu as ouvert trop large (sans transformer la revoke panic en nouvelle arnaque).

## Clipboard hijack : le piege du copier-coller

Certains malwares surveillent le presse-papiers. Tu copies une adresse BTC ou ETH legitime. Au moment du collage dans le champ "destinataire", le malware substitue une adresse attaquant - parfois avec les memes premiers caracteres pour tromper un coup d'oeil rapide. Tu confirmes en pensant avoir verifie.

**Rituel anti-clipboard :** apres collage, re-verifie manuellement les **4 a 6 premiers** et **4 a 6 derniers** caracteres de l'adresse affichee. Si ton device est douteux, dictee / verification croisee sur un second canal de confiance, ou transfert test minuscule d'abord. Ne te fie pas a "ca ressemble". Les attaquants savent ce que tu regardes.

Le clipboard hijack n'a pas besoin que tu visites un faux site le jour J : il a besoin que tu aies deja un malware et que tu fasses confiance aveugle au collage. D'ou l'hygiene appareil : sources logicielles officielles, mefiance des cracks, pas d'outil "accelerateur de gas" telecharge depuis un forum obscur.

## Autres surfaces frequentes

Fausses apps / extensions homonymes. QR de paiement manipules. Wi-Fi public + hate de verifier. 2FA SMS (SIM swap) plus faible qu'une app d'authentification ou une cle physique quand c'est disponible. Reutilisation de mots de passe email = porte d'entree vers reset de comptes exchange. Et toujours : seed demandee = stop.

## Rituels concrets (a adopter tels quels)

Verifier les 4-6 premiers et derniers caracteres d'une adresse apres collage. Faire un **small test transfer** avant un gros montant. Preferer 2FA app / cle a SMS quand c'est possible. Separater navigateur ou machine pour les operations importantes si ton usage le justifie. Bookmarks des vrais sites. Phrase de raccrochage contre les DM support. Mises a jour raisonnables du systeme sans installer n'importe quel "patch wallet".

## Petite histoire

Nora copie une adresse. Le malware change le milieu. Elle verifie prefixes et suffixes : ca ne match pas. Elle annule, scanne, sauve la mise. Max, une fois, n'a pas verifie : lecon chere, montants modestes mais ego bruise. Sam desactive une extension inconnue apres lecture d'une alerte et se sent "parano" - puis lit le chapitre arnaques et se sent simplement proportionne. DanielCraft prefere la paranoia legere au recit "j'aurais du".

## Erreur classique

Verifier seulement le debut de l'adresse. Signer sous urgence Discord. Garder la seed dans un notes synchronise "parce que c'est plus safe que le papier". Croire que le hardware wallet dispense de verifier l'adresse sur l'ecran de l'appareil.

## En vrai

Ajoute a ta checklist ecrite : "verifier adresse apres collage" + "transfert test". Fais-le une fois a blanc (sans fonds) pour sentir le geste.

## A toi

Ouis / non : j'ai une phrase de raccrochage phishing. Si non, ecris-la maintenant. Ajoute "verifier adresse" a cote du % max.

:::retenir
Petit transfert test + verification d'adresse apres collage. Securite = rituel, pas badge.
:::

:::attention
Clipboard hijack existe : regarde vraiment ce que tu as colle, debut et fin.
:::

:::astuce
2FA app ou cle > SMS quand c'est possible ; bookmarks > liens DM.
:::
