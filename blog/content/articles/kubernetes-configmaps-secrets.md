---
title: "Kubernetes : gérer la configuration avec ConfigMaps et Secrets"
date: 2025-01-16
excerpt: "Séparer le code de la configuration : variables d'environnement, fichiers de config, secrets (mots de passe, clés API) avec ConfigMaps et Secrets Kubernetes."
type: article
tags: [Kubernetes, ConfigMap, Secret, configuration]
series: kubernetes-serie
series_order: 4
og_image: k8s-configmaps-secrets-1200x630.jpg
---

# Kubernetes : gérer la configuration avec ConfigMaps et Secrets

Tu ne veux pas re‑builder ton image à chaque fois que :

- tu changes une URL de base de données,
- tu modifies une clé API,
- tu actives un mode `DEBUG`.

Kubernetes te fournit deux briques pour ça :

- les **ConfigMaps** (configuration non sensible),
- les **Secrets** (données sensibles).

---

## ConfigMaps : configuration "classique"

Les ConfigMaps stockent des paires clé/valeur ou des fichiers de configuration complets.

### Exemple simple

```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: api-config
data:
  APP_ENV: "production"
  LOG_LEVEL: "info"
```

Tu peux ensuite les monter dans un Deployment :

```yaml
envFrom:
  - configMapRef:
      name: api-config
```

Dans ton conteneur, tu retrouveras alors `APP_ENV` et `LOG_LEVEL` comme variables d'environnement.

---

## Secrets : pour les mots de passe et clés

Les Secrets fonctionnent comme les ConfigMaps, mais sont destinés aux **données sensibles** :

- mots de passe,
- clés API,
- certificats.

Exemple (en clair, pour la lisibilité ici) :

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

Et dans le Deployment :

```yaml
envFrom:
  - secretRef:
      name: db-secret
```

Kubernetes stocke les Secrets encodés en base64. Ça n'est **pas** un chiffrement, mais ça évite au moins les fuites triviales. Pour des environnements sensibles, on ajoute souvent :

- chiffrement au repos (EncryptionConfiguration),
- intégration avec un système de secrets (Vault, AWS KMS, etc.).

---

## Monter des fichiers de config

ConfigMaps et Secrets peuvent aussi être montés comme **fichiers** :

```yaml
volumeMounts:
  - name: config-volume
    mountPath: /app/config

volumes:
  - name: config-volume
    configMap:
      name: app-config
```

Tu obtiens alors des fichiers dans `/app/config` correspondant aux clés de la ConfigMap.

Même principe avec un Secret :

```yaml
volumes:
  - name: certs
    secret:
      secretName: tls-cert
```

---

## Bonnes pratiques

- Ne stocke pas les Secrets en clair dans ton repo (ou alors sur des environnements de test uniquement).  
- Regroupe la config par *application* ou *domaine* fonctionnel (`api-config`, `payments-config`, etc.).  
- Documente les variables attendues par chaque service (README technique).

Dans la suite de la série, on verra comment **observer** ce qui se passe : logs, métriques et events, pour comprendre le comportement de tes pods en conditions réelles.
