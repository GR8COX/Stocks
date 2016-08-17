import urllib.request
import re, requests
from bs4 import BeautifulSoup


def parseHtml(url):

    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    pattern = re.compile('Net Income')

    title = soup.findAll('strong')
    row = title.parent.parent
    cells = row.find_all('td')[1:]

    values = [c.text.strip() for c in cells]
    print(values)
