import string

with open('morse.html', encoding='utf-8') as f:
    text = f.read()

text = text.split('\n')
for line in text:
    letters = line.strip()
    if not letters.startswith('<td class="original">'):
        continue
    letters = line.strip()
    letters = letters.replace('<td class="original">','')
    letters = letters.replace('</td>', '')
    print(letters[:4])