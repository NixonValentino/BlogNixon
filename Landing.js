(function(){
    var lensWrap = document.getElementById('lensWrap');
    var lens = document.getElementById('lens');
    var lensImg = document.getElementById('lensImg');
    var hero = document.querySelector('.hero');
    if(!lensWrap || !hero) return;

    var reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

    function positionImageFromEvent(clientX, clientY){
      var rect = hero.getBoundingClientRect();
      var xRatio = (clientX - rect.left) / rect.width;
      var yRatio = (clientY - rect.top) / rect.height;
      xRatio = Math.max(0, Math.min(1, xRatio));
      yRatio = Math.max(0, Math.min(1, yRatio));
      var imgW = 900, imgH = 1350, lensSize = 220;
      var offsetX = -(xRatio * (imgW - lensSize));
      var offsetY = -(yRatio * (imgH - lensSize));
      lensImg.style.transform = 'translate(' + offsetX + 'px,' + offsetY + 'px)';
    }

    if(!reduceMotion){
      hero.addEventListener('mousemove', function(e){
        positionImageFromEvent(e.clientX, e.clientY);
      });
    }

    // sensible default position
    lensImg.style.top = '0px';
    lensImg.style.left = '0px';
  })();

  // ---------- Translate ID / EN ----------
  (function(){
    var btn = document.getElementById('langToggle');
    if(!btn) return;
    
    var currentLang = localStorage.getItem('langPref') || 'id';

    function updateLanguageDOM(lang) {
      var nodes = document.querySelectorAll('[data-id][data-en]');
      nodes.forEach(function(node){
        node.innerHTML = lang === 'en' ? node.getAttribute('data-en') : node.getAttribute('data-id');
      });
      document.documentElement.lang = lang;
      btn.textContent = lang === 'en' ? 'ID' : 'EN';
      btn.title = lang === 'en' ? 'Beralih ke Bahasa Indonesia' : 'Switch to English';
      currentLang = lang;
      localStorage.setItem('langPref', lang);
    }

    function applyLang(lang){
      var nodes = document.querySelectorAll('[data-id][data-en]');
      
      nodes.forEach(function(node){
        node.classList.add('fade-out');
      });

      setTimeout(function(){
        updateLanguageDOM(lang);
        nodes.forEach(function(node){
          node.classList.remove('fade-out');
        });
      }, 300);
    }

    updateLanguageDOM(currentLang);

    btn.addEventListener('click', function(){
      applyLang(currentLang === 'id' ? 'en' : 'id');
    });
  })();

  // ---------- Music toggle ----------
  (function(){
    var btn = document.getElementById('musicToggle');
    var audio = document.getElementById('bgm');
    if(!btn || !audio) return;

    btn.addEventListener('click', function(){
      // Belum ada file musik? tombol tetap bisa diklik, tapi tidak akan memutar apa pun
      // sampai kamu menambahkan <source> di dalam tag <audio id="bgm">.
      if(audio.paused){
        audio.play().then(function(){
          btn.classList.add('is-active');
        }).catch(function(){
          console.warn('Belum ada file musik yang ditambahkan ke tag <audio id="bgm">.');
        });
      } else {
        audio.pause();
        btn.classList.remove('is-active');
      }
    });

    audio.addEventListener('ended', function(){
      btn.classList.remove('is-active');
    });
  })();
  // ---------- Hamburger Menu ----------
  (function(){
    var menuBtn = document.getElementById('menuToggle');
    var pillbar = document.querySelector('.pillbar');
    if(!menuBtn || !pillbar) return;
    menuBtn.addEventListener('click', function(){
      var open = pillbar.classList.toggle('show');
      menuBtn.setAttribute('aria-expanded', String(open));
    });
    document.querySelectorAll('.pillbar a').forEach(function(a){
      a.addEventListener('click', function(){ pillbar.classList.remove('show'); });
    });
    document.addEventListener('click', function(e){
      if(!e.target.closest('.nav')){ pillbar.classList.remove('show'); }
    });
  })();
