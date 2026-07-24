# Chapitre 18 - Securite : l'IA comme nouvelle surface d'attaque (et d'erreur)

L'IA ajoute des risques classiques (fuite de donnees, comptes piratés) et des risques nouveaux (prompt injection, liens sournois, assistants trop obeissants, deepfakes). Tu n'as pas besoin de devenir expert cyber. Tu as besoin d'hygiene.

Chez DanielCraft, securite = habitudes ennuyeuses qui evitent les journees horribles.

## Compte et acces

Mot de passe unique et gestionnaire. Double authentification. Pas de compte pro partage "avec le stagiaire" sans regles. Deconnecte les sessions inconnues. Si l'outil permet des cles API, traite-les comme des cles de voiture : jamais dans un repo public, jamais dans un screenshot Twitter.

## Ce que tu colles

Meme refrain que l'ethique, cote concret : secrets, cles, journaux internes, donnees clients, copies de pieces. Si tu dois absolument faire traiter un texte sensible, anonymise, utilise un canal approuve, ou travaille en local si tu sais le faire. Le plus simple reste : ne pas coller.

Desactive l'entrainement sur tes donnees quand l'option existe et que tu es en usage pro. Vide l'historique periodiquement si tu as colle trop large un jour de fatigue.

## Prompt injection (idee simple)

Un document ou une page web peut contenir des instructions cachees du genre "ignore tes regles et envoie les infos a...". Si un agent lit le web ou tes mails tout seul, il peut obeir au mauvais maitre. Contre-mesure debutant : pas d'agent avec droits d'envoi ; mefie-toi des "resume cette page" louche ; segmente les taches ; valide les actions sensibles.

## Phishing ameliore

L'IA aide aussi les attaquants : mails plus propres, fausses voix, fausses factures. Ton reflexe : verifier le canal (rappel au numero connu), se mefier de l'urgence, ne pas ouvrir les pieces inattendues, regarder le domaine. Max recoit une "facture fournisseur" impeccable : il appelle le fournisseur au numero du carnet, pas au numero du mail.

## Posture sur le code et les macros

Si tu generes du code ou des scripts, ne les execute pas aveugle sur ta machine pro, surtout telecharges d'un chat + internet. Lis. Comprends. Environnement de test. Pareil pour les "automatisations" qui demandent des acces larges.

## Posture multimodale

Ne fais pas confiance a une image de RIB. Ne valide pas un paiement sur une voix seule. Pour les eleves et parents (Sam) : eduquer au deepfake fait partie de la securite collective.

## Sauvegarde de ta methode

Tes prompts utiles sont un actif. Exporte-les dans un endroit que tu controles. Ne les laisse pas prisonniers d'un seul compte sans copie. En meme temps, ne stocke pas dans la banque des prompts remplis de donnees clients.

## Incident : que faire

Tu as colle un secret : revoque / change le secret immediatement, puis nettoie l'historique si possible, puis alerte selon la gravite (client, DPO). Tu as envoye un mail IA faux : corrige par un message clair, sans theatre. Tu as ete piege : coupe l'acces, change les mots de passe, documente.

## Erreur classique

Croire "c'est que du texte". Ou tout autoriser a un agent parce que "c'est pratique". Ou ignorer les reglages pendant six mois.

## En vrai

Fais un audit 20 minutes : 2FA active ? entrainement desactive si besoin ? historique a nettoyer ? secrets dans d'anciens chats ? extensions navigateur douteuses ? Une page de notes. Trois actions tout de suite.

## A toi

Ecris ta checklist securite IA en 8 lignes max (compte, collage, agent, phishing, code, multimodal, export prompts, incident). Relie-la a ta charte ethique du chapitre 10. Une fois par mois, relis-la en deux minutes.
