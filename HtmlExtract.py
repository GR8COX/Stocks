import requests
from bs4 import BeautifulSoup


def parseHtml(url):

    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    #pattern = re.compile('Net Income')

    titles = soup.findAll('td', {'class': 'rowTitle'})
    for title in titles:
        if 'EPS (Basic) Growth' in title.text:
            continue
        if 'EPS (Basic)' in title.text:
            y = title.parent
            yParent = y.parent
            nextY = y.findAll('td', {'class': 'valueCell'})
            for z in nextY:
                text = z.getText()
                print(text)

    #row = titles.parent.parent
    #cells = row.find_all('td')[1:]

    #values = [c.text.strip() for c in cells]
    #print(values)
