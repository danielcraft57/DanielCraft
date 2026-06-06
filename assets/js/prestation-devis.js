/**
 * Panneau devis fiche prestation : options type e-commerce, total indicatif, envoi Facturio.
 */
(function () {
  'use strict';

  const root = document.querySelector('.prestation-detail-root');
  if (!root) return;

  const form = document.getElementById('prestationDevisForm');
  const feedback = document.getElementById('prestationDevisFeedback');
  const submitBtn = document.getElementById('prestationDevisSubmit');
  const totalEl = document.querySelector('[data-prestation-total]');
  const totalInput = document.querySelector('[data-prestation-total-input]');
  const basePriceEl = document.querySelector('[data-prestation-base-price]');
  const addonsMount = document.querySelector('[data-prestation-addons]');

  const basePrice = parseInt(basePriceEl?.getAttribute('data-prestation-base-price') || '0', 10) || 0;
  let addons = [];

  function parseAddons() {
    if (!addonsMount) return [];
    const raw = addonsMount.getAttribute('data-prestation-addons') || '[]';
    try {
      const parsed = JSON.parse(raw);
      return Array.isArray(parsed) ? parsed : [];
    } catch {
      return [];
    }
  }

  function formatEur(n) {
    return `${n} €`;
  }

  function recalcTotal() {
    let total = basePrice;
    const checked = form?.querySelectorAll('input[name="addon_id[]"]:checked') || [];
    checked.forEach((input) => {
      const price = parseInt(input.getAttribute('data-addon-price') || '0', 10);
      if (!Number.isNaN(price)) total += price;
    });
    if (totalEl) totalEl.textContent = formatEur(total);
    if (totalInput) totalInput.value = String(total);
    return total;
  }

  function renderAddons() {
    addons = parseAddons();
    if (!addonsMount || !addons.length) return;
    addonsMount.hidden = false;
    addonsMount.innerHTML = '';
    const title = document.createElement('p');
    title.className = 'prestation-devis-addons-title';
    title.textContent = 'Options (facultatif)';
    addonsMount.appendChild(title);

    addons.forEach((addon) => {
      if (!addon || !addon.id) return;
      const label = document.createElement('label');
      label.className = 'prestation-devis-addon';
      const input = document.createElement('input');
      input.type = 'checkbox';
      input.name = 'addon_id[]';
      input.value = addon.id;
      input.setAttribute('data-addon-price', String(addon.price_eur || 0));
      input.addEventListener('change', recalcTotal);
      const text = document.createElement('span');
      const price = parseInt(addon.price_eur, 10) || 0;
      text.innerHTML = `<strong>${escapeHtml(addon.title || '')}</strong> (+${price} €)${
        addon.description ? ` — ${escapeHtml(addon.description)}` : ''
      }`;
      label.appendChild(input);
      label.appendChild(text);
      addonsMount.appendChild(label);
    });
  }

  function escapeHtml(s) {
    return String(s)
      .replace(/&/g, '&amp;')
      .replace(/</g, '&lt;')
      .replace(/>/g, '&gt;')
      .replace(/"/g, '&quot;');
  }

  function showFeedback(message, isError) {
    if (!feedback) return;
    feedback.hidden = false;
    feedback.textContent = message;
    feedback.classList.toggle('is-error', !!isError);
    feedback.classList.toggle('is-success', !isError);
  }

  function setLoading(loading) {
    if (!submitBtn) return;
    submitBtn.disabled = loading;
    submitBtn.setAttribute('aria-busy', loading ? 'true' : 'false');
  }

  async function onSubmit(ev) {
    ev.preventDefault();
    if (!form) return;
    if (!form.reportValidity()) return;

    setLoading(true);
    if (feedback) feedback.hidden = true;

    const fd = new FormData(form);
    fd.set('total_eur', String(recalcTotal()));

    try {
      const res = await fetch('/api/request-prestation-devis.php', {
        method: 'POST',
        body: fd,
        credentials: 'same-origin',
        headers: { Accept: 'application/json' },
      });
      const data = await res.json().catch(() => ({}));
      if (res.ok && data.success) {
        showFeedback(
          data.message ||
            'Merci ! Votre demande est enregistrée : consultez votre boîte mail pour le devis.',
          false,
        );
        form.reset();
        recalcTotal();
      } else {
        showFeedback(data.error || 'Envoi impossible. Réessayez ou contactez-nous.', true);
      }
    } catch {
      showFeedback(
        'Connexion au serveur impossible. Utilisez le formulaire de contact sur l’accueil si besoin.',
        true,
      );
    } finally {
      setLoading(false);
    }
  }

  renderAddons();
  recalcTotal();
  form?.addEventListener('submit', onSubmit);
})();
