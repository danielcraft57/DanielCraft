/**
 * Page /audit — formulaire gratuit + paiement Stripe audit complet IA.
 */
(function () {
  'use strict';

  const root = document.querySelector('.page-audit');
  if (!root) return;

  const stripePk = (root.getAttribute('data-stripe-pk') || '').trim();
  const paidCard = document.querySelector('.audit-form-card--paid');
  const auditSlug = paidCard ? (paidCard.getAttribute('data-audit-slug') || 'audit-complet-ia').trim() : 'audit-complet-ia';

  const STORAGE_KEY = 'danielcraft_audit_paid_pending';

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

  /* ——— Test URL (loupe) ——— */
  var freeTestBtn = document.getElementById('auditFreeTestBtn');
  var freeUrl = document.getElementById('auditFreeUrl');
  if (freeTestBtn && freeUrl) {
    freeTestBtn.addEventListener('click', function () { openAnalysePreview(freeUrl); });
  }
  var paidTestBtn = document.getElementById('auditPaidTestBtn');
  var paidUrl = document.getElementById('auditPaidUrl');
  if (paidTestBtn && paidUrl) {
    paidTestBtn.addEventListener('click', function () { openAnalysePreview(paidUrl); });
  }

  /* ——— Audit gratuit ——— */
  var freeForm = document.getElementById('auditFreeForm');
  var freeSubmit = document.getElementById('auditFreeSubmit');
  var freeFeedback = document.getElementById('auditFreeFeedback');

  if (freeForm) {
    freeForm.addEventListener('submit', function (e) {
      e.preventDefault();
      var url = normalizeUrl(document.getElementById('auditFreeUrl').value);
      var email = (document.getElementById('auditFreeEmail').value || '').trim();
      var name = (document.getElementById('auditFreeName').value || '').trim();

      if (!url) {
        setFeedback(freeFeedback, 'URL du site invalide.', true);
        return;
      }
      if (!email || !/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email)) {
        setFeedback(freeFeedback, 'Email invalide.', true);
        return;
      }

      setSubmitLoading(freeSubmit, true);
      setFeedback(freeFeedback, '', false);

      fetch('/api/request-free-audit.php', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ website: url, email: email })
      })
        .then(parseJsonResponse)
        .then(function (ref) {
          if (ref.res.ok && ref.data && ref.data.success) {
            setFeedback(
              freeFeedback,
              (ref.data && ref.data.message) ||
                'Merci ! Votre audit arrive dans votre boîte mail sous 48 h.',
              false
            );
            freeForm.reset();
            return;
          }
          var errMsg = (ref.data && ref.data.error) || 'Envoi impossible. Réessayez ou contactez-nous.';
          if (ref.res.status === 429) {
            errMsg = (ref.data && ref.data.error) || 'Vous avez déjà demandé un audit récemment. Réessayez plus tard.';
          }
          setFeedback(freeFeedback, errMsg, true);
        })
        .catch(function () {
          setFeedback(freeFeedback, 'Serveur injoignable. Vérifiez que PHP tourne sur dist/.', true);
        })
        .finally(function () {
          setSubmitLoading(freeSubmit, false);
        });
    });
  }

  /* ——— Stripe audit payant ——— */
  var paidStripeBtn = document.getElementById('auditPaidStripeBtn');
  var paidStripeFb = document.getElementById('auditPaidStripeFeedback');

  function stripeFeedback(text, isError) {
    if (!paidStripeFb) return;
    paidStripeFb.hidden = false;
    paidStripeFb.textContent = text;
    paidStripeFb.className = 'form-feedback audit-stripe-feedback' + (isError ? ' audit-stripe-feedback--error' : ' audit-stripe-feedback--ok');
  }

  function startPaidCheckout() {
    var url = normalizeUrl(document.getElementById('auditPaidUrl').value);
    var email = (document.getElementById('auditPaidEmail').value || '').trim();
    var name = (document.getElementById('auditPaidName').value || '').trim();

    if (!url) {
      stripeFeedback('URL du site invalide.', true);
      return;
    }
    if (!email || !/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email)) {
      stripeFeedback('Email invalide.', true);
      return;
    }

    try {
      sessionStorage.setItem(
        STORAGE_KEY,
        JSON.stringify({ site_url: url, email: email, name: name || 'Client audit IA' })
      );
    } catch (err) { /* ignore */ }

    setSubmitLoading(paidStripeBtn, true);
    paidStripeFb.hidden = true;

    fetch('/api/stripe-create-audit-checkout.php', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        audit_slug: auditSlug,
        email: email,
        site_url: url,
        name: name
      })
    })
      .then(parseJsonResponse)
      .then(function (ref) {
        if (ref.res.ok && ref.data && ref.data.success && ref.data.url) {
          window.location.href = ref.data.url;
          return;
        }
        stripeFeedback((ref.data && ref.data.error) || 'Impossible d’ouvrir le paiement Stripe.', true);
      })
      .catch(function () {
        stripeFeedback('Serveur injoignable.', true);
      })
      .finally(function () {
        setSubmitLoading(paidStripeBtn, false);
      });
  }

  if (paidStripeBtn) {
    paidStripeBtn.addEventListener('click', startPaidCheckout);
  }

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
    } catch (e) { /* ignore */ }

    fetch('/api/request-paid-audit.php', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        website: data.site_url || '',
        email: data.email || '',
        stripe_session_id: sessionId
      })
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
            (ref.body.message ||
              'Merci ! Facture envoyée par email, puis lancement de l’audit complet.') +
            '';
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
        } catch (e) { /* ignore */ }
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
