#!/usr/bin/env python3
"""Génère les 5 vitrines SaaS IA (FlowMetrics, TalentLoop, MetricPulse, QueryBase, PingFlow)."""
from vitrine_ai_lib import write_ai_site, HUB

# ── Typo commune (rappelé dans chaque CSS) ──────────────────────────────────
_TYPO = """
body {
  font-family: "Plus Jakarta Sans", system-ui, sans-serif;
  font-size: 17px;
  line-height: 1.6;
  margin: 0;
}
.ai-prose p, .ai-lead, .ai-section > p {
  max-width: 65ch;
}
.ai-cta, .ai-btn {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  min-height: 44px;
  padding: 0.75rem 1.5rem;
  font-weight: 600;
  text-decoration: none;
  border-radius: 10px;
  border: none;
  cursor: pointer;
  font-size: 1rem;
  font-family: inherit;
}
"""


def _flowmetrics():
    body = f"""
<header class="ai-nav ai-nav--landing">
  <a class="ai-logo" href="#">FlowMetrics</a>
  <nav class="ai-nav-links">
    <a href="#preuve">Clients</a>
    <a href="#avant-apres">Résultats</a>
    <a href="#tarifs">Tarifs</a>
  </nav>
  <a class="ai-cta ai-cta--primary" href="#tarifs">Essai gratuit 14 jours</a>
</header>

<main>
  <section class="ai-hero ai-hero--landing">
    <p class="ai-eyebrow">Analytics produit · sans data team</p>
    <h1>Transformez vos métriques en décisions avant le stand-up de lundi</h1>
    <p class="ai-lead">FlowMetrics centralise funnels, cohortes et alertes en un seul tableau de bord. Branchez votre stack en douze minutes et voyez enfin où vos utilisateurs décrochent — avant qu'ils ne partent chez la concurrence.</p>
    <div class="ai-hero-actions">
      <a class="ai-cta ai-cta--primary" href="#tarifs">Démarrer l'essai — carte non requise</a>
      <a class="ai-cta ai-cta--ghost" href="#preuve">Voir les témoignages</a>
    </div>
    <div class="ai-social-proof">
      <span class="ai-proof-chip">★ 4,9/5 sur G2</span>
      <span class="ai-proof-chip"><strong>2 847</strong> équipes actives</span>
      <span class="ai-proof-chip">+38 % rétention moyenne</span>
    </div>
    <figure class="ai-hero-visual">
      <img src="images/hero.png" alt="Tableau de bord funnel FlowMetrics avec cohortes et alertes" width="960" height="540" decoding="async" fetchpriority="high">
    </figure>
  </section>

  <section id="preuve" class="ai-section ai-section--proof">
    <h2>Ils ont arrêté de deviner</h2>
    <p class="ai-prose">Des fondateurs B2B, des PM en scale-up et des équipes growth nous font confiance pour remplacer les exports Excel du vendredi soir.</p>
    <div class="ai-testimonials">
      <blockquote class="ai-quote">
        <p>« En trois semaines, on a identifié un goulot d'étranglement à l'étape 4 du onboarding. Le taux d'activation est passé de 31 % à 58 %. »</p>
        <footer>— Camille Renard, CPO chez Ledgerly</footer>
      </blockquote>
      <blockquote class="ai-quote">
        <p>« Nos investisseurs demandaient des cohortes propres. FlowMetrics nous a évité six mois de recrutement data. »</p>
        <footer>— Mehdi Ouali, fondateur de StackNest</footer>
      </blockquote>
      <blockquote class="ai-quote">
        <p>« L'alerte Slack quand le churn hebdo dépasse 2 % a sauvé notre trimestre. Personne ne surveillait ce chiffre avant. »</p>
        <footer>— Julie Moreau, Head of Growth chez NovaPay</footer>
      </blockquote>
    </div>
    <div class="ai-logos-row" aria-label="Logos clients">
      <span>Ledgerly</span><span>StackNest</span><span>NovaPay</span><span>OrbitHR</span><span>Clarion</span>
    </div>
  </section>

  <section id="avant-apres" class="ai-section ai-section--compare">
    <h2>Avant / après FlowMetrics</h2>
    <p class="ai-prose">Ce que nos clients décrivaient le premier jour — et ce qu'ils constatent après trente jours d'usage réel.</p>
    <div class="ai-compare-grid">
      <article class="ai-compare-card">
        <div class="ai-before">
          <h3>Avant</h3>
          <p>Trois outils déconnectés, un Google Sheet partagé et une réunion « metrics » chaque lundi qui ne mène nulle part.</p>
        </div>
        <div class="ai-after">
          <h3>Après</h3>
          <p>Un seul funnel live, alertes configurées en cinq clics, toute l'équipe lit les mêmes chiffres.</p>
        </div>
      </article>
      <article class="ai-compare-card">
        <div class="ai-before">
          <h3>Avant</h3>
          <p>Onboarding opaque : 40 % des inscrits ne dépassent jamais la première étape, sans qu'on sache pourquoi.</p>
        </div>
        <div class="ai-after">
          <h3>Après</h3>
          <p>Parcours tracé étape par étape, drop-off visible en temps réel, tests A/B sur le copy du bouton principal.</p>
        </div>
      </article>
      <article class="ai-compare-card">
        <div class="ai-before">
          <h3>Avant</h3>
          <p>Pricing flou, plan « contactez-nous » partout, prospects qui abandonnent faute de transparence.</p>
        </div>
        <div class="ai-after">
          <h3>Après</h3>
          <p>Grille lisible, plan recommandé mis en avant, conversion page tarifs +22 % en moyenne.</p>
        </div>
      </article>
    </div>
  </section>

  <section id="tarifs" class="ai-section ai-section--pricing">
    <h2>Tarifs transparents, sans surprise</h2>
    <p class="ai-prose">Choisissez le plan adapté à votre stade. Passez à l'échelle supérieure quand votre MRR le justifie — sans renégocier.</p>
    <div class="ai-pricing-grid">
      <article class="ai-plan">
        <h3>Starter</h3>
        <p class="ai-price">29 €<span>/mois</span></p>
        <p class="ai-plan-desc">Pour les side-projects et les premières validations marché.</p>
        <ul>
          <li>1 projet actif</li>
          <li>7 jours de rétention données</li>
          <li>Funnels de base</li>
          <li class="ai-miss">Pas d'alertes Slack</li>
        </ul>
        <button type="button" class="ai-btn ai-btn--outline">Choisir Starter</button>
      </article>
      <article class="ai-plan ai-plan--featured">
        <span class="ai-badge">Le plus choisi</span>
        <h3>Pro</h3>
        <p class="ai-price">79 €<span>/mois</span></p>
        <p class="ai-plan-desc">≈ 2,60 € par jour — moins qu'un café d'équipe.</p>
        <ul>
          <li>Projets illimités</li>
          <li>365 jours de rétention</li>
          <li>Cohortes &amp; funnels avancés</li>
          <li>Alertes Slack &amp; email</li>
          <li>Export CSV &amp; API</li>
        </ul>
        <button type="button" class="ai-btn ai-btn--primary">Essai 14 jours gratuit</button>
      </article>
      <article class="ai-plan ai-plan--anchor">
        <h3>Scale</h3>
        <p class="ai-price">199 €<span>/mois</span></p>
        <p class="ai-plan-desc">Pour les équipes qui ont dépassé le million d'ARR.</p>
        <ul>
          <li>SSO SAML &amp; SCIM</li>
          <li>SLA 99,9 %</li>
          <li>Support dédié &lt; 2 h</li>
          <li>Audit logs &amp; conformité</li>
        </ul>
        <button type="button" class="ai-btn ai-btn--outline">Contacter les ventes</button>
      </article>
    </div>
  </section>

  <section class="ai-section ai-section--cta-final">
    <h2>Prêt à voir votre funnel en clair ?</h2>
    <p class="ai-lead">Rejoignez 2 847 équipes qui ont remplacé les tableurs par des insights actionnables. Installation en douze minutes, résultats dès la première semaine.</p>
    <a class="ai-cta ai-cta--primary ai-cta--lg" href="#tarifs">Activer mon essai gratuit</a>
  </section>
</main>
<footer class="ai-foot">{HUB}</footer>
"""
    css = _TYPO + """
:root {
  --ai-bg: #0a0f1e;
  --ai-surface: #121a2e;
  --ai-indigo: #6366f1;
  --ai-indigo-light: #818cf8;
  --ai-text: #e8edf7;
  --ai-muted: #94a3b8;
  --ai-border: #1e2a45;
  --ai-success: #34d399;
}
* { box-sizing: border-box; }
body { background: var(--ai-bg); color: var(--ai-text); }
.ai-nav--landing {
  display: flex; align-items: center; gap: 1.5rem;
  padding: 1rem clamp(1rem, 4vw, 2.5rem);
  border-bottom: 1px solid var(--ai-border);
  position: sticky; top: 0; z-index: 50;
  background: rgba(10, 15, 30, 0.92); backdrop-filter: blur(12px);
}
.ai-logo { font-weight: 800; font-size: 1.15rem; color: #fff; text-decoration: none; }
.ai-nav-links { display: flex; gap: 1.25rem; flex: 1; }
.ai-nav-links a { color: var(--ai-muted); text-decoration: none; font-size: 0.95rem; }
.ai-nav-links a:hover { color: var(--ai-text); }
.ai-cta--primary { background: var(--ai-indigo); color: #fff; }
.ai-cta--primary:hover { background: var(--ai-indigo-light); }
.ai-cta--ghost { background: transparent; color: var(--ai-text); border: 1px solid var(--ai-border); }
.ai-hero--landing {
  text-align: center; padding: clamp(3rem, 8vw, 5.5rem) clamp(1rem, 4vw, 2rem) 3rem;
  max-width: 1100px; margin: 0 auto;
}
.ai-eyebrow { color: var(--ai-indigo-light); font-weight: 600; font-size: 0.85rem; text-transform: uppercase; letter-spacing: 0.08em; }
.ai-hero--landing h1 { font-size: clamp(2rem, 5vw, 3.2rem); line-height: 1.15; margin: 0.75rem auto; max-width: 22ch; letter-spacing: -0.02em; }
.ai-lead { color: var(--ai-muted); margin: 0 auto 1.75rem; }
.ai-hero-actions { display: flex; gap: 0.75rem; justify-content: center; flex-wrap: wrap; margin-bottom: 1.5rem; }
.ai-social-proof { display: flex; gap: 0.75rem; justify-content: center; flex-wrap: wrap; margin-bottom: 2.5rem; }
.ai-proof-chip { background: var(--ai-surface); border: 1px solid var(--ai-border); padding: 0.4rem 0.9rem; border-radius: 999px; font-size: 0.9rem; color: var(--ai-muted); }
.ai-proof-chip strong { color: var(--ai-text); }
.ai-hero-visual img { width: 100%; max-width: 960px; border-radius: 16px; border: 1px solid var(--ai-border); box-shadow: 0 24px 80px rgba(99, 102, 241, 0.15); }
.ai-section { padding: clamp(3rem, 7vw, 5rem) clamp(1rem, 4vw, 2.5rem); max-width: 1100px; margin: 0 auto; }
.ai-section h2 { font-size: clamp(1.6rem, 3vw, 2.1rem); margin-bottom: 0.75rem; }
.ai-prose { color: var(--ai-muted); margin-bottom: 2rem; }
.ai-testimonials { display: grid; grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); gap: 1.25rem; margin-bottom: 2rem; }
.ai-quote { background: var(--ai-surface); border: 1px solid var(--ai-border); border-radius: 14px; padding: 1.5rem; margin: 0; }
.ai-quote p { font-style: italic; margin: 0 0 1rem; color: var(--ai-text); }
.ai-quote footer { font-size: 0.9rem; color: var(--ai-muted); }
.ai-logos-row { display: flex; gap: 2rem; flex-wrap: wrap; justify-content: center; color: var(--ai-muted); font-weight: 600; opacity: 0.6; font-size: 0.95rem; }
.ai-compare-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 1.25rem; }
.ai-compare-card { border-radius: 14px; overflow: hidden; border: 1px solid var(--ai-border); }
.ai-before, .ai-after { padding: 1.25rem 1.5rem; }
.ai-before { background: #1a1225; }
.ai-after { background: linear-gradient(135deg, #1a2540, #1e2a50); border-top: 2px solid var(--ai-indigo); }
.ai-before h3, .ai-after h3 { margin: 0 0 0.5rem; font-size: 0.8rem; text-transform: uppercase; letter-spacing: 0.06em; }
.ai-before h3 { color: #f87171; }
.ai-after h3 { color: var(--ai-success); }
.ai-pricing-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); gap: 1.25rem; align-items: start; }
.ai-plan { background: var(--ai-surface); border: 1px solid var(--ai-border); border-radius: 16px; padding: 1.75rem; position: relative; }
.ai-plan--featured { border-color: var(--ai-indigo); box-shadow: 0 0 0 1px var(--ai-indigo), 0 20px 60px rgba(99, 102, 241, 0.2); transform: scale(1.02); }
.ai-plan--anchor { opacity: 0.85; }
.ai-badge { position: absolute; top: -0.65rem; left: 50%; transform: translateX(-50%); background: var(--ai-indigo); color: #fff; font-size: 0.75rem; font-weight: 700; padding: 0.25rem 0.75rem; border-radius: 999px; }
.ai-price { font-size: 2.5rem; font-weight: 800; margin: 0.5rem 0; }
.ai-price span { font-size: 1rem; font-weight: 500; color: var(--ai-muted); }
.ai-plan-desc { color: var(--ai-muted); font-size: 0.95rem; margin-bottom: 1rem; }
.ai-plan ul { list-style: none; padding: 0; margin: 0 0 1.5rem; }
.ai-plan li { padding: 0.35rem 0; border-bottom: 1px solid var(--ai-border); font-size: 0.95rem; }
.ai-miss { color: #64748b; text-decoration: line-through; }
.ai-btn { width: 100%; }
.ai-btn--primary { background: var(--ai-indigo); color: #fff; }
.ai-btn--outline { background: transparent; color: var(--ai-text); border: 1px solid var(--ai-border); }
.ai-section--cta-final { text-align: center; background: linear-gradient(180deg, transparent, rgba(99, 102, 241, 0.08)); border-radius: 24px; margin-bottom: 2rem; }
.ai-cta--lg { font-size: 1.05rem; padding: 0.85rem 2rem; }
.ai-foot { text-align: center; padding: 2rem; border-top: 1px solid var(--ai-border); color: var(--ai-muted); }
"""
    write_ai_site(
        "saas-landing",
        "FlowMetrics — Landing SaaS conversion",
        "Landing page SaaS dark indigo : preuve sociale, comparatif avant/après et grille tarifaire à trois plans.",
        body,
        css,
        layout="contrast-pricing-dark",
    )


