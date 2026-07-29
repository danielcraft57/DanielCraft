# Atelier : tester XSS (defense)

## Exercice

1. Identifie 3 endroits ou du texte utilisateur est affiche.
2. Pour chacun : echapper ou utiliser textContent.
3. Ajoute une CSP : `script-src 'self'`.
4. Teste avec `<script>alert(1)</script>` : doit etre neutralise.

## Verification

- Le script ne s'execute pas.
- Le texte s'affiche litteralement ou est filtre.
