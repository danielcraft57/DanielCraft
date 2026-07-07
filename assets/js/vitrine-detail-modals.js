/**
 * Modale fiche vitrine : pré-commande modèle (sans paiement immédiat).
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
  const orderForm = document.getElementById('vitrineOrderForm');
  const card = document.querySelector('.vitrine-purchase-card');

  if (!orderDialog || !orderForm) return;

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
      if ('inert' in el) {
        el.inert = !on;
      }
    });
  }

  /** Parse JSON même si le serveur renvoie du HTML (404, erreur PHP) pour éviter un catch silencieux. */
  function parseFetchJson(res) {
    return res.text().then(function (text) {
      var ct = (res.headers.get('content-type') || '').toLowerCase();
      var trimmed = (text || '').trim();
      if (ct.indexOf('application/json') !== -1 || (trimmed && trimmed.charAt(0) === '{')) {
        try {
          return { res: res, data: JSON.parse(text) };
        } catch (e) {
          return {
            res: res,
            data: { success: false, error: trimmed.slice(0, 280) || 'Réponse serveur illisible.' }
          };
        }
      }
      return {
        res: res,
        data: {
          success: false,
          error: trimmed
            ? trimmed.replace(/<[^>]+>/g, ' ').replace(/\s+/g, ' ').trim().slice(0, 280)
            : 'HTTP ' + res.status
        }
      };
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
      '<div><dt>Modèle</dt><dd>' +
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
      '--- Pré-commande catalogue (aucun paiement sur le site) ---\n' +
      'Modèle : ' +
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
      .then(parseFetchJson)
      .then(function (_ref) {
        const res = _ref.res;
        const data = _ref.data;
        if (
          (res.status === 501 || res.status === 405) &&
          /^https?:\/\/(127\.0\.0\.1|localhost)(:\d+)?$/i.test(window.location.origin)
        ) {
          showFeedback(orderFeedback, MSG_STATIC, true);
        } else if (res.ok && data.success) {
          var okMsg = data.devis_issued
            ? data.message ||
              (data.fallback
                ? 'Demande enregistrée — devis PDF sous 24 h ouvrées.'
                : 'Devis envoyé par e-mail. Vérifiez votre boîte mail.')
            : data.dry_run
              ? 'Demande acceptée (mode test sans email sur ce serveur).'
              : 'Demande envoyée. Vous recevrez une confirmation par email sous peu.';
          showFeedback(orderFeedback, okMsg, false);
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

  /* ----- Ouverture / fermeture ----- */
  function openOrder() {
    const cur = orderProjectType.value || 'web';
    renderProjectTypes(orderMount, orderProjectType, cur);
    orderVitrineTitle.value = readVitrineTitle();
    hideFeedback(orderFeedback);
    setOrderStep(1);
    orderDialog.showModal();
  }

  document.querySelectorAll('[data-vitrine-open="order"]').forEach(function (btn) {
    btn.addEventListener('click', openOrder);
  });

  orderDialog.querySelectorAll('[data-vitrine-close]').forEach(function (btn) {
    btn.addEventListener('click', function () {
      orderDialog.close();
    });
  });

  orderDialog.addEventListener('click', function (ev) {
    if (ev.target === orderDialog) orderDialog.close();
  });

  renderProjectTypes(orderMount, orderProjectType, 'web');
  orderProjectType.value = 'web';
  setProgressItems(orderProgressLis, 1);
})();