def _talentloop():
    body = f"""
<div class="ai-split">
  <aside class="ai-split-brand">
    <a class="ai-logo" href="#">TalentLoop</a>
    <h1>Bienvenue chez NovaRH</h1>
    <p class="ai-lead">Votre parcours d'intégration commence ici. Quatre étapes, moins de dix minutes — et vous serez opérationnel dès lundi matin.</p>
    <ul class="ai-benefits">
      <li>✓ Contrat signé électroniquement</li>
      <li>✓ Accès aux outils internes</li>
      <li>✓ Rencontre avec votre binôme</li>
      <li>✓ Premier objectif à 30 jours défini</li>
    </ul>
    <figure class="ai-brand-visual">
      <img src="images/hero.png" alt="Interface TalentLoop — parcours d'onboarding RH en quatre étapes" width="480" height="360" decoding="async">
    </figure>
  </aside>

  <main class="ai-split-main">
    <header class="ai-wizard-header">
      <span class="ai-step-label">Étape <strong id="ai-step-num">1</strong> sur 4</span>
      <div class="ai-progress" role="progressbar" aria-valuenow="25" aria-valuemin="0" aria-valuemax="100">
        <div class="ai-progress-bar" style="width:25%"></div>
      </div>
    </header>

    <section class="ai-wizard-step ai-wizard-step--active" data-step="1">
      <h2>Vos informations personnelles</h2>
      <p class="ai-prose">Commençons par les bases. Ces données alimentent votre fiche employé et votre badge d'accès.</p>
      <form class="ai-form" action="#" method="get">
        <label>Prénom <input type="text" placeholder="Élodie" value="Élodie"></label>
        <label>Nom <input type="text" placeholder="Marchand" value="Marchand"></label>
        <label>Date de prise de poste <input type="date" value="2026-07-14"></label>
        <label>Service
          <select><option>Produit &amp; Design</option><option>Ingénierie</option><option>Commercial</option></select>
        </label>
      </form>
    </section>

    <section class="ai-wizard-step" data-step="2">
      <h2>Documents administratifs</h2>
      <p class="ai-prose">Téléversez les pièces demandées par les RH. Formats acceptés : PDF, JPG — 10 Mo max par fichier.</p>
      <div class="ai-upload-zone">
        <p>📄 Carte d'identité — <strong>validé</strong></p>
        <p>📄 RIB — <strong>en attente</strong></p>
        <p>📄 Attestation mutuelle — <strong>à fournir</strong></p>
      </div>
    </section>

    <section class="ai-wizard-step" data-step="3">
      <h2>Configuration de vos accès</h2>
      <p class="ai-prose">Sélectionnez les outils dont vous aurez besoin dès le premier jour. Votre manager validera la liste.</p>
      <div class="ai-checklist">
        <label><input type="checkbox" checked> Google Workspace</label>
        <label><input type="checkbox" checked> Slack — canal #produit</label>
        <label><input type="checkbox" checked> Notion — wiki équipe</label>
        <label><input type="checkbox"> Figma — lecture seule</label>
        <label><input type="checkbox"> Linear — projets actifs</label>
      </div>
    </section>

    <section class="ai-wizard-step" data-step="4">
      <h2>Votre binôme et premier objectif</h2>
      <p class="ai-prose">TalentLoop vous assigne un référent et un objectif mesurable pour vos trente premiers jours.</p>
      <article class="ai-buddy-card">
        <div class="ai-buddy-avatar">SM</div>
        <div>
          <strong>Sophie Martin</strong>
          <p>Lead Product Designer · votre binôme</p>
          <p class="ai-objective">Objectif J+30 : livrer la refonte du tunnel d'inscription mobile.</p>
        </div>
      </article>
    </section>

    <nav class="ai-wizard-nav">
      <button type="button" class="ai-btn ai-btn--ghost">Retour</button>
      <button type="button" class="ai-btn ai-btn--primary">Continuer</button>
    </nav>

    <section class="ai-section ai-section--contact">
      <h2>Une question sur votre intégration ?</h2>
      <p class="ai-prose">L'équipe RH répond sous quatre heures ouvrées. Vous pouvez aussi consulter la FAQ interne.</p>
      <a class="ai-cta ai-cta--primary" href="mailto:rh@novarh.fr">Contacter les RH</a>
    </section>
  </main>
</div>
<footer class="ai-foot">{HUB}</footer>
"""
    css = _TYPO + """
:root {
  --ai-coral: #f97316;
  --ai-teal: #14b8a6;
  --ai-cream: #fffbf5;
  --ai-ink: #1c1917;
  --ai-muted: #78716c;
  --ai-border: #e7e5e4;
}
* { box-sizing: border-box; }
body { background: var(--ai-cream); color: var(--ai-ink); }
.ai-split { display: grid; grid-template-columns: 1fr 1.1fr; min-height: 100vh; }
.ai-split-brand {
  background: linear-gradient(160deg, #fff7ed 0%, #fef3c7 50%, #ccfbf1 100%);
  padding: clamp(2rem, 5vw, 3.5rem);
  display: flex; flex-direction: column;
  border-right: 1px solid var(--ai-border);
}
.ai-logo { font-weight: 800; font-size: 1.1rem; color: var(--ai-coral); text-decoration: none; margin-bottom: 2rem; }
.ai-split-brand h1 { font-size: clamp(1.75rem, 3.5vw, 2.4rem); line-height: 1.2; margin: 0 0 1rem; max-width: 20ch; }
.ai-lead { color: var(--ai-muted); margin-bottom: 1.5rem; }
.ai-benefits { list-style: none; padding: 0; margin: 0 0 2rem; }
.ai-benefits li { padding: 0.4rem 0; color: var(--ai-ink); font-weight: 500; }
.ai-brand-visual img { width: 100%; border-radius: 16px; border: 1px solid var(--ai-border); margin-top: auto; }
.ai-split-main { padding: clamp(2rem, 5vw, 3rem); display: flex; flex-direction: column; }
.ai-wizard-header { margin-bottom: 2rem; }
.ai-step-label { font-size: 0.9rem; color: var(--ai-muted); display: block; margin-bottom: 0.5rem; }
.ai-progress { height: 8px; background: var(--ai-border); border-radius: 999px; overflow: hidden; }
.ai-progress-bar { height: 100%; background: linear-gradient(90deg, var(--ai-coral), var(--ai-teal)); border-radius: 999px; transition: width 0.3s; }
.ai-wizard-step h2 { font-size: 1.5rem; margin-bottom: 0.5rem; }
.ai-prose { color: var(--ai-muted); margin-bottom: 1.5rem; }
.ai-form { display: grid; gap: 1rem; max-width: 420px; }
.ai-form label { display: flex; flex-direction: column; gap: 0.35rem; font-weight: 600; font-size: 0.9rem; }
.ai-form input, .ai-form select {
  padding: 0.65rem 0.85rem; border: 1px solid var(--ai-border); border-radius: 10px;
  font-family: inherit; font-size: 1rem; background: #fff;
}
.ai-upload-zone { background: #fff; border: 2px dashed var(--ai-border); border-radius: 14px; padding: 1.5rem; }
.ai-upload-zone p { margin: 0.5rem 0; }
.ai-checklist { display: flex; flex-direction: column; gap: 0.65rem; }
.ai-checklist label { display: flex; align-items: center; gap: 0.5rem; font-weight: 500; }
.ai-buddy-card { display: flex; gap: 1rem; background: #fff; border: 1px solid var(--ai-border); border-radius: 14px; padding: 1.25rem; }
.ai-buddy-avatar { width: 56px; height: 56px; border-radius: 50%; background: var(--ai-teal); color: #fff; display: flex; align-items: center; justify-content: center; font-weight: 700; flex-shrink: 0; }
.ai-objective { color: var(--ai-coral); font-weight: 600; margin-top: 0.5rem; }
.ai-wizard-nav { display: flex; justify-content: space-between; margin-top: 2rem; padding-top: 1.5rem; border-top: 1px solid var(--ai-border); }
.ai-btn--primary { background: var(--ai-coral); color: #fff; min-width: 140px; }
.ai-btn--ghost { background: transparent; color: var(--ai-muted); border: 1px solid var(--ai-border); }
.ai-cta--primary { background: var(--ai-teal); color: #fff; }
.ai-section--contact { margin-top: 3rem; padding-top: 2rem; border-top: 1px solid var(--ai-border); }
.ai-foot { text-align: center; padding: 1.5rem; color: var(--ai-muted); grid-column: 1 / -1; }
@media (max-width: 900px) {
  .ai-split { grid-template-columns: 1fr; }
  .ai-split-brand { border-right: none; border-bottom: 1px solid var(--ai-border); }
}
"""
    write_ai_site(
        "saas-onboarding",
        "TalentLoop — Onboarding RH",
        "Parcours d'intégration RH en split screen : quatre étapes guidées avec barre de progression.",
        body,
        css,
        layout="split-wizard",
    )


