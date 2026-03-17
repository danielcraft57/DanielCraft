// ===== Rapport d'analyse - Page /analyse =====

(function () {
  const API_BASE = '';
  const ENDPOINT = '/api/website-analysis.php';

  const els = {
    form: document.getElementById('plForm'),
    url: document.getElementById('plUrl'),
    submit: document.getElementById('plSubmitBtn'),
    clear: document.getElementById('plClearBtn'),
    feedback: document.getElementById('plFeedback'),
    report: document.getElementById('plReport'),
    reportMeta: document.getElementById('plReportMeta'),
    copyLink: document.getElementById('plCopyLinkBtn'),
    openSite: document.getElementById('plOpenSiteBtn'),
    scores: document.getElementById('plScores'),
    screenshot: document.getElementById('plScreenshot'),
    keyValues: document.getElementById('plKeyValues'),
    highlights: document.getElementById('plHighlights'),
    details: document.getElementById('plDetails')
  };

  if (!els.form || !els.url || !els.submit) return;

  function setFeedback(message, isError) {
    if (!els.feedback) return;
    if (!message) {
      els.feedback.hidden = true;
      els.feedback.textContent = '';
      return;
    }
    els.feedback.hidden = false;
    els.feedback.textContent = message;
    els.feedback.className = 'form-feedback ' + (isError ? 'form-feedback--error' : 'form-feedback--success');
  }

  function setLoading(isLoading) {
    els.submit.classList.toggle('is-loading', isLoading);
    els.submit.disabled = isLoading;
  }

  function safeUrl(raw) {
    try {
      const u = new URL(raw);
      if (!['http:', 'https:'].includes(u.protocol)) return null;
      return u.toString();
    } catch {
      return null;
    }
  }

  function scoreColor(score0to100) {
    if (score0to100 >= 90) return 'var(--accent-color)';
    if (score0to100 >= 50) return '#f59e0b';
    return 'var(--danger-color)';
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

  function tableHtml(headers, rows) {
    const th = headers.map(h => `<th>${escapeHtml(h)}</th>`).join('');
    const tr = rows.map(r => `<tr>${r.map(c => `<td>${c}</td>`).join('')}</tr>`).join('');
    return `<div class="pl-table"><table><thead><tr>${th}</tr></thead><tbody>${tr}</tbody></table></div>`;
  }

  function renderScores(cards) {
    if (!els.scores) return;
    els.scores.innerHTML = '';

    const list = Array.isArray(cards) ? cards : [];
    if (!list.length) {
      els.scores.innerHTML = '<p style="color: var(--gray-600); margin: 0;">Aucun score disponible.</p>';
      return;
    }

    list.forEach((it) => {
      const key = it?.key || it?.label || 'score';
      const score100 = typeof it?.value === 'number' ? Math.round(it.value) : null;
      const ring = score100 == null ? 0 : Math.max(0, Math.min(100, score100));
      const color = score100 == null ? 'rgba(17, 24, 39, 0.18)' : scoreColor(score100);
      const note = it?.note || (score100 == null ? '—' : (score100 >= 90 ? 'Excellent' : score100 >= 50 ? 'Moyen' : 'Faible'));

      const card = document.createElement('div');
      card.className = 'pl-score-card';
      card.innerHTML = `
        <div class="pl-score-ring" style="--pl-ring:${ring}%; --pl-ring-color:${color};" aria-label="${escapeHtml(String(key))}: ${score100 ?? '—'}">
          <div class="pl-score-value">${score100 ?? '—'}</div>
        </div>
        <div class="pl-score-meta">
          <div class="pl-score-label">${escapeHtml(it?.label || String(key))}</div>
          <div class="pl-score-note">${escapeHtml(note)}</div>
          ${typeof it?.value === 'number' ? `<div class="pl-bar" aria-hidden="true"><div class="pl-bar-fill" style="background:${color}" data-pl-bar="${ring}"></div></div>` : ''}
        </div>
      `;
      els.scores.appendChild(card);
    });

    requestAnimationFrame(() => {
      document.querySelectorAll('[data-pl-bar]').forEach((el) => {
        const v = Number(el.getAttribute('data-pl-bar') || '0');
        el.style.width = `${Math.max(0, Math.min(100, v))}%`;
      });
    });
  }

  function renderPreview(preview) {
    const { finalUrl, entreprise, technical, seo, pentest, osint } = preview || {};

    if (els.screenshot) {
      els.screenshot.innerHTML = '';
      const box = document.createElement('div');
      box.className = 'pl-skeleton';
      box.style.width = '100%';
      box.style.height = '100%';
      box.setAttribute('aria-hidden', 'true');
      els.screenshot.appendChild(box);
    }

    if (els.openSite && finalUrl) {
      els.openSite.href = finalUrl;
      els.openSite.setAttribute('aria-disabled', 'false');
    } else if (els.openSite) {
      els.openSite.href = '#';
      els.openSite.setAttribute('aria-disabled', 'true');
    }

    if (!els.keyValues) return;
    const rows = [];
    if (entreprise?.nom) rows.push(['Entreprise', entreprise.nom]);
    if (finalUrl) rows.push(['Site', finalUrl.replace(/^https?:\/\//, '')]);
    if (entreprise?.secteur) rows.push(['Secteur', entreprise.secteur]);
    if (entreprise?.taille_estimee) rows.push(['Taille', entreprise.taille_estimee]);
    if (entreprise?.opportunite) rows.push(['Opportunité', entreprise.opportunite]);
    if (technical?.latest?.cms) rows.push(['CMS', technical.latest.cms]);
    if (technical?.latest?.cdn) rows.push(['CDN', technical.latest.cdn]);
    if (seo?.latest?.score != null) rows.push(['Score SEO', `${seo.latest.score}/100`]);
    if (pentest?.latest?.risk_score != null) rows.push(['Risque', `${pentest.latest.risk_score}/100`]);
    if (osint?.latest?.summary?.emails_count != null) rows.push(['Emails trouvés', String(osint.latest.summary.emails_count)]);
    els.keyValues.innerHTML = rows.map(([k, v]) => `<dt>${escapeHtml(k)}</dt><dd>${escapeHtml(v)}</dd>`).join('');
  }

  function renderHighlights(items) {
    if (!els.highlights) return;
    const list = Array.isArray(items) ? items : [];
    els.highlights.innerHTML = '';
    if (!list.length) {
      els.highlights.innerHTML = '<p style="color: var(--gray-600); margin: 0;">Aucun point clé disponible.</p>';
      return;
    }
    list.forEach((it) => {
      const div = document.createElement('div');
      div.className = 'pl-audit ' + (it?.tone ? `pl-audit--${it.tone}` : '');
      div.innerHTML = `
        <div class="pl-audit-title">${escapeHtml(it.title)}</div>
        <div class="pl-audit-desc">${escapeHtml(it.desc || '—')}</div>
      `;
      els.highlights.appendChild(div);
    });
  }

  function renderDetails(sections) {
    if (!els.details) return;
    els.details.innerHTML = '';

    const list = Array.isArray(sections) ? sections : [];
    if (!list.length) {
      els.details.innerHTML = '<p style="color: var(--gray-600); margin: 0;">Aucun détail disponible.</p>';
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

    const scoreCards = [
      { key: 'performance', label: 'Performance', value: entreprise?.performance_score, note: 'Temps de réponse, poids, optimisation' },
      { key: 'seo', label: 'SEO', value: entreprise?.score_seo ?? seo?.latest?.score, note: 'Meta, structure, indexabilité' },
      { key: 'securite', label: 'Sécurité', value: entreprise?.score_securite, note: 'Headers, SSL/TLS, hygiène' },
      { key: 'pentest', label: 'Pentest', value: entreprise?.score_pentest ?? pentest?.latest?.risk_score, note: 'Surface & risques détectés' }
    ].filter(x => typeof x.value === 'number');

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
    if (td?.mobile_friendly === false) highlights.push({ title: 'Mobile', desc: 'Site non “mobile-friendly”.', tone: 'bad' });
    if (td?.viewport_meta === 'Manquant') highlights.push({ title: 'UX', desc: 'Meta viewport manquante.', tone: 'warn' });

    const pLatest = pentest?.latest || {};
    const pSum = pLatest?.summary || {};
    if (pSum?.risk_level) {
      highlights.push({
        title: 'Risque sécurité',
        desc: `${pSum.risk_level} — ${pSum.total_vulnerabilities ?? 0} vulnérabilité(s)`,
        tone: toneFromScore(pLatest?.risk_score, true)
      });
    }

    const oLatest = osint?.latest || {};
    if (oLatest?.summary_warning) highlights.push({ title: 'OSINT', desc: stripHtml(oLatest.summary_warning), tone: 'warn' });

    const sections = [];

    const addr = [entreprise?.address_1, entreprise?.address_2].filter(Boolean).join(', ');
    const tags = toArray(entreprise?.tags).slice(0, 12).map(t => `<span class="pl-badge">${escapeHtml(String(t))}</span>`).join(' ');
    sections.push({
      title: 'Entreprise',
      pill: entreprise?.statut ? String(entreprise.statut) : '',
      html: `
        ${entreprise?.resume ? `<p class="pl-muted">${escapeHtml(entreprise.resume)}</p>` : ''}
        <div class="pl-topline">
          <div class="pl-badges">
            ${entreprise?.cms ? `<span class="pl-badge pl-badge--good"><i class="fas fa-cube" aria-hidden="true"></i>${escapeHtml(entreprise.cms)}</span>` : ''}
            ${entreprise?.framework ? `<span class="pl-badge"><i class="fas fa-layer-group" aria-hidden="true"></i>${escapeHtml(entreprise.framework)}</span>` : ''}
            ${entreprise?.note_google ? `<span class="pl-badge pl-badge--good"><i class="fas fa-star" aria-hidden="true"></i>${escapeHtml(String(entreprise.note_google))} (${escapeHtml(String(entreprise.nb_avis_google || 0))} avis)</span>` : ''}
            ${entreprise?.opportunite ? `<span class="pl-badge pl-badge--warn"><i class="fas fa-bullseye" aria-hidden="true"></i>${escapeHtml(entreprise.opportunite)}</span>` : ''}
          </div>
        </div>
        <p class="pl-muted" style="margin-top:0.9rem;">
          ${addr ? `<strong>Adresse :</strong> ${escapeHtml(addr)}<br>` : ''}
          ${entreprise?.telephone ? `<strong>Téléphone :</strong> <span class="pl-mono">${escapeHtml(entreprise.telephone)}</span><br>` : ''}
        </p>
        ${tags ? `<div class="pl-badges" style="margin-top:0.8rem;">${tags}</div>` : ''}
      `
    });

    const pagesSummary = tLatest?.pages_summary || {};
    const techRows = [
      ['CMS', tLatest?.cms || '—'],
      ['Version', tLatest?.cms_version || '—'],
      ['CDN', tLatest?.cdn || '—'],
      ['IP', tLatest?.ip_address ? `<span class="pl-mono">${escapeHtml(tLatest.ip_address)}</span>` : '—'],
      ['SSL', tLatest?.ssl_valid ? 'Valide' : 'À vérifier'],
      ['Serveur', td?.server_type || td?.server || tLatest?.server_software || '—'],
      ['Mobile-friendly', td?.mobile_friendly === false ? 'Non' : (td?.mobile_friendly === true ? 'Oui' : '—')],
      ['Viewport', td?.viewport_meta || '—']
    ];
    sections.push({
      title: 'Technique',
      pill: tLatest?.framework ? String(tLatest.framework) : '',
      html: `
        ${tableHtml(['Indicateur', 'Valeur'], techRows.map(([a,b]) => [escapeHtml(a), (typeof b === 'string' ? b : String(b))]))}
        <p class="pl-muted" style="margin-top:0.9rem;">
          <strong>Pages :</strong> ${escapeHtml(String(pagesSummary.pages_scanned ?? pagesSummary.pages_count ?? 0))} ·
          <strong>Temps moyen :</strong> ${escapeHtml(String(pagesSummary.avg_response_time_ms ?? '—'))} ms ·
          <strong>Poids moyen :</strong> ${escapeHtml(String(pagesSummary.avg_weight_bytes ? Math.round(pagesSummary.avg_weight_bytes/1024) + ' KB' : '—'))}
        </p>
      `
    });

    const meta = safeJsonParse(seoLatest?.meta_tags_json) || {};
    const structure = safeJsonParse(seoLatest?.structure_json) || {};
    const seoRows = [
      ['Score', seoLatest?.score != null ? `${seoLatest.score}/100` : '—'],
      ['Title', meta?.title ? escapeHtml(meta.title) : '—'],
      ['Canonical', meta?.canonical ? `<span class="pl-mono">${escapeHtml(meta.canonical)}</span>` : '—'],
      ['H1', structure?.h1_count != null ? String(structure.h1_count) : '—'],
      ['Images sans alt', structure?.images_without_alt != null ? String(structure.images_without_alt) : '—']
    ];
    const seoIssuesHtml = toArray(seoIssues).slice(0, 12).map((it) => {
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
        ${tableHtml(['Élément', 'Valeur'], seoRows.map(([a,b]) => [escapeHtml(a), (typeof b === 'string' ? b : String(b))]))}
        ${seoIssuesHtml ? `<div style="margin-top:1rem;"><strong>Alertes</strong>${seoIssuesHtml}</div>` : '<p class="pl-muted" style="margin-top:1rem;">Aucune alerte SEO.</p>'}
      `
    });

    const vulns = toArray(pLatest?.vulnerabilities).slice(0, 12);
    const vulnHtml = vulns.map(v => {
      const sev = (v?.severity || '').toLowerCase();
      const tone = sev === 'high' ? 'bad' : sev === 'medium' ? 'warn' : 'good';
      return `<div class="pl-audit pl-audit--${tone}" style="margin-top:0.7rem;">
        <div class="pl-audit-title">${escapeHtml(v?.name || v?.type || 'Vulnérabilité')}</div>
        <div class="pl-audit-desc">${escapeHtml(v?.description || '')}${v?.recommendation ? `<p style="margin-top:0.5rem;"><strong>Reco :</strong> ${escapeHtml(v.recommendation)}</p>` : ''}</div>
      </div>`;
    }).join('');
    sections.push({
      title: 'Sécurité & audit',
      pill: pLatest?.risk_score != null ? `${pLatest.risk_score}/100` : '',
      html: `
        <p class="pl-muted">
          ${pSum?.risk_level ? `<strong>Niveau :</strong> ${escapeHtml(String(pSum.risk_level))} · ` : ''}
          ${pSum?.total_vulnerabilities != null ? `<strong>Vulnérabilités :</strong> ${escapeHtml(String(pSum.total_vulnerabilities))}` : ''}
        </p>
        ${vulnHtml || '<p class="pl-muted" style="margin-top:0.8rem;">Aucune vulnérabilité listée.</p>'}
      `
    });

    const dns = oLatest?.dns_records || {};
    const emails = toArray(oLatest?.emails || oLatest?.emails_found || []).slice(0, 12);
    const scLatest = scraping?.latest || {};
    const scrEmails = toArray(scLatest?.emails).slice(0, 10);
    const scrPhones = toArray(scLatest?.phones_from_scrapers || scLatest?.phones).slice(0, 10);
    const dnsRows = Object.entries(dns).slice(0, 8).map(([k, v]) => [escapeHtml(k), escapeHtml(Array.isArray(v) ? v.join(', ') : String(v))]);
    const emailsHtml = emails.length ? `<ul>${emails.map(e => `<li><span class="pl-mono">${escapeHtml(e)}</span></li>`).join('')}</ul>` : '<p class="pl-muted">Aucun email.</p>';
    const scrEmailsHtml = scrEmails.length ? `<ul>${scrEmails.map(e => `<li><span class="pl-mono">${escapeHtml(e.email || '')}</span>${e.analysis?.provider ? ` <span class="pl-muted">(${escapeHtml(e.analysis.provider)})</span>` : ''}</li>`).join('')}</ul>` : '<p class="pl-muted">Aucun email.</p>';
    const scrPhonesHtml = scrPhones.length ? `<ul>${scrPhones.map(p => `<li><span class="pl-mono">${escapeHtml(p.phone || '')}</span></li>`).join('')}</ul>` : '<p class="pl-muted">Aucun téléphone.</p>';
    sections.push({
      title: 'Données publiques',
      pill: oLatest?.status ? String(oLatest.status) : '',
      html: `
        <p class="pl-muted">
          <strong>Statut :</strong> ${escapeHtml(String(oLatest?.status || '—'))} ·
          <strong>Date :</strong> ${escapeHtml(formatDate(oLatest?.date_analyse) || formatDate(scLatest?.date_modification) || '—')}
        </p>
        ${dnsRows.length ? `<div style="margin-top:0.9rem;"><strong>DNS</strong>${tableHtml(['Type', 'Valeur'], dnsRows)}</div>` : ''}
        <div style="margin-top:0.9rem;"><strong>Emails</strong>${emailsHtml}</div>
        <div style="margin-top:0.9rem;"><strong>Emails (scraping)</strong>${scrEmailsHtml}</div>
        <div style="margin-top:0.9rem;"><strong>Téléphones</strong>${scrPhonesHtml}</div>
      `
    });

    return {
      finalUrl: website,
      entreprise,
      technical,
      seo,
      pentest,
      osint,
      scraping,
      scoreCards,
      highlights,
      sections,
      metaLine: entreprise?.date_analyse ? formatDate(entreprise.date_analyse) : null
    };
  }

  async function apiGetWebsiteAnalysis({ website, full }) {
    const u = new URL((API_BASE || '') + ENDPOINT, window.location.origin);
    u.searchParams.set('website', website);
    if (full != null) u.searchParams.set('full', String(full));

    const res = await fetch(u.toString(), { method: 'GET' });
    const data = await res.json().catch(() => ({}));
    if (!res.ok) {
      const msg = data?.error || data?.message || `Erreur API (${res.status})`;
      throw new Error(msg);
    }
    return data;
  }

  function buildShareUrl({ website, full }) {
    const u = new URL(window.location.href);
    u.searchParams.delete('website');
    u.searchParams.delete('full');
    if (website) u.searchParams.set('website', website);
    if (full != null) u.searchParams.set('full', String(full));
    u.hash = '';
    return u.toString();
  }

  async function showReport(raw) {
    const r = normalizeReport(raw);

    if (els.reportMeta) {
      const metaParts = [];
      if (r.finalUrl) metaParts.push(`Site : ${r.finalUrl}`);
      if (r.entreprise?.nom) metaParts.push(`Entreprise : ${r.entreprise.nom}`);
      if (r.metaLine) metaParts.push(`Analyse : ${r.metaLine}`);
      els.reportMeta.textContent = metaParts.join(' · ');
    }

    renderScores(r.scoreCards);
    renderPreview(r);
    renderHighlights(r.highlights);
    renderDetails(r.sections);

    if (els.copyLink) {
      const share = buildShareUrl({ website: r.finalUrl, full: 1 });
      els.copyLink.onclick = async () => {
        try {
          await navigator.clipboard.writeText(share);
          setFeedback('Lien copié dans le presse-papier.', false);
        } catch {
          setFeedback('Impossible de copier automatiquement. Copiez ce lien manuellement : ' + share, true);
        }
      };
    }

    if (els.report) els.report.hidden = false;
    els.report?.scrollIntoView({ behavior: 'smooth', block: 'start' });
  }

  async function handleSubmit(websiteUrl, full) {
    setFeedback('', false);
    setLoading(true);
    if (els.report) els.report.hidden = true;
    if (els.scores) els.scores.innerHTML = '<div class="pl-skeleton" style="height:120px;"></div>';
    if (els.highlights) els.highlights.innerHTML = '<div class="pl-skeleton" style="height:120px;"></div>';
    if (els.details) els.details.innerHTML = '<div class="pl-skeleton" style="height:180px;"></div>';
    if (els.screenshot) els.screenshot.innerHTML = '<div class="pl-skeleton" style="height:100%;"></div>';
    try {
      const report = await apiGetWebsiteAnalysis({ website: websiteUrl, full: full ?? 1 });
      await showReport(report);
      const share = buildShareUrl({ website: websiteUrl, full: full ?? 1 });
      window.history.replaceState({}, '', share);
    } catch (e) {
      setFeedback((e && e.message ? e.message : 'Erreur inconnue.'), true);
    } finally {
      setLoading(false);
    }
  }

  els.form.addEventListener('submit', async (e) => {
    e.preventDefault();
    const v = safeUrl(els.url.value.trim());
    if (!v) {
      setFeedback('Veuillez saisir une URL valide (http ou https).', true);
      els.url.focus();
      return;
    }
    await handleSubmit(v, 1);
  });

  if (els.clear) {
    els.clear.addEventListener('click', () => {
      setFeedback('', false);
      els.url.value = '';
      if (els.report) els.report.hidden = true;
      if (els.scores) els.scores.innerHTML = '';
      if (els.highlights) els.highlights.innerHTML = '';
      if (els.details) els.details.innerHTML = '';
      if (els.screenshot) els.screenshot.innerHTML = '';
      if (els.keyValues) els.keyValues.innerHTML = '';
      window.history.replaceState({}, '', '/analyse');
      els.url.focus();
    });
  }

  (async function initFromQuery() {
    const q = new URLSearchParams(window.location.search);
    const website = q.get('website');
    const full = q.get('full');
    if (website) {
      const v = safeUrl(website);
      if (v) {
        els.url.value = v;
        const fullNum = full != null ? Number(full) : 1;
        await handleSubmit(v, Number.isFinite(fullNum) ? fullNum : 1);
      }
    }
  })();
})();

