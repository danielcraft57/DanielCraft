// ===== Rapport d'analyse - Page /analyse (maquette A) =====

(function () {
  const API_BASE = '';
  const ENDPOINT = '/api/website-analysis.php';
  const FREE_AUDIT_ENDPOINT = '/api/request-free-audit.php';

  const pageRoot = document.querySelector('.page-analyse');

  const OFFERS = [
    {
      key: 'performance',
      slug: 'rapport-vitesse',
      title: 'Site plus rapide',
      desc: 'Optimise la vitesse de chargement et l\'expérience sur mobile.',
      icon: 'fa-gauge-high',
      iconMod: 'perf'
    },
    {
      key: 'seo',
      slug: 'referencement-google',
      title: 'Être trouvé sur Google',
      desc: 'Améliore ton référencement et ta visibilité locale.',
      icon: 'fa-magnifying-glass',
      iconMod: 'seo'
    },
    {
      key: 'securite',
      slug: 'sauvegardes-securite',
      title: 'Sécuriser le site',
      desc: 'Protège ton site et tes données avec les bons réflexes.',
      icon: 'fa-shield-halved',
      iconMod: 'sec'
    },
    {
      key: 'vitrine',
      slug: 'site-vitrine',
      title: 'Vitrine claire',
      desc: 'Mets en valeur ton activité avec un site clair et efficace.',
      icon: 'fa-window-maximize',
      iconMod: 'vitrine'
    }
  ];

  const CHARACTER_FILES = [
    'dc-character-artisan.jpg',
    'dc-character-auto.jpg',
    'dc-character-batiment.jpg',
    'dc-character-bureau.jpg',
    'dc-character-coiffure.jpg',
    'dc-character-commerce.jpg',
    'dc-character-fleuriste.jpg',
    'dc-character-immo.jpg',
    'dc-character-loic.jpg',
    'dc-character-resto.jpg',
    'dc-character-sante.jpg',
    'dc-character-sport.jpg'
  ];
  const CHARACTER_BASE = '/assets/img/analyse/characters/';

  const els = {
    bootWrap: document.getElementById('plBootWrap'),
    boot: document.getElementById('plBoot'),
    form: document.getElementById('plForm'),
    url: document.getElementById('plUrl'),
    submit: document.getElementById('plSubmitBtn'),
    bootFeedback: document.getElementById('plBootFeedback'),
    loading: document.getElementById('plLoading'),
    loadingTitle: document.getElementById('plLoadingTitle'),
    loadingScores: document.getElementById('plLoadingScores'),
    loadingStep: document.getElementById('plLoadingStep'),
    convertReport: document.getElementById('plConvertReport'),
    leadModal: document.getElementById('plLeadModal'),
    leadModalTitle: document.getElementById('plLeadModalTitle'),
    leadModalLead: document.getElementById('plLeadModalLead'),
    leadSubmitLabel: document.getElementById('plLeadSubmitLabel'),
    storySection: document.getElementById('plStorySection'),
    report: document.getElementById('plReport'),
    scores: document.getElementById('plScores'),
    storyChart: document.getElementById('plStoryChart'),
    intro: document.querySelector('.analyse-intro'),
    narrative: document.getElementById('plNarrative'),
    narrativeNav: document.getElementById('plNarrativeNav'),
    storySkip: document.getElementById('plStorySkip'),
    details: document.getElementById('plDetails'),
    offers: document.getElementById('plOffers'),
    leadForm: document.getElementById('plLeadForm'),
    leadName: document.getElementById('plLeadName'),
    leadEmail: document.getElementById('plLeadEmail'),
    leadSite: document.getElementById('plLeadSite'),
    leadSubmit: document.getElementById('plLeadSubmit'),
    leadFeedback: document.getElementById('plLeadFeedback'),
    winModal: document.getElementById('plWinModal'),
    winModalText: document.getElementById('plWinModalText')
  };

  if (!els.form || !els.url || !els.submit) return;

  /** Ancien HTML prod : second bloc feedback premium - on le retire si présent. */
  document.getElementById('plPremiumFeedback')?.remove();

  let currentWebsite = '';
  let leadSubmitting = false;
  let loadingStepTimer = null;
  let loadingStepIndex = 0;
  let loaderRevealToken = 0;
  let narrativeToken = 0;
  let narrativeChapters = [];
  let narrativePlaying = false;
  let narrativeTailReveal = null;
  /** Pause entre mots pendant le stream. */
  const STORY_WORD_MS = 85;
  /** Pause après une ponctuation forte. */
  const STORY_PUNCT_MS = 280;
  /** Pause entre deux blocs empilés. */
  const STORY_BLOCK_GAP_MS = 900;
  /** Mots / motifs à mettre en surbrillance dans la narration. */
  const STORY_KEYWORDS = new Set([
    'https', 'http', 'ssl', 'hsts', 'seo', 'google', 'téléphone', 'telephone',
    'mobile', 'sécurité', 'securite', 'cnaps', 'design', 'refonte', 'confiance',
    'urgence', 'urgent', 'devis', 'crédibilité', 'credibilite', 'bug', 'bugs',
    'meta', 'title', 'description', 'viewport', 'wordpress', 'amateur',
    'professionnel', 'cliquable', 'jaune', 'noir', 'performance', 'risque',
    'garde', 'gardiennage', 'surveillance', 'metz', 'nancy', 'lorraine'
  ]);
  /** Mode de la modale lead : free (rapport simple) ou gemini (complet). */
  let modalMode = 'free';
  let modalPreviousFocus = null;

  const LOADING_STEPS = [
    'On se connecte au site…',
    'On regarde le design…',
    'On vérifie la visibilité sur Google…',
    'On contrôle la sécurité…',
    'On prépare la lecture…'
  ];

  function setFeedback(el, message, isError) {
    if (!el) return;
    if (!message) {
      el.hidden = true;
      el.textContent = '';
      el.removeAttribute('aria-hidden');
      return;
    }
    el.hidden = false;
    el.textContent = message;
    el.className = 'form-feedback ' + (isError ? 'form-feedback--error' : 'form-feedback--success');
    el.removeAttribute('aria-hidden');
  }

  /**
   * Un seul message visible dans la modal (évite le doublon lead + premium en prod).
   * @param {string} message
   * @param {boolean} isError
   */
  function setLeadModalFeedback(message, isError) {
    if (els.leadModal) {
      els.leadModal.querySelectorAll('.form-feedback').forEach((box) => {
        if (box !== els.leadFeedback) {
          box.hidden = true;
          box.textContent = '';
          box.setAttribute('aria-hidden', 'true');
        }
      });
    }
    setFeedback(els.leadFeedback, message, isError);
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
      case 'design': return '#4f46e5';
      case 'gemini': return '#4f46e5';
      case 'performance': return '#10b981';
      case 'seo': return '#2563eb';
      case 'securite': return '#0d9488';
      case 'risque':
      case 'pentest': return '#f59e0b';
      default: return '#64748b';
    }
  }

  function scoreNote(key, value) {
    if (typeof value !== 'number') return '-';
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
    if (key === 'seo' || key === 'design' || key === 'gemini') {
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

  function convertSections() {
    return [els.convertReport].filter(Boolean);
  }

  function resetConvertCardReveal(section) {
    if (!section) return;
    section.querySelectorAll('.analyse-convert-card.is-in').forEach((el) => el.classList.remove('is-in'));
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

  /**
   * Ouvre la modale email pour demander un rapport.
   * @param {'free'|'gemini'} [mode='free'] - Rapport simple ou Gemini complet.
   */
  function openLeadModal(mode) {
    if (!els.leadModal) return;
    modalMode = mode === 'gemini' ? 'gemini' : 'free';
    if (els.leadModalTitle) {
      els.leadModalTitle.textContent =
        modalMode === 'gemini' ? 'Recevoir le rapport Gemini' : 'Recevoir le rapport simple';
    }
    if (els.leadModalLead) {
      els.leadModalLead.textContent =
        modalMode === 'gemini'
          ? 'Renseigne ton email - le rapport complet part gratuitement pour l\'instant.'
          : 'Renseigne ton email - PDF léger par email, sans carte bancaire.';
    }
    if (els.leadSubmitLabel) {
      els.leadSubmitLabel.textContent =
        modalMode === 'gemini' ? 'Recevoir le rapport complet' : 'Recevoir le rapport simple';
    }
    setLeadModalFeedback('', false);
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
    if (!els.winModal || els.winModal.hidden) {
      document.body.classList.remove('analyse-modal-open');
    }
    if (modalPreviousFocus && typeof modalPreviousFocus.focus === 'function') {
      modalPreviousFocus.focus();
    }
    modalPreviousFocus = null;
  }

  /**
   * Ouvre la modale succès « C'est parti » (style casino).
   * @param {string} message - Texte affiché sous le titre.
   */
  function openWinModal(message) {
    if (!els.winModal) return;
    if (els.winModalText) {
      els.winModalText.textContent =
        message || 'Rapport en route - tu le reçois par email.';
    }
    els.winModal.hidden = false;
    els.winModal.setAttribute('aria-hidden', 'false');
    document.body.classList.add('analyse-modal-open');
    requestAnimationFrame(() => {
      const cta = els.winModal.querySelector('[data-analyse-win-close].analyse-win-modal__cta');
      if (cta) cta.focus();
    });
  }

  /** Ferme la modale succès casino. */
  function closeWinModal() {
    if (!els.winModal || els.winModal.hidden) return;
    els.winModal.hidden = true;
    els.winModal.setAttribute('aria-hidden', 'true');
    document.body.classList.remove('analyse-modal-open');
  }

  function setConvertVisible(show) {
    if (!show) setConvertReportVisible(false);
  }

  function setLoadingVisible(show, websiteUrl) {
    if (els.loading) {
      els.loading.hidden = !show;
      els.loading.setAttribute('aria-busy', show ? 'true' : 'false');
    }
    if (show) {
      const host = websiteUrl ? displayHost(websiteUrl) : '';
      if (els.loadingTitle) {
        els.loadingTitle.textContent = host ? `On regarde ${host}` : 'On regarde ton site';
      }
      setConvertReportVisible(false);
      startLoadingSteps();
      revealLoaderGauges();
    } else {
      stopLoadingSteps();
      loaderRevealToken += 1;
      resetLoaderGauges();
    }
  }

  /** Remet les jauges du loader à l'état « en cours ». */
  function resetLoaderGauges() {
    if (!els.loadingScores) return;
    els.loadingScores.querySelectorAll('.analyse-loader__score').forEach((card) => {
      card.classList.remove('is-in');
      const value = card.querySelector('.analyse-loader__score-value');
      if (value) value.textContent = 'En cours…';
    });
  }

  /**
   * Fait apparaître les 4 jauges du loader une par une.
   * @returns {Promise<void>}
   */
  async function revealLoaderGauges() {
    const token = ++loaderRevealToken;
    resetLoaderGauges();
    const cards = els.loadingScores
      ? Array.from(els.loadingScores.querySelectorAll('.analyse-loader__score'))
      : [];
    if (!cards.length) return;
    const step = prefersReducedMotion() ? 0 : 160;
    for (let i = 0; i < cards.length; i += 1) {
      if (token !== loaderRevealToken) return;
      if (step > 0) await sleep(step);
      cards[i].classList.add('is-in');
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

    if (els.storySection) els.storySection.hidden = false;
    if (els.report) els.report.hidden = false;

    const reduced = prefersReducedMotion();
    const token = ++narrativeToken;

    const markIn = (nodes, step) => {
      nodes.forEach((node, index) => {
        window.setTimeout(() => node.classList.add('is-in'), step * index);
      });
    };

    const revealStoryVisuals = () => {
      if (token !== narrativeToken) return;
      const gauges = els.scores ? els.scores.querySelectorAll('.analyse-score') : [];
      markIn(gauges, 90);
      gauges.forEach((g) => animateScoreRing(g));
      if (els.storyChart) {
        els.storyChart.classList.add('is-in');
        els.storyChart.querySelectorAll('.analyse-story__bar-fill').forEach((bar, index) => {
          window.setTimeout(() => bar.classList.add('is-grown'), 120 + index * 90);
        });
      }
    };

    const revealTail = () => {
      if (token !== narrativeToken) return;
      if (els.convertReport) {
        els.convertReport.classList.add('is-in');
        markIn(els.convertReport.querySelectorAll('.analyse-convert-card'), 90);
      }
      const offers = els.offers ? els.offers.querySelectorAll('.analyse-offer') : [];
      const accordions = els.details ? els.details.querySelectorAll('.pl-accordion') : [];
      window.setTimeout(() => markIn(offers, 65), 160);
      window.setTimeout(() => markIn(accordions, 50), 300);
    };

    requestAnimationFrame(() => {
      root.classList.add('is-revealed');
      if (els.storySection) els.storySection.classList.add('is-in');
      revealStoryVisuals();

      if (reduced) {
        root.querySelectorAll('#plReport [data-reveal-order]').forEach((el) => el.classList.add('is-in'));
        playNarrativeSequence(token, { instant: true, onAfterSecondChapter: revealTail });
        return;
      }

      playNarrativeSequence(token, { instant: false, onAfterSecondChapter: revealTail });
    });
  }

  /**
   * Rejette les faux prénoms dérivés d'emails génériques (contact@, info@…).
   * @param {string} value
   * @returns {boolean}
   */
  function isGenericLeadName(value) {
    const raw = String(value || '').trim().toLowerCase();
    if (!raw) return true;
    const local = raw.includes('@') ? raw.split('@')[0] : raw;
    const token = local.replace(/[^a-z0-9]+/gi, '');
    const generic = new Set([
      'info', 'infos', 'contact', 'contacts', 'hello', 'bonjour', 'hi',
      'support', 'sav', 'admin', 'administration', 'commercial', 'sales',
      'service', 'services', 'secretariat', 'accueil', 'office', 'team',
      'equipe', 'webmaster', 'postmaster', 'noreply', 'noreply', 'mail',
      'email', 'newsletter', 'notification', 'notifications', 'principal',
      'monsieur', 'madame', 'monsieurmadame', 'cherprospect', 'na', 'n/a'
    ]);
    if (generic.has(local) || generic.has(token)) return true;
    const first = local.split(/[\s._+-]+/).filter(Boolean)[0] || '';
    return generic.has(first) || generic.has(first.replace(/[^a-z0-9]+/gi, ''));
  }

  function sanitizeLeadName(value) {
    const text = String(value || '').trim();
    if (!text || isGenericLeadName(text)) return '';
    return text;
  }

  function prefillLead({ website, email, name, first, last }) {
    if (website && els.leadSite) els.leadSite.value = website;
    if (email && els.leadEmail) els.leadEmail.value = email;
    const safeName = sanitizeLeadName(name);
    const safeFirst = sanitizeLeadName(first);
    const safeLast = sanitizeLeadName(last);
    if (safeName && els.leadName && !els.leadName.value) {
      els.leadName.value = safeName;
    } else if ((safeFirst || safeLast) && els.leadName && !els.leadName.value) {
      els.leadName.value = [safeFirst, safeLast].filter(Boolean).join(' ');
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
        <div class="pl-score-ring" style="--pl-ring:${ring}%; --pl-ring-live:0%; --pl-ring-color:${color};" data-ring-target="${ring}" aria-label="${escapeHtml(String(it.label || key))}: ${score100 ?? '-'}">
          <div class="pl-score-value">${score100 ?? '-'}</div>
        </div>
        <div>
          <div class="analyse-score__label">${escapeHtml(it?.label || String(key))}</div>
          <div class="analyse-score__note">${escapeHtml(note)}</div>
        </div>
      `;
      els.scores.appendChild(card);
    });
    renderScoreChart(list);
  }

  /**
   * Barres horizontales des scores sous les jauges (argumentation).
   * @param {array} cards
   */
  function renderScoreChart(cards) {
    if (!els.storyChart) return;
    const list = (Array.isArray(cards) ? cards : []).filter((c) => typeof c?.value === 'number');
    if (!list.length) {
      els.storyChart.innerHTML = '';
      els.storyChart.hidden = true;
      return;
    }
    els.storyChart.hidden = false;
    els.storyChart.classList.remove('is-in');
    els.storyChart.innerHTML = `
      <p class="analyse-story__chart-title">Vue d'ensemble des notes</p>
      <div class="analyse-story__bars">
        ${list.map((c) => {
          const val = Math.max(0, Math.min(100, Math.round(c.value)));
          const color = ringColorForKey(c.key);
          const invert = c.key === 'risque' || c.key === 'pentest';
          const width = invert ? Math.max(0, 100 - val) : val;
          return `
            <div class="analyse-story__bar-row">
              <span class="analyse-story__bar-label">${escapeHtml(c.label || c.key)}</span>
              <div class="analyse-story__bar-track" role="img" aria-label="${escapeHtml(c.label || '')} ${val} sur 100">
                <span class="analyse-story__bar-fill" style="--bar-color:${color}; --bar-w:${width}%"></span>
              </div>
              <span class="analyse-story__bar-val">${val}</span>
            </div>
          `;
        }).join('')}
      </div>
    `;
  }

  function renderScreenshot() {
    /* Capture retiree du rapport - garder la fonction no-op pour les appels existants. */
  }

  function hashSeed(str) {
    let h = 2166136261;
    const s = String(str || 'danielcraft');
    for (let i = 0; i < s.length; i++) {
      h ^= s.charCodeAt(i);
      h = Math.imul(h, 16777619);
    }
    return h >>> 0;
  }

  function pickCharacterFiles(host, count) {
    const seed = hashSeed(host);
    const pool = CHARACTER_FILES.slice();
    for (let i = pool.length - 1; i > 0; i--) {
      const j = (seed + i * 2654435761) % (i + 1);
      const tmp = pool[i];
      pool[i] = pool[j];
      pool[j] = tmp;
    }
    return pool.slice(0, Math.max(0, count));
  }

  /**
   * Normalise une liste Gemini / highlights en paragraphes distincts.
   * @param {array} items
   * @param {string} fallback
   * @returns {string[]}
   */
  function toParagraphs(items, fallback) {
    const parts = toArray(items)
      .map((it) => {
        if (typeof it === 'string') return it.trim();
        if (it && typeof it === 'object') {
          return String(it.action || it.message || it.title || it.desc || '').trim();
        }
        return '';
      })
      .filter(Boolean)
      .slice(0, 6)
      .map((p) => (/[.!?…]$/.test(p) ? p : p + '.'));
    if (!parts.length) return [fallback];
    return parts;
  }

  /**
   * Decoupe un bloc de prose en paragraphes (double saut de ligne ou phrases longues).
   * @param {string} text
   * @returns {string[]}
   */
  function proseFromText(text) {
    const raw = String(text || '').trim();
    if (!raw) return [];
    const blocks = raw.split(/\n{2,}/).map((p) => p.trim()).filter(Boolean);
    if (blocks.length > 1) return blocks;
    const sentences = raw.match(/[^.!?…]+[.!?…]+/g);
    if (sentences && sentences.length > 2) {
      const grouped = [];
      for (let i = 0; i < sentences.length; i += 2) {
        grouped.push(sentences.slice(i, i + 2).join(' ').trim());
      }
      return grouped.filter(Boolean);
    }
    return [raw];
  }

  function highlightsParagraphs(highlights, tones, fallback) {
    const wanted = new Set(tones);
    const parts = toArray(highlights)
      .filter((h) => wanted.has(h?.tone || 'warn'))
      .map((h) => [h?.title, h?.desc].filter(Boolean).join(' : '))
      .filter(Boolean)
      .slice(0, 4);
    return toParagraphs(parts, fallback);
  }

  function scoreSummaryLine(scoreCards, company) {
    const bits = toArray(scoreCards)
      .filter((c) => typeof c?.value === 'number')
      .map((c) => `${c.label} ${Math.round(c.value)}/100`);
    const name = company || 'Ce site';
    if (!bits.length) {
      return `${name} : on a un premier regard sur le rapport. Guette voir le détail plus bas.`;
    }
    return `${name} - première lecture des scores : ${bits.join(', ')}. On démêle ça juste en dessous.`;
  }

  function designFallback(highlights) {
    const mobile = toArray(highlights).find((h) => /mobile|affichage|viewport/i.test(String(h?.title || '') + ' ' + String(h?.desc || '')));
    if (mobile) {
      return [mobile.title, mobile.desc].filter(Boolean).join(' - ') + '.';
    }
    return "Côté design, on regarde surtout la clarté sur téléphone et la première impression. Le détail technique est plus bas.";
  }

  function actionsFallback(highlights) {
    return highlightsParagraphs(
      highlights,
      ['bad', 'warn'],
      "Priorité : clarifier les points faibles du rapport, puis avancer sur une paire d'actions concrètes."
    );
  }

  /**
   * Construit les chapitres narratifs a partir de Gemini + fallbacks locaux.
   * @param {{ gemini?: object|null, highlights?: array, scoreCards?: array, entreprise?: object, finalUrl?: string }} report
   * @returns {array}
   */
  function buildNarrativeChapters(report) {
    const geminiWrap = report?.gemini || null;
    const g = geminiWrap?.report || geminiWrap || null;
    const highlights = report?.highlights || [];
    const company = report?.entreprise?.nom || displayHost(report?.finalUrl) || 'Ce site';
    const host = displayHost(report?.finalUrl || currentWebsite || company);
    const design = g?.design_analysis || {};

    const resumeParas = proseFromText(g?.executive_summary);
    const designRaw = String(design?.summary || design?.ux_notes || design?.ui_notes || '').trim();
    const designParas = proseFromText(designRaw);
    const suiteRaw = String(g?.commercial_pitch || '').trim()
      || 'Si tu veux, on peut en parler entre midi - devis simple, un interlocuteur, et on avance sans faire le nareux.';

    const defs = [
      {
        id: 'resume',
        label: 'Résumé',
        paragraphs: resumeParas.length ? resumeParas : [scoreSummaryLine(report?.scoreCards, company)]
      },
      {
        id: 'forces',
        label: 'Forces',
        paragraphs: toArray(g?.what_works).length
          ? toParagraphs(g?.what_works, `${company} a déjà des bases utiles - on les garde en tête.`)
          : highlightsParagraphs(highlights, ['good'], `${company} a déjà des bases utiles - on les garde en tête.`)
      },
      {
        id: 'vigilance',
        label: 'Vigilance',
        paragraphs: g?.whats_wrong
          ? toParagraphs(g?.whats_wrong, 'Rien de critique listé pour l\'instant - le détail reste disponible plus bas.')
          : highlightsParagraphs(highlights, ['bad', 'warn'], 'Rien de critique listé pour l\'instant - le détail reste disponible plus bas.')
      },
      {
        id: 'design',
        label: 'Design',
        paragraphs: designParas.length ? designParas : [designFallback(highlights)]
      },
      {
        id: 'actions',
        label: 'Actions',
        paragraphs: toArray(g?.priority_actions).length
          ? toParagraphs(g?.priority_actions, "Priorité : clarifier les points faibles du rapport, puis avancer sur une paire d'actions concrètes.")
          : actionsFallback(highlights)
      },
      {
        id: 'suite',
        label: 'Suite',
        paragraphs: proseFromText(suiteRaw).length ? proseFromText(suiteRaw) : [suiteRaw]
      }
    ];

    const chars = pickCharacterFiles(host, defs.length);
    const startRight = hashSeed(host) % 2 === 1;

    return defs.map((d, index) => ({
      ...d,
      text: (d.paragraphs || []).join(' '),
      characterSrc: CHARACTER_BASE + (chars[index] || CHARACTER_FILES[index % CHARACTER_FILES.length]),
      side: ((startRight ? index + 1 : index) % 2 === 0) ? 'left' : 'right',
      streamed: false
    }));
  }

  /**
   * Met a jour la puce active dans la nav des chapitres.
   * @param {string} chapterId
   */
  function setNarrativeActive(chapterId) {
    if (!els.narrativeNav) return;
    els.narrativeNav.querySelectorAll('.analyse-story__chip').forEach((chip) => {
      chip.classList.toggle('is-active', chip.getAttribute('data-chapter') === chapterId);
    });
  }

  /**
   * Marque un chapitre comme lu dans la nav.
   * @param {string} chapterId
   */
  function markChapterDone(chapterId) {
    if (!els.narrativeNav) return;
    const chip = els.narrativeNav.querySelector(`[data-chapter="${chapterId}"]`);
    if (chip) chip.classList.add('is-done');
  }

  /**
   * Affiche ou masque le bouton "Voir toute la lecture".
   * @param {boolean} show
   */
  function toggleStorySkip(show) {
    if (!els.storySkip) return;
    els.storySkip.hidden = !show;
  }

  /**
   * Detecte si un token merite une surbrillance (mot-cle ou chiffre fort).
   * @param {string} token
   * @returns {boolean}
   */
  function isStoryKeyword(token) {
    const raw = String(token || '');
    const clean = raw.replace(/^[«"'(]+|[»"'.,;:!?…)%]+$/g, '').toLowerCase();
    if (!clean) return false;
    if (STORY_KEYWORDS.has(clean)) return true;
    if (/^\d+([.,]\d+)?%?$/.test(clean) && Number(clean.replace(',', '.').replace('%', '')) >= 0) return true;
    if (/^\d+\/100$/.test(clean)) return true;
    return false;
  }

  /**
   * Decoupe les paragraphes en mots pour l'animation mot par mot.
   * @param {HTMLElement} textEl
   * @param {string[]} paragraphs
   * @param {{ visible?: boolean }} opts
   */
  function renderNarrativeParagraphs(textEl, paragraphs, { visible }) {
    const paras = Array.isArray(paragraphs) && paragraphs.length
      ? paragraphs
      : [String(paragraphs || '')];
    textEl.innerHTML = paras.map((para) => {
      const parts = String(para || '').split(/(\s+)/);
      const inner = parts.map((part) => {
        if (!part) return '';
        if (/^\s+$/.test(part)) return part;
        const cls = visible ? 'analyse-word is-visible' : 'analyse-word';
        const body = escapeHtml(part);
        if (isStoryKeyword(part)) {
          return `<span class="${cls}"><mark class="analyse-story__mark">${body}</mark></span>`;
        }
        return `<span class="${cls}">${body}</span>`;
      }).join('');
      return `<p class="analyse-story__para">${inner}</p>`;
    }).join('');
    if (visible) textEl.classList.add('is-complete');
    else textEl.classList.remove('is-complete');
  }

  /**
   * Anime le texte mot par mot, paragraphe par paragraphe.
   * @param {HTMLElement} textEl
   * @param {string[]} paragraphs
   * @param {number} token
   */
  async function streamNarrativeText(textEl, paragraphs, token) {
    if (!textEl) return;
    textEl.classList.remove('is-complete');
    if (prefersReducedMotion()) {
      renderNarrativeParagraphs(textEl, paragraphs, { visible: true });
      return;
    }
    renderNarrativeParagraphs(textEl, paragraphs, { visible: false });
    const words = textEl.querySelectorAll('.analyse-word');
    for (let i = 0; i < words.length; i++) {
      if (token !== narrativeToken) return;
      words[i].classList.add('is-visible');
      const raw = words[i].textContent || '';
      const pause = /[.!?…]$/.test(raw) ? STORY_PUNCT_MS : STORY_WORD_MS;
      await sleep(pause);
    }
    if (token === narrativeToken) textEl.classList.add('is-complete');
  }

  /**
   * Remonte doucement un bloc s'il sort du cadre - sans plonger en bas d'un coup.
   * @param {HTMLElement} block
   * @param {{ force?: boolean }} opts
   */
  function scrollStoryBlockIntoView(block, opts) {
    if (!block) return;
    const force = !!(opts && opts.force);
    const rect = block.getBoundingClientRect();
    const viewH = window.innerHeight || document.documentElement.clientHeight || 0;
    if (!viewH) return;

    const stickyOffset = 120;
    const bottomPad = 48;
    const fullyOk = rect.top >= stickyOffset && rect.bottom <= viewH - bottomPad;
    if (!force && fullyOk) return;

    // Cible : le haut du bloc juste sous la nav sticky, avec un petit marge.
    // On plafonne le deplacement pour eviter un grand saut.
    const desiredTop = stickyOffset + 12;
    const delta = rect.top - desiredTop;
    if (Math.abs(delta) < 24 && !force) return;

    const maxStep = Math.round(viewH * 0.42);
    const clampedDelta = Math.max(-maxStep, Math.min(maxStep, delta));
    const nextTop = Math.max(0, window.scrollY + clampedDelta);

    window.scrollTo({
      top: nextTop,
      behavior: prefersReducedMotion() ? 'auto' : 'smooth'
    });
  }

  /**
   * Revele un bloc empile (personnage + texte stream).
   * @param {object} chapter
   * @param {number} token
   * @param {{ instant?: boolean }} opts
   */
  async function playChapter(chapter, token, opts) {
    if (!els.narrative || !chapter) return;
    const instant = !!(opts && opts.instant);
    const block = els.narrative.querySelector(`[data-chapter="${chapter.id}"]`);
    if (!block) return;

    setNarrativeActive(chapter.id);
    block.hidden = false;
    block.classList.add('is-in');

    const alreadyStreamed = !!chapter.streamed;
    // Premier bloc : on reste en haut. Ensuite : petit coup de scroll si besoin.
    const isFirstVisible = !narrativeChapters.some((c) => c.id !== chapter.id && c.streamed);
    if (!alreadyStreamed && !isFirstVisible) {
      window.requestAnimationFrame(() => scrollStoryBlockIntoView(block));
    }

    const char = block.querySelector('.analyse-story__char');
    const textEl = block.querySelector('.analyse-story__text');
    if (char && !prefersReducedMotion()) {
      char.classList.add('is-float');
    }

    if (instant) {
      if (textEl) renderNarrativeParagraphs(textEl, chapter.paragraphs, { visible: true });
    } else {
      await streamNarrativeText(textEl, chapter.paragraphs, token);
    }
    if (token !== narrativeToken) return;
    chapter.streamed = true;
    markChapterDone(chapter.id);
  }

  /**
   * Affiche tous les blocs d'un coup (skip / lecture complete).
   */
  function revealAllStoryBlocks() {
    if (!els.narrative) return;
    narrativeChapters.forEach((c) => {
      const block = els.narrative.querySelector(`[data-chapter="${c.id}"]`);
      if (!block) return;
      block.hidden = false;
      block.classList.add('is-in');
      const textEl = block.querySelector('.analyse-story__text');
      if (textEl) renderNarrativeParagraphs(textEl, c.paragraphs, { visible: true });
      c.streamed = true;
      markChapterDone(c.id);
    });
  }

  /**
   * Passe en mode lecture complete et revele la suite du rapport.
   */
  function skipNarrative() {
    narrativeToken += 1;
    narrativePlaying = false;
    toggleStorySkip(false);
    if (els.narrativeNav) {
      els.narrativeNav.querySelectorAll('.analyse-story__chip').forEach((chip) => chip.classList.remove('is-active'));
    }
    revealAllStoryBlocks();
    if (typeof narrativeTailReveal === 'function') narrativeTailReveal();
  }

  /**
   * Enchaine les blocs empiles un apres l'autre.
   * @param {number} token
   * @param {{ instant?: boolean, onAfterSecondChapter?: Function }} opts
   */
  async function playNarrativeSequence(token, opts) {
    const instant = !!(opts && opts.instant);
    const onAfterSecond = opts && typeof opts.onAfterSecondChapter === 'function' ? opts.onAfterSecondChapter : null;
    narrativeTailReveal = onAfterSecond;
    let tailStarted = false;
    narrativePlaying = true;
    toggleStorySkip(!instant && !prefersReducedMotion());

    try {
      for (let i = 0; i < narrativeChapters.length; i++) {
        if (token !== narrativeToken) return;
        await playChapter(narrativeChapters[i], token, { instant });
        if (token !== narrativeToken) return;
        if (!tailStarted && i >= 1 && onAfterSecond) {
          tailStarted = true;
          onAfterSecond();
        }
        if (!instant && i < narrativeChapters.length - 1) {
          await sleep(STORY_BLOCK_GAP_MS);
        }
      }
      if (!tailStarted && onAfterSecond) onAfterSecond();
    } finally {
      if (token === narrativeToken) {
        narrativePlaying = false;
        toggleStorySkip(false);
      }
    }
  }

  /**
   * Saute a un chapitre via la nav : revele tout avant, puis continue le stream.
   * @param {string} chapterId
   */
  async function jumpToNarrativeChapter(chapterId) {
    const index = narrativeChapters.findIndex((c) => c.id === chapterId);
    if (index < 0) return;
    const token = ++narrativeToken;
    narrativePlaying = true;
    toggleStorySkip(true);

    for (let i = 0; i <= index; i++) {
      await playChapter(narrativeChapters[i], token, { instant: true });
    }
    if (token !== narrativeToken) return;
    if (index >= 1 && typeof narrativeTailReveal === 'function') narrativeTailReveal();

    for (let j = index + 1; j < narrativeChapters.length; j++) {
      if (token !== narrativeToken) return;
      await sleep(STORY_BLOCK_GAP_MS);
      await playChapter(narrativeChapters[j], token, { instant: false });
    }
    if (token === narrativeToken) {
      narrativePlaying = false;
      toggleStorySkip(false);
    }
  }

  /**
   * Construit la nav + tous les blocs empiles (caches jusqu'au stream).
   * @param {array} chapters
   */
  function renderNarrative(chapters) {
    narrativeChapters = Array.isArray(chapters) ? chapters : [];
    narrativeChapters.forEach((c) => { c.streamed = false; });

    if (els.narrativeNav) {
      els.narrativeNav.innerHTML = narrativeChapters.map((c, index) => `
        <button type="button" class="analyse-story__chip" data-chapter="${escapeHtml(c.id)}" aria-label="Chapitre ${index + 1} : ${escapeHtml(c.label)}">
          ${escapeHtml(c.label)}
        </button>
      `).join('');
      els.narrativeNav.querySelectorAll('.analyse-story__chip').forEach((chip) => {
        chip.addEventListener('click', () => jumpToNarrativeChapter(chip.getAttribute('data-chapter')));
      });
    }

    if (!els.narrative) return;
    els.narrative.innerHTML = `
      <div class="analyse-story__stack">
        ${narrativeChapters.map((c) => `
          <article class="analyse-story__block analyse-story__block--${escapeHtml(c.side)}" data-chapter="${escapeHtml(c.id)}" hidden>
            <figure class="analyse-story__char">
              <img src="${escapeHtml(c.characterSrc)}" alt="" width="220" height="260" loading="lazy" decoding="async">
            </figure>
            <div class="analyse-story__panel">
              <p class="analyse-story__kicker">${escapeHtml(c.label)}</p>
              <div class="analyse-story__text"></div>
            </div>
          </article>
        `).join('')}
      </div>
    `;
    toggleStorySkip(false);
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
        if (c.key === 'design' || c.key === 'gemini') worstKey = 'vitrine';
        else if (c.key === 'performance') worstKey = 'performance';
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
          ${isSpecial ? '<span class="analyse-offer__ribbon">Offre spéciale pour toi</span>' : ''}
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
      els.details.innerHTML = '<p class="pl-muted" style="margin:0;">Aucun détail disponible.</p>';
      return;
    }
    list.forEach((sec, idx) => {
      const title = sec?.title || `Section ${idx + 1}`;
      const pill = sec?.pill || '';
      const bodyHtml = sec?.html || '<p class="pl-muted">Aucune donnée.</p>';
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
    const gemini = raw?.gemini || root?.gemini || null;

    const geminiPayload = gemini?.report || gemini || null;
    const designScoreRaw =
      geminiPayload?.design_analysis?.score ??
      gemini?.design_analysis?.score ??
      gemini?.overall_score ??
      geminiPayload?.overall_score;
    const designScore = typeof designScoreRaw === 'number' ? designScoreRaw : null;

    const scoreCards = [
      { key: 'design', label: 'Design', value: designScore },
      { key: 'seo', label: 'SEO', value: entreprise?.score_seo ?? seo?.latest?.score },
      { key: 'securite', label: 'Sécurité', value: entreprise?.score_securite },
      { key: 'risque', label: 'Risque', value: entreprise?.score_pentest ?? pentest?.latest?.risk_score }
    ].map((x) => ({
      ...x,
      noteClient: typeof x.value === 'number' ? scoreNote(x.key, x.value) : '-'
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
    if (td?.mobile_friendly === false) highlights.push({ title: 'Mobile', desc: 'Site peu confortable sur téléphone.', tone: 'bad' });
    if (td?.viewport_meta === 'Manquant') highlights.push({ title: 'Affichage', desc: 'Meta viewport manquante.', tone: 'warn' });
    if (typeof entreprise?.performance_score === 'number' && entreprise.performance_score >= 80) {
      highlights.push({ title: 'Vitesse', desc: 'Bon niveau de performance global.', tone: 'good' });
    }
    if (typeof (entreprise?.score_seo ?? seoLatest?.score) === 'number' && (entreprise?.score_seo ?? seoLatest?.score) >= 80) {
      highlights.push({ title: 'Visibilité', desc: 'Bases SEO plutôt solides.', tone: 'good' });
    }

    const pLatest = pentest?.latest || {};
    const pSum = pLatest?.summary || {};
    if (pSum?.risk_level) {
      highlights.push({
        title: 'Risque sécurité',
        desc: `${pSum.risk_level} - ${pSum.total_vulnerabilities ?? 0} point(s) à surveiller`,
        tone: toneFromScore(pLatest?.risk_score, true)
      });
    }

    const oLatest = osint?.latest || {};
    if (oLatest?.summary_warning) highlights.push({ title: 'Données publiques', desc: stripHtml(oLatest.summary_warning), tone: 'warn' });

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
          ${entreprise?.telephone ? `<strong>Téléphone :</strong> <span class="pl-mono">${escapeHtml(entreprise.telephone)}</span><br>` : ''}
        </p>
        ${tags ? `<div class="pl-badges" style="margin-top:0.8rem;">${tags}</div>` : ''}
      `
    });

    const pagesSummary = tLatest?.pages_summary || {};

    const techRows = [
      ['CMS', tLatest?.cms || '-'],
      ['CDN', tLatest?.cdn || '-'],
      ['SSL', tLatest?.ssl_valid ? 'Valide' : 'À vérifier'],
      ['Mobile', td?.mobile_friendly === false ? 'Non' : (td?.mobile_friendly === true ? 'Oui' : '-')]
    ];
    sections.push({
      title: 'Technique',
      pill: tLatest?.framework ? String(tLatest.framework) : '',
      html: `
        ${tableHtml(['Indicateur', 'Valeur'], techRows.map(([a, b]) => [escapeHtml(a), escapeHtml(String(b))]))}
        <p class="pl-muted" style="margin-top:0.9rem;">
          <strong>Pages :</strong> ${escapeHtml(String(pagesSummary.pages_scanned ?? pagesSummary.pages_count ?? 0))} ·
          <strong>Temps moyen :</strong> ${escapeHtml(String(pagesSummary.avg_response_time_ms ?? '-'))} ms
        </p>
      `
    });

    const meta = safeJsonParse(seoLatest?.meta_tags_json) || {};
    const structure = safeJsonParse(seoLatest?.structure_json) || {};
    const seoRows = [
      ['Score', seoLatest?.score != null ? `${seoLatest.score}/100` : '-'],
      ['Title', meta?.title ? escapeHtml(meta.title) : '-'],
      ['H1', structure?.h1_count != null ? String(structure.h1_count) : '-'],
      ['Images sans alt', structure?.images_without_alt != null ? String(structure.images_without_alt) : '-']
    ];
    const seoIssuesHtml = toArray(seoIssues).slice(0, 8).map((it) => {
      const impact = it?.impact || 'medium';
      const tone = impact === 'high' ? 'bad' : impact === 'medium' ? 'warn' : 'good';
      return `<div class="pl-audit pl-audit--${tone}" style="margin-top:0.7rem;">
        <div class="pl-audit-title">${escapeHtml(it?.category ? `SEO · ${it.category}` : 'SEO')}</div>
        <div class="pl-audit-desc">${escapeHtml(it?.message || '-')}</div>
      </div>`;
    }).join('');
    sections.push({
      title: 'SEO',
      pill: seoLatest?.score != null ? `${seoLatest.score}/100` : '',
      html: `
        ${tableHtml(['Élément', 'Valeur'], seoRows.map(([a, b]) => [escapeHtml(a), (typeof b === 'string' ? b : String(b))]))}
        ${seoIssuesHtml || '<p class="pl-muted" style="margin-top:1rem;">Aucune alerte SEO.</p>'}
      `
    });

    const vulns = toArray(pLatest?.vulnerabilities).slice(0, 10);
    const vulnHtml = vulns.map(v => {
      const sev = (v?.severity || '').toLowerCase();
      const tone = sev === 'high' ? 'bad' : sev === 'medium' ? 'warn' : 'good';
      return `<div class="pl-audit pl-audit--${tone}" style="margin-top:0.7rem;">
        <div class="pl-audit-title">${escapeHtml(v?.name || v?.type || 'Point sécurité')}</div>
        <div class="pl-audit-desc">${escapeHtml(v?.description || '')}</div>
      </div>`;
    }).join('');
    sections.push({
      title: 'Sécurité',
      pill: pLatest?.risk_score != null ? `${pLatest.risk_score}/100` : '',
      html: `
        <p class="pl-muted">
          ${pSum?.risk_level ? `<strong>Niveau :</strong> ${escapeHtml(String(pSum.risk_level))}` : ''}
        </p>
        ${vulnHtml || '<p class="pl-muted" style="margin-top:0.8rem;">Rien de critique listé.</p>'}
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
      title: 'Données publiques',
      pill: oLatest?.status ? String(oLatest.status) : '',
      html: `
        <p class="pl-muted">
          <strong>Date :</strong> ${escapeHtml(formatDate(oLatest?.date_analyse) || formatDate(scLatest?.date_modification) || '-')}
        </p>
      `
    });

    return {
      finalUrl: website,
      entreprise,
      scoreCards,
      highlights,
      gemini,
      sections,
      metaLine: entreprise?.date_analyse ? formatDate(entreprise.date_analyse) : null,
      suggestedEmail: typeof firstEmail === 'string' ? firstEmail : null
    };
  }

  function formatLookupError(message) {
    const msg = String(message || '').trim();
    if (/aucun rapport/i.test(msg)) {
      return 'Aucun rapport enregistré pour cette adresse. Reprends l\'URL exacte du lien email, ou demande une analyse via « Recevoir le rapport ».';
    }
    return msg || 'Impossible de charger le rapport. Réessaie dans un instant.';
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

    renderScores(r.scoreCards);
    renderNarrative(buildNarrativeChapters(r));
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
    if (els.storySection) els.storySection.hidden = true;
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
    if (els.storySection) els.storySection.hidden = true;
    if (els.report) els.report.hidden = true;
    if (els.intro) els.intro.classList.remove('is-hidden');

    prefillLead({
      website: websiteUrl,
      email: (queryPrefill && queryPrefill.email) || '',
      name: (queryPrefill && queryPrefill.name) || '',
      first: queryPrefill && queryPrefill.first,
      last: queryPrefill && queryPrefill.last
    });

    try {
      const report = await apiGetWebsiteAnalysis({ website: websiteUrl, full: full ?? 1 });
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

  /**
   * Envoie la demande de rapport (simple ou Gemini) selon modalMode.
   */
  function submitLeadAudit() {
    if (leadSubmitting) return;

    const vals = readLeadValues();
    if (vals.honeypot) return;
    if (!vals.url) {
      setLeadModalFeedback('URL du site invalide.', true);
      return;
    }
    if (!vals.email || !/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(vals.email)) {
      setLeadModalFeedback('Email invalide.', true);
      return;
    }

    const isGemini = modalMode === 'gemini';
    leadSubmitting = true;
    setBtnLoading(els.leadSubmit, true);
    setLeadModalFeedback('', false);

    const payload = {
      website: vals.url,
      email: vals.email,
      name: vals.name
    };
    if (isGemini) {
      payload.complete = true;
      payload.audit = 'gemini';
    }

    fetch(FREE_AUDIT_ENDPOINT, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(payload)
    })
      .then(async (res) => {
        const data = await res.json().catch(() => ({}));
        return { res, data };
      })
      .then((ref) => {
        if (ref.res.ok && ref.data && ref.data.success) {
          setBtnLoading(els.leadSubmit, false);
          closeLeadModal();
          const fallback = isGemini
            ? `Le rapport Gemini part sur ${vals.email}.`
            : `Le rapport simple part sur ${vals.email}.`;
          openWinModal((ref.data && ref.data.message) || fallback);
          return;
        }
        let errMsg = (ref.data && ref.data.error) || 'Envoi impossible. Réessaie ou contacte-nous.';
        if (ref.res.status === 429) {
          errMsg = (ref.data && ref.data.error) || 'Tu as déjà demandé un rapport récemment. Réessaie plus tard.';
        }
        setLeadModalFeedback(errMsg, true);
      })
      .catch(() => {
        setLeadModalFeedback('Serveur injoignable.', true);
      })
      .finally(() => {
        leadSubmitting = false;
        setBtnLoading(els.leadSubmit, false);
      });
  }

  els.form.addEventListener('submit', async (e) => {
    e.preventDefault();
    const v = safeUrl(els.url.value);
    if (!v) {
      setFeedback(els.bootFeedback, 'Saisis une URL valide (http ou https).', true);
      els.url.focus();
      return;
    }
    await handleSubmit(v, 1, null);
  });

  if (els.storySkip) {
    els.storySkip.addEventListener('click', () => skipNarrative());
  }

  if (els.leadForm) {
    els.leadForm.addEventListener('submit', (e) => {
      e.preventDefault();
      submitLeadAudit();
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
      const geminiBtn = e.target.closest('[data-analyse-audit-gemini]');
      if (geminiBtn) {
        e.preventDefault();
        openLeadModal('gemini');
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

  if (els.winModal) {
    els.winModal.addEventListener('click', (e) => {
      if (e.target.closest('[data-analyse-win-close]')) {
        e.preventDefault();
        closeWinModal();
      }
    });
  }

  document.addEventListener('keydown', (e) => {
    if (e.key !== 'Escape') return;
    if (els.winModal && !els.winModal.hidden) {
      closeWinModal();
      return;
    }
    closeLeadModal();
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
