/**
 * Paiement Stripe Checkout depuis une fiche livre PDF.
 */
(function () {
  'use strict';

  const root = document.querySelector('.livre-detail-root');
  if (!root) return;

  const slug = (root.getAttribute('data-livre-slug') || '').trim();
  const card = document.querySelector('.livre-purchase-card');
  const staticUrl = ((card && card.getAttribute('data-stripe-static-url')) || '').trim();
  const returnEl = document.getElementById('livreStripeReturn');
  const feedbackEl = document.getElementById('livreStripeFeedback');

  function feedback(el, text, isError) {
    if (!el) return;
    el.hidden = false;
    el.textContent = text;
    el.classList.toggle('livre-stripe-feedback--error', !!isError);
    el.classList.toggle('livre-stripe-feedback--ok', !isError);
  }

  function setLoading(btn, on) {
    if (!btn) return;
    btn.disabled = on;
    btn.setAttribute('aria-busy', on ? 'true' : 'false');
    const label = btn.querySelector('.livre-stripe-btn__label');
    const load = btn.querySelector('.livre-stripe-btn__loading');
    if (label) label.hidden = on;
    if (load) load.hidden = !on;
  }

  function sanitizeServerError(text) {
    var raw = String(text || '').trim();
    if (!raw) return 'Paiement indisponible pour le moment.';
    if (/<[a-z][\s\S]*>/i.test(raw) || /Fatal error|curl_init|Stack trace/i.test(raw)) {
      return 'Paiement temporairement indisponible sur ce serveur. Ecris a contact@danielcraft.fr ou reessaie plus tard.';
    }
    return raw.length > 220 ? raw.slice(0, 220) + '…' : raw;
  }

  function parseJsonResponse(res) {
    return res.text().then(function (text) {
      var trimmed = (text || '').trim();
      if (trimmed.charAt(0) === '{') {
        try {
          return { res: res, data: JSON.parse(text) };
        } catch (e) {
          return { res: res, data: { success: false, error: 'Reponse serveur illisible.' } };
        }
      }
      return {
        res: res,
        data: { success: false, error: sanitizeServerError(trimmed) || 'HTTP ' + res.status },
      };
    });
  }

  function startCheckout(btn, fb) {
    if (staticUrl) {
      window.location.href = staticUrl;
      return;
    }
    if (!slug) {
      feedback(fb, 'Reference livre manquante.', true);
      return;
    }
    setLoading(btn, true);
    if (fb) {
      fb.hidden = true;
      fb.textContent = '';
    }

    fetch('/api/stripe-create-livre-checkout.php', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ livre_slug: slug }),
    })
      .then(parseJsonResponse)
      .then(function (ref) {
        var res = ref.res;
        var data = ref.data;
        if (res.ok && data && data.success && data.url) {
          window.location.href = data.url;
          return;
        }
        feedback(fb || feedbackEl, (data && data.error) || 'Paiement indisponible pour le moment.', true);
        setLoading(btn, false);
      })
      .catch(function () {
        feedback(fb || feedbackEl, 'Reseau indisponible. Reessaie ou ecris a contact@danielcraft.fr.', true);
        setLoading(btn, false);
      });
  }

  document.querySelectorAll('[data-livre-stripe-checkout]').forEach(function (btn) {
    btn.addEventListener('click', function () {
      startCheckout(btn, feedbackEl);
    });
  });

  try {
    const params = new URLSearchParams(window.location.search);
    const st = params.get('stripe');
    if (st === 'success') {
      const sessionId = (params.get('session_id') || '').trim();
      const dest =
        '/bouquins/telechargement/' +
        (sessionId
          ? '?stripe=success&session_id=' + encodeURIComponent(sessionId)
          : '');
      window.location.replace(dest);
    } else if (returnEl && st === 'cancel') {
      returnEl.hidden = false;
      returnEl.textContent = 'Paiement annule. Tu peux reessayer quand tu veux.';
    }
  } catch (_) {
    /* ignore */
  }
})();
