/* Moteur de personnalisation ProspectLab (offres, projets, blog) */
(function () {
  'use strict';

  const ENDPOINT = '/api/prospect-context.php';
  // v2 pour invalider les anciens contextes sans prefill enrichi
  const STORAGE_KEY = 'dc_pl_ctx_v2';
  const STORAGE_TS_KEY = 'dc_pl_ctx_ts_v2';
  const EMAIL_STORAGE_KEY = 'dc_pl_email_v2';
  const CONTEXT_TTL_MS = 15 * 60 * 1000;

  function nowMs() {
    return Date.now();
  }

  function toArray(value) {
    return Array.isArray(value) ? value : [];
  }

  function normalizeTokens(items) {
    return toArray(items)
      .map((x) => String(x || '').trim().toLowerCase())
      .filter(Boolean);
  }

  function contextTokens(context) {
    const entreprise = (context && context.entreprise) || {};
    const rawText = [
      entreprise.industry,
      entreprise.secteur,
      entreprise.company_size,
      entreprise.taille,
      entreprise.description,
      entreprise.resume
    ].join(' ');
    return String(rawText || '').toLowerCase();
  }

  function safeJsonParse(raw) {
    try {
      return JSON.parse(raw);
    } catch (_) {
      return null;
    }
  }

  function readCachedContext() {
    try {
      const raw = localStorage.getItem(STORAGE_KEY);
      const tsRaw = localStorage.getItem(STORAGE_TS_KEY);
      if (!raw || !tsRaw) return null;
      const ts = Number(tsRaw);
      if (!Number.isFinite(ts) || (nowMs() - ts) > CONTEXT_TTL_MS) return null;
      const parsed = safeJsonParse(raw);
      if (!parsed || parsed.success !== true) return null;
      return parsed;
    } catch (_) {
      return null;
    }
  }

  function writeCachedContext(ctx) {
    try {
      localStorage.setItem(STORAGE_KEY, JSON.stringify(ctx));
      localStorage.setItem(STORAGE_TS_KEY, String(nowMs()));
    } catch (_) {
      // ignore
    }
  }

  function tokenMatch(haystackTokens, candidates) {
    const hs = normalizeTokens(haystackTokens);
    const cs = normalizeTokens(candidates);
    return cs.some((c) => hs.some((h) => h.includes(c) || c.includes(h)));
  }

  function inferPrioritiesFromText(text) {
    const t = String(text || '').toLowerCase();
    const out = [];
    if (/seo|google|trafic|visibilit|référenc|referenc/.test(t)) out.push('seo');
    if (/ia|ai|chatgpt|llm|automation|automatisation/.test(t)) out.push('ai');
    if (/api|backend|intégration|integration|webhook/.test(t)) out.push('api');
    if (/crm|prospect|lead|conversion/.test(t)) out.push('crm');
    if (/outil|workflow|process|productivité|productivite/.test(t)) out.push('automation');
    if (!out.length) out.push('web');
    return Array.from(new Set(out));
  }

  function extractWebsiteFromLocation() {
    const q = new URLSearchParams(window.location.search);
    return q.get('website') || q.get('domain') || q.get('url') || '';
  }

  function extractEmailFromLocation() {
    const q = new URLSearchParams(window.location.search);
    const raw = (q.get('email') || '').trim();
    if (!raw) return '';
    // Validation légère côté front; validation stricte reste côté backend.
    if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(raw)) return '';
    try {
      localStorage.setItem(EMAIL_STORAGE_KEY, raw);
    } catch (_) {
      // ignore
    }
    // Nettoie l'URL pour masquer ?email=... sans recharger la page.
    if (q.has('email')) {
      q.delete('email');
      const next = window.location.pathname + (q.toString() ? ('?' + q.toString()) : '') + window.location.hash;
      window.history.replaceState({}, document.title, next);
    }
    return raw;
  }

  function readStoredEmail() {
    try {
      const raw = String(localStorage.getItem(EMAIL_STORAGE_KEY) || '').trim();
      if (!raw) return '';
      return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(raw) ? raw : '';
    } catch (_) {
      return '';
    }
  }

  async function fetchContext(params) {
    const u = new URL(ENDPOINT, window.location.origin);
    if (params.email) u.searchParams.set('email', params.email);
    else if (params.website) u.searchParams.set('website', params.website);
    else return null;

    const res = await fetch(u.toString(), { method: 'GET' });
    const data = await res.json().catch(() => null);
    if (!res.ok || !data || data.success !== true) return null;
    writeCachedContext(data);
    return data;
  }

  async function getContext(opts) {
    const options = opts || {};
    const useCache = options.useCache !== false;

    // IMPORTANT: on lit d'abord l'URL pour détecter un nouvel email de campagne
    // avant de servir le cache, sinon aucun nouvel appel API n'est déclenché.
    const urlEmail = extractEmailFromLocation();
    const explicitEmail = String(options.email || '').trim();
    const storedEmail = readStoredEmail();
    const email = explicitEmail || urlEmail || storedEmail;
    const website = String(options.website || '').trim() || extractWebsiteFromLocation();

    // Si l'email vient de l'URL, on force un refetch (campagne)
    // afin d'eviter de servir un cache ancien pour un nouveau prospect.
    const shouldBypassCache = !!urlEmail;

    if (useCache && !shouldBypassCache) {
      const cached = readCachedContext();
      if (cached) {
        const cachedEmail = String((cached.query && cached.query.email) || '').trim().toLowerCase();
        const requestedEmail = String(email || '').trim().toLowerCase();
        const cachedWebsite = String((cached.query && cached.query.website) || '').trim().toLowerCase();
        const requestedWebsite = String(website || '').trim().toLowerCase();
        const hasNewIdentity =
          (requestedEmail && requestedEmail !== cachedEmail) ||
          (!requestedEmail && requestedWebsite && requestedWebsite !== cachedWebsite);
        if (!hasNewIdentity) return cached;
      }
    }

    if (!email && !website) return null;
    try {
      return await fetchContext({ email, website });
    } catch (_) {
      return null;
    }
  }

  function scoreServiceItem(item, context) {
    let score = 0;
    const reasons = [];
    if (!item || !context) return score;
    const priorities = normalizeTokens(context.priorities);
    const segments = normalizeTokens(context.segments);
    const ctxText = contextTokens(context);
    const text = [item.slug, item.title, item.hint, (item.tags || []).join(' ')].join(' ').toLowerCase();

    if (priorities.includes('seo') && /seo|google|geo|chatgpt|discover|découvr/.test(text)) { score += 40; reasons.push('SEO/visibilité'); }
    if (priorities.includes('ai') && /ia|ai|assistant|chatbot|automatisation|automation/.test(text)) { score += 36; reasons.push('IA/automatisation'); }
    if (priorities.includes('api') && /api|webhook|backend|intégration|integration/.test(text)) { score += 30; reasons.push('intégration API'); }
    if (priorities.includes('crm') && /crm|support client|email|commercial/.test(text)) { score += 24; reasons.push('gestion prospects/CRM'); }
    if (priorities.includes('automation') && /automatisation|automation|outil|migration|intégration|integration/.test(text)) { score += 26; reasons.push('gains de productivité'); }

    if (segments.includes('pme') && /maintenance|crm|support|site|seo/.test(text)) { score += 12; reasons.push('adapté PME'); }
    if (segments.includes('ecommerce') && /chatbot|seo|site|api|webhook/.test(text)) { score += 14; reasons.push('adapté e-commerce'); }
    if (segments.includes('local-business') && /vitrine|seo|identité|identite/.test(text)) { score += 16; reasons.push('adapté activité locale'); }

    if (/saas|logiciel|software/.test(ctxText) && /api|backend|crm|automatisation|automation/.test(text)) {
      score += 10;
      reasons.push('cohérent avec une activité SaaS');
    }
    if (/artisan|commerce|restaurant|coiffeur|local/.test(ctxText) && /vitrine|seo|identité|identite/.test(text)) {
      score += 10;
      reasons.push('cohérent avec un commerce local');
    }

    if (item.slug === 'besoin_a_preciser' || item.slug === 'projet_sur_mesure') score += 5;
    return { score, reasons: Array.from(new Set(reasons)) };
  }

  function rankServices(items, context) {
    const list = toArray(items).map((item) => {
      const rated = scoreServiceItem(item, context);
      return {
        ...item,
        _personalizationScore: rated.score || 0,
        _personalizationReasons: rated.reasons || []
      };
    });
    return list.sort((a, b) => (b._personalizationScore || 0) - (a._personalizationScore || 0));
  }

  function scoreProjectItem(project, context) {
    let score = 0;
    const reasons = [];
    if (!project || !context) return { score, reasons };
    const priorities = normalizeTokens(context.priorities);
    const segments = normalizeTokens(context.segments);
    const ctxText = contextTokens(context);
    const text = [
      project.title, project.description, project.category,
      toArray(project.technologies).join(' ')
    ].join(' ').toLowerCase();
    const id = String(project.id || '').toLowerCase();
    const title = String(project.title || '').toLowerCase();

    if (priorities.includes('seo') && /seo|marketing|visibilit|site|web/.test(text)) { score += 30; reasons.push('SEO/visibilité'); }
    if (priorities.includes('web') && String(project.category || '').toLowerCase() === 'web') { score += 45; reasons.push('projet web pertinent'); }
    if (priorities.includes('ai') && /ia|ai|ml|llm|data|analyse/.test(text)) { score += 36; reasons.push('IA/data'); }
    if (priorities.includes('api') && /api|backend|fastapi|nestjs|node|integration|intégration/.test(text)) { score += 34; reasons.push('API/backend'); }
    if (priorities.includes('automation') && /workflow|automatisation|tool|outil|script/.test(text)) { score += 28; reasons.push('automatisation'); }
    if (segments.includes('pme') && /crm|gestion|dashboard|suivi|saas/.test(text)) { score += 12; reasons.push('adapté PME'); }
    if (segments.includes('ecommerce') && /shop|ecom|conversion|client/.test(text)) { score += 10; reasons.push('adapté e-commerce'); }
    if (/artisan|commerce|restaurant|local/.test(ctxText) && /web|site|seo/.test(text)) { score += 8; reasons.push('adapté activité locale'); }

    // Règles métier explicites pour profils commerce local / e-commerce.
    if (segments.includes('local-business') || segments.includes('ecommerce')) {
      if (/quickbill/.test(id) || /quickbill/.test(title)) {
        score += 40;
        reasons.push('preuve de valeur business rapide');
      }
      if (/clientcrm|client-crm/.test(id) || /crm/.test(title)) {
        score += 44;
        reasons.push('gestion clients/prospects');
      }
      if (/deliverytrack|delivery-track/.test(id) || /delivery/.test(title)) {
        score += 28;
        reasons.push('suivi opérationnel client');
      }
      if (/socialcare-hub|social-care-hub/.test(id) || /socialcare/.test(title)) {
        score += 22;
        reasons.push('plateforme orientée parcours utilisateur');
      }
      if (/restaurationrapide|restauration/.test(id) || /restauration/.test(title)) {
        score += 50;
        reasons.push('cas proche restauration');
      }
      // On évite de sur-prioriser les vitrines "R&D" sur ce persona.
      if (/crypto|nft|cluster|trading|ecodatahub|turfrace/.test(id + ' ' + title)) {
        score -= 18;
      }
    }

    if (project.featured) score += 12;
    return { score, reasons: Array.from(new Set(reasons)) };
  }

  function rankProjects(projects, context) {
    return toArray(projects).map((project) => {
      const rated = scoreProjectItem(project, context);
      return {
        ...project,
        _personalizationScore: rated.score || 0,
        _personalizationReasons: rated.reasons || []
      };
    }).sort((a, b) => (b._personalizationScore || 0) - (a._personalizationScore || 0));
  }

  function scoreArticleItem(article, context) {
    if (!article || !context) return { score: 0, reasons: [] };
    const priorities = normalizeTokens(context.priorities);
    const reasons = [];
    const text = [article.title, article.excerpt, article.type, toArray(article.tags).join(' ')].join(' ').toLowerCase();
    let score = 0;
    if (priorities.includes('seo') && /seo|geo|search|google/.test(text)) { score += 40; reasons.push('SEO/GEO'); }
    if (priorities.includes('ai') && /ia|ai|llm|chatgpt/.test(text)) { score += 34; reasons.push('IA'); }
    if (priorities.includes('api') && /api|backend|graphql|rest/.test(text)) { score += 30; reasons.push('API/backend'); }
    if (priorities.includes('automation') && /automatisation|ci\/cd|devops|workflow/.test(text)) { score += 26; reasons.push('automatisation'); }
    return { score, reasons: Array.from(new Set(reasons)) };
  }

  function rankArticles(articles, context) {
    return toArray(articles).map((article) => {
      const rated = scoreArticleItem(article, context);
      return {
        ...article,
        _personalizationScore: rated.score || 0,
        _personalizationReasons: rated.reasons || []
      };
    }).sort((a, b) => (b._personalizationScore || 0) - (a._personalizationScore || 0));
  }

  function deriveContextFromContentFallback(contentText) {
    return {
      success: true,
      source: 'content-fallback',
      priorities: inferPrioritiesFromText(contentText),
      segments: [],
      confidence: 0.35
    };
  }

  window.Personalization = {
    getContext,
    getTrackedEmail: function () {
      return extractEmailFromLocation() || readStoredEmail();
    },
    rankServices,
    rankProjects,
    rankArticles,
    deriveContextFromContentFallback
  };
})();

