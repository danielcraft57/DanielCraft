# Quiz final - Teste-toi !

Meme regle que dans tout le parcours : cherche d'abord, corrige ensuite. Ce quiz n'est pas la pour te coller une note sur le front. C'est pour verifier que **TypeScript** n'est plus un brouillard : types, annotations, interfaces, unions, fonctions, narrowing, `any` vs `unknown`, erreurs `tsc`. Chez DanielCraft, un quiz sert a cibler les chapitres a relire - pas a mesurer ta valeur humaine. Lea revoit parfois ces bases avant une demo. Max a refait le quiz un samedi. Sam l'utilise en fin de sequence.

Lis chaque question calmement. Reponds dans ta tete ou sur papier. Puis descends aux corriges. Note tes hesitations : elles valent plus que les reponses faciles. Si tu bloques sur Q9 et Q10, tu sais ou aller (narrowing / any). Si tout passe, tu peux attaquer le bravo en confiance.

## Questions

Avant de commencer, respire. Douze questions, douze checkpoints. Pas de piege volontaire. Juste le socle construit chapitre apres chapitre.

**Q1.** TypeScript, c'est surtout :
- A) Un framework UI
- B) JavaScript + types verifies avant l'execution
- C) Un remplacement de HTML

**Q2.** Que produit generalement `tsc` a partir d'un `.ts` ?
- A) Du Python
- B) Du CSS
- C) Du JavaScript (`.js`)

**Q3.** Quelle annotation declare un nombre ?
- A) `let n: number = 3`
- B) `let n: string = 3`
- C) `let n: boolean = 3`

**Q4.** Une **interface** sert surtout a :
- A) Styliser la page
- B) Decrire la forme d'un objet
- C) Remplacer npm

**Q5.** `email?: string` signifie :
- A) email obligatoire number
- B) email facultatif de type string
- C) email toujours `any`

Les cinq premieres couvrent le socle : idee TS, compilation, annotation, interface, optionnel. Si tu hesites ici, revois les chapitres 1 a 6.

**Q6.** Dans `function f(x: number): string`, le `: string` annonce :
- A) Le type du parametre
- B) Le type de retour
- C) Un fichier CSS

**Q7.** `number[]` designe :
- A) Un seul number
- B) Un tableau de numbers
- C) Une union number | string

**Q8.** Le narrowing avec `typeof x === "string"` sert a :
- A) Effacer le fichier
- B) Prouver que x est string dans la branche
- C) Activer `any`

**Q9.** Entre `any` et `unknown`, lequel force souvent une verification avant usage ?
- A) `any`
- B) `unknown`
- C) ni l'un ni l'autre

**Q10.** Face a `Type 'string' is not assignable to type 'number'`, tu devrais surtout :
- A) Ajouter `as any` tout de suite
- B) Lire types fourni vs attendu, puis corriger
- C) Supprimer TypeScript

La moitie du quiz. Fonctions, tableaux, narrowing, any, erreurs. C'est la que Lea revoit le plus avant une livraison.

**Q11.** Apres `document.querySelector("#x")`, un reflexe sain est :
- A) Ignorer le `null` possible
- B) Garder / tester avant d'utiliser
- C) Cast `as any` systematique

**Q12.** Pour un etat metier fini (brouillon / envoye / paye), on prefere souvent :
- A) `string` ouverte
- B) Une union de litteraux
- C) `any`

Les deux dernieres questions verifient DOM garde et unions de litteraux. Si tu hesitais, relis chapitres 6 et 12.

## Reponses

1. **B** - TS = JS + types verifies avant l'execution.
2. **C** - `tsc` genere du JavaScript.
3. **A** - `: number` pour un nombre.
4. **B** - L'interface decrit la forme d'un objet.
5. **B** - `?` = facultatif, ici string.
6. **B** - Apres les parentheses, c'est le retour.
7. **B** - `number[]` = tableau de numbers.
8. **B** - Narrowing = preuve dans la branche.
9. **B** - `unknown` demande une verification ; `any` desactive.
10. **B** - Lire le diagnostic, corriger le contrat / la valeur.
11. **B** - Toujours considerer `null` / absence.
12. **B** - Union de litteraux > string libre pour des etats finis.

## Score indicatif

- **0 a 5** : reprends les chapitres 1 a 7 sans te juger. Refais Q1-Q6 demain.
- **6 a 9** : socle OK, cible narrowing, `any`/`unknown`, erreurs (8-11) et DOM.
- **10 a 12** : tu as le filtre. Passe au bravo et code un petit projet perso type.

Chez DanielCraft, une mauvaise reponse est une carte de revision, pas un verdict. Lea note ses trous. Max refait seulement les questions ratees. Sam dit : "le quiz mesure un instant, pas ta valeur".
