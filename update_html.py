import re

def modify_html():
    with open('index.html', 'r', encoding='utf-8') as f:
        html = f.read()

    replacements = [
        (
            r'<p class="eyebrow mono">\s*Catatan pribadi &middot; Jakarta\s*</p>',
            r'<p class="eyebrow mono" data-id="Catatan pribadi &middot; Jakarta" data-en="Personal Notes &middot; Jakarta">Catatan pribadi &middot; Jakarta</p>'
        ),
        (
            r'<p class="tagline">\s*Ruang kecil tempat saya menulis tentang film, edukasi,\s*dan hal-hal sederhana yang saya temui sehari-hari.\s*</p>',
            r'<p class="tagline" data-id="Ruang kecil tempat saya menulis tentang film, edukasi, dan hal-hal sederhana yang saya temui sehari-hari." data-en="A small space where I write about movies, education, and simple things I encounter every day.">Ruang kecil tempat saya menulis tentang film, edukasi, dan hal-hal sederhana yang saya temui sehari-hari.</p>'
        ),
        (
            r'<a href="#tulisan" class="hero-cta">\s*Baca tulisan terbaru &nbsp;→\s*</a>',
            r'<a href="#tulisan" class="hero-cta" data-id="Baca tulisan terbaru &nbsp;→" data-en="Read latest posts &nbsp;→">Baca tulisan terbaru &nbsp;→</a>'
        ),
        (
            r'<p class="lens-caption">\s*Fokus &middot; di balik yang blur\s*</p>',
            r'<p class="lens-caption" data-id="Fokus &middot; di balik yang blur" data-en="Focus &middot; behind the blur">Fokus &middot; di balik yang blur</p>'
        ),
        (
            r'<h2 class="display">\s*Perihal\s*</h2>',
            r'<h2 class="display" data-id="Perihal" data-en="About">Perihal</h2>'
        ),
        (
            r'<span class="mono">\s*01 &mdash; Tentang saya\s*</span>',
            r'<span class="mono" data-id="01 &mdash; Tentang saya" data-en="01 &mdash; About me">01 &mdash; Tentang saya</span>'
        ),
        (
            r'<p>\s*Halo, saya Nixon. Blog ini saya mulai sebagai catatan pribadi — tempat menyimpan\s*pikiran yang kadang terlalu panjang untuk diketik di caption media sosial.\s*</p>',
            r'<p data-id="Halo, saya Nixon. Blog ini saya mulai sebagai catatan pribadi — tempat menyimpan pikiran yang kadang terlalu panjang untuk diketik di caption media sosial." data-en="Hello, I\'m Nixon. I started this blog as a personal note — a place to store thoughts that are sometimes too long to type in social media captions.">Halo, saya Nixon. Blog ini saya mulai sebagai catatan pribadi — tempat menyimpan pikiran yang kadang terlalu panjang untuk diketik di caption media sosial.</p>'
        ),
        (
            r'<p>\s*Saya suka mengamati beberapa film di layar lebar, mulai dari film holywood sampai Indonesia. Sebagian\s*besar tulisan di sini\s*lahir dari obrolan santai, perjalanan singkat, atau sekadar duduk memperhatikan\s*film yang sedang saya tonton.\s*</p>',
            r'<p data-id="Saya suka mengamati beberapa film di layar lebar, mulai dari film holywood sampai Indonesia. Sebagian besar tulisan di sini lahir dari obrolan santai, perjalanan singkat, atau sekadar duduk memperhatikan film yang sedang saya tonton." data-en="I like observing several movies on the big screen, from Hollywood to Indonesian movies. Most of the writings here are born from casual conversations, short trips, or just sitting and watching the movie I am watching.">Saya suka mengamati beberapa film di layar lebar, mulai dari film holywood sampai Indonesia. Sebagian besar tulisan di sini lahir dari obrolan santai, perjalanan singkat, atau sekadar duduk memperhatikan film yang sedang saya tonton.</p>'
        ),
        (
            r'<span class="tag">\s*Film\s*</span>',
            r'<span class="tag" data-id="Film" data-en="Movie">Film</span>'
        ),
        (
            r'<span class="tag">\s*Edukasi\s*</span>',
            r'<span class="tag" data-id="Edukasi" data-en="Education">Edukasi</span>'
        ),
        (
            r'<span class="tag">\s*Cerita harian\s*</span>',
            r'<span class="tag" data-id="Cerita harian" data-en="Daily story">Cerita harian</span>'
        ),
        (
            r'<span class="tag">\s*Pengalaman\s*</span>',
            r'<span class="tag" data-id="Pengalaman" data-en="Experience">Pengalaman</span>'
        ),
        (
            r'<h2 class="display">\s*Tulisan Terbaru\s*</h2>',
            r'<h2 class="display" data-id="Tulisan Terbaru" data-en="Latest Posts">Tulisan Terbaru</h2>'
        ),
        (
            r'<span class="mono">\s*02 &mdash; Arsip\s*</span>',
            r'<span class="mono" data-id="02 &mdash; Arsip" data-en="02 &mdash; Archive">02 &mdash; Arsip</span>'
        ),
        (
            r'<span class="mono">\s*08 Agt 2026\s*</span>',
            r'<span class="mono" data-id="08 Agt 2026" data-en="08 Aug 2026">08 Agt 2026</span>'
        ),
        (
            r'<h3>\s*Mengapa Film Odyssey Merupakan Film yang Patut di Apresiasi\s*</h3>',
            r'<h3 data-id="Mengapa Film Odyssey Merupakan Film yang Patut di Apresiasi" data-en="Why The Odyssey Movie Is A Movie Worth Appreciating">Mengapa Film Odyssey Merupakan Film yang Patut di Apresiasi</h3>'
        ),
        (
            r'<p>\s*Di luar dari banyak-nya kontroversi film the odyssey karya nolan. Film itu tetap harus di\s*apresiasi.\s*</p>',
            r'<p data-id="Di luar dari banyak-nya kontroversi film the odyssey karya nolan. Film itu tetap harus di apresiasi." data-en="Apart from the many controversies of Nolan\'s The Odyssey movie. The movie still deserves to be appreciated.">Di luar dari banyak-nya kontroversi film the odyssey karya nolan. Film itu tetap harus di apresiasi.</p>'
        ),
        (
            r'<span class="mono">\s*10 July 2025\s*</span>',
            r'<span class="mono" data-id="10 July 2025" data-en="10 July 2025">10 July 2025</span>'
        ),
        (
            r'<h3>\s*Pengalaman Mengunjungi Museum Kemerdekaan Indonesia\s*</h3>',
            r'<h3 data-id="Pengalaman Mengunjungi Museum Kemerdekaan Indonesia" data-en="Experience of Visiting the Indonesian Independence Museum">Pengalaman Mengunjungi Museum Kemerdekaan Indonesia</h3>'
        ),
        (
            r'<p>\s*Saya melihat sebuah kesederhanaan dibalik besarnya negara Indonesia.\s*</p>',
            r'<p data-id="Saya melihat sebuah kesederhanaan dibalik besarnya negara Indonesia." data-en="I see a simplicity behind the greatness of the Indonesian state.">Saya melihat sebuah kesederhanaan dibalik besarnya negara Indonesia.</p>'
        ),
        (
            r'<span class="mono">\s*27 Jul 2026\s*</span>',
            r'<span class="mono" data-id="27 Jul 2026" data-en="27 Jul 2026">27 Jul 2026</span>'
        ),
        (
            r'<h3>\s*Belajar dari Nolan\s*</h3>',
            r'<h3 data-id="Belajar dari Nolan" data-en="Learning from Nolan">Belajar dari Nolan</h3>'
        ),
        (
            r'<p>\s*Terkadang para producer hanya mencari film yang akan populer, namun sutradara mencari film yang\s*akan berkenan.\s*</p>',
            r'<p data-id="Terkadang para producer hanya mencari film yang akan populer, namun sutradara mencari film yang akan berkenan." data-en="Sometimes producers only look for movies that will be popular, but directors look for movies that will be memorable.">Terkadang para producer hanya mencari film yang akan populer, namun sutradara mencari film yang akan berkenan.</p>'
        ),
        (
            r'<h2 class="display">\s*Ngobrol&nbsp;yuk.\s*</h2>',
            r'<h2 class="display" data-id="Ngobrol&nbsp;yuk." data-en="Let\'s&nbsp;talk.">Ngobrol&nbsp;yuk.</h2>'
        ),
        (
            r'<p>\s*Punya cerita, kritik, atau sekadar mau menyapa\? Kotak masuk saya selalu terbuka\s*untuk obrolan baru.\s*</p>',
            r'<p data-id="Punya cerita, kritik, atau sekadar mau menyapa? Kotak masuk saya selalu terbuka untuk obrolan baru." data-en="Got a story, critique, or just want to say hi? My inbox is always open for a new chat.">Punya cerita, kritik, atau sekadar mau menyapa? Kotak masuk saya selalu terbuka untuk obrolan baru.</p>'
        ),
        (
            r'<a href="#">\s*Langganan email &nbsp;→\s*</a>',
            r'<a href="#" data-id="Langganan email &nbsp;→" data-en="Email subscription &nbsp;→">Langganan email &nbsp;→</a>'
        ),
        (
            r'<span>\s*© 2026 Nixon — Catatan Pribadi\s*</span>',
            r'<span data-id="© 2026 Nixon — Catatan Pribadi" data-en="© 2026 Nixon — Personal Notes">© 2026 Nixon — Catatan Pribadi</span>'
        ),
        (
            r'<span>\s*Dibuat dengan secangkir kopi\s*</span>',
            r'<span data-id="Dibuat dengan secangkir kopi" data-en="Made with a cup of coffee">Dibuat dengan secangkir kopi</span>'
        ),
        (
            r'<audio id="bgm" loop preload="none">.*?</audio>',
            r'''<audio id="bgm" loop preload="none">
                    <!-- Lofi music source from Pixabay (royalty free) -->
                    <source src="https://cdn.pixabay.com/audio/2022/05/27/audio_1808fbf07a.mp3" type="audio/mpeg">
                </audio>'''
        )
    ]

    for pattern, new in replacements:
        new_html = re.sub(pattern, new, html, flags=re.DOTALL)
        if new_html == html:
            print(f"Warning: Could not find snippet to replace for pattern:\n{pattern}\n")
        html = new_html
            
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html)

if __name__ == "__main__":
    modify_html()
