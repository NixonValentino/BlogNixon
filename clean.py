import re
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()
html = re.sub(r'<img[^>]+>', '<img>', html)
html = re.sub(r'data:image/[^\"]+', '', html)
with open('clean.html', 'w', encoding='utf-8') as f:
    f.write(html)
