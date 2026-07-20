---
title: "Kubernetes : reglages et secrets hors de l'image"
date: 2025-01-16
excerpt: "ConfigMaps pour la config visible, Secrets pour ce qui doit rester cache."
type: article
tags: [Kubernetes, ConfigMap, Secret, configuration]
series: kubernetes-serie
series_order: 4
og_image: k8s-configmaps-secrets-1200x630.jpg
---

# Kubernetes : reglages et secrets hors de l'image

<figure class="schema-figure">
  <img src="/assets/images/blog/schemas/k8s-config-secrets.svg" alt="Schema ConfigMaps et Secrets" class="schema-inline" width="640" />
  <figcaption>Config non secrete vs secrets proteges.</figcaption>
</figure>

Tu ne veux pas rebuilder ton image Docker à chaque changement de configuration : une URL de base de données, un niveau de log, une feature flag. Kubernetes sépare le **code** (image) de la **configuration** (ConfigMaps et Secrets). C'est un principe fondamental du Twelve-Factor App, adapté au monde conteneurisé.

## ConfigMaps : la configuration non sensible

Les ConfigMaps stockent des paires clé/valeur ou des fichiers de configuration complets. Elles sont pensées pour tout ce qui n'est pas secret : URL de services internes, niveau de log, feature flags, textes de messages.

### Exemple et injection en variables d'environnement

```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: api-config
data:
  APP_ENV: "production"
  LOG_LEVEL: "info"
  API_BASE_URL: "https://api.interne.svc.cluster.local"
```

Dans le Deployment :

```yaml
spec:
  containers:
    - name: api
      envFrom:
        - configMapRef:
            name: api-config
```

Le conteneur reçoit `APP_ENV`, `LOG_LEVEL` et `API_BASE_URL` comme variables d'environnement. Tu modifies la ConfigMap, tu redémarres les pods (ou tu relies sur un mécanisme de reload), et la nouvelle config s'applique — sans rebuild d'image.

### Monter une ConfigMap comme fichiers

Pour une config au format fichier (`nginx.conf`, `app.yaml`, `settings.json`) :

```yaml
volumeMounts:
  - name: config-volume
    mountPath: /app/config
    readOnly: true

volumes:
  - name: config-volume
    configMap:
      name: app-config
```

Chaque clé de la ConfigMap devient un fichier dans `/app/config`. Pratique quand ton application lit un fichier plutôt que des variables d'environnement.

## Secrets : les données sensibles

Les Secrets fonctionnent comme les ConfigMaps, mais pour les **données sensibles** : mots de passe, clés API, certificats TLS, tokens OAuth.

```yaml
apiVersion: v1
kind: Secret
metadata:
  name: db-secret
type: Opaque
stringData:
  DB_USER: "postgres"
  DB_PASSWORD: "super-secret"
```

Injection identique :

```yaml
envFrom:
  - secretRef:
      name: db-secret
```

### Attention : base64 n'est pas du chiffrement

Kubernetes encode les Secrets en base64, pas en chiffré. N'importe qui avec accès à l'API Kubernetes (`kubectl get secret -o yaml`) peut les lire. En production, ajoute :

- **Chiffrement au repos** via EncryptionConfiguration (etcd chiffré)
- **RBAC strict** : seuls les ServiceAccounts autorisés accèdent aux Secrets
- **Opérateurs externes** : HashiCorp Vault, AWS Secrets Manager, Sealed Secrets, SOPS

Ne commite jamais de Secrets en clair dans Git. Pour le GitOps, utilise Sealed Secrets ou SOPS pour chiffrer les valeurs avant le push.

## ConfigMaps vs variables d'environnement dans le Dockerfile

| Approche | Avantage | Inconvénient |
|----------|----------|--------------|
| ENV dans Dockerfile | Simple en dev | Rebuild à chaque changement |
| ConfigMap / Secret | Changement sans rebuild | Nécessite un restart pod |
| Vault / External Secrets | Rotation, audit, chiffrement | Complexité accrue |

La règle : tout ce qui varie entre environnements (dev/staging/prod) sort de l'image et va dans ConfigMap ou Secret.

## Organisation par application et environnement

Regroupe la config par domaine fonctionnel :

- `api-config` : variables métier de l'API
- `api-db-secret` : credentials base de données
- `payments-config` : config du module paiement

Utilise des namespaces séparés (`staging`, `production`) avec des ConfigMaps/Secrets distincts. Évite un ConfigMap géant partagé par dix services : la modification d'une clé impacte tout le monde.

Documente les variables attendues dans un README technique ou un fichier `.env.example` (sans valeurs réelles).

## Bonnes pratiques opérationnelles

- **Immutabilité des Secrets** : pour changer un mot de passe, crée un nouveau Secret et mets à jour le Deployment (rolling update)
- **Limites de taille** : ConfigMap max 1 Mo ; au-delà, monte un volume externe ou un object storage
- **SubPath avec attention** : monter une seule clé via `subPath` ne se met pas à jour automatiquement si la ConfigMap change
- **Validation** : teste en staging que les variables sont bien injectées (`kubectl exec ... env | grep DB_`)

## Conclusion

ConfigMaps et Secrets séparent configuration et code dans Kubernetes. Utilise les ConfigMaps pour la config visible, les Secrets pour les credentials, et renforce la sécurité avec chiffrement et RBAC en production. Pour la gestion des secrets côté pipeline CI/CD (avant même le déploiement), voir aussi le guide sur les [secrets et variables d'environnement en CI/CD](/blog/articles/ci-cd-secrets-variables-environnement.html).
