---
title: "Adapter : faire marcher deux pieces incompatibles"
date: 2026-04-07
excerpt: "Traduire une interface pour brancher l'ancien sur le nouveau."
type: article
tags: [Design Patterns, GoF, Adapter, Structurel, TypeScript, Python, junior]
og_image: design-patterns-adapter-1200x630.jpg
series: design-patterns-serie
series_order: 7
---

# Adapter : faire marcher deux pieces incompatibles

<figure class="schema-figure">
  <img src="/assets/images/blog/schemas/dp-adapter.svg" alt="Schema Adapter" class="schema-inline" width="640" />
  <figcaption>Ancien format, adaptateur, nouveau format.</figcaption>
</figure>

**Famille :** Structurel · **Série :** Design Patterns GoF · **Article 7/24** · **Popularité :** #6 sur 23

Adapter convertit l'interface d'une classe existante en celle attendue par le client, sans modifier le code legacy.

---

## En une phrase

Adapter convertit l'interface d'une classe existante en celle attendue par le client, sans modifier le code legacy.

---

## Le problème sans ce pattern

Tu intègres une API de paiement legacy qui expose `sendPayment(amountUsd)` alors que ton domaine parle en euros via `pay(euros)`.

```typescript
// Partout dans l'app : conversion manuelle + appel direct
function checkout(amountEur: number) {
  const legacy = new LegacyPayPal();
  const usd = amountEur * 1.08;
  const r = legacy.sendPayment(usd);
  if (!r.success) throw new Error('Paiement refusé');
}
```

Chaque nouveau fournisseur = nouveau bricolage dans les controllers.

### Symptômes dans ton code

- Fichiers qui grossissent à chaque nouvelle variante.
- Tests difficiles : trop de mocks ou d'effets de bord cachés.
- Tu as peur de toucher une classe car « tout dépend de tout ».

---

## L'idée du pattern Adapter

L'**Adapter** implémente **ton** port (`PaymentPort`) et encapsule l'adaptee (SDK legacy). Le client ne voit que l'interface propre.

| Rôle | Responsabilité |
|------|----------------|
| **Client** | Appelle `PaymentPort` |
| **Target** | Interface attendue (`pay`) |
| **Adapter** | Traduit appels et formats |
| **Adaptee** | API existante non modifiable |

| Rôle | Responsabilité |
|------|----------------|
| **Client** | Checkout, service métier |
| **PaymentPort** | Interface cible |
| **PayPalAdapter** | Traduction EUR→USD |
| **LegacyPayPal** | SDK tiers |

### Analogie du quotidien

Adaptateur **prise EU → US** : l'appareil (client) reste identique ; l'adaptateur convertit le courant.

---

## Exemple complet en TypeScript

```typescript
interface PaymentPort {
  pay(euros: number): Promise<{ ok: boolean; ref?: string }>;
}

class LegacyPayPal {
  sendPayment(amountUsd: number) {
    return { success: amountUsd > 0, transactionId: `PP-${amountUsd}` };
  }
}

class PayPalAdapter implements PaymentPort {
  constructor(
    private readonly legacy: LegacyPayPal,
    private readonly eurToUsd: number,
  ) {}

  async pay(euros: number) {
    const usd = Math.round(euros * this.eurToUsd * 100) / 100;
    const result = this.legacy.sendPayment(usd);
    return { ok: result.success, ref: result.transactionId };
  }
}

async function checkout(port: PaymentPort, amount: number) {
  const r = await port.pay(amount);
  if (!r.ok) throw new Error('Paiement échoué');
  return r.ref;
}
```

### Ce qu'il faut retenir du code

- Le **client** dépend d'abstractions, pas de détails partout.
- Chaque nouvelle variante = **nouvelle classe** (ou module), pas un `if` de plus.
- Nomme tes types pour le **métier** (noms métier explicites, pas `Strategy1`).

---

## Exemple en Python

```python
from abc import ABC, abstractmethod

class PaymentPort(ABC):
    @abstractmethod
    async def pay(self, euros: float) -> dict: ...

class LegacyPayPal:
    def send_payment(self, amount_usd: float) -> dict:
        return {"success": amount_usd > 0, "transaction_id": f"PP-{amount_usd}"}

class PayPalAdapter(PaymentPort):
    def __init__(self, legacy: LegacyPayPal, eur_to_usd: float) -> None:
        self._legacy = legacy
        self._rate = eur_to_usd

    async def pay(self, euros: float) -> dict:
        usd = round(euros * self._rate, 2)
        r = self._legacy.send_payment(usd)
        return {"ok": r["success"], "ref": r["transaction_id"]}
```

---

## Quand utiliser Adapter

- Intégration SDK/API que tu ne peux pas modifier.
- Formats de données différents (XML, SOAP, binaire).
- Plusieurs clients doivent partager la même traduction.

---

## Quand ne pas utiliser Adapter

- Tu contrôles le code legacy et peux le refactoriser directement.
- Un simple mapper fonction suffit (pas besoin d'objet Adapter).

---

## Erreurs fréquentes des juniors

- Adapter qui fait de la logique métier (doit seulement traduire).
- Oublier les erreurs du adaptee (timeouts, codes).
- Créer un adapter par appel au lieu d'un par service.

---

## Patterns proches

- **Facade** : Simplifie un sous-système entier
- **Decorator** : Ajoute un comportement, ne change pas l'interface cible

---

## Comparaisons utiles

| Pattern | Quand |
|---------|-------|
| Adapter | Interface incompatible |
| Facade | Sous-système complexe, même techno |
| Decorator | Même interface, couche en plus |

---

## Dans le monde réel

Stripe SDK derrière ton port interne. Axios + transform pour API REST legacy. Lecteurs de fichiers Node (`fs` streams).

---

## Questions fréquentes (FAQ)

**C'est obligatoire en entretien ?** Non — on teste surtout ta capacité à reconnaître le problème. Le nom Adapter aide à communiquer en équipe.

**Ça remplace les frameworks ?** Non — React, Express ou Spring implémentent souvent ces idées pour toi. Comprendre Adapter te permet de les utiliser correctement.

**Je dois tout refactoriser ?** Non — applique le pattern quand la douleur est réelle (nouveaux bugs à chaque feature).

---

## Mini test unitaire (idée)

```typescript
// Exemple de test : mocke les collaborateurs, vérifie le comportement public
describe('Adapter', () => {
  it('fonctionne avec une variante', () => {
    // Arrange → Act → Assert
  });
});
```

Adapte ce squelette à ton framework (Jest, Vitest, pytest).

---

## Pas à pas : implémenter en 5 étapes

1. **Nomme le problème** — est-ce vraiment Adapter ?
2. **Dessine les rôles** sur papier (client, abstraction, implémentations).
3. **Écris un test** qui décrit le comportement attendu.
4. **Implémente une variante** — valide avant d'en ajouter d'autres.
5. **Documente en équipe** — « ici on utilise Adapter parce que… ».

---

## Checklist code review

- [ ] Le client ne dépend pas de classes concrètes inutiles
- [ ] Pas de sur-abstraction sur un cas unique
- [ ] Tests sur chaque variante / handler / état
- [ ] Nommage métier clair

---

## Exercice pratique (25–35 min)

Branche `StripeAdapter` et `PayPalAdapter` sur le même `PaymentPort`. Teste le checkout avec un mock sans appeler l'API réelle.

---

## Résumé

Adapter = traduire une interface incompatible — le client reste propre.

---

## Navigation dans la série

- Précédent : [Decorator](/blog/articles/design-patterns-decorator.html)
- Suivant : [Facade](/blog/articles/design-patterns-facade.html)
