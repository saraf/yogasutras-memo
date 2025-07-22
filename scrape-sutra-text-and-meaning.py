import requests
from bs4 import BeautifulSoup
import csv

url = "https://www.sanskrit-trikashaivism.com/en/patanjali-yoga-sutras/629"
r = requests.get(url)
soup = BeautifulSoup(r.content, "html.parser")

# Collect all 'sutra' paragraphs only (excluding chapter-endings)
ps = [
    p for p in soup.find_all('p', class_='alignmentcentered')
    if "Here concludes the" not in p.get_text()
]

results = []

for i in ps:
    content = i.get_text()
    results.append([content])

'''
for i in range(0, len(ps)-1, 2):
    p1 = ps[i]
    p2 = ps[i+1]

    # Devanagari
    orig_span = p1.find('span', class_='unicodesfont')
    original = orig_span.get_text(strip=True) if orig_span else ''
    # IAST Transliteration: text after <br>
    translit = ''
    found_br = False
    for x in p1.children:
        if found_br:
            translit += str(x)
        if x.name == 'br':
            found_br = True
    translit = BeautifulSoup(translit, 'html.parser').get_text(strip=True)

    # Meaning (strip all tags, concatenate spans)
    meaning = p2.get_text(separator=' ', strip=True)

    results.append([original, translit, meaning])
'''

with open("patanjali_sutras_four.csv", "w", newline='', encoding="utf-8") as f:
    writer = csv.writer(f)
    #writer.writerow(['Original', 'Transliteration', 'Meaning'])
    #writer.writerow(['Original', 'Transliteration', 'Meaning'])
    writer.writerows(results)

print(f"Wrote {len(results)} sutras to patanjali_sutras.csv")
