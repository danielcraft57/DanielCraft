/**
 * Animations page index blog : révélation au scroll, tilt léger sur les cartes.
 */
(function () {
  const prefersReduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  if (prefersReduced) {
    document.querySelectorAll('.blog-reveal-item').forEach((el) => el.classList.add('is-visible'));
    return;
  }

  const revealItems = document.querySelectorAll('.blog-reveal-item');
  if (revealItems.length && 'IntersectionObserver' in window) {
    const io = new IntersectionObserver(
      (entries) => {
        entries.forEach((entry) => {
          if (entry.isIntersecting) {
            entry.target.classList.add('is-visible');
            io.unobserve(entry.target);
          }
        });
      },
      { rootMargin: '0px 0px -8% 0px', threshold: 0.08 }
    );
    revealItems.forEach((el) => io.observe(el));
  } else {
    revealItems.forEach((el) => el.classList.add('is-visible'));
  }

  const cards = document.querySelectorAll('.blog-card-animated');
  cards.forEach((card) => {
    const media = card.querySelector('.article-card-media img, .series-card-media img');
    if (!media) return;

    card.addEventListener('mousemove', (e) => {
      const rect = card.getBoundingClientRect();
      const x = (e.clientX - rect.left) / rect.width - 0.5;
      const y = (e.clientY - rect.top) / rect.height - 0.5;
      media.style.transform = `scale(1.06) translate(${x * 6}px, ${y * 4}px)`;
    });

    card.addEventListener('mouseleave', () => {
      media.style.transform = '';
    });
  });
})();