def _metricpulse():
    body = f"""
<div class="ai-app">
  <aside class="ai-sidebar">
    <a class="ai-logo" href="#">MetricPulse</a>
    <nav class="ai-sidebar-nav">
      <a class="ai-nav-item ai-nav-item--active" href="#">Vue d'ensemble</a>
      <a class="ai-nav-item" href="#">Funnels</a>
      <a class="ai-nav-item" href="#">Cohortes</a>
      <a class="ai-nav-item" href="#">Alertes</a>
      <a class="ai-nav-item" href="#">Rapports</a>
    </nav>
    <div class="ai-sidebar-footer">
      <p>Projet : <strong>Acme SaaS</strong></p>
      <a class="ai-cta ai-cta--sidebar" href="#">+ Nouveau rapport</a>
    </div>
  </aside>

  <div class="ai-main">
    <header class="ai-topbar">
      <div>
        <h1>Vue d'ensemble</h1>
        <p class="ai-subtitle">Semaine du 23 au 29 juin 2026 · fuseau Europe/Paris</p>
      </div>
      <div class="ai-topbar-actions">
        <button type="button" class="ai-btn ai-btn--ghost">Exporter</button>
        <button type="button" class="ai-btn ai-btn--primary">Partager</button>
      </div>
    </header>

    <section class="ai-kpi-row">
      <article class="ai-kpi">
        <span class="ai-kpi-label">Utilisateurs actifs</span>
        <strong class="ai-kpi-value">12 847</strong>
        <span class="ai-kpi-delta ai-kpi-delta--up">+8,3 % vs S-1</span>
      </article>
      <article class="ai-kpi">
        <span class="ai-kpi-label">Taux d'activation</span>
        <strong class="ai-kpi-value">64,2 %</strong>
        <span class="ai-kpi-delta ai-kpi-delta--up">+2,1 pts</span>
      </article>
      <article class="ai-kpi">
        <span class="ai-kpi-label">MRR estimé</span>
        <strong class="ai-kpi-value">48 290 €</strong>
        <span class="ai-kpi-delta ai-kpi-delta--up">+12 %</span>
      </article>
      <article class="ai-kpi">
        <span class="ai-kpi-label">Churn hebdo</span>
        <strong class="ai-kpi-value">1,8 %</strong>
        <span class="ai-kpi-delta ai-kpi-delta--down">−0,4 pts</span>
      </article>
    </section>

    <section class="ai-section ai-section--funnel">
      <h2>Funnel d'acquisition — campagne été</h2>
      <p class="ai-prose">Du clic publicitaire à la première valeur perçue. Le goulet principal reste l'étape « configuration initiale » avec 34 % d'abandon.</p>
      <div class="ai-funnel">
        <div class="ai-funnel-step" style="--ai-width:100%">
          <span>Visite landing</span><strong>24 500</strong>
        </div>
        <div class="ai-funnel-step" style="--ai-width:72%">
          <span>Inscription</span><strong>17 640</strong>
        </div>
        <div class="ai-funnel-step" style="--ai-width:48%">
          <span>Email vérifié</span><strong>11 760</strong>
        </div>
        <div class="ai-funnel-step ai-funnel-step--warn" style="--ai-width:31%">
          <span>Config initiale</span><strong>7 595</strong>
        </div>
        <div class="ai-funnel-step" style="--ai-width:22%">
          <span>Première action clé</span><strong>5 390</strong>
        </div>
      </div>
      <figure class="ai-chart-visual">
        <img src="images/hero.png" alt="Dashboard MetricPulse — graphiques KPI et entonnoir de conversion" width="800" height="450" decoding="async">
      </figure>
    </section>

    <section class="ai-section ai-section--insights">
      <h2>Insights automatiques</h2>
      <div class="ai-insight-grid">
        <article class="ai-insight">
          <h3>🔔 Alerte churn</h3>
          <p>Le segment « PME 10-50 » a vu son churn passer de 1,2 % à 2,1 % cette semaine. Corrélation forte avec la mise à jour du 24 juin.</p>
        </article>
        <article class="ai-insight">
          <h3>📈 Opportunité</h3>
          <p>Les utilisateurs qui complètent le tutoriel en moins de 4 min ont 3× plus de chances de convertir en payant.</p>
        </article>
        <article class="ai-insight">
          <h3>🎯 Recommandation</h3>
          <p>Raccourcir le formulaire de config de 6 à 3 champs pourrait récupérer ~1 800 utilisateurs par mois.</p>
        </article>
      </div>
    </section>

    <section class="ai-section ai-section--cta-final">
      <h2>Besoin d'un audit de votre funnel ?</h2>
      <p class="ai-prose">Nos experts analysent vos données MetricPulse et livrent un plan d'action en quarante-huit heures.</p>
      <a class="ai-cta ai-cta--primary" href="#">Demander un audit gratuit</a>
    </section>
  </div>
</div>
<footer class="ai-foot">{HUB}</footer>
"""
    css = _TYPO + """
:root {
  --ai-bg: #f0f4f8;
  --ai-sidebar: #0f2942;
  --ai-accent: #0ea5e9;
  --ai-green: #10b981;
  --ai-warn: #f59e0b;
  --ai-text: #0f172a;
  --ai-muted: #64748b;
  --ai-card: #ffffff;
  --ai-border: #e2e8f0;
}
* { box-sizing: border-box; }
body { background: var(--ai-bg); color: var(--ai-text); }
.ai-app { display: grid; grid-template-columns: 240px 1fr; min-height: 100vh; }
.ai-sidebar { background: var(--ai-sidebar); color: #e2e8f0; padding: 1.5rem 1rem; display: flex; flex-direction: column; }
.ai-logo { font-weight: 800; font-size: 1.1rem; color: #fff; text-decoration: none; display: block; margin-bottom: 2rem; padding: 0 0.5rem; }
.ai-sidebar-nav { display: flex; flex-direction: column; gap: 0.25rem; flex: 1; }
.ai-nav-item { color: #94a3b8; text-decoration: none; padding: 0.6rem 0.75rem; border-radius: 8px; font-size: 0.95rem; }
.ai-nav-item--active, .ai-nav-item:hover { background: rgba(14, 165, 233, 0.15); color: #fff; }
.ai-sidebar-footer { border-top: 1px solid rgba(255,255,255,0.1); padding-top: 1rem; font-size: 0.85rem; }
.ai-cta--sidebar { background: var(--ai-accent); color: #fff; width: 100%; margin-top: 0.75rem; font-size: 0.9rem; }
.ai-main { padding: clamp(1.25rem, 3vw, 2rem); overflow-x: auto; }
.ai-topbar { display: flex; justify-content: space-between; align-items: flex-start; flex-wrap: wrap; gap: 1rem; margin-bottom: 1.5rem; }
.ai-topbar h1 { font-size: 1.75rem; margin: 0; }
.ai-subtitle { color: var(--ai-muted); margin: 0.25rem 0 0; font-size: 0.9rem; }
.ai-topbar-actions { display: flex; gap: 0.5rem; }
.ai-btn--primary { background: var(--ai-accent); color: #fff; }
.ai-btn--ghost { background: var(--ai-card); color: var(--ai-text); border: 1px solid var(--ai-border); }
.ai-kpi-row { display: grid; grid-template-columns: repeat(auto-fit, minmax(180px, 1fr)); gap: 1rem; margin-bottom: 2rem; }
.ai-kpi { background: var(--ai-card); border: 1px solid var(--ai-border); border-radius: 14px; padding: 1.25rem; }
.ai-kpi-label { display: block; font-size: 0.85rem; color: var(--ai-muted); margin-bottom: 0.35rem; }
.ai-kpi-value { font-size: 1.75rem; display: block; line-height: 1.2; }
.ai-kpi-delta { font-size: 0.85rem; font-weight: 600; }
.ai-kpi-delta--up { color: var(--ai-green); }
.ai-kpi-delta--down { color: var(--ai-green); }
.ai-section { margin-bottom: 2rem; }
.ai-section h2 { font-size: 1.35rem; margin-bottom: 0.5rem; }
.ai-prose { color: var(--ai-muted); margin-bottom: 1.25rem; }
.ai-funnel { display: flex; flex-direction: column; gap: 0.5rem; margin-bottom: 1.5rem; }
.ai-funnel-step {
  display: flex; justify-content: space-between; align-items: center;
  background: linear-gradient(90deg, var(--ai-accent), #38bdf8);
  color: #fff; padding: 0.75rem 1rem; border-radius: 8px;
  width: var(--ai-width); min-width: 200px;
}
.ai-funnel-step--warn { background: linear-gradient(90deg, var(--ai-warn), #fbbf24); }
.ai-chart-visual img { width: 100%; border-radius: 12px; border: 1px solid var(--ai-border); }
.ai-insight-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(240px, 1fr)); gap: 1rem; }
.ai-insight { background: var(--ai-card); border: 1px solid var(--ai-border); border-radius: 12px; padding: 1.25rem; }
.ai-insight h3 { margin: 0 0 0.5rem; font-size: 1rem; }
.ai-insight p { margin: 0; color: var(--ai-muted); font-size: 0.95rem; }
.ai-section--cta-final { background: var(--ai-card); border: 1px solid var(--ai-border); border-radius: 16px; padding: 2rem; text-align: center; }
.ai-cta--primary { background: var(--ai-accent); color: #fff; }
.ai-foot { text-align: center; padding: 1.5rem; color: var(--ai-muted); }
@media (max-width: 768px) { .ai-app { grid-template-columns: 1fr; } .ai-sidebar { flex-direction: row; flex-wrap: wrap; align-items: center; gap: 0.5rem; } .ai-sidebar-nav { flex-direction: row; flex-wrap: wrap; } }
"""
    write_ai_site(
        "saas-dashboard",
        "MetricPulse — Dashboard analytics",
        "Interface dashboard SaaS : sidebar, KPIs temps réel, entonnoir de conversion et insights automatiques.",
        body,
        css,
        layout="sidebar-analytics",
    )


