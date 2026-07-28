# Chapitre 2 - Installer et lancer tsc

Pour ecrire du TypeScript, tu as besoin d'un outil qui lit les fichiers `.ts` et produit du `.js`. Cet outil s'appelle souvent **`tsc`** (TypeScript Compiler). Tu peux l'installer via npm (`npm install -g typescript` ou en local dans un projet). Ensuite, tu ecris `app.ts`, tu lances `tsc app.ts`, et tu obtiens `app.js`. Chez DanielCraft, on reste volontairement leger : pas de parcours webpack de trois heures. Lea travaille souvent avec un petit dossier et un `tsconfig.json` simple. Max a commence sans config, juste `tsc compteur.ts`. Sam montre les deux chemins : fichier isole, puis projet avec config.

Le fichier **`tsconfig.json`** dit a `tsc` comment se comporter : quel dossier compiler, quel niveau de strictesse, ou mettre le JS genere. Tu n'as pas besoin de connaitre toutes les options. Quelques intuitions suffisent : `strict` te protege plus, `outDir` range le JS ailleurs, `rootDir` dit d'ou partent les sources. Si la config manque, `tsc` peut quand meme compiler un fichier passe en argument. L'important, c'est le geste : ecrire, compiler, lire les erreurs, corriger.

:::retenir
Tu ecris en `.ts`. `tsc` verifie et genere du `.js`. `tsconfig.json` guide le projet sans etre magique.
:::

## Ce que ce n'est pas

Ce n'est pas obligatoire d'installer vingt extensions VS Code avant d'ecrire une ligne. Ce n'est pas "Vite ou rien". Ce n'est pas un cours npm avance. Ce n'est pas non plus "je copie une config Stack Overflow de 80 lignes". Une config courte et comprise bat une usine opaque. Et ce n'est pas paniquer si le premier `tsc` affiche rouge : c'est normal, c'est le metier.

## Les fichiers que tu touches

Un fichier source : `compteur.ts`. Un fichier de sortie : `compteur.js` (genere). Parfois un `tsconfig.json` a la racine. Lea ajoute souvent un script npm `"build": "tsc"` pour ne pas retaper la commande. Max double-clique encore sur sa ligne de commande. Sam insiste : ouvre le `.js` genere une fois pour voir que ce n'est "que" du JavaScript. Le mystere tombe.

```json
{
  "compilerOptions": {
    "target": "ES2020",
    "strict": true,
    "outDir": "dist",
    "rootDir": "src"
  },
  "include": ["src/**/*"]
}
```

Tu n'as pas a memoriser chaque cle. Retiens : `strict` = plus de garde-fous. `outDir` = le JS va dans `dist/`. `include` = quels fichiers regarder.

:::astuce
Commence par un seul fichier `.ts` et `tsc monfichier.ts`. Ajoute `tsconfig.json` quand le dossier grandit.
:::

## Petite histoire

Lea a perdu une heure a chercher pourquoi "rien ne changeait" dans le navigateur. Elle editait le `.ts` mais rechargeait un vieux `.js`. Depuis, elle verifie la date du fichier genere ou elle lance toujours `tsc` avant le refresh. Max a nomme son fichier `app.TS` en majuscules sur un systeme tatillon ; Sam lui a montre que la casse compte. DanielCraft repete : le flux ecrire -> compiler -> tester est le vrai IDE, pas la couleur de theme.

## Erreur classique

Installer TypeScript globalement, oublier de relancer le terminal, puis croire que `tsc` n'existe pas. Ou editer le `.js` a la main et perdre les changements au prochain compile. Autre piege : coller une config "pro" sans comprendre `strict`, puis abandonner face a une pluie d'erreurs. Lea desactive une option a la fois si besoin, mais elle ne desactive pas le cerveau. Lis le message. Corrige une erreur. Relance.

:::attention
Ne modifie pas le `.js` genere a la main. Tu ecris dans le `.ts`, tu recompiles. Sinon tu ecrases ton travail.
:::

## En vrai

Cree un dossier `hello-ts`. Ecris `hello.ts` avec `const msg: string = "salut"; console.log(msg);`. Lance `tsc hello.ts`. Ouvre `hello.js`. Compare. Note une difference (souvent le typage disparait). Tu as vu le coeur du pipeline.

## Le geste quotidien

Lea ouvre son terminal, lance `tsc`, lit la premiere erreur, corrige, relance. Elle ne cherche pas a "tout configurer parfaitement" avant d'ecrire la premiere ligne. Max a perdu du temps a choisir entre dix templates de starter ; Sam lui a dit de creer un dossier vide et un fichier `.ts`. Chez DanielCraft, le starter parfait est celui que tu comprends. Si tu ne sais pas ce que fait une option de `tsconfig`, ne la copie pas.

Quand le projet grandit, tu ranges les sources dans `src/` et la sortie dans `dist/`. Tu ajoutes un script npm seulement si tu en as besoin. Tu peux aussi lancer `tsc --watch` pour recompiler a chaque sauvegarde : pratique pendant un atelier. L'important reste le meme : le fichier que tu edites est le `.ts`, le fichier que tu charges dans le navigateur est le `.js` a jour.

Pense aussi a la version de TypeScript. Un message d'erreur un peu different selon les versions, ce n'est pas grave. Le vocabulaire reste proche : type incompatible, propriete manquante, objet possiblement undefined. Apprends a lire ces trois familles et tu seras deja autonome.

## A toi

Ecris `age.ts` avec `let age: number = 29;` puis `console.log(age);`. Compile. Change volontairement `age = "vingt";`, recompile, lis l'erreur sans paniquer. Remets le nombre. Chez DanielCraft, ce premier cycle tsc vaut plus qu'un tutorial d'install de trente minutes.
