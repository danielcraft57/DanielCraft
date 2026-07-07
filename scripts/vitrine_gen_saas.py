#!/usr/bin/env python3
"""Génère les vitrines SaaS / product UX (inspirées contenus TikTok UX)."""
from vitrine_gen_lib import fig, write_demo

HUB = '<p class="hub-back"><a href="../index.html">← Hub vitrines</a></p>'


def gen_saas_landing():
    g = "sl"
    body = f"""
<a class="skip" href="#contenu">Aller au contenu</a>
<div class="sl-live" aria-live="polite"><strong>247</strong> équipes actives cette semaine · <span>Mise à jour live</span></div>
<header class="sl-nav">
  <span class="sl-logo">FlowMetrics</span>
  <nav><a href="#features">Fonctionnalités</a><a href="#pricing">Tarifs</a><a href="#compare">Comparatif</a></nav>
  <a class="sl-btn sl-btn--primary sl-btn--ctv" href="#pricing">Voir mon funnel en 14 jours — gratuit</a>
</header>
<main id="contenu">
  <section class="sl-hero">
    <p class="sl-eyebrow">Pour fondateurs SaaS · analytics produit</p>
    <h1>Quoi ? Funnels &amp; cohortes. Pour qui ? Équipes produit sans data team. Pourquoi ? Décider avant lundi.</h1>
    <p class="sl-lead">Branché en 12 minutes — pas en 12 semaines. Un seul CTA principal (loi de Hick).</p>
    <div class="sl-hero-cta">
      <a class="sl-btn sl-btn--primary sl-btn--ctv" href="#pricing">Activer mon essai — 14 jours offerts</a>
    </div>
    <figure class="sl-hero-visual">{fig(g, "hero.png", "Dashboard funnel FlowMetrics", lazy=False)}</figure>
  </section>

  <section id="features" class="sl-section">
    <h2>Ce que vous gagnez concrètement</h2>
    <div class="sl-features">
      <article class="sl-feature">
        <div class="sl-before"><strong>Avant</strong><p>3 outils, exports Excel, réunion de sync chaque lundi.</p></div>
        <div class="sl-after"><strong>Après</strong><p>Tout au même endroit, alertes auto, zéro réunion.</p></div>
      </article>
      <article class="sl-feature">
        <div class="sl-before"><strong>Avant</strong><p>Onboarding opaque — personne ne sait où cliquer.</p></div>
        <div class="sl-after"><strong>Après</strong><p>Parcours guidé vers la première victoire en &lt; 2 min.</p></div>
      </article>
      <article class="sl-feature">
        <div class="sl-before"><strong>Avant</strong><p>Pricing flou, plan « contactez-nous » partout.</p></div>
        <div class="sl-after"><strong>Après</strong><p>Grille lisible, plan recommandé mis en avant.</p></div>
      </article>
    </div>
  </section>

  <section id="pricing" class="sl-section sl-pricing">
    <h2>Tarifs transparents</h2>
    <p class="sl-muted">Effet de contraste : l'ancre haute rend le plan Pro évident.</p>
    <div class="sl-plans">
      <article class="sl-plan">
        <h3>Starter</h3>
        <p class="sl-price">29 €<span>/mois</span></p>
        <ul><li>1 projet</li><li>7 jours rétention</li><li class="sl-miss">Pas d'alertes</li></ul>
        <button type="button">Choisir</button>
      </article>
      <article class="sl-plan sl-plan--featured">
        <span class="sl-badge">Le plus choisi</span>
        <h3>Pro</h3>
        <p class="sl-price">79 €<span>/mois</span></p>
        <p class="sl-framing">≈ 2,60 €/jour — moins qu'un café équipe</p>
        <ul><li>Projets illimités</li><li>Alertes Slack</li><li>Cohortes &amp; funnels</li></ul>
        <button type="button" class="sl-btn sl-btn--primary">Essai 14 jours</button>
      </article>
      <article class="sl-plan sl-plan--anchor">
        <h3>Scale</h3>
        <p class="sl-price">199 €<span>/mois</span></p>
        <ul><li>SSO &amp; SLA</li><li>Support dédié</li><li>Export API</li></ul>
        <button type="button">Contacter</button>
      </article>
    </div>
  </section>

  <section id="compare" class="sl-section">
    <h2>Pourquoi FlowMetrics</h2>
    <table class="sl-table">
      <thead><tr><th>Critère</th><th>FlowMetrics</th><th>Spreadsheet + BI</th></tr></thead>
      <tbody>
        <tr><td>Time-to-value</td><td class="sl-yes">✓ &lt; 15 min</td><td class="sl-no">✗ Semaines</td></tr>
        <tr><td>Alertes produit</td><td class="sl-yes">✓ Native</td><td class="sl-no">✗ Manuel</td></tr>
        <tr><td>Onboarding guidé</td><td class="sl-yes">✓ Inclus</td><td class="sl-no">✗ —</td></tr>
      </tbody>
    </table>
  </section>
</main>
<footer class="sl-foot">{HUB}</footer>
"""
    css = """
:root{--bg:#0b1220;--card:#141c2e;--accent:#6366f1;--text:#e2e8f0;--muted:#94a3b8}
*{box-sizing:border-box}body{margin:0;font-family:system-ui,sans-serif;background:var(--bg);color:var(--text);line-height:1.5}
.skip{position:absolute;left:-9999px}.skip:focus{left:1rem;top:1rem;background:#fff;color:#000;padding:.5rem;z-index:99}
.sl-nav{display:flex;align-items:center;gap:1.5rem;padding:1rem 1.5rem;border-bottom:1px solid #1e293b;position:sticky;top:0;background:rgba(11,18,32,.95);backdrop-filter:blur(8px);z-index:10}
.sl-logo{font-weight:800;color:#fff}.sl-nav nav{display:flex;gap:1rem;flex:1}.sl-nav a{color:var(--muted);text-decoration:none;font-size:.9rem}
.sl-btn{display:inline-block;padding:.6rem 1.1rem;border-radius:8px;text-decoration:none;font-weight:600;border:none;cursor:pointer;font-size:.9rem}
.sl-btn--primary{background:var(--accent);color:#fff}.sl-btn--ghost{border:1px solid #334155;color:var(--text)}
.sl-hero{padding:4rem 1.5rem 2rem;max-width:960px;margin:0 auto;text-align:center}
.sl-eyebrow{color:var(--accent);font-size:.85rem;font-weight:600;text-transform:uppercase;letter-spacing:.06em}
.sl-hero h1{font-size:clamp(2rem,5vw,3rem);margin:.75rem 0;line-height:1.15}
.sl-lead{color:var(--muted);max-width:36rem;margin:0 auto 1.5rem}
.sl-hero-cta{display:flex;gap:.75rem;justify-content:center;flex-wrap:wrap;margin-bottom:2rem}
.sl-live{text-align:center;padding:.5rem;background:#1e293b;color:#94a3b8;font-size:.85rem}.sl-live strong{color:#4ade80}
.sl-btn--ctv{font-size:1rem;padding:.75rem 1.35rem}
.sl-framing{font-size:.8rem;color:var(--muted);margin:-.25rem 0 .75rem}
.sl-hero-visual{max-width:720px;margin:2rem auto 0;border-radius:12px;overflow:hidden;border:1px solid #1e293b}
.sl-hero-visual img{width:100%;display:block}
.sl-section{padding:3rem 1.5rem;max-width:960px;margin:0 auto}
.sl-section h2{text-align:center;margin-bottom:1.5rem}
.sl-muted{text-align:center;color:var(--muted);margin-top:-1rem;margin-bottom:2rem}
.sl-features{display:grid;gap:1rem}
.sl-feature{display:grid;grid-template-columns:1fr 1fr;gap:1rem;background:var(--card);border-radius:12px;padding:1rem;border:1px solid #1e293b}
.sl-before{color:var(--muted)}.sl-after strong{color:#a5b4fc}
.sl-plans{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:1rem;align-items:start}
.sl-plan{background:var(--card);border:1px solid #1e293b;border-radius:12px;padding:1.25rem;position:relative}
.sl-plan--featured{border-color:var(--accent);box-shadow:0 0 0 1px var(--accent)}
.sl-plan--anchor{opacity:.85}.sl-badge{position:absolute;top:-10px;left:50%;transform:translateX(-50%);background:var(--accent);color:#fff;font-size:.7rem;padding:.2rem .6rem;border-radius:99px;white-space:nowrap}
.sl-price{font-size:2rem;font-weight:800;margin:.5rem 0}.sl-price span{font-size:.9rem;font-weight:400;color:var(--muted)}
.sl-plan ul{list-style:none;padding:0;margin:1rem 0;font-size:.9rem;color:var(--muted)}
.sl-plan li{margin:.35rem 0}.sl-miss{text-decoration:line-through;opacity:.6}
.sl-plan button{width:100%;padding:.65rem;border-radius:8px;border:1px solid #334155;background:transparent;color:var(--text);cursor:pointer}
.sl-table{width:100%;border-collapse:collapse;font-size:.9rem}
.sl-table th,.sl-table td{padding:.75rem;border-bottom:1px solid #1e293b;text-align:left}
.sl-yes{color:#4ade80}.sl-no{color:#f87171}
.sl-foot{padding:2rem;text-align:center;color:var(--muted);border-top:1px solid #1e293b}
@media(max-width:640px){.sl-feature{grid-template-columns:1fr}.sl-nav nav{display:none}}
"""
    write_demo("saas-landing", "contrast-pricing", "tailwind", "FlowMetrics — Landing SaaS",
               "Landing SaaS : hero, features avant/après, pricing avec effet de contraste.", body, css)


