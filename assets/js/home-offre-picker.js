/**
 * Modale accueil : choix parmi 3 offres vitrine, puis devis par-dessus.
 */
(function () {
  'use strict';

  const picker = document.getElementById('homeOffrePickerDialog');
  if (!picker || typeof picker.showModal !== 'function') return;

  const closeBtn = document.getElementById('homeOffrePickerClose');
  /** @type {Element|null} */
  let lastFocus = null;

  /**
   * Ouvre la modale de choix d'offre et mémorise le focus.
   * @returns {void}
   */
  function openPicker() {
    lastFocus = document.activeElement;
    if (!picker.open) picker.showModal();
    document.body.classList.add('home-offre-picker-open');
  }

  /**
   * Ferme la modale et restitue le focus précédent.
   * @returns {void}
   */
  function closePicker() {
    if (picker.open) picker.close();
    document.body.classList.remove('home-offre-picker-open');
    if (lastFocus && typeof lastFocus.focus === 'function') lastFocus.focus();
    lastFocus = null;
  }

  /**
   * Parse le JSON des lignes de devis attaché à un bouton d'offre.
   * @param {string|null} raw - Chaîne JSON attendue (tableau de lignes).
   * @returns {Array<object>|null} Lignes parsées, ou null si invalide.
   */
  function parseLines(raw) {
    if (!raw) return null;
    try {
      const parsed = JSON.parse(raw);
      return Array.isArray(parsed) ? parsed : null;
    } catch (e) {
      return null;
    }
  }

  document.addEventListener('click', function (ev) {
    const openTrigger = ev.target.closest('[data-home-offre-picker-open]');
    if (openTrigger) {
      ev.preventDefault();
      openPicker();
      return;
    }

    const choose = ev.target.closest('[data-home-offre-choose]');
    if (!choose || !picker.contains(choose)) return;
    ev.preventDefault();
    ev.stopPropagation();

    const lines = parseLines(choose.getAttribute('data-offre-lines'));
    const ctx = {
      slug: choose.getAttribute('data-prestation-slug') || '',
      serviceSlug: choose.getAttribute('data-service-slug') || '',
      title: choose.getAttribute('data-prestation-title') || 'Prestation',
      price: choose.getAttribute('data-prestation-price') || '',
      basePrice: choose.getAttribute('data-prestation-price') || '',
      lines: lines,
    };

    if (window.prestationDevisModal && typeof window.prestationDevisModal.open === 'function') {
      window.prestationDevisModal.open(ctx);
    }
  });

  closeBtn?.addEventListener('click', closePicker);

  picker.addEventListener('cancel', function (ev) {
    // Si le devis est ouvert par-dessus, laisser le devis gérer Escape.
    const devis = document.getElementById('prestationDevisDialog');
    if (devis && devis.open) {
      ev.preventDefault();
      return;
    }
    closePicker();
  });

  picker.addEventListener('click', function (ev) {
    if (ev.target === picker) {
      const devis = document.getElementById('prestationDevisDialog');
      if (devis && devis.open) return;
      closePicker();
    }
  });

  window.homeOffrePicker = { open: openPicker, close: closePicker };
})();
