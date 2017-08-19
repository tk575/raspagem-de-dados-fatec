import sys
from urllib.request import urlopen
from bs4 import BeautifulSoup

url = 'http://www.fatecjd.edu.br/site/a-fatec-jd/corpo-docente'
html = urlopen(url)

bsObj = BeautifulSoup(html.read(), 'html.parser')

body = bsObj.tbody
rows = body.findAll('tr')

for row in rows:
    name = row.find('td').text

    if sys.argv[1].upper() in name:
        print(row.text)
