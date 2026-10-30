(function () {
  var sidebar = document.getElementById('sidebar');
  var toggle = document.querySelector('.menu-toggle');
  var links = Array.prototype.slice.call(document.querySelectorAll('.sidebar a[data-target]'));

  toggle.addEventListener('click', function () {
    var open = sidebar.classList.toggle('open');
    toggle.setAttribute('aria-expanded', String(open));
  });

  links.forEach(function (link) {
    link.addEventListener('click', function () {
      sidebar.classList.remove('open');
      toggle.setAttribute('aria-expanded', 'false');
    });
  });

  var sections = links.map(function (l) { return document.getElementById(l.dataset.target); });

  var observer = new IntersectionObserver(function (entries) {
    entries.forEach(function (entry) {
      if (!entry.isIntersecting) return;
      links.forEach(function (l) {
        l.classList.toggle('active', l.dataset.target === entry.target.id);
      });
    });
  }, { rootMargin: '-20% 0px -70% 0px' });

  sections.forEach(function (s) { if (s) observer.observe(s); });
})();
