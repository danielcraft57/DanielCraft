---
title: "Visitor : ajouter une operation sans toucher les classes"
date: 2026-04-23
excerpt: "Une nouvelle action qui visite chaque type d'objet, sans modifier leur code."
type: article
tags: [Design Patterns, GoF, Visitor, Comportemental, TypeScript, Python, junior]
og_image: design-patterns-visitor-1200x630.jpg
series: design-patterns-serie
series_order: 23
---

# Visitor : ajouter une operation sans toucher les classes

<figure class="schema-figure">
  <img src="/assets/images/blog/schemas/dp-visitor.svg" alt="Schema Visitor" class="schema-inline" width="640" />
  <figcaption>Objets visites par un visiteur.</figcaption>
</figure>

**Famille :** Comportemental · **Série :** Design Patterns GoF · **Article 23/24** · **Popularité :** #22 sur 23

Visitor te permet d'**ajouter une opération** sur une famille d'objets (souvent une hiérarchie stable) **sans modifier** le code de chaque classe — l'opération vit dans le visiteur.

---

## En une phrase

Visitor ajoute des opérations sur une hiérarchie sans la modifier.

---

## Le problème sans ce pattern

Tu as un AST (arbre syntaxique) ou un document : `Heading`, `Paragraph`, `Image`… Tu veux `exportPdf`, puis `exportHtml`, puis `compterMots`. Sans Visitor, tu ajoutes une méthode sur **chaque** classe à chaque nouvelle opération. Les fichiers métier gonflent ; Open/Closed souffre.

Le `switch (node.type)` dispersé pose le même problème sous une autre forme : chaque opération recopie la liste des types, et TypeScript / le compilateur ne te sauvent que si tu as une union discriminée bien typée. Visitor (ou son équivalent exhaustif) centralise cette liste *par opération*.

### Symptômes dans ton code

- Quinze classes touchées pour une seule feature « export ».
- Gros `switch (node.type)` dispersés et incomplets.
- Logique d'affichage / export / analyse mélangée dans les nœuds.
- Peur d'ajouter un type : il faudrait mettre à jour toutes les opérations.

---

## L'idée du pattern Visitor

Double dispatch classique : l'élément appelle `visitor.visitX(this)`, le visiteur implémente `visitHeading`, `visitParagraph`, etc.

| Rôle | Responsabilité |
|------|----------------|
| **Element** | `accept(visitor)` |
| **ConcreteElement** | Délègue au bon `visit…` |
| **Visitor** | Interface des opérations par type |
| **ConcreteVisitor** | Export PDF, stats, validation… |

Les éléments restent « bêtes » (structure) ; les visiteurs portent le comportement transversal. C'est l'inverse du réflexe junior « j'ajoute une méthode sur la classe » : ici, tu assumes que la famille de types bouge peu, et que ce sont les *actions* (export, stats, lint) qui se multiplient.

### Analogie du quotidien

Un **immeuble** inspecté par plusieurs experts : l'électricien, le plombier, le contrôleur incendie. Le bâtiment (hiérarchie de pièces) ne change pas. Chaque expert (Visitor) parcourt les mêmes pièces mais fait un métier différent. Tu ajoutes un expert acoustique sans reconstruire l'immeuble.

---

## Exemple en TypeScript

```typescript
interface DocVisitor {
  visitHeading(text: string): void;
  visitParagraph(text: string): void;
}

interface DocNode {
  accept(v: DocVisitor): void;
}

class Heading implements DocNode {
  constructor(public text: string) {}
  accept(v: DocVisitor) { v.visitHeading(this.text); }
}

class Paragraph implements DocNode {
  constructor(public text: string) {}
  accept(v: DocVisitor) { v.visitParagraph(this.text); }
}

class MarkdownVisitor implements DocVisitor {
  private out: string[] = [];
  visitHeading(t: string) { this.out.push(`# ${t}`); }
  visitParagraph(t: string) { this.out.push(t); }
  result() { return this.out.join('\n\n'); }
}

