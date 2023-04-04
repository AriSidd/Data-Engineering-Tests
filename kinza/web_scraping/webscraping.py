from bs4 import BeautifulSoup
import html5lib
import requests
import pandas as pd

import requests
from bs4 import BeautifulSoup
import json


import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://web.archive.org/web/20200318083015/https://en.wikipedia.org/wiki/List_of_largest_banks"
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")


data = pd.DataFrame(columns=["Name", "Market Cap (US$ Billion)"])

for row in soup.find_all('tbody')[2].find_all('tr'):
    col = row.find_all('td')






# table = soup.find("table", {"class": "wikitable sortable"})
# rows = table.findAll("tr")[1:]

# data = []

# for row in rows:
#     cols = row.findAll("td")
#     data.append({
#         "name": cols[1].text.strip(),
#         "market_cap": cols[2].text.strip()
#     })

# df = pd.DataFrame(data)
# df.columns = ['Bank Name', 'Market Cap (US$ Billion)']
# print(df.head())










# url = "https://web.archive.org/web/20200318083015/https://en.wikipedia.org/wiki/List_of_largest_banks"
# response = requests.get(url)
# soup = BeautifulSoup(response.content, "html.parser")

# table = soup.find("table", {"class": "wikitable sortable"})
# rows = table.findAll("tr")[1:]

# data = []

# for row in rows:
#     cols = row.findAll("td")
#     data.append({
#         "rank": cols[0].text.strip(),
#         "name": cols[1].text.strip(),
#         "market_cap": cols[2].text.strip(),
#         "country": cols[3].text.strip()
#     })

# with open("largest_banks.json", "w") as f:
#     json.dump(data, f)
