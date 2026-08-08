
# Update HTML – add hamburger button
with open('Landing.html', 'r', encoding='utf-8') as f:
    html = f.read()

btn = (
    '<button type="button" class="icon-btn hamburger-btn" id="menuToggle" '
    'aria-label="Toggle menu" title="Menu">'
    '<span class="ham-icon">'
    '<svg viewBox="0 0 24 24"><path d="M4 6h16M4 12h16M4 18h16"></path></svg>'
    '</span></button>\n                '
)

target = '<button type="button" class="icon-btn" id="langToggle"'
if 'id="menuToggle"' not in html:
    html = html.replace(target, btn + target)
    with open('Landing.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print('HTML OK')
else:
    print('HTML already done')

# Update JS – hamburger toggle logic
with open('Landing.js', 'r', encoding='utf-8') as f:
    js = f.read()

jscode = """
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
"""

if 'Hamburger Menu' not in js:
    with open('Landing.js', 'a', encoding='utf-8') as f:
        f.write(jscode)
    print('JS OK')
else:
    print('JS already done')

# Update CSS – hamburger styles
with open('Landing.css', 'r', encoding='utf-8') as f:
    css = f.read()

csscode = """
/* ---------- Hamburger Responsive Nav ---------- */
.hamburger-btn { display: none; }
.ham-icon svg { width:20px; height:20px; stroke:currentColor; fill:none; stroke-width:2; stroke-linecap:round; stroke-linejoin:round; }

@media(max-width:640px){
  .hamburger-btn { display: flex; }

  .nav {
    position: relative;
    flex-direction: row;
    flex-wrap: nowrap;
    justify-content: flex-end;
    align-items: center;
    gap: 8px;
    padding: 18px 16px 0;
  }

  .nav-tools { order: 0; }

  .pillbar {
    display: none !important;
    position: absolute;
    top: calc(100% + 10px);
    left: 50%;
    transform: translateX(-50%);
    width: 88vw;
    flex-direction: column;
    gap: 4px;
    background: rgba(21,19,17,0.97);
    backdrop-filter: blur(24px);
    -webkit-backdrop-filter: blur(24px);
    border: 1px solid rgba(244,239,227,0.22);
    border-radius: 18px;
    padding: 14px;
    z-index: 200;
    animation: hamSlideDown 0.22s ease;
  }

  .pillbar.show { display: flex !important; }

  .pillbar a {
    border-radius: 10px;
    padding: 12px 18px;
    text-align: center;
    font-size: 13px;
    white-space: nowrap;
  }
}

@keyframes hamSlideDown {
  from { opacity: 0; transform: translateX(-50%) translateY(-8px); }
  to   { opacity: 1; transform: translateX(-50%) translateY(0); }
}
"""

if 'hamburger-btn' not in css:
    with open('Landing.css', 'a', encoding='utf-8') as f:
        f.write(csscode)
    print('CSS OK')
else:
    print('CSS already done')

print('All done!')
