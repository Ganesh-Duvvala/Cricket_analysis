import requests
from bs4 import BeautifulSoup
import pandas as pd
url='https://www.scrapethissite.com/pages/forms/'
page = requests.get(url)
a= BeautifulSoup(page.text,"html")
table1 = (a.find('table'))
titles = (table1.find_all('th'))
headers = [title.text.strip() for title in titles]
df = pd.DataFrame(columns = headers)
column_data = table1.find_all('tr')
for row in column_data[1:]:
    row_data = row.find_all("td")
    all_rows = [row_text.text.strip() for row_text in row_data]
    length = len(df)
    df.loc[length] = all_rows

    