/**
 * Modale devis prestation : récap, coordonnées, envoi Facturio.
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
  const recapLines = document.getElementById('prestationDevisDialogRecapLines');
  const totalHtEl = document.getElementById('prestationDevisDialogTotalHt');
  const totalTtcEl = document.getElementById('prestationDevisDialogTotalTtc');
  const slugInput = document.getElementById('prestationDevisDialogSlug');
  const serviceInput = document.getElementById('prestationDevisDialogServiceSlug');
  const totalInput = document.getElementById('prestationDevisDialogTotal');
  const successText = document.getElementById('prestationDevisDialogSuccessText');
  const successEmail = document.getElementById('prestationDevisDialogSuccessEmail');
  const errorText = document.getElementById('prestationDevisDialogErrorText');
  const loadingText = document.getElementById('prestationDevisDialogLoadingText');
  const loadingSteps = document.getElementById('prestationDevisDialogLoadingSteps');
  const successClose = document.getElementById('prestationDevisDialogSuccessClose');
  const errorClose = document.getElementById('prestationDevisDialogErrorClose');
  const retryBtn = document.getElementById('prestationDevisDialogRetry');
  const optionalDetails = document.getElementById('prestationDevisDialogOptional');

  const steps = dialog.querySelectorAll('[data-devis-step]');
  const progressDots = dialog.querySelectorAll('[data-devis-progress]');
  let currentCtx = null;
  let loadingTimer = null;
  let savedForm = null;
  let lastFocusBeforeOpen = null;

  const FOCUSABLE =
    'button:not([disabled]), [href], input:not([disabled]), select:not([disabled]), textarea:not([disabled]), [tabindex]:not([tabindex="-1"])';

  const TVA = 0.2;

  function formatEur(n) {
    const v = Math.round(n);
    return v.toLocaleString('fr-FR') + ' €';
  }

  function parsePrice(val) {
    const p = parseInt(String(val || ''), 10);
    return Number.isFinite(p) && p > 0 ? p : 0;
  }

  function showStep(name) {
    steps.forEach(function (el) {
      const on = el.getAttribute('data-devis-step') === name;
      el.classList.toggle('is-active', on);
      el.setAttribute('aria-hidden', on ? 'false' : 'true');
      if ('inert' in el) el.inert = !on;
    });

    const order = ['form', 'loading', 'done'];
    const stateIndex = name === 'success' ? 2 : name === 'loading' ? 1 : 0;
    progressDots.forEach(function (dot) {
      const key = dot.getAttribute('data-devis-progress');
      const idx = order.indexOf(key || '');
      if (idx < 0) return;
      dot.classList.toggle('is-active', idx === stateIndex);
      dot.classList.toggle('is-done', idx < stateIndex);
    });
  }

  function clearLoadingAnimation() {
    if (loadingTimer) {
      window.clearInterval(loadingTimer);
      loadingTimer = null;
    }
    if (loadingSteps) {
      loadingSteps.querySelectorAll('li').forEach(function (li, i) {
        li.classList.toggle('is-active', i === 0);
        li.classList.remove('is-done');
      });
    }
  }

  function startLoadingAnimation() {
    clearLoadingAnimation();
    const messages = [
      'Vérification de votre demande.',
      'Création du devis avec le détail de la prestation…',
      'Envoi du PDF à votre adresse e-mail…',
    ];
    let idx = 0;
    if (loadingText) loadingText.textContent = messages[0];
    loadingTimer = window.setInterval(function () {
      idx = Math.min(idx + 1, 2);
      if (loadingText) loadingText.textContent = messages[idx];
      if (!loadingSteps) return;
      loadingSteps.querySelectorAll('li').forEach(function (li, i) {
        li.classList.toggle('is-active', i === idx);
        li.classList.toggle('is-done', i < idx);
      });
    }, 1400);
  }

  function renderRecap(ctx) {
    const title = (ctx.title || 'Prestation').trim();
    const basePrice = parsePrice(ctx.basePrice ?? ctx.price);
    const addonLines = Array.isArray(ctx.addonLines) ? ctx.addonLines : [];
    let total = basePrice;
    addonLines.forEach(function (line) {
      total += parsePrice(line.price);
    });
    if (total <= 0 && ctx.price) total = parsePrice(ctx.price);

    if (recapLines) {
      recapLines.innerHTML = '';
      const main = document.createElement('li');
      main.className = 'prestation-devis-dialog__recap-line';
      main.innerHTML =
        '<span>' + escapeHtml(title) + '</span><span>' + formatEur(basePrice) + ' HT</span>';
      recapLines.appendChild(main);
      addonLines.forEach(function (line) {
        if (!line || !line.title) return;
        const li = document.createElement('li');
        li.className = 'prestation-devis-dialog__recap-line';
        li.innerHTML =
          '<span>+ ' +
          escapeHtml(line.title) +
          '</span><span>' +
          formatEur(parsePrice(line.price)) +
          ' HT</span>';
        recapLines.appendChild(li);
      });
    }
    if (totalHtEl) totalHtEl.textContent = formatEur(total);
    if (totalTtcEl) totalTtcEl.textContent = formatEur(Math.round(total * (1 + TVA)));
    if (totalInput) totalInput.value = String(total);
  }

  function escapeHtml(s) {
    return String(s)
      .replace(/&/g, '&amp;')
      .replace(/</g, '&lt;')
      .replace(/>/g, '&gt;')
      .replace(/"/g, '&quot;');
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

  function saveFormState() {
    if (!form) return;
    savedForm = {
      slug: slugInput?.value || '',
      email: form.email?.value || '',
      name: form.name?.value || '',
      phone: form.phone?.value || '',
      company: form.company?.value || '',
      message: form.message?.value || '',
      optionalOpen: optionalDetails?.open || false,
    };
  }

  function restoreFormState() {
    if (!form || !savedForm) return;
    if (form.email) form.email.value = savedForm.email;
    if (form.name) form.name.value = savedForm.name;
    if (form.phone) form.phone.value = savedForm.phone;
    if (form.company) form.company.value = savedForm.company;
    if (form.message) form.message.value = savedForm.message;
    if (optionalDetails) optionalDetails.open = !!savedForm.optionalOpen;
  }

  function openModal(ctx) {
    currentCtx = ctx || {};
    const title = (currentCtx.title || 'Prestation').trim();
    const slug = (currentCtx.slug || '').trim();
    const service = (currentCtx.serviceSlug || slug).trim();
    const price = currentCtx.price || currentCtx.basePrice || '';

    if (slugInput) slugInput.value = slug;
    if (serviceInput) serviceInput.value = service;
    ensureAddonFields(currentCtx.addonIds);

    if (titleEl) titleEl.textContent = title;
    if (subtitleEl) {
      subtitleEl.textContent =
        'Vérifiez le montant ci-dessous, puis indiquez où envoyer le PDF.';
    }

    if (savedForm && savedForm.slug === slug) {
      restoreFormState();
    } else {
      if (form) {
        form.reset();
        form.querySelectorAll('.form-input.is-invalid').forEach(function (input) {
          input.classList.remove('is-invalid');
        });
      }
      if (optionalDetails) optionalDetails.open = false;
    }

    if (slugInput) slugInput.value = slug;
    if (serviceInput) serviceInput.value = service;
    ensureAddonFields(currentCtx.addonIds);

    renderRecap({
      title: title,
      price: price,
      basePrice: currentCtx.basePrice || price,
      addonLines: currentCtx.addonLines,
    });

    showStep('form');
    lastFocusBeforeOpen = document.activeElement;
    dialog.showModal();
    document.body.classList.add('prestation-devis-dialog-open');
    window.setTimeout(function () {
      const email = document.getElementById('prestationDevisDialogEmail');
      if (email && !email.value) email.focus();
      else if (form?.name && !form.name.value) form.name.focus();
    }, 80);
  }

  function trapFocus(ev) {
    if (!dialog.open || ev.key !== 'Tab') return;
    const nodes = dialog.querySelectorAll(FOCUSABLE);
    if (!nodes.length) return;
    const list = Array.from(nodes).filter(function (el) {
      return el.offsetParent !== null || el === document.activeElement;
    });
    if (!list.length) return;
    const first = list[0];
    const last = list[list.length - 1];
    if (ev.shiftKey && document.activeElement === first) {
      ev.preventDefault();
      last.focus();
    } else if (!ev.shiftKey && document.activeElement === last) {
      ev.preventDefault();
      first.focus();
    }
  }

  function closeModal() {
    clearLoadingAnimation();
    if (dialog.open) dialog.close();
    document.body.classList.remove('prestation-devis-dialog-open');
    showStep('form');
    currentCtx = null;
    if (lastFocusBeforeOpen && typeof lastFocusBeforeOpen.focus === 'function') {
      lastFocusBeforeOpen.focus();
    }
    lastFocusBeforeOpen = null;
  }

  function setSubmitting(busy) {
    if (!submitBtn) return;
    submitBtn.disabled = busy;
    submitBtn.setAttribute('aria-busy', busy ? 'true' : 'false');
  }

  function markInvalidFields() {
    if (!form) return false;
    let valid = true;
    form.querySelectorAll('.form-input').forEach(function (input) {
      const ok = input.checkValidity();
      input.classList.toggle('is-invalid', !ok);
      if (!ok) valid = false;
    });
    return valid;
  }

  function clearFieldInvalid(ev) {
    const input = ev.target;
    if (!input || !input.classList || !input.classList.contains('form-input')) return;
    if (input.checkValidity()) input.classList.remove('is-invalid');
  }

  async function onSubmit(ev) {
    ev.preventDefault();
    if (!form || !markInvalidFields() || !form.reportValidity()) return;

    saveFormState();

    setSubmitting(true);
    showStep('loading');
    startLoadingAnimation();

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
      clearLoadingAnimation();

      if (res.ok && data.success) {
        const mail = (form.email?.value || '').trim();
        if (successText) {
          successText.textContent =
            data.message ||
            (data.fallback
              ? 'C’est envoyé — consultez votre boîte mail. Vous recevrez votre devis sous 24 h ouvrées.'
              : 'C’est envoyé — consultez votre boîte mail (vérifiez les spams si besoin).');
        }
        if (successEmail) {
          if (mail) {
            successEmail.hidden = false;
            successEmail.innerHTML =
              'Envoyé à <strong>' + escapeHtml(mail) + '</strong>';
          } else {
            successEmail.hidden = true;
          }
        }
        showStep('success');
      } else {
        if (errorText) {
          errorText.textContent =
            data.error ||
            'Le devis n\'a pas pu être envoyé. Réessayez ou contactez contact@danielcraft.fr.';
        }
        const hint = document.getElementById('prestationDevisDialogErrorHint');
        if (hint) {
          hint.hidden = data.error_code !== 'facturio_unavailable';
        }
        showStep('error');
      }
    } catch {
      clearLoadingAnimation();
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
      basePrice: trigger.getAttribute('data-prestation-base-price') || trigger.getAttribute('data-prestation-price'),
      priceLabel: trigger.getAttribute('data-prestation-price-label'),
    });
  });

  closeBtn?.addEventListener('click', closeModal);
  successClose?.addEventListener('click', closeModal);
  errorClose?.addEventListener('click', closeModal);
  retryBtn?.addEventListener('click', function () {
    restoreFormState();
    showStep('form');
    const email = document.getElementById('prestationDevisDialogEmail');
    if (email) email.focus();
  });

  dialog.addEventListener('cancel', function (ev) {
    ev.preventDefault();
    closeModal();
  });

  dialog.addEventListener('keydown', trapFocus);

  dialog.addEventListener('click', function (ev) {
    if (ev.target === dialog) closeModal();
  });

  dialog.addEventListener('close', function () {
    document.body.classList.remove('prestation-devis-dialog-open');
    clearLoadingAnimation();
  });

  form?.addEventListener('submit', onSubmit);
  form?.addEventListener('input', clearFieldInvalid);
  form?.addEventListener('blur', clearFieldInvalid, true);

  window.prestationDevisModal = { open: openModal, close: closeModal };
})();