def gen_saas_onboarding():
    g = "ob"
    body = f"""
<a class="skip" href="#contenu">Aller au contenu</a>
<main id="contenu" class="ob-shell">
  <aside class="ob-aside">
    <div class="ob-preview">
      <p>TalentLoop</p>
      {fig(g, "hero.png", "Aperçu offre publiée", lazy=False)}
    </div>
  </aside>
  <section class="ob-panel" id="ob-step2">
    <div class="ob-progress" role="progressbar" aria-valuenow="2" aria-valuemin="1" aria-valuemax="4">
      <div class="ob-progress-fill" style="width:50%"></div>
    </div>
    <p class="ob-step-label">Étape 2 sur 4 — Infos entreprise</p>
    <h1>Ces infos apparaîtront sur votre offre publiée</h1>
    <p class="ob-hint">Nom, logo et localisation rassurent les candidats avant même la description du poste.</p>
    <form class="ob-form" action="#" onsubmit="return false">
      <label>Nom de l'entreprise<input type="text" placeholder="Ex. Atelier Nord" value=""></label>
      <label>Secteur<select><option>Tech &amp; produit</option><option>Industrie</option></select></label>
      <label>Ville<input type="text" placeholder="Metz"></label>
      <div class="ob-actions">
        <button type="button" class="ob-back">Retour</button>
        <button type="submit" class="ob-next">Continuer →</button>
      </div>
    </form>
    <ol class="ob-trail" aria-label="Parcours onboarding">
      <li class="done">Inscription</li>
      <li class="active">Entreprise</li>
      <li>Créer l'offre</li>
      <li>Publier</li>
    </ol>
  </section>
  <section class="ob-victory" id="ob-victory" hidden>
    <div class="ob-victory-inner">
      <p class="ob-victory-badge">Peak moment ✓</p>
      <h2>Votre offre est en ligne</h2>
      <p>Les candidats peuvent postuler — vous avez atteint votre aha moment en 4 étapes.</p>
      <button type="button" class="ob-next">Inviter mon équipe (optionnel)</button>
      <a href="#" class="ob-skip">Plus tard — explorer le tableau de bord</a>
    </div>
  </section>
</main>
<footer class="ob-foot">{HUB}</footer>
"""
    css = """
:root{--bg:#f8fafc;--card:#fff;--accent:#0ea5e9;--text:#0f172a;--muted:#64748b}
*{box-sizing:border-box}body{margin:0;font-family:system-ui,sans-serif;background:var(--bg);color:var(--text)}
.skip{position:absolute;left:-9999px}.skip:focus{left:1rem;top:1rem;background:#000;color:#fff;padding:.5rem;z-index:99}
.ob-shell{display:grid;grid-template-columns:1fr 1fr;min-height:100vh}
.ob-aside{background:linear-gradient(135deg,#0c4a6e,#0369a1);color:#fff;padding:2rem;display:flex;align-items:center;justify-content:center}
.ob-preview{text-align:center}.ob-preview img{width:100%;border-radius:12px;margin-top:1rem}
.ob-victory{padding:3rem 1.5rem;text-align:center;background:#ecfdf5;min-height:50vh;display:flex;align-items:center;justify-content:center}
.ob-victory-inner{max-width:420px}.ob-victory-badge{color:#16a34a;font-weight:700;font-size:.85rem}
.ob-victory h2{margin:.5rem 0}.ob-skip{display:block;margin-top:1rem;color:var(--muted);font-size:.85rem}
.ob-panel{padding:2.5rem 2rem;max-width:480px;display:flex;flex-direction:column;justify-content:center;margin:0 auto;width:100%}
.ob-progress{height:6px;background:#e2e8f0;border-radius:99px;margin-bottom:1rem;overflow:hidden}
.ob-progress-fill{height:100%;background:var(--accent);border-radius:99px}
.ob-step-label{font-size:.8rem;color:var(--accent);font-weight:600;margin:0 0 .5rem}
.ob-panel h1{font-size:1.5rem;margin:0 0 .75rem;line-height:1.25}
.ob-hint{color:var(--muted);font-size:.95rem;margin:0 0 1.5rem}
.ob-form label{display:block;margin-bottom:1rem;font-size:.85rem;font-weight:600}
.ob-form input,.ob-form select{width:100%;margin-top:.35rem;padding:.65rem;border:1px solid #cbd5e1;border-radius:8px;font:inherit}
.ob-actions{display:flex;gap:.75rem;margin-top:.5rem}
.ob-back{padding:.65rem 1rem;border:1px solid #cbd5e1;background:#fff;border-radius:8px;cursor:pointer}
.ob-next{padding:.65rem 1.25rem;background:var(--accent);color:#fff;border:none;border-radius:8px;font-weight:600;cursor:pointer;flex:1}
.ob-trail{display:flex;gap:.5rem;list-style:none;padding:0;margin:2rem 0 0;font-size:.75rem;color:var(--muted);flex-wrap:wrap}
.ob-trail li{padding:.25rem .5rem;border-radius:99px;background:#e2e8f0}
.ob-trail .done{background:#dcfce7;color:#166534}.ob-trail .active{background:#e0f2fe;color:#0369a1;font-weight:600}
.ob-foot{padding:1rem;text-align:center;color:var(--muted);font-size:.85rem}
@media(max-width:768px){.ob-shell{grid-template-columns:1fr}.ob-aside{display:none}}
"""
    write_demo("saas-onboarding", "hr-path", "tailwind", "TalentLoop — Onboarding SaaS RH",
               "Onboarding en 4 étapes : barre de progression, copy orienté valeur, aha moment.", body, css)


