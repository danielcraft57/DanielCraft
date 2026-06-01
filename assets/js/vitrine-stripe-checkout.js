/**
 * Paiement Stripe Checkout depuis une fiche vitrine (clé publique + POST /api/stripe-create-checkout.php).
 */
(function () {
  'use strict';

  const card = document.querySelector('.vitrine-purchase-card');
  if (!card) return;

  const slug = (card.getAttribute('data-vitrine-slug') || '').trim();
  const pk = (document.querySelector('.vitrine-detail-root') || card).getAttribute('data-stripe-pk') || '';
  const staticUrl = (card.getAttribute('data-stripe-static-url') || '').trim();

  function feedback(el, text, isError) {
    if (!el) return;
    el.hidden = false;
    el.textContent = text;
    el.classList.toggle('vitrine-stripe-feedback--error', !!isError);
    el.classList.toggle('vitrine-stripe-feedback--ok', !isError);
  }

  function setLoading(btn, on) {
    if (!btn) return;
    btn.disabled = on;
    btn.setAttribute('aria-busy', on ? 'true' : 'false');
    const label = btn.querySelector('.vitrine-stripe-btn__label');
    const load = btn.querySelector('.vitrine-stripe-btn__loading');
    if (label) label.hidden = on;
    if (load) load.hidden = !on;
  }

  function hideFeedback(el) {
    if (!el) return;
    el.hidden = true;
    el.textContent = '';
    el.classList.remove('vitrine-stripe-feedback--error', 'vitrine-stripe-feedback--ok');
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
        data: { success: false, error: trimmed.slice(0, 200) || 'HTTP ' + res.status }
      };
    });
  }

  function startCheckout(btn, fb) {
    if (staticUrl) {
      window.location.href = staticUrl;
      return;
    }
    if (!slug) {
      feedback(fb, 'Référence modèle manquante.', true);
      return;
    }
    setLoading(btn, true);
    hideFeedback(fb);

    fetch('/api/stripe-create-checkout.php', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ vitrine_slug: slug })
    })
      .then(parseJsonResponse)
      .then(function (ref) {
        var res = ref.res;
        var data = ref.data;
        if (res.ok && data && data.success && data.url) {
          window.location.href = data.url;
          return;
        }
        feedback(fb, (data && data.error) || 'Impossible d’ouvrir le paiement Stripe.', true);
      })
      .catch(function () {
        feedback(fb, 'Serveur injoignable. Utilisez PHP sur dist/ (php -S … -t dist).', true);
      })
      .finally(function () {
        setLoading(btn, false);
      });
  }

  document.querySelectorAll('[data-vitrine-stripe-checkout]').forEach(function (btn) {
    var fb = btn.parentElement && btn.parentElement.querySelector('.vitrine-stripe-feedback');
    btn.addEventListener('click', function () {
      startCheckout(btn, fb);
    });
  });

  var params = new URLSearchParams(window.location.search);
  var stripeParam = params.get('stripe');
  if (stripeParam === 'success') {
    var banner = document.getElementById('vitrineStripeReturn');
    if (banner) {
      banner.hidden = false;
      banner.textContent = 'Merci — votre paiement Stripe a été enregistré. Je vous contacte sous peu pour la suite.';
      banner.classList.add('vitrine-stripe-return--ok');
    }
  } else if (stripeParam === 'cancel') {
    var bannerCancel = document.getElementById('vitrineStripeReturn');
    if (bannerCancel) {
      bannerCancel.hidden = false;
      bannerCancel.textContent = 'Paiement annulé. Vous pouvez réessayer ou utiliser « Commander » sans paiement immédiat.';
      bannerCancel.classList.add('vitrine-stripe-return--cancel');
    }
  }
})();