const doc: DocNode[] = [new Heading('Salut'), new Paragraph('Monde')];
const md = new MarkdownVisitor();
for (const node of doc) node.accept(md);
console.log(md.result());
```

Pour un export HTML, tu ajoutes `HtmlVisitor` — sans retoucher `Heading` / `Paragraph`.

### Version Python minimale

```python
class MarkdownVisitor:
    def __init__(self) -> None:
        self.out: list[str] = []

    def visit_heading(self, text: str) -> None:
        self.out.append(f"# {text}")

    def visit_paragraph(self, text: str) -> None:
        self.out.append(text)
```

(En Python, on utilise souvent `functools.singledispatch` ou un `match` sur des dataclasses — l'esprit reste « opération hors des nœuds ».)

---

## Quand utiliser Visitor

- Hiérarchie d'éléments **stable**, opérations **nombreuses** et changeantes.
- Compilateurs, outils d'analyse, exports multiples, reporting.
- Tu veux centraliser une opération transversale.

## Quand ne pas utiliser Visitor

- Tu ajoutes souvent de **nouveaux types** d'éléments → chaque Visitor explose.
- Une seule opération simple : une méthode sur la classe suffit.
- Équipe junior + pattern trop cérébral pour le gain.

---

## Erreurs fréquentes des juniors

- Oublier `accept` → plus de double dispatch, juste des `if`.
- Visiteur god-object qui fait dix métiers.
- Muter l'arbre pendant la visite sans règles.
- Confondre avec **Iterator** (parcours) : Visitor = *quoi faire* sur chaque type.

---

## Patterns proches

- **Iterator** : parcourt ; Visitor *opère* en parcourant.
- **Strategy** : algorithme interchangeable pour *un* contexte, pas une famille de types.
- **Composite** : souvent visité (arbres UI / documents).

---

## Dans le monde réel

Compilateurs (visiteurs de typage, codegen), ESLint/AST browsers, serializers, outils de doc. En TypeScript, un `switch` exhaustif sur une union discriminée est parfois un « Visitor léger » sans classes.

Exemple concret : un outil interne qui parcourt ton catalogue produits (`Simple`, `Bundle`, `Subscription`) pour générer un flux XML marketplace, puis un autre visiteur pour un export comptable. Les classes produit restent stables ; chaque nouveau canal d'export = un nouveau visiteur, pas une invasion de méthodes `toXml` / `toLedger` dans le domaine.

---

## Questions fréquentes (FAQ)

**C'est obligatoire en entretien ?** Rare — plutôt pour montrer que tu connais Open/Closed sur les opérations.

**Ça remplace les frameworks ?** Non — les libs d'AST l'utilisent déjà.

**Je dois tout refactoriser ?** Non — introduis Visitor quand la 3ᵉ opération force à toucher toutes les classes.

---

## Checklist code review

- [ ] Chaque élément a un `accept` cohérent
- [ ] Nouveaux visiteurs n'exigent pas de modifier les éléments
- [ ] Types d'éléments peu fréquents à étendre (sinon autre design)
- [ ] Tests par visiteur (export, stats…)

---

## Exercice pratique (25–35 min)

Modélise `Heading` + `Paragraph`. Écris un visiteur Markdown et un visiteur « compteur de mots ». Ajoute un nœud `Image` et constate ce qu'il faut mettre à jour (spoiler : tous les visiteurs).

---

## Résumé

- Visitor = nouvel expert qui inspecte sans reconstruire le bâtiment.
- Idéal si les **types sont stables** et les **opérations bougent**.
- Coût : ajouter un type d'élément touche tous les visiteurs.

---

## Navigation dans la série

- Précédent : [Memento](/blog/articles/design-patterns-memento.html)
- Suivant : [Interpreter](/blog/articles/design-patterns-interpreter.html)
