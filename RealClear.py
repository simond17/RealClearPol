
import pandas as pd
from bs4 import BeautifulSoup
import urllib


def get_real_clear():

    url = f"https://www.realclearpolitics.com/epolls/2020/president/us/2020_democratic_presidential_nomination-6730.html"
    content = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(content)

    data = []
    table = soup.find_all('table')[-1]
    rows = table.find_all('tr')
    for row in rows:
        cols = row.find_all('td')
        cols = [ele.text.strip() for ele in cols]
        data.append([ele for ele in cols if ele])

    data = pd.DataFrame(data)

    return data

