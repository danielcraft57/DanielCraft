# Chapitre 5 - Prompts et system prompts : briefer comme un pro

Un **prompt**, c'est ta demande. Pas une formule magique. Pas une incantation. Un brief. Plus il est clair, plus la reponse a des chances d'etre utile. Chez DanielCraft, on enseigne un squelette simple que tu peux enrichir : role, tache, public, contraintes, format, et faits fournis. Ensuite, on ajoute l'idee du **system prompt** : la consigne durable qui cadre le comportement de l'assistant avant meme ta question du jour.

:::retenir
Prompt = brief clair (role, tache, public, contraintes, format, faits). System prompt = politique de maison durable.
:::

## Le squelette du prompt utile

**Role** : qui doit "jouer" le modele (conseiller sober pour artisans, prof de 6e, relecteur exigeant). Tache : ce que tu veux exactement (plan, mail, checklist, reformulation). Public : pour qui c'est ecrit. Contraintes : longueur, ton, interdits, niveau de jargon, langue. Format : puces, tableau, email pret a envoyer, sections numerotees. Faits : ce que tu apportes (prix, dates, details vrais) pour eviter l'invention.

Exemple pour Max. Mauvais prompt : `ameliorer mon devis`. Bon prompt :

```text
Role : relecteur pour un artisan plombier.
Tache : reecrire le devis ci-dessous.
Public : particulier presse, francais simple.
Contraintes :
- garde les prix exacts (ne rien inventer)
- 12 lignes max
- pas de promesse de delai si absente des notes
Format : texte pret a coller dans un email.
Notes brutes :
- debouchage evier cuisine
- deplacement 45 EUR
- main d oeuvre 1h30 a 55 EUR/h
```

Compare les deux sorties une fois. Tu verras clarte, prix fideles, moins de blabla.

Mini-appel API (schema pedagogique, adapte a ton fournisseur) :

```python
prompt = """Tu es relecteur pour un artisan.
Reecris le devis en francais simple, 12 lignes max.
Garde les prix exacts. Notes : debouchage, 45 EUR deplacement, 1h30 a 55 EUR/h."""

messages = [
    {"role": "system", "content": "Francais simple. N'invente aucun prix."},
    {"role": "user", "content": prompt},
]
# reponse = client.chat.completions.create(
#     model="ton-modele",
#     messages=messages,
#     temperature=0.2,
# )
```

:::astuce
"Tu es relecteur pour un artisan. Reecris ce devis en francais simple, 12 lignes max, garde mes prix exacts." bat "ameliorer mon devis".
:::

## System prompt : le cadre durable

Dans beaucoup d'outils (API, assistants custom, "projets", "GPTs", instructions persistantes), tu peux definir une consigne systeme : un texte qui dit comment l'assistant doit se comporter a chaque echange. Exemple : "Tu reponds toujours en francais simple. Tu signales les incertitudes. Tu ne inventes pas de chiffres. Tu proposes d'abord un plan court puis le detail si on te le demande."

Le system prompt n'est pas une baguette. C'est une politique de maison. Il reduit les derives de style et les oublis. Il ne remplace pas un bon prompt de tache. Lea met dans ses instructions : "Ecris comme une freelance web francaise, ton clair, pas de marketing agressif, toujours proposer 2 options." Sam met : "Niveau college, analogies du quotidien, jamais de contenu sensible non demande."

## Iterer sans tourner en rond

Premier jet : demande large mais cadree. Deuxieme : "garde la structure, coupe le blabla, renforce l'exemple 2". Troisieme : "maintenant version plus courte pour un SMS". L'**iteration** intelligente bat le "regenerer" aveugle. Si ca part en vrille, nouveau fil + brief reconstitue. Ton **contexte** restera propre.

## Techniques simples qui marchent

Donne un exemple de ton style ("ecris comme ceci : ..."). Demande des variantes puis choisis. Impose "si information manquante, pose 3 questions avant de rediger". Demande une auto-critique : "liste 5 faiblesses de ta reponse". Separe clairement : "CONTEXTE :" puis "DEMANDE :". Pour le mode strict, ajoute "n'invente aucune source ; dis inconnu".

:::astuce
Separe critique et reecriture : "liste objections d'abord" puis "corrige uniquement les points 2 et 5".
:::

## Ce qu'il ne faut pas faire

Prompt vide de sens. Prompt qui melange cinq taches sans priorite. Prompt qui demande "des sources academiques" sans intention de les ouvrir. Prompt qui colle des donnees sensibles "parce que ce sera plus perso". Prompt hostile ("tu es nul, recommence") : inutile. Mieux vaut preciser le critere manque.

