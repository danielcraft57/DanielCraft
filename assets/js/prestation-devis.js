/**
 * Fiche prestation : options type e-commerce, total indicatif, ouverture modale devis.
 */
(function () {
  'use strict';

  const root = document.querySelector('.prestation-detail-root');
  if (!root) return;

  const totalEl = document.querySelector('[data-prestation-total]');
  const totalInput = document.querySelector('[data-prestation-total-input]');
  const basePriceEl = document.querySelector('[data-prestation-base-price]');
  const addonsMount = document.querySelector('[data-prestation-addons]');

  const basePrice = parseInt(basePriceEl?.getAttribute('data-prestation-base-price') || '0', 10) || 0;

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
    return n + ' €';
  }

  function recalcTotal() {
    let total = basePrice;
    const checked = root.querySelectorAll('input[name="addon_id[]"]:checked') || [];
    checked.forEach(function (input) {
      const price = parseInt(input.getAttribute('data-addon-price') || '0', 10);
      if (!Number.isNaN(price)) total += price;
    });
    if (totalEl) totalEl.textContent = formatEur(total);
    if (totalInput) totalInput.value = String(total);
    syncModalTriggers(total);
    return total;
  }

  function syncModalTriggers(total) {
    root.querySelectorAll('[data-prestation-devis-open]').forEach(function (btn) {
      btn.setAttribute('data-prestation-price', String(total));
    });
    const hiddenTotal = document.getElementById('prestationDevisDialogTotal');
    if (hiddenTotal && document.getElementById('prestationDevisDialog')?.open) {
      hiddenTotal.value = String(total);
    }
  }

  function escapeHtml(s) {
    return String(s)
      .replace(/&/g, '&amp;')
      .replace(/</g, '&lt;')
      .replace(/>/g, '&gt;')
      .replace(/"/g, '&quot;');
  }

  function renderAddons() {
    const addons = parseAddons();
    if (!addonsMount || !addons.length) return;
    addonsMount.hidden = false;
    addonsMount.innerHTML = '';
    const title = document.createElement('p');
    title.className = 'prestation-devis-addons-title';
    title.textContent = 'Options (facultatif)';
    addonsMount.appendChild(title);

    addons.forEach(function (addon) {
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
      text.innerHTML =
        '<strong>' +
        escapeHtml(addon.title || '') +
        '</strong> (+' +
        price +
        ' €)' +
        (addon.description ? ' — ' + escapeHtml(addon.description) : '');
      label.appendChild(input);
      label.appendChild(text);
      addonsMount.appendChild(label);
    });
  }

  document.addEventListener('click', function (ev) {
    const trigger = ev.target.closest('.prestation-detail-root [data-prestation-devis-open]');
    if (!trigger) return;
    const total = recalcTotal();
    const modal = window.prestationDevisModal;
    if (!modal || typeof modal.open !== 'function') return;
    ev.preventDefault();
    ev.stopImmediatePropagation();
    const addonIds = [];
    root.querySelectorAll('input[name="addon_id[]"]:checked').forEach(function (input) {
      addonIds.push(input.value);
    });
    modal.open({
      slug: trigger.getAttribute('data-prestation-slug'),
      serviceSlug: trigger.getAttribute('data-service-slug'),
      title: trigger.getAttribute('data-prestation-title'),
      price: String(total),
      priceLabel: trigger.getAttribute('data-prestation-price-label'),
      addonIds: addonIds,
    });
  });

  renderAddons();
  recalcTotal();
})();
