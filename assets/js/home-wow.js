/**
 * Accueil : stagger reveal, tilt, lazy images, rotation blog.
 */
(function () {
  'use strict';

  if (
    !document.querySelector('.home-hero--wow') &&
    !document.querySelector('.home-offers') &&
    !document.querySelector('.home-body-ecom')
  ) {
    return;
  }

  const reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  function initTiltCards() {
    if (reduceMotion) return;
    document.querySelectorAll('[data-home-tilt]').forEach(function (card) {
      const max = 10;
      card.addEventListener('mousemove', function (ev) {
        const rect = card.getBoundingClientRect();
        const x = (ev.clientX - rect.left) / rect.width - 0.5;
        const y = (ev.clientY - rect.top) / rect.height - 0.5;
        card.style.transform =
          'perspective(900px) rotateX(' + -y * max + 'deg) rotateY(' + x * max + 'deg) translateY(-6px)';
        card.classList.add('is-tilt-active');
      });
      card.addEventListener('mouseleave', function () {
        card.style.transform = '';
        card.classList.remove('is-tilt-active');
      });
    });
  }

  function initHeroParallax() {
    if (reduceMotion) return;
    if (window.matchMedia('(max-width: 959px)').matches) return;
    const media =
      document.querySelector('.home-hero-anim__stack') ||
      document.querySelector('.home-split__media img');
    if (!media) return;
    window.addEventListener(
      'scroll',
      function () {
        const y = window.scrollY;
        if (y > 700) return;
        media.style.transform = 'translateY(' + y * 0.05 + 'px)';
      },
      { passive: true },
    );
  }

  function initStagger() {
    const blocks = document.querySelectorAll('.home-stagger');
    if (!blocks.length) return;

    if (window.matchMedia('(max-width: 767px)').matches || reduceMotion) {
      blocks.forEach(function (el) {
        el.classList.add('is-visible');
      });
      return;
    }

    const io = new IntersectionObserver(
      function (entries) {
        entries.forEach(function (entry) {
          if (entry.isIntersecting) {
            entry.target.classList.add('is-visible');
            io.unobserve(entry.target);
          }
        });
      },
      { threshold: 0.12, rootMargin: '0px 0px -40px 0px' },
    );
    blocks.forEach(function (el) {
      io.observe(el);
    });
  }

  function hydrateLazyImage(img) {
    if (!img || img.dataset.homeEager !== undefined) return;
    if (img.dataset.lazyDone === '1') return;
    const picture = img.closest('picture');
    if (picture) {
      picture.querySelectorAll('source[data-srcset]').forEach(function (source) {
        source.setAttribute('srcset', source.getAttribute('data-srcset'));
        source.removeAttribute('data-srcset');
      });
    }
    const src = img.getAttribute('data-src');
    if (src) {
      img.setAttribute('src', src);
      img.removeAttribute('data-src');
    }
    img.dataset.lazyDone = '1';
    img.classList.add('is-loaded');
  }

  function initScrollLazyImages(scope) {
    const root = scope || document.querySelector('.page-home-ecom');
    if (!root) return;

    root.querySelectorAll('img:not([data-home-eager])').forEach(function (img) {
      if (img.classList.contains('home-lazy-img') && img.getAttribute('data-src')) return;
      const current = img.getAttribute('src');
      if (!current || current.indexOf('data:') === 0) return;
      img.setAttribute('data-src', current);
      img.removeAttribute('src');
      img.classList.add('home-lazy-img');
      const picture = img.closest('picture');
      if (picture) {
        picture.querySelectorAll('source[srcset]').forEach(function (source) {
          source.setAttribute('data-srcset', source.getAttribute('srcset'));
          source.removeAttribute('srcset');
        });
      }
    });

    const targets = root.querySelectorAll('img.home-lazy-img');
    if (!targets.length) return;

    if (!('IntersectionObserver' in window)) {
      targets.forEach(hydrateLazyImage);
      return;
    }

    const io = new IntersectionObserver(
      function (entries) {
        entries.forEach(function (entry) {
          if (!entry.isIntersecting) return;
          hydrateLazyImage(entry.target);
          io.unobserve(entry.target);
        });
      },
      { root: null, rootMargin: '280px 0px', threshold: 0.01 },
    );

    targets.forEach(function (img) {
      io.observe(img);
    });

    const heroB = document.querySelector('.home-hero-anim__frame--b img.home-lazy-img');
    if (heroB) {
      const kick = function () {
        hydrateLazyImage(heroB);
      };
      if ('requestIdleCallback' in window) {
        window.requestIdleCallback(kick, { timeout: 1800 });
      } else {
        window.setTimeout(kick, 900);
      }
    }
  }

  function ogWebpFromJpg(path) {
    if (!path || !/\.jpe?g$/i.test(path)) return '';
    return path.replace(/\.jpe?g$/i, '.webp');
  }

  function formatViews(count) {
    if (count == null || Number.isNaN(Number(count))) return '';
    const n = Number(count);
    if (n >= 1000000) return (n / 1000000).toFixed(1).replace('.0', '') + ' M vues';
    if (n >= 1000) return (n / 1000).toFixed(1).replace('.0', '') + ' k vues';
    return n + ' vues';
  }

  function applyBlogCards(root, items) {
    const cards = root.querySelectorAll('.home-blog-card');
    cards.forEach(function (card, i) {
      const item = items[i];
      if (!item) return;
      const media = card.querySelector('.home-blog-card__media');
      const img = card.querySelector('img');
      const source = card.querySelector('source');
      const cat = card.querySelector('.home-blog-card__cat');
      const titleA = card.querySelector('h3 a');
      const more = card.querySelector('.home-blog-card__more');
      const schemaUrl = card.querySelector('link[itemprop="url"]');
      const schemaImg = card.querySelector('link[itemprop="image"]');
      const viewsEl = card.querySelector('.home-blog-card__views');
      const imgPath = item.img || '/assets/images/og/blog-1200x630.jpg';
      const webpPath = ogWebpFromJpg(imgPath);

      if (media) media.setAttribute('href', item.href);
      if (schemaUrl) schemaUrl.setAttribute('href', item.href);
      if (schemaImg) schemaImg.setAttribute('href', imgPath);
      if (img) {
        img.alt = '';
        img.dataset.lazyDone = '0';
        img.classList.add('home-lazy-img');
        img.setAttribute('data-src', imgPath);
        img.removeAttribute('src');
      }
      if (source) {
        source.removeAttribute('srcset');
        if (webpPath) {
          source.setAttribute('data-srcset', webpPath);
          source.setAttribute('type', 'image/webp');
        } else {
          source.removeAttribute('data-srcset');
        }
      }
      if (cat) cat.textContent = item.cat || '';
      if (titleA) {
        titleA.href = item.href;
        titleA.textContent = item.title;
      }
      if (more) more.href = item.href;
      if (viewsEl) {
        const label = formatViews(item.views);
        viewsEl.textContent = label;
        viewsEl.hidden = !label;
      }
    });
    initScrollLazyImages(root);
  }

  function pickBlogPool(data) {
    const pools = data.pools || [];
    if (!pools.length) return [];
    const perDay = data.rotationPerDay || 2;
    const hour = new Date().getHours();
    let slot = 0;
    if (perDay <= 1) {
      slot = 0;
    } else if (perDay === 2) {
      slot = hour < 12 ? 0 : 1;
    } else {
      slot = hour < 8 ? 0 : hour < 16 ? 1 : 2;
    }
    return pools[slot] || pools[0];
  }

  function initBlogRotate() {
    const root = document.querySelector('[data-home-blog-rotate]');
    if (!root) return;

    fetch('/blog/home-rotation.json', { credentials: 'same-origin' })
      .then(function (response) {
        if (!response.ok) throw new Error('home-rotation');
        return response.json();
      })
      .then(function (data) {
        const items = pickBlogPool(data);
        if (items && items.length) applyBlogCards(root, items);
      })
      .catch(function () {
        /* HTML statique = secours si le JSON est indisponible */
      });
  }

  initTiltCards();
  initHeroParallax();
  initStagger();
  initBlogRotate();
  initScrollLazyImages();
})();
