/**
 * Page /livres/telechargement/ — code unique + telechargement PDF (securise).
 */
(function () {
  'use strict';

  var root = document.getElementById('ldlRoot');
  if (!root) return;

  var payBanner = document.getElementById('ldlPayBanner');
  var form = document.getElementById('ldlCodeForm');
  var input = document.getElementById('ldlCodeInput');
  var unlockBtn = document.getElementById('ldlUnlockBtn');
  var gateFeedback = document.getElementById('ldlGateFeedback');
  var copyBtn = document.getElementById('ldlCopyBtn');
  var retryBtn = document.getElementById('ldlRetryBtn');
  var formTsEl = document.getElementById('ldlFormTs');
  var companyEl = document.getElementById('ldlCompany');
  var websiteEl = document.getElementById('ldlWebsite');

  var formLoadedAt = Math.floor(Date.now() / 1000);
  if (formTsEl) formTsEl.value = String(formLoadedAt);

  function showView(name) {
    root.setAttribute('data-ldl-state', name);
    root.querySelectorAll('[data-ldl-view]').forEach(function (el) {
      el.hidden = el.getAttribute('data-ldl-view') !== name;
    });
  }

  function setBusy(btn, on) {
    if (!btn) return;
    btn.disabled = !!on;
    btn.setAttribute('aria-busy', on ? 'true' : 'false');
  }

  function normalizeCodeInput(raw) {
    var s = String(raw || '')
      .toUpperCase()
      .replace(/[^A-Z0-9]/g, '');
    if (s.indexOf('DC') === 0) s = s.slice(2);
    s = s.slice(0, 8);
    if (s.length <= 4) return s;
    return s.slice(0, 4) + '-' + s.slice(4);
  }

  function formatCodeForApi(raw) {
    var n = normalizeCodeInput(raw).replace(/-/g, '');
    if (n.length !== 8) return '';
    return 'DC-' + n.slice(0, 4) + '-' + n.slice(4);
  }

  function showGateError(msg) {
    if (!gateFeedback) return;
    gateFeedback.hidden = !msg;
    gateFeedback.textContent = msg || '';
  }

  function setBanner(text, isError) {
    if (!payBanner) return;
    if (!text) {
      payBanner.hidden = true;
      payBanner.textContent = '';
      return;
    }
    payBanner.hidden = false;
    payBanner.textContent = text;
    payBanner.classList.toggle('ldl-banner--error', !!isError);
  }

  function parseJson(res) {
    return res.text().then(function (text) {
      var trimmed = (text || '').trim();
      if (trimmed.charAt(0) === '{') {
        try {
          return { res: res, data: JSON.parse(text) };
        } catch (e) {
          return { res: res, data: { ok: false, error: 'Reponse illisible.' } };
        }
      }
      return { res: res, data: { ok: false, error: 'HTTP ' + res.status } };
    });
  }

  function escapeHtml(s) {
    return String(s || '')
      .replace(/&/g, '&amp;')
      .replace(/</g, '&lt;')
      .replace(/>/g, '&gt;')
      .replace(/"/g, '&quot;');
  }

  function showLocked(data) {
    var el = document.getElementById('ldlLockedText');
    if (el) {
      el.textContent =
        (data && data.error) ||
        'Pour proteger les PDF, l\'acces est bloque environ 24 h depuis cette connexion.';
    }
    showView('locked');
  }

  function handleLookupFailure(ref, preferGate) {
    var data = (ref && ref.data) || {};
    if (data.locked || (ref && ref.res && ref.res.status === 429 && data.locked)) {
      showLocked(data);
      return false;
    }
    var err =
      data.error ||
      'Code invalide ou expire. Verifie ta saisie, ou ecris a contact@danielcraft.fr.';
    if (preferGate) {
      showView('gate');
      showGateError(err);
      return false;
    }
    var errorText = document.getElementById('ldlErrorText');
    if (errorText) errorText.textContent = err;
    showView('error');
    return false;
  }

  function renderReady(data) {
    var titleEl = document.getElementById('ldlReadyTitle');
    var leadEl = document.getElementById('ldlReadyLead');
    var codeEl = document.getElementById('ldlCodeDisplay');
    var expiryEl = document.getElementById('ldlExpiry');
    var filesEl = document.getElementById('ldlFiles');
    var coverWrap = document.getElementById('ldlCoverWrap');
    var coverImg = document.getElementById('ldlCover');

    var title = data.title || 'Ton PDF DanielCraft';
    var isPack = data.kind === 'pack';
    if (titleEl) titleEl.textContent = title;
    if (leadEl) {
      leadEl.textContent = isPack
        ? 'Voici les PDF du pack — telecharge-les un par un.'
        : 'Un clic et le PDF est a toi. Garde aussi ton code pour plus tard.';
    }
    if (codeEl) codeEl.textContent = data.code || '—';
    if (expiryEl) {
      var days = Number(data.days_left || 0);
      expiryEl.textContent = days > 0 ? 'Valable encore ~' + days + ' j' : 'Bientot expire';
    }

    if (coverWrap && coverImg) {
      var cover = (data.cover || '').trim();
      if (cover) {
        coverImg.src = cover;
        coverImg.alt = 'Couverture — ' + title;
        coverWrap.setAttribute('aria-hidden', 'false');
        coverWrap.hidden = false;
      } else {
        coverWrap.setAttribute('aria-hidden', 'true');
        coverWrap.hidden = true;
        coverImg.removeAttribute('src');
      }
    }

    if (filesEl) {
      var files = Array.isArray(data.files) ? data.files : [];
      filesEl.innerHTML = files
        .map(function (f) {
          var label = escapeHtml(f.label || f.filename || 'PDF');
          var url = escapeHtml(f.download_url || '#');
          var thumb = (f.cover || '').trim();
          var media = thumb
            ? '<img class="ldl-file__thumb" src="' +
              escapeHtml(thumb) +
              '" alt="" width="48" height="64" loading="lazy">'
            : '<div class="ldl-file__icon" aria-hidden="true"><i class="fas fa-file-pdf"></i></div>';
          return (
            '<li class="ldl-file">' +
            media +
            '<div class="ldl-file__meta">' +
            '<p class="ldl-file__title">' +
            label +
            '</p>' +
            '<p class="ldl-file__sub">PDF · telechargement securise</p>' +
            '</div>' +
            '<a class="btn btn-primary ldl-file__btn" href="' +
            url +
            '" rel="noopener"><i class="fas fa-download" aria-hidden="true"></i> Telecharger</a>' +
            '</li>'
          );
        })
        .join('');
    }

    showView('ready');

    try {
      var url = new URL(window.location.href);
      if (data.code) {
        url.searchParams.delete('token');
        url.searchParams.delete('session_id');
        url.searchParams.delete('stripe');
        url.searchParams.delete('error');
        url.searchParams.set('code', data.code);
        window.history.replaceState({}, '', url.pathname + '?' + url.searchParams.toString());
      }
    } catch (_) {
      /* ignore */
    }
  }

  function buildLookupBody(fields) {
    var body = {
      form_ts: formLoadedAt,
      company: companyEl ? companyEl.value : '',
      website: websiteEl ? websiteEl.value : '',
      source: fields.source || 'form',
    };
    if (fields.code) body.code = fields.code;
    if (fields.token) body.token = fields.token;
    return body;
  }

  function lookup(fields, opts) {
    opts = opts || {};
    showView('boot');
    return fetch('/api/livre-download-lookup.php', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json', Accept: 'application/json' },
      body: JSON.stringify(buildLookupBody(fields)),
      credentials: 'same-origin',
    })
      .then(parseJson)
      .then(function (ref) {
        if (ref.res.ok && ref.data && ref.data.ok) {
          renderReady(ref.data);
          return true;
        }
        return handleLookupFailure(ref, !!opts.preferGate);
      })
      .catch(function () {
        if (opts.preferGate) {
          showView('gate');
          showGateError('Reseau indisponible. Reessaie dans un instant.');
        } else {
          var errorText = document.getElementById('ldlErrorText');
          if (errorText) errorText.textContent = 'Reseau indisponible. Reessaie dans un instant.';
          showView('error');
        }
        return false;
      });
  }

  function fulfillSession(sessionId) {
    showView('boot');
    setBanner('Paiement recu — preparation de ta facture et de ton code…', false);
    return fetch('/api/request-paid-livre.php', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ stripe_session_id: sessionId }),
    })
      .then(parseJson)
      .then(function (ref) {
        var data = ref.data || {};
        if (ref.res.ok && data.success) {
          setBanner(
            data.message ||
              'Merci ! Facture envoyee par e-mail. Voici ta page de telechargement.',
            false
          );
          if (data.code) {
            return lookup({ code: data.code, source: 'auto' }, { preferGate: true });
          }
          if (data.download_url) {
            try {
              var u = new URL(data.download_url, window.location.origin);
              var code = u.searchParams.get('code');
              var token = u.searchParams.get('token');
              if (code) return lookup({ code: code, source: 'auto' }, { preferGate: true });
              if (token) return lookup({ token: token, source: 'link' }, { preferGate: true });
            } catch (_) {
              /* fallthrough */
            }
          }
          showView('gate');
          return false;
        }
        setBanner(
          (data && data.error) ||
            'Paiement enregistre, mais la livraison a echoue. Ecris a contact@danielcraft.fr.',
          true
        );
        showView('gate');
        return false;
      })
      .catch(function () {
        setBanner(
          'Paiement recu. Si tu n\'as pas le mail sous peu, contact@danielcraft.fr avec ton e-mail Stripe.',
          false
        );
        showView('gate');
        return false;
      });
  }

  if (form) {
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      showGateError('');
      if (companyEl && companyEl.value) return;
      if (websiteEl && websiteEl.value) return;

      var elapsed = Math.floor(Date.now() / 1000) - formLoadedAt;
      if (elapsed < 2) {
        showGateError('Un peu trop rapide — reessaie dans une seconde.');
        return;
      }

      var code = formatCodeForApi(input ? input.value : '');
      if (!code) {
        showGateError('Entre un code au format DC-XXXX-XXXX.');
        if (input) input.focus();
        return;
      }
      setBusy(unlockBtn, true);
      lookup({ code: code, source: 'form' }, { preferGate: true }).finally(function () {
        setBusy(unlockBtn, false);
      });
    });
  }

  if (input) {
    input.addEventListener('input', function () {
      var before = input.value;
      var next = normalizeCodeInput(before);
      if (next !== before) {
        input.value = next;
        try {
          input.setSelectionRange(next.length, next.length);
        } catch (_) {
          /* ignore */
        }
      }
    });
  }

  if (copyBtn) {
    copyBtn.addEventListener('click', function () {
      var codeEl = document.getElementById('ldlCodeDisplay');
      var text = (codeEl && codeEl.textContent) || '';
      if (!text || text === '—') return;
      var done = function () {
        copyBtn.classList.add('is-copied');
        var span = copyBtn.querySelector('span');
        if (span) span.textContent = 'Copie !';
        setTimeout(function () {
          copyBtn.classList.remove('is-copied');
          if (span) span.textContent = 'Copier';
        }, 1600);
      };
      if (navigator.clipboard && navigator.clipboard.writeText) {
        navigator.clipboard.writeText(text).then(done).catch(done);
      } else {
        done();
      }
    });
  }

  if (retryBtn) {
    retryBtn.addEventListener('click', function () {
      setBanner('', false);
      showGateError('');
      showView('gate');
      if (input) input.focus();
    });
  }

  // Boot
  try {
    var params = new URLSearchParams(window.location.search);
    var stripe = params.get('stripe');
    var sessionId = (params.get('session_id') || '').trim();
    var code = (params.get('code') || '').trim();
    var token = (params.get('token') || '').trim();
    var err = params.get('error');

    if (err === 'expired') {
      setBanner('Ce lien a expire. Entre ton code si tu l\'as encore, ou contacte-moi.', true);
    } else if (err === 'locked') {
      showLocked({
        error:
          'Trop d\'essais incorrects. Acces bloque environ 24 h. Ecris a contact@danielcraft.fr si besoin.',
      });
      return;
    }

    if (stripe === 'success' && sessionId) {
      fulfillSession(sessionId);
    } else if (token) {
      lookup({ token: token, source: 'link' });
    } else if (code) {
      if (input) input.value = normalizeCodeInput(code);
      // Petit delai pour respecter le timing min serveur
      setTimeout(function () {
        lookup({ code: formatCodeForApi(code) || code, source: 'link' }, { preferGate: true });
      }, 2100);
    } else {
      showView('gate');
    }
  } catch (_) {
    showView('gate');
  }
})();