def gen_saas_dashboard():
    g = "db"
    body = f"""
<a class="skip" href="#contenu">Aller au contenu</a>
<div class="db-layout">
  <aside class="db-sidebar" aria-label="Navigation produit">
    <span class="db-logo">MetricPulse</span>
    <nav>
      <p class="db-nav-group">Pilotage</p>
      <a class="active" href="#"><i aria-hidden="true">📊</i> Vue d'ensemble</a>
      <a href="#"><i aria-hidden="true">🎯</i> Activation</a>
      <a href="#"><i aria-hidden="true">📈</i> Rétention</a>
      <p class="db-nav-group">Actions</p>
      <a href="#"><i aria-hidden="true">🔔</i> Alertes</a>
      <a href="#"><i aria-hidden="true">⚙️</i> Paramètres</a>
    </nav>
    <p class="db-sidebar-hint">≤7 items · regroupés par intention</p>
  </aside>
  <main id="contenu" class="db-main">
    <header class="db-top"><h1>Vue d'ensemble</h1><span class="db-period">7 derniers jours</span></header>
    <figure class="db-hero-fig">{fig(g, "hero.png", "Aperçu dashboard", lazy=False)}</figure>
    <div class="db-kpis">
      <article><strong>84 %</strong><span>Activation J7</span><em class="up">+12 pts</em></article>
      <article><strong>3m 42s</strong><span>Time to value</span><em class="up">−28 %</em></article>
      <article><strong>2,4 %</strong><span>Churn mensuel</span><em class="down">+0,3 pt</em></article>
    </div>
    <section class="db-chart-block" aria-label="Graphique activation">
      <h2>Funnel onboarding</h2>
      <div class="db-bars">
        <div style="--w:100%"><span>Inscription</span><i style="width:var(--w)"></i></div>
        <div style="--w:72%"><span>Profil complété</span><i style="width:var(--w)"></i></div>
        <div style="--w:58%"><span>Première action</span><i style="width:var(--w)"></i></div>
        <div style="--w:41%"><span>Aha moment</span><i style="width:var(--w)"></i></div>
      </div>
    </section>
    <section class="db-table-block">
      <h2>Événements récents</h2>
      <table><thead><tr><th>Utilisateur</th><th>Événement</th><th>Quand</th></tr></thead>
      <tbody>
        <tr><td>marie@…</td><td>Première offre publiée</td><td>Il y a 4 min</td></tr>
        <tr><td>alex@…</td><td>Onboarding terminé</td><td>Il y a 12 min</td></tr>
        <tr><td>team@…</td><td>Invite équipe (skip)</td><td>Il y a 1 h</td></tr>
      </tbody></table>
    </section>
  </main>
</div>
<footer class="db-foot">{HUB}</footer>
"""
    css = """
:root{--bg:#f1f5f9;--sidebar:#0f172a;--card:#fff;--accent:#8b5cf6;--text:#0f172a;--muted:#64748b}
*{box-sizing:border-box}body{margin:0;font-family:system-ui,sans-serif;background:var(--bg);color:var(--text);font-size:14px}
.skip{position:absolute;left:-9999px}.skip:focus{left:1rem;top:1rem;background:#000;color:#fff;padding:.5rem;z-index:99}
.db-layout{display:grid;grid-template-columns:220px 1fr;min-height:100vh}
.db-sidebar{background:var(--sidebar);color:#cbd5e1;padding:1.25rem 0}
.db-logo{display:block;padding:0 1.25rem 1rem;font-weight:800;color:#fff;font-size:1.1rem}
.db-nav-group{padding:.75rem 1.25rem .25rem;font-size:.65rem;text-transform:uppercase;letter-spacing:.08em;color:#475569;margin:0}
.db-sidebar nav a{display:flex;align-items:center;gap:.5rem;padding:.55rem 1.25rem;color:#94a3b8;text-decoration:none;border-left:3px solid transparent}
.db-sidebar nav a.active{background:#1e293b;color:#fff;border-left-color:var(--accent)}
.db-sidebar-hint{padding:1rem 1.25rem;font-size:.65rem;color:#475569;margin:0}
.db-hero-fig{margin:0 0 1rem;border-radius:10px;overflow:hidden;border:1px solid #e2e8f0}
.db-hero-fig img{width:100%;display:block}
.db-main{padding:1.5rem 2rem}
.db-top{display:flex;justify-content:space-between;align-items:center;margin-bottom:1.25rem}
.db-top h1{margin:0;font-size:1.35rem}.db-period{font-size:.85rem;color:var(--muted);background:var(--card);padding:.35rem .75rem;border-radius:6px}
.db-kpis{display:grid;grid-template-columns:repeat(auto-fit,minmax(160px,1fr));gap:1rem;margin-bottom:1.5rem}
.db-kpis article{background:var(--card);padding:1rem;border-radius:10px;border:1px solid #e2e8f0}
.db-kpis strong{display:block;font-size:1.75rem}.db-kpis span{color:var(--muted);font-size:.8rem}
.db-kpis em{font-size:.75rem;font-style:normal;display:block;margin-top:.25rem}
.db-kpis .up{color:#16a34a}.db-kpis .down{color:#dc2626}
.db-chart-block,.db-table-block{background:var(--card);border-radius:10px;padding:1.25rem;border:1px solid #e2e8f0;margin-bottom:1rem}
.db-chart-block h2,.db-table-block h2{margin:0 0 1rem;font-size:1rem}
.db-bars{display:flex;flex-direction:column;gap:.65rem}
.db-bars div{display:grid;grid-template-columns:140px 1fr;align-items:center;gap:.75rem;font-size:.85rem;color:var(--muted)}
.db-bars i{display:block;height:10px;background:linear-gradient(90deg,var(--accent),#c4b5fd);border-radius:99px}
.db-table-block table{width:100%;border-collapse:collapse;font-size:.85rem}
.db-table-block th,.db-table-block td{padding:.5rem 0;border-bottom:1px solid #f1f5f9;text-align:left}
.db-foot{padding:1rem 2rem 1rem 240px;color:var(--muted);font-size:.85rem}
@media(max-width:768px){.db-layout{grid-template-columns:1fr}.db-sidebar{display:none}.db-foot{padding-left:1rem}}
"""
    write_demo("saas-dashboard", "sidebar-analytics", "tailwind", "MetricPulse — Dashboard SaaS",
               "Dashboard produit : sidebar par intention, KPIs activation, funnel onboarding.", body, css)


