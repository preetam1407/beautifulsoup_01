import requests
from bs4 import BeautifulSoup
import pandas as pd

data = {"title":[], "Price":[]}

proxies = {
  "http": "http://10.10.1.10:3128",
  "https": "https://10.10.1.10:1080",
}

url = "https://www.flipkart.com/search?q=samsung+mobile&as=on&as-show=on&otracker=AS_Query_OrganicAutoSuggest_5_8_na_na_na&otracker1=AS_Query_OrganicAutoSuggest_5_8_na_na_na&as-pos=5&as-type=RECENT&suggestionId=samsung+mobile&requestId=e2dfea76-c3f3-4a2b-802a-84750653358b&as-searchtext=smasung%20"
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

r = requests.get(url, headers=headers)

soup = BeautifulSoup(r.text, 'html.parser')


spans = soup.select("div._4rR01T")
for span in spans:
    # print(span.string)
    data["title"].append(span.string)

prices = soup.select("div._30jeq3._1_WHN1")

for price in prices:
    # print(price.string)
    data["Price"].append(price.get_text())


df = pd.DataFrame.from_dict(data)
df.to_excel("data.xlsx", index = False)

