/**
 * Modale devis prestation : e-mail + nom → Facturio (attente, succès, erreur).
 */
(function () {
  'use strict';

  const dialog = document.getElementById('prestationDevisDialog');
  if (!dialog || typeof dialog.showModal !== 'function') return;

  const form = document.getElementById('prestationDevisDialogForm');
  const closeBtn = document.getElementById('prestationDevisDialogClose');
  const submitBtn = document.getElementById('prestationDevisDialogSubmit');
  const titleEl = document.getElementById('prestationDevisDialogTitle');
  const subtitleEl = document.getElementById('prestationDevisDialogSubtitle');
  const priceEl = document.getElementById('prestationDevisDialogPrice');
  const slugInput = document.getElementById('prestationDevisDialogSlug');
  const serviceInput = document.getElementById('prestationDevisDialogServiceSlug');
  const totalInput = document.getElementById('prestationDevisDialogTotal');
  const successText = document.getElementById('prestationDevisDialogSuccessText');
  const errorText = document.getElementById('prestationDevisDialogErrorText');
  const successClose = document.getElementById('prestationDevisDialogSuccessClose');
  const errorClose = document.getElementById('prestationDevisDialogErrorClose');
  const retryBtn = document.getElementById('prestationDevisDialogRetry');

  const steps = dialog.querySelectorAll('[data-devis-step]');
  let currentCtx = null;

  function showStep(name) {
    steps.forEach(function (el) {
      const on = el.getAttribute('data-devis-step') === name;
      el.classList.toggle('is-active', on);
      el.setAttribute('aria-hidden', on ? 'false' : 'true');
      if ('inert' in el) el.inert = !on;
    });
  }

  function formatPrice(price, label) {
    const p = parseInt(String(price || ''), 10);
    if (!p || p <= 0) return label || '';
    const lbl = (label || 'Forfait').trim();
    return 'Indicatif · ' + lbl + ' · ' + p + ' € HT';
  }

  function ensureAddonFields(ids) {
    if (!form) return;
    form.querySelectorAll('input[name="addon_id[]"]').forEach(function (el) {
      el.remove();
    });
    (ids || []).forEach(function (id) {
      if (!id) return;
      const input = document.createElement('input');
      input.type = 'hidden';
      input.name = 'addon_id[]';
      input.value = id;
      form.appendChild(input);
    });
  }

  function openModal(ctx) {
    currentCtx = ctx || {};
    const title = (currentCtx.title || 'Prestation').trim();
    const slug = (currentCtx.slug || '').trim();
    const service = (currentCtx.serviceSlug || slug).trim();
    const price = currentCtx.price || '';
    const label = currentCtx.priceLabel || 'Forfait';

    if (slugInput) slugInput.value = slug;
    if (serviceInput) serviceInput.value = service;
    if (totalInput) totalInput.value = String(parseInt(price, 10) || 0);
    ensureAddonFields(currentCtx.addonIds);

    if (titleEl) titleEl.textContent = 'Devis : ' + title;
    if (subtitleEl) {
      subtitleEl.textContent =
        'Indiquez votre e-mail : je crée le devis et vous l\'envoie tout de suite, comme sur une boutique en ligne (sans panier).';
    }
    if (priceEl) {
      const txt = formatPrice(price, label);
      if (txt) {
        priceEl.textContent = txt;
        priceEl.hidden = false;
      } else {
        priceEl.hidden = true;
      }
    }

    if (form) form.reset();
    if (slugInput) slugInput.value = slug;
    if (serviceInput) serviceInput.value = service;
    if (totalInput) totalInput.value = String(parseInt(price, 10) || 0);
    ensureAddonFields(currentCtx.addonIds);

    showStep('form');
    dialog.showModal();
    window.setTimeout(function () {
      const email = document.getElementById('prestationDevisDialogEmail');
      if (email) email.focus();
    }, 80);
  }

  function closeModal() {
    if (dialog.open) dialog.close();
    showStep('form');
    currentCtx = null;
  }

  function setSubmitting(busy) {
    if (!submitBtn) return;
    submitBtn.disabled = busy;
    submitBtn.setAttribute('aria-busy', busy ? 'true' : 'false');
  }

  async function onSubmit(ev) {
    ev.preventDefault();
    if (!form || !form.reportValidity()) return;

    setSubmitting(true);
    showStep('loading');

    const fd = new FormData(form);

    try {
      const res = await fetch('/api/request-prestation-devis.php', {
        method: 'POST',
        body: fd,
        credentials: 'same-origin',
        headers: { Accept: 'application/json' },
      });
      const data = await res.json().catch(function () {
        return {};
      });
      if (res.ok && data.success) {
        if (successText) {
          successText.textContent =
            data.message ||
            'Merci ! Votre devis a été envoyé. Consultez votre boîte mail (et les spams si besoin).';
        }
        showStep('success');
      } else {
        if (errorText) {
          errorText.textContent =
            data.error || 'Le devis n\'a pas pu être envoyé. Réessayez ou contactez contact@danielcraft.fr.';
        }
        showStep('error');
      }
    } catch {
      if (errorText) {
        errorText.textContent =
          'Connexion au serveur impossible. Vérifiez votre réseau ou utilisez le formulaire de contact sur l\'accueil.';
      }
      showStep('error');
    } finally {
      setSubmitting(false);
    }
  }

  document.addEventListener('click', function (ev) {
    const trigger = ev.target.closest('[data-prestation-devis-open]');
    if (!trigger) return;
    if (trigger.closest('.prestation-detail-root')) return;
    ev.preventDefault();
    openModal({
      slug: trigger.getAttribute('data-prestation-slug'),
      serviceSlug: trigger.getAttribute('data-service-slug'),
      title: trigger.getAttribute('data-prestation-title'),
      price: trigger.getAttribute('data-prestation-price'),
      priceLabel: trigger.getAttribute('data-prestation-price-label'),
    });
  });

  closeBtn?.addEventListener('click', closeModal);
  successClose?.addEventListener('click', closeModal);
  errorClose?.addEventListener('click', closeModal);
  retryBtn?.addEventListener('click', function () {
    showStep('form');
    const email = document.getElementById('prestationDevisDialogEmail');
    if (email) email.focus();
  });

  dialog.addEventListener('cancel', function (ev) {
    ev.preventDefault();
    closeModal();
  });

  dialog.addEventListener('click', function (ev) {
    if (ev.target === dialog) closeModal();
  });

  form?.addEventListener('submit', onSubmit);

  window.prestationDevisModal = { open: openModal, close: closeModal };
})();