def gen_saas_empty():
    body = f"""
<a class="skip" href="#contenu">Aller au contenu</a>
<header class="es-nav"><span class="es-logo">QueryBase</span></header>
<main id="contenu" class="es-main">
  <div class="es-search-wrap">
    <figure class="es-hero">{fig("es", "hero.png", "Recherche QueryBase", lazy=False)}</figure>
    <label for="q" class="visually-hidden">Rechercher</label>
    <input id="q" type="search" value="rapport fiscal Q4" readonly aria-describedby="es-hint">
    <p id="es-hint" class="es-hint">Démo : recherche sans résultat exact — trois patterns UX.</p>
  </div>

  <section class="es-empty" aria-labelledby="es-title">
    <div class="es-icon" aria-hidden="true">🔍</div>
    <h1 id="es-title">Aucun résultat pour « rapport fiscal Q4 »</h1>
    <p class="es-sub">Mais voici ce que d'autres équipes consultent le plus :</p>
    <div class="es-suggestions">
      <a class="es-chip" href="#">Rapport revenus mensuel</a>
      <a class="es-chip" href="#">Export comptable CSV</a>
      <a class="es-chip" href="#">Tableau TVA trimestriel</a>
    </div>
  </section>

  <section class="es-roadmap" aria-labelledby="es-roadmap-title">
    <h2 id="es-roadmap-title">Pas encore disponible ?</h2>
    <p>Dites-nous si vous voulez qu'on le développe — ça priorise notre roadmap.</p>
    <button type="button" class="es-vote">👍 Je vote pour « rapport fiscal Q4 »</button>
    <span class="es-votes">127 votes cette semaine</span>
  </section>

  <section class="es-didyou" aria-labelledby="es-didyou-title">
    <h2 id="es-didyou-title">Vouliez-vous dire…</h2>
    <ul>
      <li><a href="#">Billing — facturation &amp; abonnements</a></li>
      <li><a href="#">Fiscal — paramètres TVA</a></li>
    </ul>
  </section>
</main>
<footer class="es-foot">{HUB}</footer>
"""
    css = """
:root{--bg:#fafafa;--card:#fff;--accent:#059669;--text:#171717;--muted:#737373}
*{box-sizing:border-box}body{margin:0;font-family:system-ui,sans-serif;background:var(--bg);color:var(--text)}
.visually-hidden{position:absolute;width:1px;height:1px;padding:0;margin:-1px;overflow:hidden;clip:rect(0,0,0,0);border:0}
.skip{position:absolute;left:-9999px}.skip:focus{left:1rem;top:1rem;background:#000;color:#fff;padding:.5rem;z-index:99}
.es-nav{padding:1rem 1.5rem;border-bottom:1px solid #e5e5e5;background:var(--card)}
.es-logo{font-weight:800}
.es-main{max-width:560px;margin:0 auto;padding:2rem 1.5rem}
.es-hero{margin:0 0 1.5rem;border-radius:12px;overflow:hidden}.es-hero img{width:100%;display:block}
.es-hint{font-size:.8rem;color:var(--muted);margin:.5rem 0 2rem}
.es-empty{text-align:center;padding:2rem 1rem;background:var(--card);border-radius:12px;border:1px solid #e5e5e5;margin-bottom:1.5rem}
.es-icon{font-size:2rem;margin-bottom:.5rem}
.es-empty h1{font-size:1.15rem;margin:0 0 .5rem}
.es-sub{color:var(--muted);font-size:.9rem;margin:0 0 1rem}
.es-suggestions{display:flex;flex-wrap:wrap;gap:.5rem;justify-content:center}
.es-chip{padding:.45rem .85rem;background:#ecfdf5;color:var(--accent);border-radius:99px;text-decoration:none;font-size:.85rem;font-weight:500;border:1px solid #a7f3d0}
.es-roadmap,.es-didyou{background:var(--card);border:1px solid #e5e5e5;border-radius:12px;padding:1.25rem;margin-bottom:1rem}
.es-roadmap h2,.es-didyou h2{font-size:1rem;margin:0 0 .35rem}
.es-roadmap p,.es-didyou ul{color:var(--muted);font-size:.9rem;margin:0 0 .75rem}
.es-vote{padding:.6rem 1rem;background:var(--accent);color:#fff;border:none;border-radius:8px;cursor:pointer;font-weight:600}
.es-votes{display:block;margin-top:.5rem;font-size:.8rem;color:var(--muted)}
.es-didyou ul{list-style:none;padding:0;margin:0}
.es-didyou a{color:var(--accent);text-decoration:none;font-weight:500}
.es-foot{padding:1.5rem;text-align:center;color:var(--muted);font-size:.85rem}
"""
    write_demo("saas-empty", "search-empty", "tailwind", "QueryBase — Empty states",
               "Recherche sans résultat : best-sellers, vote roadmap, correcteur d'intention.", body, css)