def _querybase():
    body = f"""
<header class="ai-nav ai-nav--minimal">
  <a class="ai-logo" href="#">QueryBase</a>
  <nav class="ai-nav-links">
    <a href="#recherche">Recherche</a>
    <a href="#roadmap">Roadmap</a>
    <a href="#suggestions">Suggestions</a>
  </nav>
  <a class="ai-cta ai-cta--primary" href="#">Nouvelle requête</a>
</header>

<main>
  <section id="recherche" class="ai-section ai-empty-state">
    <div class="ai-empty-icon" aria-hidden="true">🔍</div>
    <h1>Aucun résultat pour « intégration Salesforce bi-directionnelle »</h1>
    <p class="ai-lead">Nous n'avons trouvé aucune documentation correspondant à votre recherche. Essayez d'élargir les termes ou explorez les requêtes similaires ci-dessous.</p>
    <form class="ai-search-form" role="search">
      <input type="search" placeholder="Rechercher dans la base de connaissances…" value="intégration Salesforce bi-directionnelle">
      <button type="submit" class="ai-btn ai-btn--primary">Rechercher</button>
    </form>
    <div class="ai-empty-tips">
      <p><strong>Astuce :</strong> utilisez des guillemets pour une expression exacte — <code>"sync temps réel"</code></p>
      <p><strong>Filtres actifs :</strong> Documentation · API v3 · Français</p>
    </div>
    <figure class="ai-empty-visual">
      <img src="images/hero.png" alt="État vide QueryBase — aucun résultat de recherche avec suggestions" width="640" height="360" decoding="async">
    </figure>
  </section>

  <section id="roadmap" class="ai-section ai-section--roadmap">
    <h2>Votez pour la prochaine fonctionnalité</h2>
    <p class="ai-prose">La roadmap QueryBase est co-construite avec la communauté. Chaque vote compte — les trois demandes les plus plébiscitées entrent en développement ce trimestre.</p>
    <div class="ai-roadmap-list">
      <article class="ai-roadmap-item">
        <div class="ai-roadmap-info">
          <h3>Connecteur Salesforce bi-directionnel</h3>
          <p>Synchronisation temps réel des comptes, contacts et opportunités sans export CSV intermédiaire.</p>
          <span class="ai-tag">Intégrations</span>
        </div>
        <div class="ai-vote">
          <strong>847</strong> votes
          <button type="button" class="ai-btn ai-btn--vote ai-btn--voted">✓ Voté</button>
        </div>
      </article>
      <article class="ai-roadmap-item">
        <div class="ai-roadmap-info">
          <h3>Mode hors-ligne avec sync diff</h3>
          <p>Travaillez sans connexion, QueryBase réconcilie les modifications au retour du réseau.</p>
          <span class="ai-tag">Performance</span>
        </div>
        <div class="ai-vote">
          <strong>612</strong> votes
          <button type="button" class="ai-btn ai-btn--vote">Voter</button>
        </div>
      </article>
      <article class="ai-roadmap-item">
        <div class="ai-roadmap-info">
          <h3>Requêtes en langage naturel (FR/EN)</h3>
          <p>Décrivez ce que vous cherchez en français courant, QueryBase génère la requête SQL optimisée.</p>
          <span class="ai-tag">IA</span>
        </div>
        <div class="ai-vote">
          <strong>534</strong> votes
          <button type="button" class="ai-btn ai-btn--vote">Voter</button>
        </div>
      </article>
    </div>
  </section>

  <section id="suggestions" class="ai-section ai-section--suggestions">
    <h2>Recherches similaires qui ont abouti</h2>
    <p class="ai-prose">D'autres utilisateurs ont trouvé leur réponse avec ces formulations proches de la vôtre.</p>
    <div class="ai-suggest-grid">
      <a class="ai-suggest-card" href="#">
        <h3>Webhook HubSpot → QueryBase</h3>
        <p>Guide pas-à-pas · 4 min de lecture · mis à jour le 12 juin</p>
      </a>
      <a class="ai-suggest-card" href="#">
        <h3>Import CSV avec mapping automatique</h3>
        <p>Tutoriel vidéo · 8 min · 1 240 vues</p>
      </a>
      <a class="ai-suggest-card" href="#">
        <h3>API REST — endpoints de synchronisation</h3>
        <p>Référence technique · 12 endpoints documentés</p>
      </a>
      <a class="ai-suggest-card" href="#">
        <h3>Connecteur Zapier (legacy)</h3>
        <p>Note de dépréciation · migration vers API v3</p>
      </a>
    </div>
  </section>

  <section class="ai-section ai-section--cta-final">
    <h2>Vous ne trouvez toujours pas ?</h2>
    <p class="ai-lead">Soumettez une requête à notre équipe documentation. Réponse garantie sous vingt-quatre heures ouvrées.</p>
    <a class="ai-cta ai-cta--primary" href="#">Ouvrir un ticket support</a>
  </section>
</main>
<footer class="ai-foot">{HUB}</footer>
"""
    css = _TYPO + """
:root {
  --ai-bg: #fafafa;
  --ai-purple: #7c3aed;
  --ai-purple-light: #a78bfa;
  --ai-text: #18181b;
  --ai-muted: #71717a;
  --ai-border: #e4e4e7;
  --ai-card: #ffffff;
}
* { box-sizing: border-box; }
body { background: var(--ai-bg); color: var(--ai-text); }
.ai-nav--minimal {
  display: flex; align-items: center; gap: 1.5rem;
  padding: 1rem clamp(1rem, 4vw, 2rem);
  background: var(--ai-card); border-bottom: 1px solid var(--ai-border);
}
.ai-logo { font-weight: 800; color: var(--ai-purple); text-decoration: none; font-size: 1.1rem; }
.ai-nav-links { display: flex; gap: 1.25rem; flex: 1; }
.ai-nav-links a { color: var(--ai-muted); text-decoration: none; }
.ai-cta--primary { background: var(--ai-purple); color: #fff; }
.ai-empty-state { text-align: center; max-width: 720px; margin: 0 auto; padding-top: 3rem; }
.ai-empty-icon { font-size: 3rem; margin-bottom: 1rem; }
.ai-empty-state h1 { font-size: clamp(1.5rem, 3.5vw, 2rem); line-height: 1.25; margin-bottom: 1rem; }
.ai-lead { color: var(--ai-muted); margin: 0 auto 1.5rem; }
.ai-search-form { display: flex; gap: 0.5rem; max-width: 560px; margin: 0 auto 1.5rem; flex-wrap: wrap; justify-content: center; }
.ai-search-form input {
  flex: 1; min-width: 240px; padding: 0.75rem 1rem; border: 2px solid var(--ai-border);
  border-radius: 12px; font-family: inherit; font-size: 1rem;
}
.ai-search-form input:focus { outline: none; border-color: var(--ai-purple); }
.ai-btn--primary { background: var(--ai-purple); color: #fff; }
.ai-empty-tips { text-align: left; background: #f4f4f5; border-radius: 12px; padding: 1rem 1.25rem; margin-bottom: 2rem; font-size: 0.95rem; color: var(--ai-muted); }
.ai-empty-tips code { background: #e4e4e7; padding: 0.15rem 0.4rem; border-radius: 4px; font-size: 0.9rem; }
.ai-empty-visual img { width: 100%; border-radius: 16px; border: 1px solid var(--ai-border); opacity: 0.9; }
.ai-section { padding: clamp(2.5rem, 6vw, 4rem) clamp(1rem, 4vw, 2rem); max-width: 900px; margin: 0 auto; }
.ai-section h2 { font-size: 1.5rem; margin-bottom: 0.5rem; }
.ai-prose { color: var(--ai-muted); margin-bottom: 1.5rem; }
.ai-roadmap-list { display: flex; flex-direction: column; gap: 1rem; }
.ai-roadmap-item { display: flex; justify-content: space-between; align-items: center; gap: 1rem; flex-wrap: wrap; background: var(--ai-card); border: 1px solid var(--ai-border); border-radius: 14px; padding: 1.25rem 1.5rem; }
.ai-roadmap-info h3 { margin: 0 0 0.35rem; font-size: 1.05rem; }
.ai-roadmap-info p { margin: 0 0 0.5rem; color: var(--ai-muted); font-size: 0.95rem; max-width: 55ch; }
.ai-tag { display: inline-block; background: #ede9fe; color: var(--ai-purple); font-size: 0.75rem; font-weight: 600; padding: 0.2rem 0.6rem; border-radius: 999px; }
.ai-vote { text-align: center; min-width: 100px; }
.ai-vote strong { display: block; font-size: 1.25rem; color: var(--ai-purple); margin-bottom: 0.5rem; }
.ai-btn--vote { background: #fff; color: var(--ai-purple); border: 2px solid var(--ai-purple); min-width: 90px; }
.ai-btn--voted { background: var(--ai-purple); color: #fff; }
.ai-suggest-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 1rem; }
.ai-suggest-card { display: block; background: var(--ai-card); border: 1px solid var(--ai-border); border-radius: 12px; padding: 1.25rem; text-decoration: none; color: inherit; transition: border-color 0.2s, box-shadow 0.2s; }
.ai-suggest-card:hover { border-color: var(--ai-purple-light); box-shadow: 0 4px 20px rgba(124, 58, 237, 0.1); }
.ai-suggest-card h3 { margin: 0 0 0.35rem; font-size: 1rem; color: var(--ai-purple); }
.ai-suggest-card p { margin: 0; font-size: 0.85rem; color: var(--ai-muted); }
.ai-section--cta-final { text-align: center; background: linear-gradient(180deg, #faf5ff, var(--ai-bg)); border-radius: 20px; }
.ai-foot { text-align: center; padding: 2rem; color: var(--ai-muted); }
"""
    write_ai_site(
        "saas-empty",
        "QueryBase — Empty state & roadmap",
        "État vide de recherche, vote roadmap communautaire et suggestions de requêtes similaires.",
        body,
        css,
        layout="empty-roadmap",
    )


