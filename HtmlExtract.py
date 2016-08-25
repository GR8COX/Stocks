import requests
from bs4 import BeautifulSoup


def parseHtml(url):

    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    #pattern = re.compile('Net Income')

    titles = soup.findAll('td', {'class': 'rowTitle'})
    for title in titles:
        if 'EPS (Basic)' in title.text:
            x = (td.text
            for td in title.findNextSiblings(attrs={'class': 'valueCell'}) if td.text)
            print(x)
    #row = titles.parent.parent
    #cells = row.find_all('td')[1:]

    #values = [c.text.strip() for c in cells]
    #print(values)
