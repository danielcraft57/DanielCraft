/**
 * Page /audit — formulaire unifié (gratuit + premium) + paiement Stripe.
 */
(function () {
  'use strict';

  const root = document.querySelector('.page-audit');
  if (!root) return;

  const stripePk = (root.getAttribute('data-stripe-pk') || '').trim();
  const premiumCard = document.querySelector('.audit-offer-card--premium');
  const auditSlug = premiumCard
    ? (premiumCard.getAttribute('data-audit-slug') || 'audit-complet-ia').trim()
    : 'audit-complet-ia';

  const STORAGE_KEY = 'danielcraft_audit_paid_pending';
  let auditMode = 'free';

  const unifiedForm = document.getElementById('auditUnifiedForm');
  const unifiedUrl = document.getElementById('auditUnifiedUrl');
  const unifiedEmail = document.getElementById('auditUnifiedEmail');
  const unifiedName = document.getElementById('auditUnifiedName');
  const unifiedFeedback = document.getElementById('auditUnifiedFeedback');
  const successPanel = document.getElementById('auditSuccessPanel');
  const successLead = document.getElementById('auditSuccessLead');
  const freeSubmit = document.getElementById('auditUnifiedSubmitFree');
  const premiumSubmit = document.getElementById('auditUnifiedSubmitPremium');
  const payNote = document.getElementById('auditUnifiedPayNote');
  const testBtn = document.getElementById('auditUnifiedTestBtn');
  const modeTabs = document.querySelectorAll('[data-audit-mode]');

  function normalizeUrl(raw) {
    var s = (raw || '').trim();
    if (!s) return null;
    if (!/^https?:\/\//i.test(s)) s = 'https://' + s.replace(/^\/+/, '');
    try {
      var u = new URL(s);
      if (u.protocol !== 'http:' && u.protocol !== 'https:') return null;
      return u.toString();
    } catch (e) {
      return null;
    }
  }

  function openAnalysePreview(urlInput) {
    var url = normalizeUrl(urlInput && urlInput.value);
    if (!url) {
      alert('Indiquez une URL valide (ex. https://exemple.com).');
      return;
    }
    window.location.href = '/analyse?website=' + encodeURIComponent(url) + '&full=1';
  }

  function setFeedback(el, message, isError) {
    if (!el) return;
    if (!message) {
      el.hidden = true;
      el.textContent = '';
      return;
    }
    el.hidden = false;
    el.textContent = message;
    el.className = 'form-feedback' + (isError ? ' form-feedback--error' : ' form-feedback--success');
  }

  function setSubmitLoading(btn, on) {
    if (!btn) return;
    btn.disabled = on;
    btn.classList.toggle('is-loading', on);
  }

  function parseJsonResponse(res) {
    return res.text().then(function (text) {
      var trimmed = (text || '').trim();
      if (trimmed.charAt(0) === '{') {
        try {
          return { res: res, data: JSON.parse(text) };
        } catch (e) {
          return { res: res, data: { success: false, error: 'Réponse serveur illisible.' } };
        }
      }
      return { res: res, data: { success: false, error: trimmed.slice(0, 200) || 'HTTP ' + res.status } };
    });
  }

  function showAuditSuccess(message, email) {
    if (unifiedForm) unifiedForm.hidden = true;
    if (successPanel) {
      successPanel.hidden = false;
      if (successLead) {
        successLead.textContent =
          message ||
          (email
            ? '3 priorités pour votre site — envoyées à ' + email + ' sous 48 h ouvrées.'
            : '3 priorités pour votre site — livraison sous 48 h ouvrées.');
      }
    }
    setFeedback(unifiedFeedback, '', false);
  }

  function hideAuditSuccess() {
    if (unifiedForm) unifiedForm.hidden = false;
    if (successPanel) successPanel.hidden = true;
  }

  function setAuditMode(mode) {
    hideAuditSuccess();
    auditMode = mode === 'premium' ? 'premium' : 'free';
    modeTabs.forEach(function (tab) {
      var on = tab.getAttribute('data-audit-mode') === auditMode;
      tab.classList.toggle('is-active', on);
      tab.setAttribute('aria-selected', on ? 'true' : 'false');
    });
    if (freeSubmit) freeSubmit.hidden = auditMode !== 'free';
    if (premiumSubmit) premiumSubmit.hidden = auditMode !== 'premium';
    if (payNote) payNote.hidden = auditMode !== 'premium';
    setFeedback(unifiedFeedback, '', false);
  }

  modeTabs.forEach(function (tab) {
    tab.addEventListener('click', function () {
      setAuditMode(tab.getAttribute('data-audit-mode'));
    });
  });

  if (testBtn && unifiedUrl) {
    testBtn.addEventListener('click', function () {
      openAnalysePreview(unifiedUrl);
    });
  }

  function readFormValues() {
    return {
      url: normalizeUrl(unifiedUrl && unifiedUrl.value),
      email: (unifiedEmail && unifiedEmail.value || '').trim(),
      name: (unifiedName && unifiedName.value || '').trim(),
    };
  }

  function submitFreeAudit() {
    var vals = readFormValues();
    if (!vals.url) {
      setFeedback(unifiedFeedback, 'URL du site invalide.', true);
      return;
    }
    if (!vals.email || !/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(vals.email)) {
      setFeedback(unifiedFeedback, 'Email invalide.', true);
      return;
    }

    setSubmitLoading(freeSubmit, true);
    setFeedback(unifiedFeedback, '', false);

    fetch('/api/request-free-audit.php', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ website: vals.url, email: vals.email }),
    })
      .then(parseJsonResponse)
      .then(function (ref) {
        if (ref.res.ok && ref.data && ref.data.success) {
          showAuditSuccess(
            (ref.data && ref.data.message) || null,
            vals.email
          );
          if (unifiedForm) unifiedForm.reset();
          return;
        }
        var errMsg = (ref.data && ref.data.error) || 'Envoi impossible. Réessayez ou contactez-nous.';
        if (ref.res.status === 429) {
          errMsg =
            (ref.data && ref.data.error) ||
            'Vous avez déjà demandé un audit récemment. Réessayez plus tard.';
        }
        setFeedback(unifiedFeedback, errMsg, true);
      })
      .catch(function () {
        setFeedback(unifiedFeedback, 'Serveur injoignable. Vérifiez que PHP tourne sur dist/.', true);
      })
      .finally(function () {
        setSubmitLoading(freeSubmit, false);
      });
  }

  function startPaidCheckout() {
    var vals = readFormValues();
    if (!vals.url) {
      setFeedback(unifiedFeedback, 'URL du site invalide.', true);
      return;
    }
    if (!vals.email || !/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(vals.email)) {
      setFeedback(unifiedFeedback, 'Email invalide.', true);
      return;
    }

    try {
      sessionStorage.setItem(
        STORAGE_KEY,
        JSON.stringify({
          site_url: vals.url,
          email: vals.email,
          name: vals.name || 'Client audit IA',
        })
      );
    } catch (err) {
      /* ignore */
    }

    setSubmitLoading(premiumSubmit, true);
    setFeedback(unifiedFeedback, '', false);

    fetch('/api/stripe-create-audit-checkout.php', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        audit_slug: auditSlug,
        email: vals.email,
        site_url: vals.url,
        name: vals.name,
      }),
    })
      .then(parseJsonResponse)
      .then(function (ref) {
        if (ref.res.ok && ref.data && ref.data.success && ref.data.url) {
          window.location.href = ref.data.url;
          return;
        }
        setFeedback(
          unifiedFeedback,
          (ref.data && ref.data.error) || 'Impossible d’ouvrir le paiement Stripe.',
          true
        );
      })
      .catch(function () {
        setFeedback(unifiedFeedback, 'Serveur injoignable.', true);
      })
      .finally(function () {
        setSubmitLoading(premiumSubmit, false);
      });
  }

  if (unifiedForm) {
    unifiedForm.addEventListener('submit', function (e) {
      e.preventDefault();
      if (auditMode === 'premium') startPaidCheckout();
      else submitFreeAudit();
    });
  }

  if (premiumSubmit) {
    premiumSubmit.addEventListener('click', function (e) {
      e.preventDefault();
      setAuditMode('premium');
      startPaidCheckout();
    });
  }

  setAuditMode('free');

  function confirmPaidOrderAfterStripe() {
    var raw;
    try {
      raw = sessionStorage.getItem(STORAGE_KEY);
    } catch (e) {
      return;
    }
    if (!raw) return;

    var data;
    try {
      data = JSON.parse(raw);
    } catch (e) {
      return;
    }

    var sessionId = '';
    try {
      sessionId = (params.get('session_id') || '').trim();
    } catch (e) {
      /* ignore */
    }

    fetch('/api/request-paid-audit.php', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        website: data.site_url || '',
        email: data.email || '',
        stripe_session_id: sessionId,
      }),
    })
      .then(function (res) {
        return res.json().then(function (body) {
          return { res: res, body: body };
        });
      })
      .then(function (ref) {
        var banner = document.getElementById('auditStripeReturn');
        if (!banner) return;
        banner.hidden = false;
        if (ref.res.ok && ref.body && ref.body.success) {
          banner.textContent =
            ref.body.message ||
            'Merci ! Facture envoyée par email, puis lancement de l’audit complet.';
          banner.className = 'audit-stripe-return audit-stripe-return--ok';
        } else {
          banner.textContent =
            (ref.body && ref.body.error) ||
            'Le paiement est enregistré mais la finalisation a échoué. Écrivez-nous à contact@danielcraft.fr avec votre email.';
          banner.className = 'audit-stripe-return audit-stripe-return--error';
        }
      })
      .catch(function () {
        var banner = document.getElementById('auditStripeReturn');
        if (!banner) return;
        banner.hidden = false;
        banner.textContent =
          'Connexion interrompue après le paiement. Rechargez cette page ou contactez-nous : contact@danielcraft.fr';
        banner.className = 'audit-stripe-return audit-stripe-return--error';
      })
      .finally(function () {
        try {
          sessionStorage.removeItem(STORAGE_KEY);
        } catch (e) {
          /* ignore */
        }
      });
  }

  var params = new URLSearchParams(window.location.search);
  var stripeParam = params.get('stripe');
  var returnBanner = document.getElementById('auditStripeReturn');

  if (stripeParam === 'success') {
    if (returnBanner) {
      returnBanner.hidden = false;
      returnBanner.textContent = 'Paiement reçu — finalisation de votre commande en cours…';
      returnBanner.className = 'audit-stripe-return audit-stripe-return--pending';
    }
    confirmPaidOrderAfterStripe();
  } else if (stripeParam === 'cancel') {
    if (returnBanner) {
      returnBanner.hidden = false;
      returnBanner.textContent = 'Paiement annulé. Vous pouvez réessayer quand vous le souhaitez.';
      returnBanner.classList.add('audit-stripe-return--cancel');
    }
  }
})();
