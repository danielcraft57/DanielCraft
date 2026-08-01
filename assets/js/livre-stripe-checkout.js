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
      return {
        res: res,
        data: { success: false, error: trimmed.slice(0, 200) || 'HTTP ' + res.status },
      };
    });
  }

  function startCheckout(btn, fb) {
    if (staticUrl) {
      window.location.href = staticUrl;
      return;
    }
    if (!slug) {
      feedback(fb, 'Référence livre manquante.', true);
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
        feedback(fb || feedbackEl, 'Réseau indisponible. Réessaie ou écris à contact@danielcraft.fr.', true);
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
    if (returnEl && st === 'success') {
      returnEl.hidden = false;
      returnEl.textContent =
        'Paiement reçu — je t’envoie le PDF à l’e-mail utilisé pour Stripe (souvent sous 24 h). Merci !';
      returnEl.classList.add('livre-stripe-feedback--ok');
    } else if (returnEl && st === 'cancel') {
      returnEl.hidden = false;
      returnEl.textContent = 'Paiement annulé. Tu peux réessayer quand tu veux.';
    }
  } catch (_) {
    /* ignore */
  }
})();
