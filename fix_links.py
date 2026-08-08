with open('Landing.html', 'r', encoding='utf-8') as f:
    html = f.read()

replacements = [
    ('post.html?id=odyssey-nolan',   '08 Agt 2026'),
    ('post.html?id=museum-kemerdekaan', '10 July 2025'),
    ('post.html?id=belajar-dari-nolan', '27 Jul 2026'),
]

for href, date in replacements:
    old = f'<a class="post" href="#">\n                <span class="mono" data-id="{date}"'
    new = f'<a class="post" href="{href}">\n                <span class="mono" data-id="{date}"'
    if old in html:
        html = html.replace(old, new)
        print(f'Updated: {href}')
    else:
        print(f'NOT FOUND for date: {date}')

with open('Landing.html', 'w', encoding='utf-8') as f:
    f.write(html)

print('Done!')
