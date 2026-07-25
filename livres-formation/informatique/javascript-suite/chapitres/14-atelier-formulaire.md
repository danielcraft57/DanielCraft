# Chapitre 14 - Atelier : formulaire robuste

Objectif : construire un formulaire contact (nom, email, message) qui refuse l'envoi si un champ manque ou est invalide, et qui explique clairement quoi corriger. Duree : 30 a 45 minutes. Materiel : editeur de code, navigateur, eventuellement Live Server ou python -m http.server.

Lea fait faire cet atelier a chaque stagiaire avant de le laisser toucher a un vrai formulaire client. Max l'a refait pour son site apres avoir recu des mails vides. Sam le note sur dix en fin de seance. Ce n'est pas glamour. C'est fondamental. Chez DanielCraft, un formulaire qui laisse partir du vide, c'est un devis qui part trop tot : tu livres du bruit.

Tu vas sentir la difference entre "ca marche en demo" et "ca tient quand quelqu'un tape n'importe quoi". Le navigateur a ses validations HTML. Toi, tu restes le chef pour les messages clairs, le focus, et le preventDefault qui empeche la page de recharger au moment ou tu voulais juste lire les champs.

## Exercice 1 - Structure HTML (10 min)

Cree index.html avec un formulaire id="contact", trois champs (nom, email, message), un bouton submit, une zone #erreurs pour les messages. Utilise des label for lies aux id des inputs. Ajoute type="email" sur l'email si tu veux, mais rappelle-toi : JS reste le chef pour les messages clairs. Sans label, un champ "marche" encore - mais Sam refuse la note : l'accessibilite commence ici.

## Exercice 2 - Ecouter submit (10 min)

Selectionne le formulaire. Ecoute submit. Appelle preventDefault() tout de suite. Lis les valeurs avec .value.trim(). Loggue l'objet { nom, email, message } en console pour verifier que la lecture marche avant de valider. Si tu vois encore un rechargement de page, preventDefault n'est pas au bon endroit - ou tu ecoutes le mauvais evenement.

## Exercice 3 - Validation par liste d'erreurs (15 min)

Construis un tableau erreurs = []. Si nom vide : pousse "Indique ton nom." Si email sans @ : pousse "Email incomplete." Si message moins de 10 caracteres : pousse "Message trop court." Affiche toutes les erreurs dans #erreurs (join avec retour ligne ou ul). Si aucune erreur, affiche "Formulaire pret (simulation d'envoi)." et loggue l'objet propre en console. Lea prefere une liste d'erreurs a une seule alerte : l'utilisateur corrige tout d'un coup.

## Exercice 4 - Focus et reset (10 min)

Apres affichage d'une erreur, mets le focus sur le premier champ concerne. Quand tout est valide, simule un envoi : message de succes, puis form.reset() apres deux secondes (setTimeout). Ca prepare le vrai POST du chapitre 8. Max a adore ce detail : apres envoi, la page est prete pour le prochain client sans F5.

## Livrable

Un dossier atelier-formulaire/ avec index.html et app.js (ou script inline si tu preferes). Capture ou note : une capture d'ecran avec erreurs affichees, une avec succes. Sans livrable, le cerveau classe ca comme "lu".

## Criteres de reussite

Sans JS, le navigateur ne doit pas naviguer a cause du submit (preventDefault marche). Les messages sont en francais simple, pas des alert(). Tu peux envoyer seulement quand tout est valide. Tu logs l'objet { nom, email, message } une fois valide. Les labels sont presents.

## Petite histoire

Max a recu trois mails "contact" vides en une semaine. Il croyait que "type=email" suffisait. Lea lui a fait refaire cet atelier : trim, liste d'erreurs, focus. Plus de mails fantomes. Sam a chronometre ses eleves : ceux qui testent volontairement le champ vide comprennent plus vite que ceux qui ne cliquent que le chemin heureux.

## Erreur classique

Ne te contente pas de alert(). Les alertes agacent et bloquent la page. Un message dans #erreurs est plus pro, meme pour un exercice. Ne valide qu'au clic bouton sans ecouter submit : Entree dans un champ ne declenchera pas ta logique. Autre piege : oublier trim et accepter "   " comme un vrai nom.

:::attention
Un espace seul n'est pas un nom. trim() avant de juger. Sinon tu valides du vide deguise.
:::

## Variante avancee

Desactive le bouton pendant une fausse attente d'une seconde (setTimeout), puis reactive-le. Ajoute une validation "email doit contenir un point apres le @". Documente la regle en commentaire.

## En vrai

Remplis le formulaire correctement, puis vide le nom, puis mets un email sans @, puis un message de trois lettres. A chaque fois, verifie le message et le focus. Si les trois chemins malheureux sont clairs, l'atelier tient. Montre la page a quelqu'un : comprend-il quoi corriger sans que tu parles ?

## Note de rythme

Prends le temps. Un atelier fait a fond vaut mieux que trois ateliers survoles. Si tu es presse, fais la moitie aujourd'hui et l'autre demain - mais ecris le livrable. Sans livrable, le cerveau classe ca comme "lu", pas comme "su". DanielCraft forme des gens qui livrent, meme petit.

## A toi

Termine le livrable. Puis ecris en trois lignes ce qui etait le plus dur (preventDefault, trim, affichage erreurs ?). Garde ce retour pour le prochain formulaire reel.
