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

  /**
   * Lit les lignes « première année » embarquées dans la fiche.
   * @returns {Array<object>} Lignes de la première année (prix, libellés).
   */
  function parseYear1() {
    const el = root.querySelector('script[data-prestation-year1]');
    if (!el) return [];
    const raw = (el.textContent || '').trim() || '[]';
    try {
      const parsed = JSON.parse(raw);
      return Array.isArray(parsed) ? parsed : [];
    } catch {
      return [];
    }
  }

  /**
   * Somme les montants des lignes première année.
   * @returns {number} Total en euros.
   */
  function year1Amount() {
    return parseYear1().reduce(function (sum, line) {
      const n = parseInt(line && line.price_eur, 10);
      return sum + (Number.isFinite(n) ? n : 0);
    }, 0);
  }

  /**
   * Lit la liste d'options (addons) depuis le DOM.
   * @returns {Array<object>} Options proposées sur la fiche.
   */
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

  /**
   * Formate un montant en euros pour l'affichage.
   * @param {number} n - Montant entier.
   * @returns {string} Libellé « N € ».
   */
  function formatEur(n) {
    return n + ' €';
  }

  /**
   * Recalcule le total (base + première année + options cochées) et synchronise l'UI.
   * @returns {number} Total en euros.
   */
  function recalcTotal() {
    let total = basePrice + year1Amount();
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

  /**
   * Met à jour le prix porté par les boutons « Demander un devis ».
   * @param {number} total - Nouveau total.
   * @returns {void}
   */
  function syncModalTriggers(total) {
    root.querySelectorAll('[data-prestation-devis-open]').forEach(function (btn) {
      btn.setAttribute('data-prestation-price', String(total));
    });
    const hiddenTotal = document.getElementById('prestationDevisDialogTotal');
    if (hiddenTotal && document.getElementById('prestationDevisDialog')?.open) {
      hiddenTotal.value = String(total);
    }
  }

  /**
   * Échappe le HTML pour insertion sûre dans le DOM.
   * @param {string} s - Texte brut.
   * @returns {string} Texte échappé.
   */
  function escapeHtml(s) {
    return String(s)
      .replace(/&/g, '&amp;')
      .replace(/</g, '&lt;')
      .replace(/>/g, '&gt;')
      .replace(/"/g, '&quot;');
  }

  /**
   * Affiche les cases à cocher d'options (addons) sous le prix.
   * @returns {void}
   */
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
      text.innerHTML =
        '<strong>' +
        escapeHtml(addon.title || '') +
        '</strong>' +
        (addon.description ? ' - ' + escapeHtml(addon.description) : '');
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
    const addonLines = [];
    root.querySelectorAll('input[name="addon_id[]"]:checked').forEach(function (input) {
      const label = input.closest('.prestation-devis-addon');
      const strong = label?.querySelector('strong');
      addonLines.push({
        id: input.value,
        title: strong ? strong.textContent.trim() : input.value,
        price: parseInt(input.getAttribute('data-addon-price') || '0', 10) || 0,
      });
    });
    parseYear1().forEach(function (line) {
      if (!line || !line.title) return;
      addonLines.push({
        id: 'year1-' + (line.slug || ''),
        title: line.label || line.title,
        price: parseInt(line.price_eur, 10) || 0,
      });
    });

    modal.open({
      slug: trigger.getAttribute('data-prestation-slug'),
      serviceSlug: trigger.getAttribute('data-service-slug'),
      title: trigger.getAttribute('data-prestation-title'),
      price: String(total),
      basePrice: String(basePrice),
      priceLabel: trigger.getAttribute('data-prestation-price-label'),
      addonIds: addonIds,
      addonLines: addonLines,
    });
  });

  renderAddons();
  recalcTotal();
})();
