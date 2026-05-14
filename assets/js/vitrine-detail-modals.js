/**
 * Modales fiche vitrine : pré-commande (sans paiement) & devis rapide (type contact).
 */
(function () {
  'use strict';

  const PROJECT_TYPES = [
    { slug: 'web', label: 'Développement Web', icon: 'fa-laptop-code' },
    { slug: 'backend', label: 'Backend & APIs', icon: 'fa-server' },
    { slug: 'mobile', label: 'Application mobile', icon: 'fa-mobile-alt' },
    { slug: 'desktop', label: 'Application desktop', icon: 'fa-desktop' },
    { slug: 'tools', label: 'Outils & automatisation', icon: 'fa-tools' },
    { slug: 'specialized', label: 'Spécialisé (data, finance, IoT…)', icon: 'fa-microchip' },
    { slug: 'learning', label: 'Veille / apprentissage / proto', icon: 'fa-graduation-cap' },
    { slug: 'other', label: 'Autre / à préciser', icon: 'fa-ellipsis-h' }
  ];

  const orderDialog = document.getElementById('vitrineDialogOrder');
  const quoteDialog = document.getElementById('vitrineDialogQuote');
  const orderForm = document.getElementById('vitrineOrderForm');
  const quoteForm = document.getElementById('vitrineQuoteForm');
  const card = document.querySelector('.vitrine-purchase-card');

  if (!orderDialog || !quoteDialog || !orderForm || !quoteForm) return;

  const MSG_STATIC =
    'Le serveur actuel ne traite pas correctement le POST PHP. Lancez le site avec PHP (ex: php -S 127.0.0.1:8000 -t dist).';

  function readVitrineTitle() {
    const el = document.querySelector('.vitrine-detail-title');
    return (el && el.textContent && el.textContent.trim()) || '';
  }

  function readVitrineSlug() {
    return (card && card.getAttribute('data-vitrine-slug')) || '';
  }

  function readVitrinePrice() {
    return (card && card.getAttribute('data-vitrine-price')) || '';
  }

  function showFeedback(el, text, isError) {
    if (!el) return;
    el.hidden = false;
    el.textContent = text;
    el.classList.toggle('vitrine-modal-feedback--error', !!isError);
    el.classList.toggle('vitrine-modal-feedback--ok', !isError);
  }

  function hideFeedback(el) {
    if (!el) return;
    el.hidden = true;
    el.textContent = '';
    el.classList.remove('vitrine-modal-feedback--error', 'vitrine-modal-feedback--ok');
  }

  function renderProjectTypes(mount, hiddenInput, selectedSlug) {
    if (!mount || !hiddenInput) return;
    hiddenInput.value = selectedSlug || '';
    mount.innerHTML = '';
    const row = document.createElement('div');
    row.className = 'contact-type-chips';
    PROJECT_TYPES.forEach(function (pt) {
      const btn = document.createElement('button');
      btn.type = 'button';
      btn.className = 'contact-type-chip';
      btn.setAttribute('data-project-type', pt.slug);
      btn.setAttribute('aria-pressed', pt.slug === selectedSlug ? 'true' : 'false');
      btn.setAttribute('aria-label', 'Type de projet : ' + pt.label);
      if (pt.slug === selectedSlug) btn.classList.add('is-selected');
      btn.innerHTML =
        '<span class="contact-type-chip__icon" aria-hidden="true"><i class="fas ' +
        pt.icon +
        '"></i></span><span class="contact-type-chip__label">' +
        pt.label +
        '</span>';
      btn.addEventListener('click', function () {
        row.querySelectorAll('.contact-type-chip').forEach(function (b) {
          b.classList.remove('is-selected');
          b.setAttribute('aria-pressed', 'false');
        });
        btn.classList.add('is-selected');
        btn.setAttribute('aria-pressed', 'true');
        hiddenInput.value = pt.slug;
      });
      row.appendChild(btn);
    });
    mount.appendChild(row);
  }

  function setProgressItems(items, step) {
    items.forEach(function (li, i) {
      const n = i + 1;
      li.classList.remove('is-todo', 'is-done', 'is-active');
      if (n < step) li.classList.add('is-done');
      else if (n === step) li.classList.add('is-active');
      else li.classList.add('is-todo');
    });
  }

  function setStepVisibility(steps, step, attr) {
    steps.forEach(function (el) {
      const n = parseInt(el.getAttribute(attr), 10);
      const on = n === step;
      el.classList.toggle('is-active', on);
      el.setAttribute('aria-hidden', on ? 'false' : 'true');
    });
  }

  /* ----- Commande ----- */
  const orderFeedback = document.getElementById('vitrineOrderFeedback');
  const orderProgressLis = orderDialog.querySelectorAll('[data-vitrine-order-bar]');
  const orderSteps = orderDialog.querySelectorAll('[data-vitrine-order-step]');
  const orderMount = document.getElementById('vitrineOrderProjectMount');
  const orderProjectType = document.getElementById('vd_order_project_type');
  const orderVitrineTitle = document.getElementById('vd_order_vitrine_title');
  const orderMessage = document.getElementById('vd_order_message');
  const orderNamePost = document.getElementById('vd_order_name_post');
  let orderStep = 1;

  function setOrderStep(n) {
    orderStep = n;
    setStepVisibility(orderSteps, n, 'data-vitrine-order-step');
    setProgressItems(orderProgressLis, n);
    hideFeedback(orderFeedback);
  }

  function syncOrderName() {
    const f = document.getElementById('vd_order_first');
    const l = document.getElementById('vd_order_last');
    const a = ((f && f.value) || '').trim();
    const b = ((l && l.value) || '').trim();
    orderNamePost.value = (a + ' ' + b).trim();
  }

  function validateOrderStep2() {
    if (!orderProjectType.value) {
      showFeedback(orderFeedback, 'Choisissez un type de projet.', true);
      return false;
    }
    return true;
  }

  function validateOrderStep3() {
    syncOrderName();
    const email = (document.getElementById('vd_order_email').value || '').trim();
    const phone = (document.getElementById('vd_order_phone').value || '').trim();
    const billing = (document.getElementById('vd_order_billing').value || '').trim();
    if (!orderNamePost.value) {
      showFeedback(orderFeedback, 'Indiquez prénom et nom.', true);
      return false;
    }
    if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email)) {
      showFeedback(orderFeedback, 'Email invalide.', true);
      return false;
    }
    if (phone.replace(/\D/g, '').length < 8) {
      showFeedback(orderFeedback, 'Téléphone trop court ou invalide.', true);
      return false;
    }
    if (billing.length < 8) {
      showFeedback(orderFeedback, 'Adresse de facturation trop courte.', true);
      return false;
    }
    const urlEl = document.getElementById('vd_order_site_url');
    const rawUrl = (urlEl && urlEl.value.trim()) || '';
    if (rawUrl) {
      let u = rawUrl;
      if (!/^https?:\/\//i.test(u)) u = 'https://' + u.replace(/^\/+/, '');
      try {
        // eslint-disable-next-line no-new
        new URL(u);
      } catch {
        showFeedback(orderFeedback, 'URL du site invalide (laissez vide si inconnu).', true);
        return false;
      }
      urlEl.value = u;
    }
    return true;
  }

  function fillOrderRecap() {
    const recap = document.getElementById('vitrineOrderRecap');
    if (!recap) return;
    const site = (document.getElementById('vd_order_site_url').value || '').trim() || '—';
    const billing = (document.getElementById('vd_order_billing').value || '').trim();
    const notes = (document.getElementById('vd_order_notes').value || '').trim() || '—';
    const pt = PROJECT_TYPES.find(function (x) {
      return x.slug === orderProjectType.value;
    });
    recap.innerHTML =
      '<dl class="vitrine-cta-recap__list">' +
      '<div><dt>Vitrine</dt><dd>' +
      escapeHtml(readVitrineTitle()) +
      '</dd></div>' +
      '<div><dt>Type de projet</dt><dd>' +
      escapeHtml((pt && pt.label) || orderProjectType.value) +
      '</dd></div>' +
      '<div><dt>Contact</dt><dd>' +
      escapeHtml(orderNamePost.value) +
      '<br>' +
      escapeHtml(document.getElementById('vd_order_email').value.trim()) +
      '<br>' +
      escapeHtml(document.getElementById('vd_order_phone').value.trim()) +
      '</dd></div>' +
      '<div><dt>URL du site visée</dt><dd>' +
      escapeHtml(site) +
      '</dd></div>' +
      '<div><dt>Facturation</dt><dd><pre class="vitrine-cta-recap__pre">' +
      escapeHtml(billing) +
      '</pre></dd></div>' +
      '<div><dt>Précisions</dt><dd>' +
      escapeHtml(notes) +
      '</dd></div>' +
      '</dl>';
  }

  function escapeHtml(s) {
    return String(s)
      .replace(/&/g, '&amp;')
      .replace(/</g, '&lt;')
      .replace(/>/g, '&gt;')
      .replace(/"/g, '&quot;');
  }

  function buildOrderMessage() {
    const site = (document.getElementById('vd_order_site_url').value || '').trim() || '—';
    const billing = (document.getElementById('vd_order_billing').value || '').trim();
    const notes = (document.getElementById('vd_order_notes').value || '').trim() || '—';
    const slug = readVitrineSlug();
    const title = readVitrineTitle();
    const price = readVitrinePrice();
    return (
      '--- Pré-commande vitrine (aucun paiement sur le site) ---\n' +
      'Vitrine : ' +
      title +
      ' (slug: ' +
      slug +
      ')\n' +
      'Réf. prix catalogue : ' +
      price +
      ' € HT\n\n' +
      'URL du site visée : ' +
      site +
      '\n\n' +
      'Adresse de facturation :\n' +
      billing +
      '\n\n' +
      'Précisions :\n' +
      notes
    );
  }

  orderDialog.querySelectorAll('[data-vitrine-order-next]').forEach(function (btn) {
    btn.addEventListener('click', function () {
      const from = parseInt(btn.getAttribute('data-vitrine-order-next'), 10);
      if (from === 1) setOrderStep(2);
      else if (from === 2) {
        if (!validateOrderStep2()) return;
        setOrderStep(3);
      } else if (from === 3) {
        if (!validateOrderStep3()) return;
        orderVitrineTitle.value = readVitrineTitle();
        orderMessage.value = buildOrderMessage();
        fillOrderRecap();
        setOrderStep(4);
      }
    });
  });

  orderDialog.querySelectorAll('[data-vitrine-order-back]').forEach(function (btn) {
    btn.addEventListener('click', function () {
      const from = parseInt(btn.getAttribute('data-vitrine-order-back'), 10);
      if (from === 2) setOrderStep(1);
      else if (from === 3) setOrderStep(2);
      else if (from === 4) setOrderStep(3);
    });
  });

  function setSubmitLoading(btn, on) {
    if (!btn) return;
    const t = btn.querySelector('.btn-text');
    const l = btn.querySelector('.btn-loading');
    btn.disabled = on;
    if (t) t.hidden = on;
    if (l) l.hidden = !on;
  }

  orderForm.addEventListener('submit', function (e) {
    e.preventDefault();
    const chk = document.getElementById('vd_order_confirm');
    if (!chk.checked) {
      showFeedback(orderFeedback, 'Merci de cocher la confirmation.', true);
      return;
    }
    syncOrderName();
    orderVitrineTitle.value = readVitrineTitle();
    orderMessage.value = buildOrderMessage();
    hideFeedback(orderFeedback);
    const submitBtn = document.getElementById('vitrineOrderSubmit');
    setSubmitLoading(submitBtn, true);

    const fd = new FormData(orderForm);
    fetch('/api/send-contact.php', { method: 'POST', body: fd })
      .then(function (res) {
        return res.json().then(function (data) {
          return { res: res, data: data };
        });
      })
      .then(function (_ref) {
        const res = _ref.res;
        const data = _ref.data;
        if (
          (res.status === 501 || res.status === 405) &&
          /^https?:\/\/(127\.0\.0\.1|localhost)(:\d+)?$/i.test(window.location.origin)
        ) {
          showFeedback(orderFeedback, MSG_STATIC, true);
        } else if (res.ok && data.success) {
          showFeedback(
            orderFeedback,
            'Demande envoyée. Vous recevrez une confirmation par email sous peu.',
            false
          );
          orderForm.reset();
          setOrderStep(1);
          orderProjectType.value = '';
          renderProjectTypes(orderMount, orderProjectType, '');
          setTimeout(function () {
            orderDialog.close();
            hideFeedback(orderFeedback);
          }, 2600);
        } else {
          showFeedback(orderFeedback, (data && data.error) || 'Envoi impossible.', true);
        }
      })
      .catch(function () {
        showFeedback(orderFeedback, 'Erreur réseau ou serveur injoignable.', true);
      })
      .finally(function () {
        setSubmitLoading(submitBtn, false);
      });
  });

  /* ----- Devis ----- */
  const quoteFeedback = document.getElementById('vitrineQuoteFeedback');
  const quoteProgressLis = quoteDialog.querySelectorAll('[data-vitrine-quote-bar]');
  const quoteSteps = quoteDialog.querySelectorAll('[data-vitrine-quote-step]');
  const quoteMount = document.getElementById('vitrineQuoteProjectMount');
  const quoteProjectType = document.getElementById('vd_quote_project_type');
  const quoteVitrineTitle = document.getElementById('vd_quote_vitrine_title');
  const quoteMessage = document.getElementById('vd_quote_message');
  const quoteNamePost = document.getElementById('vd_quote_name_post');
  let quoteStep = 1;

  function setQuoteStep(n) {
    quoteStep = n;
    setStepVisibility(quoteSteps, n, 'data-vitrine-quote-step');
    setProgressItems(quoteProgressLis, n);
    hideFeedback(quoteFeedback);
  }

  function syncQuoteName() {
    const f = document.getElementById('vd_quote_first');
    const l = document.getElementById('vd_quote_last');
    quoteNamePost.value = (((f && f.value) || '').trim() + ' ' + ((l && l.value) || '').trim()).trim();
  }

  function validateQuoteStep1() {
    if (!quoteProjectType.value) {
      showFeedback(quoteFeedback, 'Choisissez un type de projet.', true);
      return false;
    }
    return true;
  }

  function validateQuoteStep2() {
    const d = (document.getElementById('vd_quote_detail').value || '').trim();
    if (d.length < 15) {
      showFeedback(quoteFeedback, 'Décrivez votre besoin en au moins quelques mots (15 caractères min.).', true);
      return false;
    }
    return true;
  }

  function validateQuoteStep3() {
    syncQuoteName();
    const email = (document.getElementById('vd_quote_email').value || '').trim();
    const phone = (document.getElementById('vd_quote_phone').value || '').trim();
    if (!quoteNamePost.value) {
      showFeedback(quoteFeedback, 'Indiquez prénom et nom.', true);
      return false;
    }
    if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email)) {
      showFeedback(quoteFeedback, 'Email invalide.', true);
      return false;
    }
    if (phone.replace(/\D/g, '').length < 8) {
      showFeedback(quoteFeedback, 'Téléphone trop court ou invalide.', true);
      return false;
    }
    return true;
  }

  function buildQuoteMessage() {
    const detail = (document.getElementById('vd_quote_detail').value || '').trim();
    const slug = readVitrineSlug();
    const title = readVitrineTitle();
    const pt = PROJECT_TYPES.find(function (x) {
      return x.slug === quoteProjectType.value;
    });
    return (
      '--- Demande devis / questions — fiche vitrine ---\n' +
      'Vitrine : ' +
      title +
      ' (slug: ' +
      slug +
      ')\n' +
      'Type de projet : ' +
      ((pt && pt.label) || quoteProjectType.value) +
      '\n\n' +
      'Besoin exprimé :\n' +
      detail
    );
  }

  quoteDialog.querySelectorAll('[data-vitrine-quote-next]').forEach(function (btn) {
    btn.addEventListener('click', function () {
      const from = parseInt(btn.getAttribute('data-vitrine-quote-next'), 10);
      if (from === 1) {
        if (!validateQuoteStep1()) return;
        setQuoteStep(2);
      } else if (from === 2) {
        if (!validateQuoteStep2()) return;
        setQuoteStep(3);
      }
    });
  });

  quoteDialog.querySelectorAll('[data-vitrine-quote-back]').forEach(function (btn) {
    btn.addEventListener('click', function () {
      const from = parseInt(btn.getAttribute('data-vitrine-quote-back'), 10);
      if (from === 2) setQuoteStep(1);
      else if (from === 3) setQuoteStep(2);
    });
  });

  quoteForm.addEventListener('submit', function (e) {
    e.preventDefault();
    if (!validateQuoteStep3()) return;
    quoteVitrineTitle.value = readVitrineTitle();
    quoteMessage.value = buildQuoteMessage();
    hideFeedback(quoteFeedback);
    const submitBtn = document.getElementById('vitrineQuoteSubmit');
    setSubmitLoading(submitBtn, true);
    const fd = new FormData(quoteForm);
    fetch('/api/send-contact.php', { method: 'POST', body: fd })
      .then(function (res) {
        return res.json().then(function (data) {
          return { res: res, data: data };
        });
      })
      .then(function (_ref2) {
        const res = _ref2.res;
        const data = _ref2.data;
        if (
          (res.status === 501 || res.status === 405) &&
          /^https?:\/\/(127\.0\.0\.1|localhost)(:\d+)?$/i.test(window.location.origin)
        ) {
          showFeedback(quoteFeedback, MSG_STATIC, true);
        } else if (res.ok && data.success) {
          showFeedback(quoteFeedback, 'Message envoyé. Je vous réponds dès que possible.', false);
          quoteForm.reset();
          setQuoteStep(1);
          quoteProjectType.value = '';
          renderProjectTypes(quoteMount, quoteProjectType, '');
          setTimeout(function () {
            quoteDialog.close();
            hideFeedback(quoteFeedback);
          }, 2600);
        } else {
          showFeedback(quoteFeedback, (data && data.error) || 'Envoi impossible.', true);
        }
      })
      .catch(function () {
        showFeedback(quoteFeedback, 'Erreur réseau ou serveur injoignable.', true);
      })
      .finally(function () {
        setSubmitLoading(submitBtn, false);
      });
  });

  /* ----- Ouverture / fermeture ----- */
  function openOrder() {
    const cur = orderProjectType.value || 'web';
    renderProjectTypes(orderMount, orderProjectType, cur);
    orderVitrineTitle.value = readVitrineTitle();
    hideFeedback(orderFeedback);
    setOrderStep(1);
    orderDialog.showModal();
  }

  function openQuote() {
    const cur = quoteProjectType.value || 'web';
    renderProjectTypes(quoteMount, quoteProjectType, cur);
    quoteVitrineTitle.value = readVitrineTitle();
    hideFeedback(quoteFeedback);
    setQuoteStep(1);
    quoteDialog.showModal();
  }

  document.querySelectorAll('[data-vitrine-open]').forEach(function (btn) {
    btn.addEventListener('click', function () {
      const which = btn.getAttribute('data-vitrine-open');
      if (which === 'order') openOrder();
      else if (which === 'quote') openQuote();
    });
  });

  orderDialog.querySelectorAll('[data-vitrine-close]').forEach(function (btn) {
    btn.addEventListener('click', function () {
      orderDialog.close();
    });
  });
  quoteDialog.querySelectorAll('[data-vitrine-close]').forEach(function (btn) {
    btn.addEventListener('click', function () {
      quoteDialog.close();
    });
  });

  orderDialog.addEventListener('click', function (ev) {
    if (ev.target === orderDialog) orderDialog.close();
  });
  quoteDialog.addEventListener('click', function (ev) {
    if (ev.target === quoteDialog) quoteDialog.close();
  });

  renderProjectTypes(orderMount, orderProjectType, 'web');
  orderProjectType.value = 'web';
  renderProjectTypes(quoteMount, quoteProjectType, 'web');
  quoteProjectType.value = 'web';
  setProgressItems(orderProgressLis, 1);
  setProgressItems(quoteProgressLis, 1);
})();