def _pingflow():
    body = f"""
<div class="ai-notif-app">
  <header class="ai-notif-header">
    <a class="ai-logo" href="#">PingFlow</a>
    <div class="ai-notif-header-actions">
      <button type="button" class="ai-btn ai-btn--ghost">Tout marquer lu</button>
      <a class="ai-cta ai-cta--primary" href="#preferences">Préférences</a>
    </div>
  </header>

  <div class="ai-notif-layout">
    <aside class="ai-notif-filters">
      <h2>Filtres</h2>
      <button type="button" class="ai-filter ai-filter--active">Toutes <span>24</span></button>
      <button type="button" class="ai-filter">Non lues <span>7</span></button>
      <button type="button" class="ai-filter">Mentions <span>3</span></button>
      <button type="button" class="ai-filter">Système <span>5</span></button>
      <button type="button" class="ai-filter">Produit <span>9</span></button>
      <hr class="ai-divider">
      <h3>Canaux</h3>
      <label class="ai-channel"><input type="checkbox" checked> In-app</label>
      <label class="ai-channel"><input type="checkbox" checked> Email digest</label>
      <label class="ai-channel"><input type="checkbox"> Push mobile</label>
      <label class="ai-channel"><input type="checkbox" checked> Slack</label>
    </aside>

    <main class="ai-notif-main">
      <div class="ai-notif-toolbar">
        <input type="search" class="ai-notif-search" placeholder="Filtrer les notifications…">
        <select class="ai-notif-sort"><option>Plus récentes</option><option>Plus anciennes</option><option>Par priorité</option></select>
      </div>

      <ul class="ai-notif-list">
        <li class="ai-notif-item ai-notif-item--unread">
          <span class="ai-notif-dot" aria-hidden="true"></span>
          <div class="ai-notif-body">
            <p><strong>Sophie Martin</strong> vous a mentionné dans <em>#release-v4.2</em></p>
            <p class="ai-notif-preview">« @vous peux-tu valider le copy du modal de confirmation avant le déploiement ? »</p>
            <time>Il y a 4 min</time>
          </div>
          <span class="ai-notif-priority ai-priority--high">Haute</span>
        </li>
        <li class="ai-notif-item ai-notif-item--unread">
          <span class="ai-notif-dot" aria-hidden="true"></span>
          <div class="ai-notif-body">
            <p><strong>Alerte MetricPulse</strong> — churn hebdo au-dessus du seuil</p>
            <p class="ai-notif-preview">Segment PME 10-50 : 2,1 % cette semaine (seuil : 2,0 %). Voir le dashboard.</p>
            <time>Il y a 28 min</time>
          </div>
          <span class="ai-notif-priority ai-priority--high">Haute</span>
        </li>
        <li class="ai-notif-item">
          <div class="ai-notif-body">
            <p><strong>Déploiement réussi</strong> — API v3.14.0 en production</p>
            <p class="ai-notif-preview">Durée : 3 min 42 s · zéro rollback · 99,97 % de requêtes 2xx.</p>
            <time>Il y a 1 h</time>
          </div>
          <span class="ai-notif-priority">Info</span>
        </li>
        <li class="ai-notif-item ai-notif-item--unread">
          <span class="ai-notif-dot" aria-hidden="true"></span>
          <div class="ai-notif-body">
            <p><strong>Nouveau vote roadmap</strong> — Connecteur Salesforce</p>
            <p class="ai-notif-preview">847 votes atteints. La fonctionnalité entre en phase de spec technique.</p>
            <time>Il y a 2 h</time>
          </div>
          <span class="ai-notif-priority">Info</span>
        </li>
        <li class="ai-notif-item">
          <div class="ai-notif-body">
            <p><strong>Rappel TalentLoop</strong> — document RIB manquant</p>
            <p class="ai-notif-preview">Votre parcours d'onboarding est bloqué à l'étape 2. Téléversez votre RIB pour continuer.</p>
            <time>Hier, 17:42</time>
          </div>
          <span class="ai-notif-priority ai-priority--med">Moyenne</span>
        </li>
      </ul>

      <figure class="ai-notif-visual">
        <img src="images/hero.png" alt="Centre de notifications PingFlow — interface sombre avec filtres et priorités" width="720" height="400" decoding="async">
      </figure>
    </main>

    <aside id="preferences" class="ai-notif-prefs">
      <h2>Préférences</h2>
      <p class="ai-prose">Configurez quand et comment PingFlow vous interrompt. Le mode focus bloque tout sauf les alertes critiques.</p>
      <div class="ai-pref-group">
        <h3>Fréquence email</h3>
        <label><input type="radio" name="freq" checked> Temps réel</label>
        <label><input type="radio" name="freq"> Digest quotidien (8 h)</label>
        <label><input type="radio" name="freq"> Digest hebdomadaire</label>
      </div>
      <div class="ai-pref-group">
        <h3>Mode focus</h3>
        <label class="ai-toggle"><input type="checkbox"> Activer 9 h – 18 h</label>
        <p class="ai-pref-hint">Seules les alertes « Haute » passent en mode focus.</p>
      </div>
      <div class="ai-pref-group">
        <h3>Sons &amp; vibrations</h3>
        <label><input type="checkbox" checked> Son discret pour mentions</label>
        <label><input type="checkbox"> Vibration mobile</label>
      </div>
      <button type="button" class="ai-btn ai-btn--primary ai-btn--full">Enregistrer</button>
    </aside>
  </div>
</div>
<footer class="ai-foot">{HUB}</footer>
"""
    css = _TYPO + """
:root {
  --ai-bg: #09090b;
  --ai-surface: #18181b;
  --ai-surface-2: #27272a;
  --ai-cyan: #22d3ee;
  --ai-cyan-dim: #0891b2;
  --ai-text: #fafafa;
  --ai-muted: #a1a1aa;
  --ai-border: #3f3f46;
  --ai-unread: #22d3ee;
  --ai-high: #f43f5e;
}
* { box-sizing: border-box; }
body { background: var(--ai-bg); color: var(--ai-text); }
.ai-notif-app { min-height: 100vh; }
.ai-notif-header {
  display: flex; justify-content: space-between; align-items: center;
  padding: 1rem clamp(1rem, 4vw, 2rem);
  border-bottom: 1px solid var(--ai-border);
  background: var(--ai-surface);
}
.ai-logo { font-weight: 800; color: var(--ai-cyan); text-decoration: none; font-size: 1.15rem; }
.ai-notif-header-actions { display: flex; gap: 0.75rem; align-items: center; }
.ai-btn--ghost { background: transparent; color: var(--ai-muted); border: 1px solid var(--ai-border); }
.ai-cta--primary { background: var(--ai-cyan-dim); color: #fff; }
.ai-notif-layout { display: grid; grid-template-columns: 220px 1fr 280px; min-height: calc(100vh - 65px); }
.ai-notif-filters { background: var(--ai-surface); border-right: 1px solid var(--ai-border); padding: 1.25rem 1rem; }
.ai-notif-filters h2, .ai-notif-filters h3 { font-size: 0.8rem; text-transform: uppercase; letter-spacing: 0.06em; color: var(--ai-muted); margin: 0 0 0.75rem; }
.ai-filter {
  display: flex; justify-content: space-between; width: 100%;
  background: transparent; border: none; color: var(--ai-muted);
  padding: 0.55rem 0.75rem; border-radius: 8px; cursor: pointer;
  font-family: inherit; font-size: 0.95rem; text-align: left; margin-bottom: 0.15rem;
}
.ai-filter--active, .ai-filter:hover { background: var(--ai-surface-2); color: var(--ai-text); }
.ai-filter span { background: var(--ai-surface-2); padding: 0.1rem 0.5rem; border-radius: 999px; font-size: 0.8rem; }
.ai-divider { border: none; border-top: 1px solid var(--ai-border); margin: 1rem 0; }
.ai-channel { display: flex; align-items: center; gap: 0.5rem; padding: 0.35rem 0; font-size: 0.9rem; color: var(--ai-muted); cursor: pointer; }
.ai-notif-main { padding: 1.25rem; overflow-y: auto; }
.ai-notif-toolbar { display: flex; gap: 0.75rem; margin-bottom: 1rem; flex-wrap: wrap; }
.ai-notif-search { flex: 1; min-width: 200px; padding: 0.65rem 1rem; background: var(--ai-surface); border: 1px solid var(--ai-border); border-radius: 10px; color: var(--ai-text); font-family: inherit; }
.ai-notif-sort { padding: 0.65rem; background: var(--ai-surface); border: 1px solid var(--ai-border); border-radius: 10px; color: var(--ai-text); font-family: inherit; }
.ai-notif-list { list-style: none; padding: 0; margin: 0 0 1.5rem; }
.ai-notif-item {
  display: flex; align-items: flex-start; gap: 0.75rem;
  padding: 1rem 1.25rem; border-bottom: 1px solid var(--ai-border);
  position: relative;
}
.ai-notif-item--unread { background: rgba(34, 211, 238, 0.04); }
.ai-notif-dot { width: 8px; height: 8px; border-radius: 50%; background: var(--ai-unread); flex-shrink: 0; margin-top: 0.45rem; }
.ai-notif-body { flex: 1; }
.ai-notif-body p { margin: 0 0 0.25rem; }
.ai-notif-preview { color: var(--ai-muted) !important; font-size: 0.9rem; }
.ai-notif-body time { font-size: 0.8rem; color: var(--ai-muted); }
.ai-notif-priority { font-size: 0.75rem; font-weight: 600; padding: 0.2rem 0.5rem; border-radius: 6px; background: var(--ai-surface-2); color: var(--ai-muted); white-space: nowrap; }
.ai-priority--high { background: rgba(244, 63, 94, 0.15); color: var(--ai-high); }
.ai-priority--med { background: rgba(34, 211, 238, 0.1); color: var(--ai-cyan); }
.ai-notif-visual img { width: 100%; border-radius: 12px; border: 1px solid var(--ai-border); opacity: 0.85; }
.ai-notif-prefs { background: var(--ai-surface); border-left: 1px solid var(--ai-border); padding: 1.25rem; }
.ai-notif-prefs h2 { font-size: 1.1rem; margin: 0 0 0.5rem; }
.ai-prose { color: var(--ai-muted); font-size: 0.9rem; margin-bottom: 1.25rem; }
.ai-pref-group { margin-bottom: 1.25rem; }
.ai-pref-group h3 { font-size: 0.85rem; color: var(--ai-muted); margin: 0 0 0.5rem; }
.ai-pref-group label { display: flex; align-items: center; gap: 0.5rem; padding: 0.3rem 0; font-size: 0.9rem; cursor: pointer; }
.ai-pref-hint { font-size: 0.8rem; color: var(--ai-muted); margin: 0.25rem 0 0; }
.ai-btn--primary { background: var(--ai-cyan-dim); color: #fff; }
.ai-btn--full { width: 100%; }
.ai-foot { text-align: center; padding: 1.5rem; color: var(--ai-muted); border-top: 1px solid var(--ai-border); }
@media (max-width: 1024px) {
  .ai-notif-layout { grid-template-columns: 1fr; }
  .ai-notif-filters, .ai-notif-prefs { border: none; border-bottom: 1px solid var(--ai-border); }
}
"""
    write_ai_site(
        "saas-notifications",
        "PingFlow — Centre de notifications",
        "Interface sombre de gestion des notifications : filtres, priorités et panneau de préférences.",
        body,
        css,
        layout="notif-center-dark",
    )


def run() -> list[str]:
    """Génère les 5 vitrines SaaS et retourne la liste des slugs."""
    builders = [_flowmetrics, _talentloop, _metricpulse, _querybase, _pingflow]
    slugs = []
    for fn in builders:
        fn()
        # slug dérivé du dernier appel — on les connaît :
    slugs = [
        "saas-landing",
        "saas-onboarding",
        "saas-dashboard",
        "saas-empty",
        "saas-notifications",
    ]
    return slugs


if __name__ == "__main__":
    generated = run()
    print(f"OK - {len(generated)} vitrines SaaS generees :")
    for s in generated:
        print(f"  · {s}")
