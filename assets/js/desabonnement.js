// ===== Désabonnement - Page /desabonnement =====

(function () {
  const ENDPOINT = '/api/unsubscribe.php';
  const STATUS_ENDPOINT = '/api/unsubscribe-status.php';

  const els = {
    website: document.getElementById('plUnsubWebsite'),
    feedback: document.getElementById('plUnsubFeedback'),
    btn: document.getElementById('plUnsubBtn'),
    skipBtn: document.getElementById('plUnsubSkipBtn'),
    noteOtherWrap: document.getElementById('plUnsubNoteOtherWrap'),
    noteOther: document.getElementById('plUnsubNoteOther'),
    loading: document.getElementById('plUnsubLoading'),
    already: document.getElementById('plUnsubAlready'),
    notFound: document.getElementById('plUnsubNotFound'),
    form: document.getElementById('plUnsubForm'),
    success: document.getElementById('plUnsubSuccess'),
    successText: document.getElementById('plUnsubSuccessText'),
    statusPill: document.getElementById('plUnsubStatusPill')
  };

  if (!els.website || !els.btn) return;

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
    els.btn.disabled = isLoading;
    els.btn.classList.toggle('is-loading', isLoading);
    // Ne pas écraser le HTML du bouton (spinner)
    els.btn.setAttribute('aria-busy', isLoading ? 'true' : 'false');
  }

  function show(el, visible) {
    if (!el) return;

    if (visible) {
      el.hidden = false;
      el.style.display = '';
      // animation
      requestAnimationFrame(() => el.classList.add('is-active'));
      return;
    }

    // hide with transition
    el.classList.remove('is-active');
    window.setTimeout(() => {
      el.hidden = true;
      el.style.display = 'none';
    }, 220);
  }

  function setPill(kind, text) {
    if (!els.statusPill) return;
    els.statusPill.className = 'unsub-pill ' + (kind ? `unsub-pill--${kind}` : '');
    els.statusPill.textContent = text || '';
  }

  function safeWebsite(raw) {
    try {
      const s = String(raw || '').trim();
      if (!s) return null;

      // URL complète
      try {
        const u = new URL(s);
        if (!['http:', 'https:'].includes(u.protocol)) return null;
        return u.toString();
      } catch {
        // domaine nu
      }

      // Domaine nu (sans chemin)
      if (!/^[a-z0-9.-]+\.[a-z]{2,}$/i.test(s)) return null;
      return s;
    } catch {
      return null;
    }
  }

  function readParams() {
    const q = new URLSearchParams(window.location.search);
    const website = q.get('website') || q.get('url') || '';
    return { website };
  }

  function getSelectedNote() {
    const checked = document.querySelector('input[name="plUnsubNote"]:checked');
    if (!checked) return null;

    const value = checked.value;
    if (value === 'other') {
      const custom = (els.noteOther?.value || '').trim();
      return custom ? custom : '';
    }

    return value ? String(value) : '';
  }

  function noteToUiSummary(note) {
    if (!note) return '';
    const s = String(note);
    return s.length > 140 ? (s.slice(0, 140) + '…') : s;
  }

  function updateOtherVisibility() {
    const checked = document.querySelector('input[name="plUnsubNote"]:checked');
    const isOther = checked && checked.value === 'other';
    if (!els.noteOtherWrap) return;
    if (isOther) els.noteOtherWrap.hidden = false;
    else els.noteOtherWrap.hidden = true;
  }

  async function callStatus({ website }) {
    const u = new URL(STATUS_ENDPOINT, window.location.origin);
    u.searchParams.set('website', website);
    const res = await fetch(u.toString(), { method: 'GET' });
    const data = await res.json().catch(() => ({}));
    if (!res.ok) {
      const msg = data?.error || data?.message || `Erreur API (${res.status})`;
      throw new Error(msg);
    }
    return data;
  }

  async function callUnsubscribe({ website, note }) {
    const u = new URL(ENDPOINT, window.location.origin);
    u.searchParams.set('website', website);
    if (note) u.searchParams.set('note', note);

    const res = await fetch(u.toString(), { method: 'GET' });
    const data = await res.json().catch(() => ({}));
    if (!res.ok) {
      const msg = data?.error || data?.message || `Erreur API (${res.status})`;
      throw new Error(msg);
    }
    return data;
  }

  async function run() {
    setFeedback('', false);
    const { website: rawWebsite } = readParams();
    const website = safeWebsite(rawWebsite);

    els.website.textContent = website ? website : (rawWebsite || '—');

    if (!website) {
      setFeedback('Lien invalide : paramètre "website" manquant ou incorrect.', true);
      els.btn.disabled = true;
      show(els.loading, false);
      show(els.form, false);
      show(els.already, false);
      show(els.notFound, false);
      show(els.success, false);
      setPill('bad', 'Lien invalide');
      return;
    }

    show(els.loading, true);
    show(els.already, false);
    show(els.notFound, false);
    show(els.form, false);
    show(els.success, false);
    setPill('warn', 'Vérification…');

    try {
      const st = await callStatus({ website });
      const already = !!st?.already_unsubscribed;
      show(els.loading, false);

      if (already) {
        show(els.already, true);
        show(els.notFound, false);
        show(els.form, false);
        show(els.success, false);
        setPill('ok', 'Déjà désabonné');
        return;
      }

      show(els.form, true);
      setPill('', 'Action requise');
    } catch (e) {
      show(els.loading, false);
      const msg = (e && e.message) ? String(e.message) : 'Impossible de vérifier le statut.';

      // Entreprise introuvable -> on masque le formulaire
      if (msg.toLowerCase().includes('entreprise introuvable')) {
        setFeedback('', true);
        show(els.form, false);
        show(els.already, false);
        show(els.success, false);
        show(els.notFound, true);
        setPill('bad', 'Introuvable');
        return;
      }

      setFeedback(msg, true);
      // Statut inconnu -> on laisse l'utilisateur se désabonner
      show(els.form, true);
      setPill('warn', 'Statut inconnu');
    }

    updateOtherVisibility();
    document.querySelectorAll('input[name="plUnsubNote"]').forEach((r) => {
      r.addEventListener('change', updateOtherVisibility);
    });

    async function doUnsubscribe(note) {
      setLoading(true);
      try {
        await callUnsubscribe({ website, note });
        const summary = noteToUiSummary(note);
        if (els.successText) {
          els.successText.textContent = summary
            ? `Votre demande a bien été prise en compte. Motif enregistré : ${summary}`
            : 'Votre demande a bien été prise en compte.';
        }
        setFeedback('', false);
        show(els.form, false);
        show(els.already, false);
        show(els.success, true);
        setPill('ok', 'Désabonné');
      } catch (e) {
        const msg = (e && e.message) ? String(e.message) : 'Erreur inconnue.';
        if (msg.toLowerCase().includes('entreprise introuvable')) {
          setFeedback('', true);
          show(els.form, false);
          show(els.already, false);
          show(els.success, false);
          show(els.notFound, true);
          setPill('bad', 'Introuvable');
          return;
        }
        setFeedback(msg, true);
      } finally {
        setLoading(false);
      }
    }

    els.btn.onclick = async () => {
      const note = getSelectedNote();
      if (note === null) {
        setFeedback('Veuillez choisir un motif, ou cliquer sur “Continuer sans motif”.', true);
        return;
      }
      await doUnsubscribe(note);
    };

    if (els.skipBtn) {
      els.skipBtn.onclick = async () => {
        await doUnsubscribe('');
      };
    }
  }

  run();
})();

