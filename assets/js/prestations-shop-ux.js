/**
 * UX boutique : tips toast, stagger cartes, sticky CTA mobile,
 * back-to-top, ripple boutons, pulse offre semaine.
 */
(function () {
  'use strict';

  var reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var page = document.querySelector('.page-nos-offres, .page-livres, .prestation-detail-root');
  if (!page) return;

  var TIPS = [
    'Astuce : filtrez avec la recherche ou les chips pour aller plus vite.',
    'Les packs coutent moins cher qu\'a l\'unite - regardez le prix barre.',
    'Un devis PDF arrive par e-mail en quelques secondes, sans engagement.',
    'Sur telephone, utilisez les categories en haut pour naviguer.',
    'L\'offre de la semaine change chaque lundi automatiquement.',
  ];

  function ensureToastHost() {
    var host = document.getElementById('shopUxToastHost');
    if (host) return host;
    host = document.createElement('div');
    host.id = 'shopUxToastHost';
    host.className = 'shop-ux-toast-host';
    host.setAttribute('aria-live', 'polite');
    document.body.appendChild(host);
    return host;
  }

  function showToast(message, opts) {
    opts = opts || {};
    var host = ensureToastHost();
    var el = document.createElement('div');
    el.className = 'shop-ux-toast';
    el.setAttribute('role', 'status');
    el.innerHTML =
      '<i class="fas fa-lightbulb" aria-hidden="true"></i>' +
      '<span>' + message + '</span>' +
      '<button type="button" class="shop-ux-toast-close" aria-label="Fermer tip">&times;</button>';
    host.appendChild(el);
    requestAnimationFrame(function () {
      el.classList.add('is-in');
    });
    var ttl = opts.ttl || 5200;
    var timer = setTimeout(function () {
      dismissToast(el);
    }, ttl);
    el.querySelector('.shop-ux-toast-close').addEventListener('click', function () {
      clearTimeout(timer);
      dismissToast(el);
    });
  }

  function dismissToast(el) {
    if (!el || !el.parentNode) return;
    el.classList.remove('is-in');
    el.classList.add('is-out');
    setTimeout(function () {
      if (el.parentNode) el.parentNode.removeChild(el);
    }, 280);
  }

  function initTips() {
    if (document.querySelector('.prestation-detail-root')) return;
    if (sessionStorage.getItem('shopUxTipShown')) return;
    var tip = TIPS[Math.floor(Math.random() * TIPS.length)];
    setTimeout(function () {
      showToast(tip);
      try {
        sessionStorage.setItem('shopUxTipShown', '1');
      } catch (e) {}
    }, 1800);

    document.querySelectorAll('.prestation-card-badge, .price-tier').forEach(function (badge) {
      badge.setAttribute('tabindex', '0');
      badge.classList.add('shop-ux-tippy');
      var label = (badge.textContent || '').trim();
      var tipText = 'Badge : ' + label;
      if (/pack/i.test(label)) tipText = 'Pack = plusieurs prestations avec remise.';
      if (/petit budget/i.test(label)) tipText = 'Entree de gamme : l\'essentiel, sans superflu.';
      if (/coup de/i.test(label)) tipText = 'Mise en avant cette semaine ou tres demandee.';
      badge.addEventListener('mouseenter', function () {
        badge.setAttribute('data-tip', tipText);
        badge.classList.add('is-tip-open');
      });
      badge.addEventListener('mouseleave', function () {
        badge.classList.remove('is-tip-open');
      });
      badge.addEventListener('focus', function () {
        badge.setAttribute('data-tip', tipText);
        badge.classList.add('is-tip-open');
      });
      badge.addEventListener('blur', function () {
        badge.classList.remove('is-tip-open');
      });
    });
  }

  function initStaggerCards() {
    var cards = document.querySelectorAll(
      '.page-prestations-catalog .prestation-card, .page-livres .livre-card, ' +
        '.prestation-detail-root .prestation-related-card'
    );
    if (!cards.length) return;
    cards.forEach(function (card, i) {
      card.classList.add('shop-ux-card');
      card.style.setProperty('--shop-stagger', Math.min(i % 8, 7) * 45 + 'ms');
    });
    if (reduceMotion || !('IntersectionObserver' in window)) {
      cards.forEach(function (c) {
        c.classList.add('is-shop-in');
      });
      return;
    }
    var io = new IntersectionObserver(
      function (entries) {
        entries.forEach(function (entry) {
          if (!entry.isIntersecting) return;
          entry.target.classList.add('is-shop-in');
          io.unobserve(entry.target);
        });
      },
      { rootMargin: '0px 0px -6% 0px', threshold: 0.08 }
    );
    cards.forEach(function (c) {
      io.observe(c);
    });
  }

  function initDetailListStagger() {
    var root = document.querySelector('.prestation-detail-root');
    if (!root) return;
    var nodes = root.querySelectorAll(
      '.prestation-benefits li, .prestation-includes li, .prestation-tech-table tr, .shop-ux-faq'
    );
    if (!nodes.length) return;
    nodes.forEach(function (el, i) {
      if (!el.style.getPropertyValue('--shop-stagger') && !el.style.getPropertyValue('--faq-stagger')) {
        el.style.setProperty('--shop-stagger', Math.min(i % 10, 9) * 40 + 'ms');
      }
    });
    if (reduceMotion || !('IntersectionObserver' in window)) {
      nodes.forEach(function (el) {
        el.classList.add('is-shop-in');
      });
      return;
    }
    var io = new IntersectionObserver(
      function (entries) {
        entries.forEach(function (entry) {
          if (!entry.isIntersecting) return;
          entry.target.classList.add('is-shop-in');
          io.unobserve(entry.target);
        });
      },
      { rootMargin: '0px 0px -8% 0px', threshold: 0.05 }
    );
    nodes.forEach(function (el) {
      io.observe(el);
    });
  }

  function initFaqAccordion() {
    var items = document.querySelectorAll('.prestation-detail-root .prestation-faq-item');
    if (!items.length) return;
    items.forEach(function (item) {
      item.addEventListener('toggle', function () {
        if (!item.open) return;
        items.forEach(function (other) {
          if (other !== item && other.open) other.open = false;
        });
      });
    });
  }

  function initDetailTips() {
    var root = document.querySelector('.prestation-detail-root');
    if (!root || sessionStorage.getItem('shopUxDetailTip')) return;
    var tips = [
      'Astuce : ouvrez les questions frequentes plus bas pour le delai et le devis.',
      'Cette offre peut faire partie d\'un pack - regardez la section packs si elle s\'affiche.',
      'Le devis PDF part par e-mail, sans engagement.',
    ];
    if (!root.querySelector('.prestation-detail-inpack')) {
      tips = tips.filter(function (t) {
        return t.indexOf('pack') === -1;
      });
    }
    var tip = tips[Math.floor(Math.random() * tips.length)];
    setTimeout(function () {
      showToast(tip);
      try {
        sessionStorage.setItem('shopUxDetailTip', '1');
      } catch (e) {}
    }, 1600);
  }

  function initButtonRipple() {
    document.addEventListener('click', function (ev) {
      var btn = ev.target.closest(
        '.service-cta, .prestations-deal-cta, .prestation-buybox .btn, [data-prestation-devis-open]'
      );
      if (!btn || reduceMotion) return;
      var rect = btn.getBoundingClientRect();
      var ripple = document.createElement('span');
      ripple.className = 'shop-ux-ripple';
      var size = Math.max(rect.width, rect.height);
      ripple.style.width = ripple.style.height = size + 'px';
      ripple.style.left = ev.clientX - rect.left - size / 2 + 'px';
      ripple.style.top = ev.clientY - rect.top - size / 2 + 'px';
      btn.classList.add('shop-ux-ripple-host');
      btn.appendChild(ripple);
      setTimeout(function () {
        if (ripple.parentNode) ripple.parentNode.removeChild(ripple);
      }, 520);
    });
  }

  function initBackToTop() {
    var btn = document.createElement('button');
    btn.type = 'button';
    btn.className = 'shop-ux-top';
    btn.setAttribute('aria-label', 'Retour en haut');
    btn.innerHTML = '<i class="fas fa-arrow-up" aria-hidden="true"></i>';
    document.body.appendChild(btn);
    var onScroll = function () {
      if (window.scrollY > 480) btn.classList.add('is-visible');
      else btn.classList.remove('is-visible');
    };
    window.addEventListener('scroll', onScroll, { passive: true });
    onScroll();
    btn.addEventListener('click', function () {
      window.scrollTo({ top: 0, behavior: reduceMotion ? 'auto' : 'smooth' });
    });
  }

  function initStickyBuybar() {
    var buybox = document.querySelector('.prestation-buybox');
    var root = document.querySelector('.prestation-detail-root');
    if (!buybox || !root) return;
    var bar = document.createElement('div');
    bar.className = 'shop-ux-sticky-buy';
    bar.setAttribute('hidden', '');
    var title = root.getAttribute('data-prestation-title') || 'Cette offre';
    var price = root.getAttribute('data-prestation-price') || '';
    bar.innerHTML =
      '<div class="shop-ux-sticky-buy-inner">' +
      '<div><strong>' +
      title +
      '</strong><span>' +
      price +
      ' € HT</span></div>' +
      '<button type="button" class="btn btn-primary" data-prestation-devis-open ' +
      'data-prestation-slug="' +
      (root.getAttribute('data-prestation-slug') || '') +
      '" data-service-slug="' +
      (root.getAttribute('data-service-slug') || '') +
      '" data-prestation-title="' +
      title.replace(/"/g, '&quot;') +
      '" data-prestation-price="' +
      price +
      '" data-prestation-price-label="' +
      (root.getAttribute('data-prestation-price-label') || 'Forfait') +
      '"><span>Demander un devis</span></button></div>';
    document.body.appendChild(bar);

    if (!('IntersectionObserver' in window)) return;
    var io = new IntersectionObserver(
      function (entries) {
        entries.forEach(function (entry) {
          if (entry.isIntersecting) {
            bar.setAttribute('hidden', '');
            bar.classList.remove('is-visible');
          } else {
            bar.removeAttribute('hidden');
            bar.classList.add('is-visible');
          }
        });
      },
      { threshold: 0.15 }
    );
    io.observe(buybox);
  }

  function initDealPulse() {
    var deal = document.querySelector('.prestations-deal-week, .livres-deal-week');
    if (!deal || reduceMotion) return;
    deal.classList.add('shop-ux-deal-pulse');
  }

  function initSidebarScrollSpy() {
    var links = document.querySelectorAll('.prestations-sidebar-link[href^="#"]');
    if (!links.length || !('IntersectionObserver' in window)) return;
    var map = {};
    links.forEach(function (a) {
      var id = (a.getAttribute('href') || '').slice(1);
      if (!id) return;
      var target = document.getElementById(id);
      if (target) map[id] = a;
    });
    var io = new IntersectionObserver(
      function (entries) {
        entries.forEach(function (entry) {
          if (!entry.isIntersecting) return;
          var id = entry.target.id;
          links.forEach(function (a) {
            a.classList.toggle('is-active', a === map[id]);
          });
        });
      },
      { rootMargin: '-30% 0px -55% 0px', threshold: 0 }
    );
    Object.keys(map).forEach(function (id) {
      var el = document.getElementById(id);
      if (el) io.observe(el);
    });
  }

  initTips();
  initStaggerCards();
  initDetailListStagger();
  initFaqAccordion();
  initDetailTips();
  initButtonRipple();
  initBackToTop();
  initStickyBuybar();
  initDealPulse();
  initSidebarScrollSpy();
})();
