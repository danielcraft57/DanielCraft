# Chapitre 19 - Bonnes pratiques deep learning

Les bonnes pratiques ne sont pas du folklore. Ce sont des garde-fous contre l'enthousiasme, l'oubli, et le "ca marche sur mon laptop". Chez DanielCraft, on les range en avant / pendant / apres, plus un mot sur les pipelines mixtes et la reproductibilite minimale.

Tu peux les transformer en checklist de 12 cases. C'est l'exercice de fin. L'objectif n'est pas la perfection documentaire : c'est eviter les erreurs deja payees par d'autres.

:::retenir
Valider le besoin, reutiliser, mesurer, regulariser, inspecter les echecs, versionner, monitorer. Sobriete > theatre.
:::

## Ce que ce n'est pas

Ce n'est pas une norme ISO a imprimer pour faire joli. Ce n'est pas non plus "ralentir pour ralentir". C'est accelerer juste : moins de retours catastrophiques, plus de cycles utiles. Et ce n'est pas reserve aux grandes equipes : Ines seule peut cocher l'essentiel.

## Avant

Valider que le deep learning est necessaire. Chercher un modele preentraine. Estimer donnees et calcul. Definir metriques et risques. Preparer un set de validation propre. Ecrire un go/no-go. Clarifier les labels avec le metier. Lea refuse de demarrer un sprint vision sans ces points ecrits.

## Pendant

Commencer petit. Logger loss et metriques. Early stopping. Regulariser. Inspecter les echecs (les vrais fichiers, pas seulement la moyenne). Ne pas toucher au test final trop souvent. Documenter hyperparametres et versions. Changer une chose a la fois. Comparer a une baseline. Arreter quand la validation stagne. Sam appelle ca "experimentation sobre" - le mot compte moins que le geste.

:::idee
Garde un journal d'experiences en 5 colonnes : hypothese, changement, metrique, decision, date. Une demi-heure de rangement economise des jours.
:::

## Apres

Evaluer hors distribution. Monitorer. Prevoir reentrainement. Versionner. Separer experiences jouets et systeme de production. Informer les utilisateurs des limites. Prevoir un repli humain. Mesurer le cout d'inference reel, pas seulement le cout d'entrainement. Max veut savoir ce qui se passe quand le telephone change ; Ines aussi.

## Usage LLM couple

Si ton systeme mele CNN + LLM + regles, teste chaque brique, puis l'ensemble. Un pipeline opaque a trois etages multiplie les hallucinations operationnelles. Lea exige un compte-rendu d'erreur par etage. Chez DanielCraft, "ca a l'air fluide de bout en bout" n'est pas un critere d'acceptation.

## Petite histoire

Ines a perdu une apres-midi a "ca marche plus". Pas de graine, pas de version donnees, pas de config sauvee. Elle a institue une reproductibilite minimale : graine, version code, version donnees, config, commit, metriques. Depuis, les regressions se discutent avec des faits. Sam a vole la checklist pour sa classe.

## Reproductibilite minimale

Graine, version code, version donnees, config, commit, metriques. Sans ca, tu ne sauras pas pourquoi "ca marche plus". Ce n'est pas du luxe enterprise. C'est de l'hygiene. Ajoute les droits / licences des modeles fondation si tu transfers.

## Erreur classique

Tout faire a la fois. Ne jamais inspecter un echec. Optimiser le test. Oublier le monitoring apres la demo. Documenter seulement quand un manager crie. Ou croire que les bonnes pratiques ralentissent les "vrais" talents.

:::attention
Une demo sans protocole n'est pas un produit. C'est une anecdote couteuse.
:::

## En vrai

Cree ta checklist 12 cases a partir de ce chapitre (avant / pendant / apres melanges). Imprime-la ou epingle-la.

## A toi

Coche la checklist sur ton prochain essai, meme toy. Une case refusee = une phrase "pourquoi j'accepte le risque". Si tu ne peux pas l'ecrire, coche autrement : en faisant le geste.

## Culture de communication

Apprends a dire "non" a un modele inutile. Apprends a dire "pas encore" quand les labels manquent. Apprends a dire "voici les limites" quand tu presentes un score. Cette honnetete te rend plus credible que n'importe quel jargon. C'est la derniere bonne pratique, et souvent la plus rentable.

## Les 12 cases (modele)

1) Besoin DL valide. 2) Baseline / preentraine cherche. 3) Metriques et risques ecrits. 4) Val propre. 5) Go/no-go. 6) Journal d'experiences. 7) Early stopping. 8) Inspection d'echecs. 9) Test rare. 10) Versions (code/donnees/config). 11) Monitoring prevu. 12) Limites communiquees. Coche. Si tu sautes, ecris pourquoi.

## Separer jouet et production

Un notebook d'exploration peut etre sale. Un systeme qui touche un client ne peut pas heriter du sale sans rituel. Promotion volontaire : code range, metriques, rollback, responsable. Chez DanielCraft, confondre les deux est le classique qui coute le plus cher apres la demo.
