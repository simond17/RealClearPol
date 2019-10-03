from selenium import webdriver
import pandas as pd
from bs4 import BeautifulSoup
import urllib


def get_real_clear():
    driver = webdriver.Chrome()
    driver.get(
        'https://www.realclearpolitics.com/epolls/2020/president/us/2020_democratic_presidential_nomination-6730.html')
    driver.find_element_by_xpath("//*[@id='more_table_data']").click()
    driver.find_element_by_xpath("//*[@id='more_table_data']").click()
    page = driver.page_source

    soup = BeautifulSoup(page)

    data = []
    table = soup.find_all('table')[3]
    rows = table.find_all('tr')
    columns = rows[0].find_all('th')
    columns = [i.get_text() for i in columns]

    for row in rows[2:]:
        cols = row.find_all('td')
        cols = [ele.text.strip() for ele in cols]
        data.append([ele for ele in cols if ele])

    data = pd.DataFrame(data)
    data.columns = columns

    return data
import numpy as np
x = np.array([[1]])
x.shape
def clean_data():




data = get_real_clear()

data['Poll'].unique()