import requests
from bs4 import BeautifulSoup
import csv

url = "https://www.sanskrit-trikashaivism.com/en/patanjali-yoga-sutras/629"

r = requests.get(url)
soup = BeautifulSoup(r.content, "html.parser")

# This setup may require adjustment based on actual html structure:
results = []
# blocks = soup.find_all("div", class_="sutra-block")  # adjust tag/class as needed
blocks = soup.find_all("span", class_="unicodesfont")  # adjust tag/class as needed

for block in blocks:
    print(f"Block: {block}")
    sutra = block.get_text(strip=True)
    #dev = block.find("div", class_="devanagari").get_text(strip=True)
    #iast = block.find("div", class_="iast").get_text(strip=True)
    #eng = block.find("div", class_="explanation").get_text(strip=True)
    results.append([sutra])
    #results.append([dev, iast, eng])

with open("yoga_sutras.csv", "w", encoding="utf-8", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Devanagari", "IAST", "English"])
    writer.writerows(results)
