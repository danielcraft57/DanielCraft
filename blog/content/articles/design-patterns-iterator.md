---
title: "Iterator : parcourir sans tout reveler"
date: 2026-04-12
excerpt: "Avancer element par element sans exposer la structure interne."
type: article
tags: [Design Patterns, GoF, Iterator, Comportemental, TypeScript, Python, junior]
og_image: design-patterns-iterator-1200x630.jpg
series: design-patterns-serie
series_order: 12
---

# Iterator : parcourir sans tout reveler

<figure class="schema-figure">
  <img src="/assets/images/blog/schemas/dp-iterator.svg" alt="Schema Iterator" class="schema-inline" width="640" />
  <figcaption>Collection, iterator, next, next, fin.</figcaption>
</figure>

**Famille :** Comportemental · **Série :** Design Patterns GoF · **Article 12/24** · **Popularité :** #11 sur 23

Iterator te laisse avancer élément par élément dans une collection **sans** connaître sa structure interne (tableau, arbre, liste chaînée, flux réseau…).

---

## En une phrase

Iterator accède aux éléments d'une collection sans exposer sa structure.

---

## Le problème sans ce pattern

Sans Iterator, le client manipule directement les détails : `.next` sur une liste chaînée, indices sur un tableau, récursion sur un arbre. Change la structure → tu casses tous les appels. Tu mélanges aussi **parcours** et **métier** dans le même fichier.

### Symptômes dans ton code

- Boucles qui connaissent trop bien la représentation interne.
- Impossible de changer Array → Set / Map sans tout réécrire.
- Deux parcours concurrents qui se marchent dessus (curseur partagé).
- Tests qui doivent reconstruire toute la structure juste pour lire trois éléments.

---

## L'idée du pattern Iterator

Tu exposes une interface simple : « donne-moi le suivant » / « y en a-t-il encore ? ». La collection crée son itérateur ; le client ne voit que cette façade. En JavaScript/TypeScript, `for…of` et les générateurs (`function*`) sont déjà des Iterator. En Python, `iter()` / `__next__` et les générateurs font le même travail.

| Rôle | Responsabilité |
|------|----------------|
| **Iterable / Aggregate** | Collection ; fabrique un Iterator |
| **Iterator** | Curseur : `next`, `hasNext` (ou équivalent) |
| **Client** | Consomme les éléments, ignore la structure |

### Analogie du quotidien

Une **télécommande** : chaîne +, chaîne −. Tu ne ouvres pas le boîtier du décodeur pour changer de chaîne. Tu avances, tu recules, tu t'arrêtes — peu importe si les chaînes sont en câble, satellite ou IPTV. L'Iterator, c'est cette télécommande pour tes données.

---

## Exemple en TypeScript

```typescript
class BookCollection implements Iterable<string> {
  private books: string[] = [];
  add(b: string) { this.books.push(b); }
  *[Symbol.iterator]() {
    for (const b of this.books) yield b;
  }
}

const shelf = new BookCollection();
shelf.add('Clean Code');
shelf.add('Design Patterns');
for (const title of shelf) {
  console.log(title); // parcours uniforme
}
```

Le client n'accède jamais à `books`. Demain, tu stockes dans un arbre ou un fichier : tant que `Symbol.iterator` reste correct, les boucles ne bougent pas.

### Version Python minimale

```python
class BookCollection:
    def __init__(self):
        self._books = []

    def add(self, title: str) -> None:
        self._books.append(title)

    def __iter__(self):
        for title in self._books:
            yield title

for title in BookCollection():  # ou après add()
    print(title)
```

---

## Quand utiliser Iterator

- Plusieurs structures de données derrière la même API de parcours.
- Besoin de **plusieurs curseurs** indépendants (deux boucles en parallèle).
- Collections paresseuses / flux (pages d'API, fichiers ligne à ligne).
- Tu veux cacher une implémentation complexe (arbre, graphe).

## Quand ne pas utiliser Iterator

- Un simple tableau lu une fois dans un script jetable.
- Tu as besoin d'accès aléatoire indexé partout (`arr[i]`) — un Iterator séquentiel ne remplace pas ça.
- Sur-abstraction : wrapper inutile autour d'un `for` déjà clair.

---

## Erreurs fréquentes des juniors

- Muter la collection pendant l'itération sans règle claire.
- Exposer quand même la structure « pour aller plus vite ».
- Confondre Iterator (parcours) et **Visitor** (opération sur chaque type de nœud).
- Oublier que `for…of` consomme l'itérateur : un second passage peut être vide si tu ne recrées pas l'itérateur.

---

## Patterns proches

- **Composite** : souvent itéré (arbre de composants).
- **Visitor** : ajoute une *opération* ; Iterator se contente de *parcourir*.
- **Generator / yield** : forme moderne et légère d'Iterator dans JS et Python.

---

## Dans le monde réel

`Array`, `Map`, `Set`, jQuery-like collections, cursors de base de données, `ReadableStream`… Dès que tu fais `for (const x of something)`, tu utilises déjà le pattern. Les frameworks de data (ORM, pandas) exposent aussi des itérateurs pour ne pas charger tout en mémoire.

Un cas fréquent en backend : paginer une API (`while hasNext { fetch page }`) derrière un générateur. Le reste du code consomme `for item in all_items()` sans savoir s'il y a 1 ou 40 pages HTTP. Tu as isolé le « comment avancer » du « quoi faire de chaque élément ».

---

## Questions fréquentes (FAQ)

**C'est obligatoire en entretien ?** Rarement sous ce nom — on teste plutôt : « comment parcourir sans exposer l'interne ? »

**Ça remplace les frameworks ?** Non — React, Express ou Spring s'en servent déjà. Comprendre Iterator t'aide à écrire des API cohérentes.

**Je dois tout refactoriser ?** Non — introduis un Iterator quand le client dépend trop de la structure.

---

## Checklist code review

- [ ] Le client n'accède pas aux champs internes de la collection
- [ ] Plusieurs itérateurs peuvent coexister si besoin
- [ ] Comportement documenté si la collection mute pendant le parcours
- [ ] Nommage métier clair (`BookCollection`, pas `MyIteratorThing`)

---

## Exercice pratique (25–35 min)

Crée une collection « playlist » (tableau interne). Expose uniquement un Iterator / générateur. Ajoute ensuite une variante « ordre aléatoire » sans changer le code client qui fait `for…of`.

---

## Résumé

- Iterator = télécommande : avancer sans ouvrir la boîte.
- Sépare **parcours** et **structure**.
- Les langages modernes l'ont intégré (`for…of`, générateurs) — apprends à le *concevoir* quand tu crées tes propres collections.

---

## Navigation dans la série

- Précédent : [Builder](/blog/articles/design-patterns-builder.html)
- Suivant : [State](/blog/articles/design-patterns-state.html)
