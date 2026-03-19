---
title: "DevSecOps : SAST, DAST, SBOM et sécurité dans la CI/CD"
date: 2025-12-02
excerpt: "Intégrer la sécurité au pipeline : scans de dépendances, SAST/DAST, secrets scanning, SBOM, politiques, et gates qualité sans ralentir l’équipe."
type: article
tags: [DevSecOps, SAST, DAST, SBOM, CI/CD]
series: cybersecurite-secops-serie
series_order: 9
og_image: devsecops-sast-dast-sbom-1200x630.jpg
---

# DevSecOps : SAST, DAST, SBOM et sécurité dans la CI/CD

Le DevSecOps n’est pas “mettre un scanner et bloquer tout”.  
C’est intégrer des contrôles **au bon endroit**, avec des règles pragmatiques, pour réduire le risque sans casser le delivery.

---

## 1) Les contrôles essentiels dans un pipeline

- **Secrets scanning** (clés API, tokens)
- **SCA** (Software Composition Analysis) : dépendances et CVE
- **SAST** : analyse statique (patterns, vulnérabilités)
- **Image scanning** (conteneurs)
- **DAST** : tests dynamiques (sur staging)
- **IaC scanning** (Terraform/K8s manifests)

---

## 2) SAST : utile si tu l’industrialises

Bon usage :

- règles adaptées au langage
- réduction des faux positifs
- focus sur les vulnérabilités critiques (injection, auth, SSRF)

Piège : noyer l’équipe sous 500 alertes.

---

## 3) DAST : tester comme un attaquant… mais au bon moment

DAST est pertinent :

- sur un environnement stable (staging)
- avec une auth réaliste
- avec des scénarios ciblés (login, upload, admin)

DAST “générique” sans auth donne souvent peu de valeur.

---

## 4) SBOM : savoir ce que tu déploies

SBOM (Software Bill of Materials) = inventaire des composants.

Intérêt :

- répondre vite à une CVE (suis‑je exposé ?)
- traçabilité supply chain
- exigences conformité (de plus en plus)

---

## 5) Gates : bloquer intelligemment

Ne bloque pas tout. Bloque :

- secrets détectés
- vulnérabilités critiques exploitées (ou exposées internet)
- erreurs IAM/IaC dangereuses

Et laisse passer le reste avec un plan :

- ticket + SLA
- owner
- exception temporaire

---

## 6) Le workflow qui marche

1. Éducation + conventions (secure defaults)
2. Scans rapides en PR (feedback immédiat)
3. Scans plus lourds sur main / nightly
4. Dashboard “risque réel” + priorisation

---

## Conclusion

DevSecOps efficace = feedback rapide + gates ciblés + SBOM + gestion vulnérabilités.  
Dernier article : conformité (RGPD, NIS2, ISO 27001) et posture.

