// ===== Rapport d'analyse - Page /analyse (maquette A) =====

(function () {
  const API_BASE = '';
  const ENDPOINT = '/api/website-analysis.php';
  const FREE_AUDIT_ENDPOINT = '/api/request-free-audit.php';
  const PREMIUM_CHECKOUT_ENDPOINT = '/api/stripe-create-audit-checkout.php';
  const STORAGE_KEY = 'dc_audit_checkout_pending';

  const pageRoot = document.querySelector('.page-analyse');
  const auditSlug = (pageRoot && pageRoot.getAttribute('data-audit-slug')) || 'audit-complet-ia';

  const OFFERS = [
    {
      key: 'performance',
      slug: 'rapport-vitesse',
      title: 'Site plus rapide',
      desc: 'Optimisez la vitesse de chargement et l\'experience sur mobile.',
      icon: 'fa-gauge-high',
      iconMod: 'perf'
    },
    {
      key: 'seo',
      slug: 'referencement-google',
      title: 'Etre trouve sur Google',
      desc: 'Ameliorez votre referencement et votre visibilite locale.',
      icon: 'fa-magnifying-glass',
      iconMod: 'seo'
    },
    {
      key: 'securite',
      slug: 'sauvegardes-securite',
      title: 'Securiser le site',
      desc: 'Protegez votre site et vos donnees avec les bons reflexes.',
      icon: 'fa-shield-halved',
      iconMod: 'sec'
    },
    {
      key: 'vitrine',
      slug: 'site-vitrine',
      title: 'Vitrine claire',
      desc: 'Mettez en valeur votre activite avec un site clair et efficace.',
      icon: 'fa-window-maximize',
      iconMod: 'vitrine'
    }
  ];

  const els = {
    bootWrap: document.getElementById('plBootWrap'),
    boot: document.getElementById('plBoot'),
    form: document.getElementById('plForm'),
    url: document.getElementById('plUrl'),
    submit: document.getElementById('plSubmitBtn'),
    bootFeedback: document.getElementById('plBootFeedback'),
    loading: document.getElementById('plLoading'),
    loadingUrl: document.getElementById('plLoadingUrl'),
    loadingStep: document.getElementById('plLoadingStep'),
    loadingScores: document.getElementById('plLoadingScores'),
    convertLoader: document.getElementById('plConvertLoader'),
    convertReport: document.getElementById('plConvertReport'),
    leadModal: document.getElementById('plLeadModal'),
    leadModalTitle: document.getElementById('plLeadModalTitle'),
    leadModalLead: document.getElementById('plLeadModalLead'),
    leadSubmitLabel: document.getElementById('plLeadSubmitLabel'),
    reportHero: document.getElementById('plReportHero'),
    report: document.getElementById('plReport'),
    companyName: document.getElementById('plCompanyName'),
    siteLink: document.getElementById('plSiteLink'),
    siteLabel: document.getElementById('plSiteLabel'),
    reportDate: document.getElementById('plReportDate'),
    scores: document.getElementById('plScores'),
    screenshot: document.getElementById('plScreenshot'),
    shotUrl: document.getElementById('plShotUrl'),
    intro: document.querySelector('.analyse-intro'),
    insights: document.getElementById('plInsights'),
    details: document.getElementById('plDetails'),
    offers: document.getElementById('plOffers'),
    leadForm: document.getElementById('plLeadForm'),
    leadName: document.getElementById('plLeadName'),
    leadEmail: document.getElementById('plLeadEmail'),
    leadSite: document.getElementById('plLeadSite'),
    leadSubmit: document.getElementById('plLeadSubmit'),
    leadFeedback: document.getElementById('plLeadFeedback'),
    leadSuccess: document.getElementById('plLeadSuccess'),
    leadSuccessText: document.getElementById('plLeadSuccessText'),
    premiumFeedback: document.getElementById('plPremiumFeedback')
  };

  if (!els.form || !els.url || !els.submit) return;

  let currentWebsite = '';
  let loadingStepTimer = null;
  let loadingStepIndex = 0;
  let loaderRevealToken = 0;
  let modalMode = 'free';
  let modalPreviousFocus = null;

  const LOADER_SCORE_DEFS = [
    { key: 'performance', label: 'Performance' },
    { key: 'seo', label: 'SEO' },
    { key: 'securite', label: 'Securite' },
    { key: 'risque', label: 'Risque' }
  ];

  const LOADING_STEPS = [
    'Connexion au site…',
    'Mesure de la performance…',
    'Analyse SEO et contenu…',
    'Verification securite…',
    'Preparation du rapport…'
  ];

  function setFeedback(el, message, isError) {
    if (!el) return;
    if (!message) {
      el.hidden = true;
      el.textContent = '';
      return;
    }
    el.hidden = false;
    el.textContent = message;
    el.className = 'form-feedback ' + (isError ? 'form-feedback--error' : 'form-feedback--success');
  }

  function setBootLoading(isLoading) {
    els.submit.classList.toggle('is-loading', isLoading);
    els.submit.disabled = isLoading;
  }

  function setBtnLoading(btn, isLoading) {
    if (!btn) return;
    btn.disabled = isLoading;
    const label = btn.querySelector('.analyse-submit__label');
    const loading = btn.querySelector('.analyse-submit__loading');
    if (label) label.hidden = !!isLoading;
    if (loading) loading.hidden = !isLoading;
  }

  function safeUrl(raw) {
    try {
      let s = String(raw || '').trim();
      if (!s) return null;
      if (!/^https?:\/\//i.test(s)) s = 'https://' + s;
      const u = new URL(s);
      if (!['http:', 'https:'].includes(u.protocol)) return null;
      return u.toString();
    } catch {
      return null;
    }
  }

  function displayHost(url) {
    try {
      return new URL(url).host.replace(/^www\./, '');
    } catch {
      return String(url || '').replace(/^https?:\/\//, '');
    }
  }

  function escapeHtml(s) {
    return String(s)
      .replaceAll('&', '&amp;')
      .replaceAll('<', '&lt;')
      .replaceAll('>', '&gt;')
      .replaceAll('"', '&quot;')
      .replaceAll("'", '&#039;');
  }

  function stripHtml(s) {
    return String(s || '').replace(/<[^>]+>/g, '').trim();
  }

  function toArray(v) {
    return Array.isArray(v) ? v : (v == null ? [] : [v]);
  }

  function formatDate(s) {
    if (!s) return null;
    const d = new Date(s);
    if (Number.isNaN(d.getTime())) return String(s);
    return d.toLocaleString('fr-FR');
  }

  function safeJsonParse(maybeJson) {
    if (maybeJson == null) return null;
    if (typeof maybeJson === 'object') return maybeJson;
    if (typeof maybeJson !== 'string') return null;
    try { return JSON.parse(maybeJson); } catch { return null; }
  }

  function toneFromScore(score100, invert) {
    const v = typeof score100 === 'number' ? score100 : null;
    if (v == null) return 'warn';
    const x = invert ? (100 - v) : v;
    if (x >= 80) return 'good';
    if (x >= 50) return 'warn';
    return 'bad';
  }

  function scoreColor(score0to100, invert) {
    const x = invert ? (100 - score0to100) : score0to100;
    if (x >= 80) return 'var(--analyse-green, #10b981)';
    if (x >= 50) return 'var(--analyse-amber, #f59e0b)';
    return 'var(--analyse-red, #dc2626)';
  }

  function ringColorForKey(key) {
    switch (key) {
      case 'performance': return '#10b981';
      case 'seo': return '#2563eb';
      case 'securite': return '#0d9488';
      case 'risque':
      case 'pentest': return '#f59e0b';
      default: return '#64748b';
    }
  }

  function scoreNote(key, value) {
    if (typeof value !== 'number') return '—';
    if (key === 'pentest' || key === 'risque') {
      if (value <= 30) return 'Faible';
      if (value <= 60) return 'Moyen';
      return 'Eleve';
    }
    if (key === 'securite') {
      if (value >= 90) return 'Excellente';
      if (value >= 75) return 'Bonne';
      if (value >= 50) return 'Moyenne';
      return 'Faible';
    }
    if (key === 'seo') {
      if (value >= 90) return 'Excellent';
      if (value >= 75) return 'Bien';
      if (value >= 50) return 'Moyen';
      return 'Faible';
    }
    if (value >= 90) return 'Excellente';
    if (value >= 75) return 'Bonne';
    if (value >= 50) return 'Moyenne';
    return 'Faible';
  }

  function tableHtml(headers, rows) {
    const th = headers.map(h => `<th>${escapeHtml(h)}</th>`).join('');
    const tr = rows.map(r => `<tr>${r.map(c => `<td>${c}</td>`).join('')}</tr>`).join('');
    return `<div class="pl-table"><table><thead><tr>${th}</tr></thead><tbody>${tr}</tbody></table></div>`;
  }

  function splitName(full) {
    const parts = String(full || '').trim().split(/\s+/).filter(Boolean);
    if (!parts.length) return { first: '', last: '' };
    if (parts.length === 1) return { first: parts[0], last: '' };
    return { first: parts[0], last: parts.slice(1).join(' ') };
  }

  function sleep(ms) {
    return new Promise((resolve) => window.setTimeout(resolve, ms));
  }

  function setBootVisible(show) {
    if (els.bootWrap) els.bootWrap.hidden = !show;
  }

  function resetLoaderScores() {
    loaderRevealToken += 1;
    if (!els.loadingScores) return;
    els.loadingScores.innerHTML = '';
    LOADER_SCORE_DEFS.forEach((def) => {
      const card = document.createElement('div');
      card.className = 'analyse-loader__score analyse-loader__score--' + def.key;
      card.dataset.scoreKey = def.key;
      card.innerHTML = `
        <div class="analyse-loader__score-ring analyse-loader__score-ring--pending" aria-hidden="true"></div>
        <div class="analyse-loader__score-copy">
          <div class="analyse-loader__score-label">${escapeHtml(def.label)}</div>
          <div class="analyse-loader__score-value">—</div>
        </div>
      `;
      els.loadingScores.appendChild(card);
    });
  }

  async function revealLoaderScorePlaceholders() {
    const token = loaderRevealToken;
    const cards = els.loadingScores ? els.loadingScores.querySelectorAll('.analyse-loader__score') : [];
    if (!cards.length) return;
    const step = prefersReducedMotion() ? 0 : 320;
    for (let i = 0; i < cards.length; i += 1) {
      if (token !== loaderRevealToken) return;
      if (step > 0) await sleep(step);
      cards[i].classList.add('is-in');
    }
  }

  function buildLoaderScoreValueHtml(it) {
    const key = it?.key || 'score';
    const score100 = typeof it?.value === 'number' ? Math.round(it.value) : null;
    const ring = score100 == null ? 0 : Math.max(0, Math.min(100, score100));
    const color = score100 == null ? 'rgba(15,23,42,0.18)' : ringColorForKey(key);
    const note = it?.noteClient || scoreNote(key, score100);
    return {
      ringHtml: `
        <div class="pl-score-ring analyse-loader__score-ring--live" style="--pl-ring:${ring}%; --pl-ring-live:0%; --pl-ring-color:${color};" data-ring-target="${ring}" aria-hidden="true">
          <div class="pl-score-value">${score100 ?? '—'}</div>
        </div>
      `,
      note: note
    };
  }

  async function fillLoaderScoresFromReport(raw) {
    const token = loaderRevealToken;
    const cards = els.loadingScores ? els.loadingScores.querySelectorAll('.analyse-loader__score') : [];
    if (!cards.length) return;
    const list = normalizeReport(raw).scoreCards || [];
    const step = prefersReducedMotion() ? 0 : 240;

    for (let i = 0; i < cards.length; i += 1) {
      if (token !== loaderRevealToken) return;
      const card = cards[i];
      const it = list[i] || LOADER_SCORE_DEFS[i];
      if (!card.classList.contains('is-in')) {
        card.classList.add('is-in');
        if (step > 0) await sleep(120);
      }
      const built = buildLoaderScoreValueHtml(it);
      const pending = card.querySelector('.analyse-loader__score-ring--pending, .analyse-loader__score-ring--live');
      if (pending) {
        const wrap = document.createElement('div');
        wrap.innerHTML = built.ringHtml.trim();
        pending.replaceWith(wrap.firstElementChild);
      }
      const valueEl = card.querySelector('.analyse-loader__score-value');
      if (valueEl) valueEl.textContent = built.note;
      card.classList.add('is-ready');
      animateScoreRing(card);
      if (step > 0) await sleep(step);
    }
  }

  function convertSections() {
    return [els.convertLoader, els.convertReport].filter(Boolean);
  }

  function resetConvertCardReveal(section) {
    if (!section) return;
    section.querySelectorAll('.analyse-convert-card.is-in').forEach((el) => el.classList.remove('is-in'));
  }

  function setConvertLoaderVisible(show) {
    if (!els.convertLoader) return;
    els.convertLoader.hidden = !show;
    if (!show) {
      resetConvertCardReveal(els.convertLoader);
      return;
    }
    els.convertLoader.querySelectorAll('.analyse-convert-card').forEach((card) => {
      card.classList.add('is-in');
    });
  }

  function setConvertReportVisible(show) {
    if (!els.convertReport) return;
    els.convertReport.hidden = !show;
    if (!show) {
      resetConvertCardReveal(els.convertReport);
      return;
    }
    els.convertReport.querySelectorAll('.analyse-convert-card').forEach((card) => {
      card.classList.add('is-in');
    });
  }

  function openLeadModal(mode) {
    if (!els.leadModal) return;
    modalMode = mode === 'premium' ? 'premium' : 'free';
    if (els.leadModalTitle) {
      els.leadModalTitle.textContent =
        modalMode === 'premium' ? 'Commander l\'audit premium' : 'Recevoir l\'audit gratuit';
    }
    if (els.leadModalLead) {
      els.leadModalLead.textContent =
        modalMode === 'premium'
          ? 'Renseignez votre email pour continuer vers le paiement securise.'
          : 'PDF par email - en general en moins d\'une minute, parfois jusqu\'a 1 h.';
    }
    if (els.leadSubmitLabel) {
      els.leadSubmitLabel.textContent =
        modalMode === 'premium' ? 'Continuer vers le paiement' : 'Recevoir l\'audit (PDF)';
    }
    setFeedback(els.premiumFeedback, '', false);
    setFeedback(els.leadFeedback, '', false);
    if (els.leadSuccess) els.leadSuccess.hidden = true;
    if (els.leadForm) els.leadForm.hidden = false;
    modalPreviousFocus = document.activeElement;
    els.leadModal.hidden = false;
    els.leadModal.setAttribute('aria-hidden', 'false');
    document.body.classList.add('analyse-modal-open');
    requestAnimationFrame(() => {
      if (els.leadEmail) els.leadEmail.focus();
    });
  }

  function closeLeadModal() {
    if (!els.leadModal || els.leadModal.hidden) return;
    els.leadModal.hidden = true;
    els.leadModal.setAttribute('aria-hidden', 'true');
    document.body.classList.remove('analyse-modal-open');
    if (modalPreviousFocus && typeof modalPreviousFocus.focus === 'function') {
      modalPreviousFocus.focus();
    }
    modalPreviousFocus = null;
  }

  async function revealConvertDuringLoad() {
    setConvertLoaderVisible(true);
  }

  function setConvertVisible(show) {
    setConvertLoaderVisible(show);
    if (!show) setConvertReportVisible(false);
  }

  function setLoadingVisible(show, websiteUrl) {
    if (els.loading) {
      els.loading.hidden = !show;
      els.loading.setAttribute('aria-busy', show ? 'true' : 'false');
    }
    if (show) {
      if (els.loadingUrl) {
        els.loadingUrl.textContent = websiteUrl ? displayHost(websiteUrl) : '';
      }
      resetLoaderScores();
      setConvertLoaderVisible(true);
      setConvertReportVisible(false);
      startLoadingSteps();
      revealConvertDuringLoad();
    } else {
      stopLoadingSteps();
      loaderRevealToken += 1;
    }
  }

  function startLoadingSteps() {
    stopLoadingSteps();
    loadingStepIndex = 0;
    updateLoadingStep(false);
    loadingStepTimer = window.setInterval(() => {
      loadingStepIndex = (loadingStepIndex + 1) % LOADING_STEPS.length;
      updateLoadingStep(true);
    }, 1800);
  }

  function stopLoadingSteps() {
    if (loadingStepTimer != null) {
      window.clearInterval(loadingStepTimer);
      loadingStepTimer = null;
    }
  }

  function updateLoadingStep(fade) {
    if (!els.loadingStep) return;
    const text = LOADING_STEPS[loadingStepIndex] || LOADING_STEPS[0];
    if (!fade) {
      els.loadingStep.textContent = text;
      els.loadingStep.classList.remove('is-changing');
      return;
    }
    els.loadingStep.classList.add('is-changing');
    window.setTimeout(() => {
      els.loadingStep.textContent = text;
      els.loadingStep.classList.remove('is-changing');
    }, 160);
  }

  function prefersReducedMotion() {
    return window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  }

  function animateScoreRing(card) {
    const ring = card && card.querySelector('.pl-score-ring');
    if (!ring) return;
    const target = ring.dataset.ringTarget || '0';
    ring.style.setProperty('--pl-ring-live', '0%');
    requestAnimationFrame(() => {
      ring.style.setProperty('--pl-ring-live', `${target}%`);
    });
  }

  function playBootReveal() {
    const root = pageRoot;
    if (!root || !els.bootWrap || els.bootWrap.hidden) return;
    if (prefersReducedMotion()) {
      root.querySelectorAll('#plBootWrap [data-reveal-order]').forEach((el) => el.classList.add('is-in'));
      root.classList.add('is-revealed');
      return;
    }
    root.classList.remove('is-revealed');
    root.querySelectorAll('#plBootWrap .is-in').forEach((el) => el.classList.remove('is-in'));
    requestAnimationFrame(() => {
      root.classList.add('is-revealed');
      root.querySelectorAll('#plBootWrap [data-reveal-order]').forEach((el, index) => {
        window.setTimeout(() => el.classList.add('is-in'), 90 + index * 110);
      });
    });
  }

  function playReportReveal() {
    const root = pageRoot;
    if (!root) return;

    root.classList.remove('is-revealed');
    root.querySelectorAll('.is-in').forEach((el) => {
      if (convertSections().some((section) => section.contains(el))) return;
      el.classList.remove('is-in');
    });

    if (els.reportHero) els.reportHero.hidden = false;
    if (els.report) els.report.hidden = false;

    const reduced = prefersReducedMotion();
    const revealItems = root.querySelectorAll('[data-reveal-order]');
    const scores = els.scores ? els.scores.querySelectorAll('.analyse-score') : [];
    const insights = els.insights ? els.insights.querySelectorAll('.analyse-insight') : [];
    const offers = els.offers ? els.offers.querySelectorAll('.analyse-offer') : [];
    const accordions = els.details ? els.details.querySelectorAll('.pl-accordion') : [];
    const shot = root.querySelector('.analyse-shot');

    const markIn = (nodes, step) => {
      nodes.forEach((node, index) => {
        window.setTimeout(() => node.classList.add('is-in'), step * index);
      });
    };

    requestAnimationFrame(() => {
      root.classList.add('is-revealed');

      if (reduced) {
        revealItems.forEach((el) => el.classList.add('is-in'));
        scores.forEach((s) => {
          s.classList.add('is-in');
          animateScoreRing(s);
        });
        if (shot) shot.classList.add('is-in');
        insights.forEach((el) => el.classList.add('is-in'));
        if (els.convertReport) {
          els.convertReport.classList.add('is-in');
          els.convertReport.querySelectorAll('.analyse-convert-card').forEach((el) => el.classList.add('is-in'));
        }
        offers.forEach((el) => el.classList.add('is-in'));
        accordions.forEach((el) => el.classList.add('is-in'));
        return;
      }

      revealItems.forEach((el, index) => {
        window.setTimeout(() => el.classList.add('is-in'), 80 * index);
      });

      window.setTimeout(() => {
        scores.forEach((s, index) => {
          window.setTimeout(() => {
            s.classList.add('is-in');
            animateScoreRing(s);
          }, 90 * index);
        });
        if (shot) shot.classList.add('is-in');
      }, 220);

      window.setTimeout(() => markIn(insights, 75), 380);
      window.setTimeout(() => {
        if (els.convertReport) els.convertReport.classList.add('is-in');
        markIn(els.convertReport ? els.convertReport.querySelectorAll('.analyse-convert-card') : [], 90);
      }, 520);
      window.setTimeout(() => markIn(offers, 65), 680);
      window.setTimeout(() => markIn(accordions, 50), 820);
    });
  }

  function setIdentityPreview({ website, company, dateLine }) {
    if (els.companyName && company) els.companyName.textContent = company;
    if (els.siteLink && website) {
      els.siteLink.href = website;
      els.siteLink.removeAttribute('aria-disabled');
    }
    if (els.siteLabel && website) els.siteLabel.textContent = website;
    if (els.reportDate && dateLine) els.reportDate.textContent = dateLine;
    if (els.shotUrl && website) els.shotUrl.textContent = displayHost(website);
  }

  function prefillLead({ website, email, name, first, last }) {
    if (website && els.leadSite) els.leadSite.value = website;
    if (email && els.leadEmail) els.leadEmail.value = email;
    if (name && els.leadName && !els.leadName.value) {
      els.leadName.value = name;
    } else if ((first || last) && els.leadName && !els.leadName.value) {
      els.leadName.value = [first, last].filter(Boolean).join(' ');
    }
  }

  function renderScores(cards) {
    if (!els.scores) return;
    els.scores.innerHTML = '';
    const list = Array.isArray(cards) ? cards : [];
    if (!list.length) {
      els.scores.innerHTML = '<p class="pl-muted" style="margin:0;">Aucun score disponible pour le moment.</p>';
      return;
    }
    list.forEach((it) => {
      const key = it?.key || 'score';
      const score100 = typeof it?.value === 'number' ? Math.round(it.value) : null;
      const ring = score100 == null ? 0 : Math.max(0, Math.min(100, score100));
      const color = score100 == null ? 'rgba(15,23,42,0.18)' : ringColorForKey(key);
      const note = it?.noteClient || scoreNote(key, score100);
      const card = document.createElement('div');
      card.className = 'analyse-score analyse-score--' + String(key).replace(/[^a-z0-9_-]/gi, '');
      card.innerHTML = `
        <div class="pl-score-ring" style="--pl-ring:${ring}%; --pl-ring-live:0%; --pl-ring-color:${color};" data-ring-target="${ring}" aria-label="${escapeHtml(String(it.label || key))}: ${score100 ?? '—'}">
          <div class="pl-score-value">${score100 ?? '—'}</div>
        </div>
        <div>
          <div class="analyse-score__label">${escapeHtml(it?.label || String(key))}</div>
          <div class="analyse-score__note">${escapeHtml(note)}</div>
        </div>
      `;
      els.scores.appendChild(card);
    });
  }

  function renderScreenshot(screenshotUrl, companyName, websiteUrl) {
    if (!els.screenshot) return;
    els.screenshot.innerHTML = '';
    if (els.shotUrl) {
      els.shotUrl.textContent = websiteUrl ? displayHost(websiteUrl) : 'votre-site.fr';
    }
    if (screenshotUrl) {
      const img = document.createElement('img');
      img.src = screenshotUrl;
      img.alt = companyName ? `Apercu de ${companyName}` : 'Apercu du site analyse';
      img.loading = 'lazy';
      img.decoding = 'async';
      img.referrerPolicy = 'no-referrer';
      img.className = 'analyse-shot__img';
      img.addEventListener('load', () => img.classList.add('is-loaded'), { once: true });
      els.screenshot.appendChild(img);
    } else {
      const box = document.createElement('div');
      box.className = 'pl-skeleton';
      box.style.width = '100%';
      box.style.height = '100%';
      box.style.minHeight = '220px';
      box.setAttribute('aria-hidden', 'true');
      els.screenshot.appendChild(box);
    }
  }

  function renderInsights(highlights) {
    if (!els.insights) return;
    const list = Array.isArray(highlights) ? highlights : [];
    const buckets = {
      good: { title: 'Points forts', icon: 'fa-arrow-trend-up', tone: 'good', items: [] },
      warn: { title: "Axes d'amelioration", icon: 'fa-magnifying-glass', tone: 'warn', items: [] },
      bad: { title: 'Points de vigilance', icon: 'fa-triangle-exclamation', tone: 'bad', items: [] }
    };
    list.forEach((it) => {
      const tone = it?.tone === 'good' || it?.tone === 'bad' ? it.tone : 'warn';
      const text = [it?.title, it?.desc].filter(Boolean).join(' - ');
      if (text) buckets[tone].items.push(text);
    });
    if (!buckets.good.items.length && !buckets.warn.items.length && !buckets.bad.items.length) {
      buckets.warn.items.push('Les details complets sont disponibles plus bas.');
    }
    Object.keys(buckets).forEach((k) => {
      if (!buckets[k].items.length) buckets[k].items.push('Rien de particulier a signaler ici.');
    });

    els.insights.innerHTML = Object.values(buckets).map((b) => `
      <article class="analyse-insight analyse-insight--${b.tone}">
        <div class="analyse-insight__head">
          <i class="fas ${b.icon}" aria-hidden="true"></i>
          <h3 class="analyse-insight__title">${escapeHtml(b.title)}</h3>
        </div>
        <ul class="analyse-insight__list">
          ${b.items.slice(0, 4).map((t) => `<li><i class="fas ${b.tone === 'bad' ? 'fa-circle-exclamation' : 'fa-check'}" aria-hidden="true"></i><span>${escapeHtml(t)}</span></li>`).join('')}
        </ul>
        <a class="analyse-insight__more" href="#analyse-details-title">Voir le detail →</a>
      </article>
    `).join('');
  }

  function weakestOfferKey(scoreCards) {
    let worstKey = 'seo';
    let worstEffective = Infinity;
    (scoreCards || []).forEach((c) => {
      if (typeof c.value !== 'number') return;
      const invert = c.key === 'pentest' || c.key === 'risque';
      const effective = invert ? (100 - c.value) : c.value;
      if (effective < worstEffective) {
        worstEffective = effective;
        if (c.key === 'performance') worstKey = 'performance';
        else if (c.key === 'seo') worstKey = 'seo';
        else if (c.key === 'securite' || c.key === 'pentest' || c.key === 'risque') worstKey = 'securite';
        else worstKey = 'vitrine';
      }
    });
    return worstKey;
  }

  function renderOffers(scoreCards) {
    if (!els.offers) return;
    const special = weakestOfferKey(scoreCards);
    els.offers.innerHTML = OFFERS.map((o) => {
      const isSpecial = o.key === special;
      return `
        <a class="analyse-offer${isSpecial ? ' analyse-offer--special' : ''}" href="/prestations/${escapeHtml(o.slug)}/" data-offer-key="${escapeHtml(o.key)}">
          ${isSpecial ? '<span class="analyse-offer__ribbon">Offre speciale pour vous</span>' : ''}
          <div class="analyse-offer__icon analyse-offer__icon--${escapeHtml(o.iconMod)}" aria-hidden="true"><i class="fas ${escapeHtml(o.icon)}"></i></div>
          <h3 class="analyse-offer__title">${escapeHtml(o.title)}</h3>
          <p class="analyse-offer__desc">${escapeHtml(o.desc)}</p>
          <span class="analyse-offer__cta">Voir l'offre →</span>
        </a>
      `;
    }).join('');
  }

  function renderDetails(sections) {
    if (!els.details) return;
    els.details.innerHTML = '';
    const list = Array.isArray(sections) ? sections : [];
    if (!list.length) {
      els.details.innerHTML = '<p class="pl-muted" style="margin:0;">Aucun detail disponible.</p>';
      return;
    }
    list.forEach((sec, idx) => {
      const title = sec?.title || `Section ${idx + 1}`;
      const pill = sec?.pill || '';
      const bodyHtml = sec?.html || '<p class="pl-muted">Aucune donnee.</p>';
      const acc = document.createElement('div');
      acc.className = 'pl-accordion';
      const panelId = `plAccPanel_${idx}`;
      acc.innerHTML = `
        <button type="button" class="pl-accordion-btn" aria-expanded="${idx === 0 ? 'true' : 'false'}" aria-controls="${panelId}">
          <strong>${escapeHtml(title)}</strong>
          <span class="pl-accordion-meta">
            ${pill ? `<span class="pl-pill">${escapeHtml(pill)}</span>` : ''}
            <i class="fas fa-chevron-down" aria-hidden="true"></i>
          </span>
        </button>
        <div class="pl-accordion-panel" id="${panelId}" ${idx === 0 ? '' : 'hidden'}>
          ${bodyHtml}
        </div>
      `;
      const btn = acc.querySelector('button');
      const panel = acc.querySelector('.pl-accordion-panel');
      btn.addEventListener('click', () => {
        const open = btn.getAttribute('aria-expanded') === 'true';
        btn.setAttribute('aria-expanded', open ? 'false' : 'true');
        panel.hidden = open;
      });
      els.details.appendChild(acc);
    });
  }

  function normalizeReport(raw) {
    const root = raw?.data || raw?.report || raw;
    const website = root?.website || root?.entreprise?.website || null;
    const entreprise = root?.entreprise || {};
    const technical = root?.technical || {};
    const seo = root?.seo || {};
    const pentest = root?.pentest || {};
    const osint = root?.osint || {};
    const scraping = root?.scraping || {};

    const scoreCards = [
      { key: 'performance', label: 'Performance', value: entreprise?.performance_score },
      { key: 'seo', label: 'SEO', value: entreprise?.score_seo ?? seo?.latest?.score },
      { key: 'securite', label: 'Securite', value: entreprise?.score_securite },
      { key: 'risque', label: 'Risque', value: entreprise?.score_pentest ?? pentest?.latest?.risk_score }
    ].map((x) => ({
      ...x,
      noteClient: typeof x.value === 'number' ? scoreNote(x.key, x.value) : '—'
    }));

    const highlights = [];
    const seoLatest = seo?.latest || {};
    const seoIssues = safeJsonParse(seoLatest.issues_json) || seoLatest.issues || [];
    toArray(seoIssues).slice(0, 4).forEach((it) => {
      const msg = it?.message || 'Alerte SEO';
      const impact = it?.impact || 'medium';
      const tone = impact === 'high' ? 'bad' : impact === 'medium' ? 'warn' : 'good';
      highlights.push({ title: 'SEO', desc: msg, tone });
    });

    const tLatest = technical?.latest || {};
    const td = tLatest?.technical_details || {};
    if (td?.mixed_content_detected) highlights.push({ title: 'Technique', desc: `Contenu mixte : ${td.mixed_content_detected}`, tone: 'warn' });
    if (td?.mobile_friendly === false) highlights.push({ title: 'Mobile', desc: 'Site peu confortable sur telephone.', tone: 'bad' });
    if (td?.viewport_meta === 'Manquant') highlights.push({ title: 'Affichage', desc: 'Meta viewport manquante.', tone: 'warn' });
    if (typeof entreprise?.performance_score === 'number' && entreprise.performance_score >= 80) {
      highlights.push({ title: 'Vitesse', desc: 'Bon niveau de performance global.', tone: 'good' });
    }
    if (typeof (entreprise?.score_seo ?? seoLatest?.score) === 'number' && (entreprise?.score_seo ?? seoLatest?.score) >= 80) {
      highlights.push({ title: 'Visibilite', desc: 'Bases SEO plutot solides.', tone: 'good' });
    }

    const pLatest = pentest?.latest || {};
    const pSum = pLatest?.summary || {};
    if (pSum?.risk_level) {
      highlights.push({
        title: 'Risque securite',
        desc: `${pSum.risk_level} - ${pSum.total_vulnerabilities ?? 0} point(s) a surveiller`,
        tone: toneFromScore(pLatest?.risk_score, true)
      });
    }

    const oLatest = osint?.latest || {};
    if (oLatest?.summary_warning) highlights.push({ title: 'Donnees publiques', desc: stripHtml(oLatest.summary_warning), tone: 'warn' });

    const sections = [];
    const addr = [entreprise?.address_1, entreprise?.address_2].filter(Boolean).join(', ');
    const tags = toArray(entreprise?.tags).slice(0, 12).map(t => `<span class="pl-badge">${escapeHtml(String(t))}</span>`).join(' ');
    sections.push({
      title: 'Entreprise',
      pill: entreprise?.statut ? String(entreprise.statut) : '',
      html: `
        ${entreprise?.resume ? `<p class="pl-muted">${escapeHtml(entreprise.resume)}</p>` : ''}
        <div class="pl-topline"><div class="pl-badges">
          ${entreprise?.cms ? `<span class="pl-badge pl-badge--good">${escapeHtml(entreprise.cms)}</span>` : ''}
          ${entreprise?.opportunite ? `<span class="pl-badge pl-badge--warn">${escapeHtml(entreprise.opportunite)}</span>` : ''}
        </div></div>
        <p class="pl-muted" style="margin-top:0.9rem;">
          ${addr ? `<strong>Adresse :</strong> ${escapeHtml(addr)}<br>` : ''}
          ${entreprise?.telephone ? `<strong>Telephone :</strong> <span class="pl-mono">${escapeHtml(entreprise.telephone)}</span><br>` : ''}
        </p>
        ${tags ? `<div class="pl-badges" style="margin-top:0.8rem;">${tags}</div>` : ''}
      `
    });

    const pagesSummary = tLatest?.pages_summary || {};
    const pages = toArray(tLatest?.pages);
    const scrLatest = scraping?.latest || {};
    const icons = scrLatest?.metadata?.icons || {};
    let screenshotUrl =
      icons.main_image ||
      icons.og_image ||
      icons.twitter_image ||
      icons.logo ||
      entreprise.og_image ||
      entreprise.favicon ||
      null;

    if (!screenshotUrl && pages.length) {
      for (let i = 0; i < pages.length; i++) {
        const p = pages[i] || {};
        const details = p.details || {};
        const ct = (details.content_type || p.content_type || '').toLowerCase();
        const url = details.final_url || p.final_url || p.page_url || p.url;
        if (!url) continue;
        if (ct.startsWith('image/')) {
          screenshotUrl = url;
          break;
        }
      }
    }

    const techRows = [
      ['CMS', tLatest?.cms || '—'],
      ['CDN', tLatest?.cdn || '—'],
      ['SSL', tLatest?.ssl_valid ? 'Valide' : 'A verifier'],
      ['Mobile', td?.mobile_friendly === false ? 'Non' : (td?.mobile_friendly === true ? 'Oui' : '—')]
    ];
    sections.push({
      title: 'Technique',
      pill: tLatest?.framework ? String(tLatest.framework) : '',
      html: `
        ${tableHtml(['Indicateur', 'Valeur'], techRows.map(([a, b]) => [escapeHtml(a), escapeHtml(String(b))]))}
        <p class="pl-muted" style="margin-top:0.9rem;">
          <strong>Pages :</strong> ${escapeHtml(String(pagesSummary.pages_scanned ?? pagesSummary.pages_count ?? 0))} ·
          <strong>Temps moyen :</strong> ${escapeHtml(String(pagesSummary.avg_response_time_ms ?? '—'))} ms
        </p>
      `
    });

    const meta = safeJsonParse(seoLatest?.meta_tags_json) || {};
    const structure = safeJsonParse(seoLatest?.structure_json) || {};
    const seoRows = [
      ['Score', seoLatest?.score != null ? `${seoLatest.score}/100` : '—'],
      ['Title', meta?.title ? escapeHtml(meta.title) : '—'],
      ['H1', structure?.h1_count != null ? String(structure.h1_count) : '—'],
      ['Images sans alt', structure?.images_without_alt != null ? String(structure.images_without_alt) : '—']
    ];
    const seoIssuesHtml = toArray(seoIssues).slice(0, 8).map((it) => {
      const impact = it?.impact || 'medium';
      const tone = impact === 'high' ? 'bad' : impact === 'medium' ? 'warn' : 'good';
      return `<div class="pl-audit pl-audit--${tone}" style="margin-top:0.7rem;">
        <div class="pl-audit-title">${escapeHtml(it?.category ? `SEO · ${it.category}` : 'SEO')}</div>
        <div class="pl-audit-desc">${escapeHtml(it?.message || '—')}</div>
      </div>`;
    }).join('');
    sections.push({
      title: 'SEO',
      pill: seoLatest?.score != null ? `${seoLatest.score}/100` : '',
      html: `
        ${tableHtml(['Element', 'Valeur'], seoRows.map(([a, b]) => [escapeHtml(a), (typeof b === 'string' ? b : String(b))]))}
        ${seoIssuesHtml || '<p class="pl-muted" style="margin-top:1rem;">Aucune alerte SEO.</p>'}
      `
    });

    const vulns = toArray(pLatest?.vulnerabilities).slice(0, 10);
    const vulnHtml = vulns.map(v => {
      const sev = (v?.severity || '').toLowerCase();
      const tone = sev === 'high' ? 'bad' : sev === 'medium' ? 'warn' : 'good';
      return `<div class="pl-audit pl-audit--${tone}" style="margin-top:0.7rem;">
        <div class="pl-audit-title">${escapeHtml(v?.name || v?.type || 'Point securite')}</div>
        <div class="pl-audit-desc">${escapeHtml(v?.description || '')}</div>
      </div>`;
    }).join('');
    sections.push({
      title: 'Securite',
      pill: pLatest?.risk_score != null ? `${pLatest.risk_score}/100` : '',
      html: `
        <p class="pl-muted">
          ${pSum?.risk_level ? `<strong>Niveau :</strong> ${escapeHtml(String(pSum.risk_level))}` : ''}
        </p>
        ${vulnHtml || '<p class="pl-muted" style="margin-top:0.8rem;">Rien de critique liste.</p>'}
      `
    });

    const emails = toArray(oLatest?.emails || oLatest?.emails_found || []).slice(0, 8);
    const scLatest = scraping?.latest || {};
    const scrEmails = toArray(scLatest?.emails).slice(0, 8);
    const firstEmail =
      (typeof emails[0] === 'string' ? emails[0] : null) ||
      (scrEmails[0] && (scrEmails[0].email || scrEmails[0])) ||
      null;

    sections.push({
      title: 'Donnees publiques',
      pill: oLatest?.status ? String(oLatest.status) : '',
      html: `
        <p class="pl-muted">
          <strong>Date :</strong> ${escapeHtml(formatDate(oLatest?.date_analyse) || formatDate(scLatest?.date_modification) || '—')}
        </p>
      `
    });

    return {
      finalUrl: website,
      entreprise,
      scoreCards,
      highlights,
      sections,
      screenshotUrl,
      metaLine: entreprise?.date_analyse ? formatDate(entreprise.date_analyse) : null,
      suggestedEmail: typeof firstEmail === 'string' ? firstEmail : null
    };
  }

  function formatLookupError(message) {
    const msg = String(message || '').trim();
    if (/aucun rapport/i.test(msg)) {
      return 'Aucun rapport enregistre pour cette adresse. Reprenez l\'URL exacte du lien email, ou demandez une analyse via « Recevoir l\'audit ».';
    }
    return msg || 'Impossible de charger le rapport. Reessayez dans un instant.';
  }

  async function apiGetWebsiteAnalysis({ website, full }) {
    const u = new URL((API_BASE || '') + ENDPOINT, window.location.origin);
    u.searchParams.set('website', website);
    if (full != null) u.searchParams.set('full', String(full));
    const res = await fetch(u.toString(), { method: 'GET' });
    const data = await res.json().catch(() => ({}));
    if (!res.ok) {
      throw new Error(data?.error || data?.message || `Erreur API (${res.status})`);
    }
    return data;
  }

  function buildShareUrl({ website, full, email, name }) {
    const u = new URL(window.location.origin + '/analyse');
    if (website) u.searchParams.set('website', website);
    if (full != null) u.searchParams.set('full', String(full));
    if (email) u.searchParams.set('email', email);
    if (name) u.searchParams.set('name', name);
    return u.toString();
  }

  function showReport(raw, queryPrefill) {
    const r = normalizeReport(raw);
    currentWebsite = r.finalUrl || currentWebsite || '';

    const company = r.entreprise?.nom || displayHost(currentWebsite) || 'Votre site';
    if (els.companyName) els.companyName.textContent = company;

    if (els.siteLink && currentWebsite) {
      els.siteLink.href = currentWebsite;
      els.siteLink.removeAttribute('aria-disabled');
    }
    if (els.siteLabel) els.siteLabel.textContent = currentWebsite || '';

    if (els.reportDate) {
      els.reportDate.textContent = r.metaLine ? `Analyse : ${r.metaLine}` : '';
    }

    renderScores(r.scoreCards);
    renderScreenshot(r.screenshotUrl, company, currentWebsite);
    renderInsights(r.highlights);
    renderOffers(r.scoreCards);
    renderDetails(r.sections);

    prefillLead({
      website: currentWebsite,
      email: (queryPrefill && queryPrefill.email) || r.suggestedEmail || '',
      name: (queryPrefill && queryPrefill.name) || '',
      first: queryPrefill && queryPrefill.first,
      last: queryPrefill && queryPrefill.last
    });

    if (els.bootWrap) els.bootWrap.hidden = true;
    if (els.loading) els.loading.hidden = true;
    setConvertLoaderVisible(false);
    setConvertReportVisible(true);
    if (pageRoot) pageRoot.classList.add('is-report-ready');
    if (els.intro) els.intro.classList.add('is-hidden');
    playReportReveal();
    window.scrollTo({ top: 0, left: 0, behavior: prefersReducedMotion() ? 'auto' : 'smooth' });
  }

  function restoreBootAfterError(message) {
    setLoadingVisible(false);
    setConvertVisible(false);
    closeLeadModal();
    setBootVisible(true);
    if (els.reportHero) els.reportHero.hidden = true;
    if (els.report) els.report.hidden = true;
    if (pageRoot) pageRoot.classList.remove('is-revealed', 'is-report-ready');
    if (els.intro) els.intro.classList.remove('is-hidden');
    setFeedback(els.bootFeedback, formatLookupError(message), true);
    playBootReveal();
  }

  async function handleSubmit(websiteUrl, full, queryPrefill) {
    setFeedback(els.bootFeedback, '', false);
    setBootLoading(true);
    setBootVisible(false);
    setLoadingVisible(true, websiteUrl);
    if (pageRoot) pageRoot.classList.remove('is-revealed', 'is-report-ready');
    if (els.reportHero) els.reportHero.hidden = true;
    if (els.report) els.report.hidden = true;
    if (els.intro) els.intro.classList.remove('is-hidden');

    const previewCompany = displayHost(websiteUrl) || 'Votre site';
    setIdentityPreview({
      website: websiteUrl,
      company: previewCompany,
      dateLine: 'Analyse en cours…'
    });
    prefillLead({
      website: websiteUrl,
      email: (queryPrefill && queryPrefill.email) || '',
      name: (queryPrefill && queryPrefill.name) || '',
      first: queryPrefill && queryPrefill.first,
      last: queryPrefill && queryPrefill.last
    });

    try {
      const revealTask = revealLoaderScorePlaceholders();
      const report = await apiGetWebsiteAnalysis({ website: websiteUrl, full: full ?? 1 });
      await revealTask;
      await fillLoaderScoresFromReport(report);
      if (!prefersReducedMotion()) await sleep(380);
      currentWebsite = websiteUrl;
      showReport(report, queryPrefill);
      const share = buildShareUrl({
        website: websiteUrl,
        full: full ?? 1,
        email: queryPrefill && queryPrefill.email,
        name: queryPrefill && queryPrefill.name
      });
      window.history.replaceState({}, '', share);
    } catch (e) {
      restoreBootAfterError(e && e.message);
    } finally {
      setBootLoading(false);
      setLoadingVisible(false);
    }
  }

  function readLeadValues() {
    const name = (els.leadName && els.leadName.value || '').trim();
    return {
      url: safeUrl(els.leadSite && els.leadSite.value) || safeUrl(currentWebsite),
      email: (els.leadEmail && els.leadEmail.value || '').trim(),
      name: name,
      honeypot: (els.leadForm && els.leadForm.querySelector('[name="company"]') || {}).value || ''
    };
  }

  function submitLead() {
    const vals = readLeadValues();
    if (vals.honeypot) return;
    if (!vals.url) {
      setFeedback(els.leadFeedback, 'URL du site invalide.', true);
      return;
    }
    if (!vals.email || !/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(vals.email)) {
      setFeedback(els.leadFeedback, 'Email invalide.', true);
      return;
    }

    setBtnLoading(els.leadSubmit, true);
    setFeedback(els.leadFeedback, '', false);

    fetch(FREE_AUDIT_ENDPOINT, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ website: vals.url, email: vals.email, name: vals.name })
    })
      .then(async (res) => {
        const data = await res.json().catch(() => ({}));
        return { res, data };
      })
      .then((ref) => {
        if (ref.res.ok && ref.data && ref.data.success) {
          if (els.leadForm) els.leadForm.hidden = true;
          if (els.leadSuccess) els.leadSuccess.hidden = false;
          if (els.leadSuccessText) {
            els.leadSuccessText.textContent =
              (ref.data && ref.data.message) ||
              `Le PDF part sur ${vals.email} - en general en moins d'une minute.`;
          }
          return;
        }
        let errMsg = (ref.data && ref.data.error) || 'Envoi impossible. Reessayez ou contactez-nous.';
        if (ref.res.status === 429) {
          errMsg = (ref.data && ref.data.error) || 'Vous avez deja demande un audit recemment. Reessayez plus tard.';
        }
        setFeedback(els.leadFeedback, errMsg, true);
      })
      .catch(() => {
        setFeedback(els.leadFeedback, 'Serveur injoignable. Reessayez dans un instant.', true);
      })
      .finally(() => {
        setBtnLoading(els.leadSubmit, false);
      });
  }

  function startPremium() {
    const vals = readLeadValues();
    if (!vals.url) {
      setFeedback(els.premiumFeedback, 'Site introuvable pour cet audit.', true);
      return;
    }
    if (!vals.email || !/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(vals.email)) {
      setFeedback(els.premiumFeedback, 'Email invalide.', true);
      return;
    }

    try {
      sessionStorage.setItem(
        STORAGE_KEY,
        JSON.stringify({
          site_url: vals.url,
          email: vals.email,
          name: vals.name || 'Client audit'
        })
      );
    } catch (err) { /* ignore */ }

    setBtnLoading(els.leadSubmit, true);
    setFeedback(els.premiumFeedback, '', false);

    fetch(PREMIUM_CHECKOUT_ENDPOINT, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        audit_slug: auditSlug,
        email: vals.email,
        site_url: vals.url,
        name: vals.name
      })
    })
      .then(async (res) => {
        const data = await res.json().catch(() => ({}));
        return { res, data };
      })
      .then((ref) => {
        if (ref.res.ok && ref.data && ref.data.success && ref.data.url) {
          window.location.href = ref.data.url;
          return;
        }
        setFeedback(
          els.premiumFeedback,
          (ref.data && ref.data.error) || "Impossible d'ouvrir le paiement pour l'instant.",
          true
        );
      })
      .catch(() => {
        setFeedback(els.premiumFeedback, 'Serveur injoignable.', true);
      })
      .finally(() => {
        setBtnLoading(els.leadSubmit, false);
      });
  }

  els.form.addEventListener('submit', async (e) => {
    e.preventDefault();
    const v = safeUrl(els.url.value);
    if (!v) {
      setFeedback(els.bootFeedback, 'Saisissez une URL valide (http ou https).', true);
      els.url.focus();
      return;
    }
    await handleSubmit(v, 1, null);
  });

  if (els.leadForm) {
    els.leadForm.addEventListener('submit', (e) => {
      e.preventDefault();
      if (modalMode === 'premium') startPremium();
      else submitLead();
    });
  }

  if (pageRoot) {
    pageRoot.addEventListener('click', (e) => {
      const freeBtn = e.target.closest('[data-analyse-audit-free]');
      if (freeBtn) {
        e.preventDefault();
        openLeadModal('free');
        return;
      }
      const premiumBtn = e.target.closest('[data-analyse-audit-premium]');
      if (premiumBtn) {
        e.preventDefault();
        openLeadModal('premium');
      }
    });
  }

  if (els.leadModal) {
    els.leadModal.addEventListener('click', (e) => {
      if (e.target.closest('[data-analyse-modal-close]')) {
        e.preventDefault();
        closeLeadModal();
      }
    });
  }

  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape') closeLeadModal();
  });

  (async function initFromQuery() {
    const q = new URLSearchParams(window.location.search);
    const website = q.get('website');
    const full = q.get('full');
    const email = q.get('email') || '';
    const name = q.get('name') || '';
    const first = q.get('first') || q.get('prenom') || '';
    const last = q.get('last') || q.get('nom') || '';
    const queryPrefill = { email, name, first, last };

    if (website) {
      const v = safeUrl(website);
      if (v) {
        els.url.value = v;
        const fullNum = full != null ? Number(full) : 1;
        await handleSubmit(v, Number.isFinite(fullNum) ? fullNum : 1, queryPrefill);
        return;
      }
    }

    if (email || name || first || last) {
      prefillLead({ website: website || '', email, name, first, last });
    }

    playBootReveal();
  })();
})();