## Erreur classique

Croire qu'un mega-prompt de quatre pages est toujours mieux. Parfois tu noies le modele. Mieux vaut un brief net + pieces jointes utiles. Autre erreur : mettre toute la politique dans chaque message au lieu d'utiliser les instructions persistantes quand elles existent. Tu te fatigues, et tu oublies une regle sur deux.

## En vrai

Prends une tache reelle. Ecris un mauvais prompt en une ligne. Puis reecris-le avec le squelette. Compare les deux reponses. Note trois differences concretes (clarte, utilite, inventions).

## A toi

Cree ton "prompt signature" en 8 a 12 lignes : identite, public, ton, 3 interdits, format prefere. Colle-le dans les instructions de ton outil si possible. Sinon, garde-le dans un fichier texte a recopier.

## Anatomie d'un system prompt solide

Un bon system prompt dit qui tu es (ou qui l'assistant doit etre pour toi), pour qui tu ecris, quel ton, quelles langues, quels interdits, comment gerer l'inconnu, quel format par defaut, et parfois quelles questions poser avant de rediger. Il evite les romans. Il evite aussi le vide. Dix a vingt lignes suffisent souvent. Au-dela, tu risques les contradictions ("sois concis" + "developpe toujours").

Exemple compact pour une TPE : "Tu aides une petite entreprise francaise. Francais simple. Pas de jargon. N'invente aucun prix ni delai. Si l'info manque, pose des questions. Structure : d'abord reponse courte, puis details. Signale les incertitudes clairement."

## Prompts de relecture

Souvent sous-estimes : "Relis ce texte comme un client mefiant. Liste objections, ambiguites, promesses dangereuses. Ne reecris pas encore." Puis seulement : "Corrige uniquement les points 2 et 5." Tu separes critique et reecriture. Tu gardes le controle.

## Bibliotheque personnelle

Range tes prompts par intention : Ecrire, Resumer, Ideer, Expliquer, Roleplay client, Anti-hallucination. Une bibliotheque de huit prompts battent un dossier de deux cents copies de "prompt miracle" trouvees sur les reseaux.

## Scene de terrain (developpee)

Imagine une matinee ordinaire. Tu ouvres l'outil, tu as une tache, tu as dix minutes. Sans methode, tu tapes une phrase vague, tu obtiens un texte poli, tu colles, tu regrettes. Avec methode, tu prends deux minutes pour cadrer : but, public, contraintes, faits, interdits. Tu generes. Tu verifies les faits critiques. Tu corriges le ton. Tu ranges le prompt si ca a marche. Le resultat n'est pas seulement "plus joli". Il est plus sur, plus reutilisable, plus respectueux des gens dont les donnees pourraient trainer dans le fil.

Cette difference se voit peu le premier jour. Elle se voit au bout d'un mois, quand tu as une bibliotheque de huit prompts, une charte donnees, une grille d'evaluation, et zero incident majeur. C'est ca que ce chapitre prepare : pas l'effet wow, l'effet fiable.

## Pieges subtils

Le piege du perfectionnisme : retoucher le prompt une heure pour un mail de huit lignes. Le piege de la paresse : ne jamais retoucher. Le piege de la nouveaute : changer d'outil chaque semaine. Le piege de la peur : ne rien automatiser jamais, meme le bas risque. Le juste milieu se construit en ecrivant tes regles personnelles et en les testant. Ce livre te donne des regles candidates ; toi tu les adaptes a ton metier, ton risque, ton budget.

## Lien avec le reste du livre

Ce que tu lis ici se branche sur les tokens (ne noie pas), le contexte (un fil propre), la temperature (strict ou creatif), le system prompt (cadre durable), les hallucinations (verifier), le multimodal (entree propre), le RAG (documents ranges), les agents (freins), l'evaluation (grille), les couts (ordre de grandeur), la securite (2FA, secrets). Tu n'as pas a tout activer d'un coup. Active une brique, solidifie, ajoute.

## Pour aller plus loin sans te perdre

Tu n'as pas a tout maitriser d'un coup. Reviens a ce chapitre quand tu butes sur un cas reel. Relis l'erreur classique. Refais le "A toi". Chez DanielCraft, on prefere trois relectures actives a une lecture passive de vingt pages. Si un paragraphe te semble encore flou, reformule-le a voix haute avec ton propre exemple. Des que ca passe a l'oral, c'est que c'est entre. Ensuite seulement, passe au chapitre suivant. Cette discipline lente cree une competence rapide sur la duree - le contraire du binge de tutos oublies le lendemain.
