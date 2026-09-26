// Shared behavior for the inner pages (city pages and the clean-yard guide).
// The homepage has its own inline script with the same core pieces plus the quote form.
(function () {
  const reduced = matchMedia('(prefers-reduced-motion: reduce)').matches;
  const $ = s => document.querySelector(s);
  const $$ = s => document.querySelectorAll(s);

  /* Nav menu */
  const nav = $('#nav'), menuBtn = $('#menuBtn');
  if (menuBtn) {
    menuBtn.addEventListener('click', () => {
      const open = nav.classList.toggle('open');
      menuBtn.setAttribute('aria-expanded', open);
    });
    $$('#navLinks a').forEach(a => a.addEventListener('click', () => {
      nav.classList.remove('open'); menuBtn.setAttribute('aria-expanded', false);
    }));
  }

  /* Scroll effects: progress bar, nav shadow, sticky phone bar, steps line, guide contents */
  const progress = $('#progress'), sticky = $('#stickyCta'), stepsEl = $('#steps'), line = $('#stepsLine');
  const tocLinks = [...$$('.toc a[href^="#"]')];
  function onScroll() {
    const y = scrollY, h = document.documentElement.scrollHeight - innerHeight;
    if (progress) progress.style.transform = `scaleX(${h > 0 ? y / h : 0})`;
    if (nav) nav.classList.toggle('scrolled', y > 30);
    if (sticky) sticky.classList.toggle('show', y > innerHeight * .6);
    if (stepsEl && line) {
      const r = stepsEl.getBoundingClientRect();
      line.style.setProperty('--p', Math.min(1, Math.max(0, (innerHeight * .85 - r.top) / (r.height + innerHeight * .2))));
    }
    if (tocLinks.length) {
      let current = null;
      tocLinks.forEach(a => { const t = document.querySelector(a.getAttribute('href')); if (t && t.getBoundingClientRect().top < 140) current = a; });
      tocLinks.forEach(a => a.classList.toggle('active', a === current));
    }
  }
  addEventListener('scroll', onScroll, { passive: true });
  onScroll();

  /* Reveal on scroll + count-up numbers */
  function countUp(el) {
    const to = +el.dataset.to;
    if (reduced || !to) { el.textContent = to; return; }
    const start = performance.now();
    (function tick(t) {
      const k = Math.min(1, (t - start) / 1200);
      el.textContent = Math.round(to * (1 - Math.pow(1 - k, 3)));
      if (k < 1) requestAnimationFrame(tick);
    })(start);
  }
  const io = new IntersectionObserver(entries => entries.forEach(e => {
    if (!e.isIntersecting) return;
    e.target.classList.add('in');
    e.target.querySelectorAll('.count').forEach(countUp);
    io.unobserve(e.target);
  }), { threshold: .12, rootMargin: '0px 0px -40px 0px' });
  $$('.reveal').forEach(el => io.observe(el));

  /* Smooth FAQ open/close */
  $$('details').forEach(d => {
    const summary = d.querySelector('summary'), body = d.querySelector('.faq-body');
    if (!body) return;
    summary.addEventListener('click', e => {
      if (reduced) return;
      e.preventDefault();
      if (d.open) {
        body.animate([{ height: body.offsetHeight + 'px' }, { height: '0px' }], { duration: 300, easing: 'ease' }).onfinish = () => d.open = false;
      } else {
        d.open = true;
        body.animate([{ height: '0px' }, { height: body.offsetHeight + 'px' }], { duration: 350, easing: 'ease' });
      }
    });
  });

  /* Rising bubbles in the closing call to action */
  const cta = $('#cta');
  if (cta && !reduced) {
    for (let i = 0; i < 8; i++) {
      const b = document.createElement('span'), size = 30 + Math.random() * 80;
      b.className = 'bubble';
      Object.assign(b.style, { width: size + 'px', height: size + 'px', left: Math.random() * 100 + '%', animationDelay: (-Math.random() * 12) + 's', animationDuration: (9 + Math.random() * 8) + 's' });
      cta.prepend(b);
    }
  }

  const year = $('#year');
  if (year) year.textContent = new Date().getFullYear();
})();
