
(function(){
  var root = document.documentElement;
  function setTheme(t){
    if (t) root.setAttribute('data-theme', t); else root.removeAttribute('data-theme');
    try { localStorage.setItem('theme', t || ''); } catch(e){}
    renderThemeBtn();
  }
  function currentIsDark(){
    var explicit = root.getAttribute('data-theme');
    if (explicit) return explicit === 'dark';
    return window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches;
  }
  function renderThemeBtn(){
    var btn = document.getElementById('theme-btn');
    btn.innerHTML = currentIsDark() ? ICON_SUN : ICON_MOON;
  }
  try {
    var saved = localStorage.getItem('theme');
    if (saved) root.setAttribute('data-theme', saved);
  } catch(e){}

  var ICON_MOON = '<svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor"><path d="M21 12.79A9 9 0 1 1 11.21 3a7 7 0 0 0 9.79 9.79Z"/></svg>';
  var ICON_SUN = '<svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor"><circle cx="12" cy="12" r="4.2"/><g stroke="currentColor" stroke-width="1.8" stroke-linecap="round"><path d="M12 2v2.2M12 19.8V22M4.2 4.2l1.55 1.55M18.25 18.25l1.55 1.55M2 12h2.2M19.8 12H22M4.2 19.8l1.55-1.55M18.25 5.75l1.55-1.55"/></g></svg>';
  renderThemeBtn();

  document.getElementById('theme-btn').addEventListener('click', function(){
    setTheme(currentIsDark() ? 'light' : 'dark');
  });

  var menuBtn = document.getElementById('menu-btn');
  var mobileMenu = document.getElementById('mobile-menu');
  menuBtn.addEventListener('click', function(){ mobileMenu.hidden = !mobileMenu.hidden; });

  var pages = document.querySelectorAll('.page');
  var navLinks = document.querySelectorAll('[data-page]');
  function show(page){
    pages.forEach(function(p){ p.classList.toggle('active', p.id === 'page-' + page); });
    navLinks.forEach(function(a){ a.classList.toggle('active', a.getAttribute('data-page') === page); });
    mobileMenu.hidden = true;
    window.scrollTo({top:0});
  }
  function routeFromHash(){
    var h = location.hash.replace('#/', '') || 'home';
    if (!document.getElementById('page-' + h)) h = 'home';
    show(h);
  }
  window.addEventListener('hashchange', routeFromHash);
  routeFromHash();
})();