def gen_saas_notifications():
    body = f"""
<a class="skip" href="#contenu">Aller au contenu</a>
<div class="nt-layout">
  <aside class="nt-sidebar"><span class="nt-logo">PingFlow</span>{fig("nt", "hero.png", "Centre notifications", lazy=False)}</aside>
  <main id="contenu" class="nt-main">
    <header class="nt-header">
      <h1>Centre de notifications</h1>
      <div class="nt-tabs" role="tablist">
        <button type="button" class="active" role="tab" aria-selected="true">Toutes</button>
        <button type="button" role="tab">Produit</button>
        <button type="button" role="tab">Équipe</button>
      </div>
    </header>
    <ul class="nt-list">
      <li class="nt-item nt-item--action">
        <span class="nt-badge nt-badge--urgent">Action requise</span>
        <strong>Votre essai se termine dans 3 jours</strong>
        <p>Ajoutez un moyen de paiement pour conserver vos alertes Slack.</p>
        <div class="nt-actions"><button type="button" class="nt-primary">Mettre à jour</button><button type="button" class="nt-ghost">Plus tard</button></div>
      </li>
      <li class="nt-item">
        <span class="nt-badge">Produit</span>
        <strong>+18 % d'activation cette semaine</strong>
        <p>Le nouveau parcours onboarding performe mieux que l'ancien.</p>
        <time datetime="2026-07-03">Il y a 2 h</time>
      </li>
      <li class="nt-item nt-item--muted">
        <span class="nt-badge">Info</span>
        <strong>Maintenance planifiée — dim. 4 h–6 h</strong>
        <p>Aucune action de votre part. Les exports seront retardés.</p>
        <time datetime="2026-07-02">Hier</time>
      </li>
      <li class="nt-item">
        <span class="nt-badge">Équipe</span>
        <strong>Marie a commenté votre rapport</strong>
        <p>« Peux-tu ajouter la cohorte mobile ? »</p>
        <time datetime="2026-07-01">Il y a 2 jours</time>
      </li>
    </ul>
    <section class="nt-settings" aria-labelledby="nt-prefs">
      <h2 id="nt-prefs">Préférences (démo)</h2>
      <label><input type="checkbox" checked> E-mail récap hebdo</label>
      <label><input type="checkbox" checked> Push in-app — actions requises</label>
      <label><input type="checkbox"> Marketing produit</label>
    </section>
  </main>
</div>
<footer class="nt-foot">{HUB}</footer>
"""
    css = """
:root{--bg:#111827;--card:#1f2937;--accent:#f59e0b;--text:#f9fafb;--muted:#9ca3af}
*{box-sizing:border-box}body{margin:0;font-family:system-ui,sans-serif;background:var(--bg);color:var(--text)}
.skip{position:absolute;left:-9999px}.skip:focus{left:1rem;top:1rem;background:#fff;color:#000;padding:.5rem;z-index:99}
.nt-layout{display:grid;grid-template-columns:180px 1fr;min-height:100vh}
.nt-sidebar{padding:1.25rem;border-right:1px solid #374151}
.nt-sidebar img{width:100%;margin-top:1rem;border-radius:8px;opacity:.85}
.nt-main{padding:1.5rem 2rem;max-width:640px}
.nt-header h1{margin:0 0 1rem;font-size:1.35rem}
.nt-tabs{display:flex;gap:.5rem;margin-bottom:1.25rem}
.nt-tabs button{padding:.4rem .85rem;border-radius:99px;border:1px solid #374151;background:transparent;color:var(--muted);cursor:pointer;font-size:.85rem}
.nt-tabs button.active{background:var(--accent);color:#111827;border-color:var(--accent);font-weight:600}
.nt-list{list-style:none;padding:0;margin:0 0 1.5rem}
.nt-item{background:var(--card);border:1px solid #374151;border-radius:10px;padding:1rem;margin-bottom:.65rem}
.nt-item--action{border-color:var(--accent)}
.nt-item--muted{opacity:.75}
.nt-badge{display:inline-block;font-size:.65rem;text-transform:uppercase;letter-spacing:.05em;padding:.15rem .45rem;border-radius:4px;background:#374151;color:var(--muted);margin-bottom:.35rem}
.nt-badge--urgent{background:#78350f;color:#fcd34d}
.nt-item strong{display:block;margin-bottom:.25rem}
.nt-item p{margin:0 0 .5rem;color:var(--muted);font-size:.9rem}
.nt-item time{font-size:.75rem;color:#6b7280}
.nt-actions{display:flex;gap:.5rem;margin-top:.5rem}
.nt-primary{padding:.45rem .85rem;background:var(--accent);color:#111827;border:none;border-radius:6px;font-weight:600;cursor:pointer}
.nt-ghost{padding:.45rem .85rem;background:transparent;color:var(--muted);border:1px solid #374151;border-radius:6px;cursor:pointer}
.nt-settings{background:var(--card);border:1px solid #374151;border-radius:10px;padding:1rem}
.nt-settings h2{font-size:.95rem;margin:0 0 .75rem}
.nt-settings label{display:block;margin:.35rem 0;font-size:.85rem;color:var(--muted)}
.nt-foot{padding:1rem 2rem 1rem 200px;color:var(--muted);font-size:.85rem}
@media(max-width:640px){.nt-layout{grid-template-columns:1fr}.nt-sidebar{display:none}.nt-foot{padding-left:1rem}}
"""
    write_demo("saas-notifications", "in-app-center", "tailwind", "PingFlow — Notifications",
               "Centre de notifications : hiérarchie, action requise, préférences granulaires.", body, css)


def run():
    gen_saas_landing()
    gen_saas_onboarding()
    gen_saas_dashboard()
    gen_saas_empty()
    gen_saas_notifications()
    print("[OK] 5 vitrines SaaS UX générées")


if __name__ == "__main__":
    run()
