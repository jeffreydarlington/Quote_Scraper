import requests
from bs4 import BeautifulSoup
import pandas as pd

url_quotes = "http://quotes.toscrape.com/"
response_get = requests.get(url_quotes)

print("Status Code:", response_get.status_code)

soup = BeautifulSoup(response_get.text, 'html.parser')

quote_divs = soup.find_all("div", class_="quote")

quotes_list = []

for q in quote_divs:
    quote_text = q.find("span", class_="text").get_text(strip=True)
    author = q.find("small", class_="author").get_text(strip=True)

    full_quote_list = [quote_text, author]
    quotes_list.append(full_quote_list)

df = pd.DataFrame({
    "Quotes:": quotes_list
})
df.to_csv("quotes.csv", index=False)
print("Scraping has been complete! Quotes have been saved to quotes.csv")
