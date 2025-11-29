# Quote_Scraper

Absolutely — here’s a polished, copy-paste **GitHub-ready README.md** for **Project 1**.
Includes proper markdown `#` headers, clean formatting, and beginner-friendly explanations.

---

# 📘 **README — Project 1: Quote Scraper (Beginner Web Scraping)**

## 🧠 **Overview**

This project is a beginner-friendly web scraping exercise using **Python**, **Requests**, **BeautifulSoup**, and **Pandas**.
You will scrape quotes from **[https://quotes.toscrape.com](https://quotes.toscrape.com)**, extract the text, and save the results into a CSV file.

This project teaches the 4-step scraping pattern used in almost every scraper:

**Fetch → Parse → Extract → Store**

---

## 🚀 **Features**

* Scrapes quote text from the homepage
* Parses HTML using BeautifulSoup
* Stores scraped data in Python lists
* Saves results to a clean CSV file
* Beginner-friendly, fully commented code
* Expandable challenge: extract author names

---

## 🛠️ **Technologies Used**

* Python 3
* Requests
* BeautifulSoup4
* Pandas

---

## 📦 **Installation**

Install dependencies:

```bash
pip install requests
pip install beautifulsoup4
pip install pandas
```

Clone this repository:

```bash
git clone YOUR_REPO_LINK_HERE
```

(Optional) Create a virtual environment:

```bash
python -m venv env
source env/bin/activate   # Mac/Linux
env\Scripts\activate      # Windows
```

---

## ▶️ **How to Run**

Run the script:

```bash
python project1_scrape_quotes.py
```

After running, you will find:

```
quotes_project1.csv
```

This file contains all the scraped quotes from the homepage.

---

## 💻 **Full Code (Main Script)**

```python
import requests
from bs4 import BeautifulSoup
import pandas as pd

# Step 1: Fetch the webpage
url = "https://quotes.toscrape.com/"
response = requests.get(url)
print("Status Code:", response.status_code)

# Step 2: Parse the page
soup = BeautifulSoup(response.text, "html.parser")

# Step 3: Extract the quotes
quote_divs = soup.find_all("div", class_="quote")

quotes_list = []

for q in quote_divs:
    quote_text = q.find("span", class_="text").get_text(strip=True)
    quotes_list.append(quote_text)

# Step 4: Save to CSV
df = pd.DataFrame({"quote": quotes_list})
df.to_csv("quotes_project1.csv", index=False)

print("Scraping complete! Saved to quotes_project1.csv")
```

---

## 📖 **How the Script Works**

### **1. Fetch**

Downloads the webpage using `requests.get()`.

### **2. Parse**

Reads the HTML using BeautifulSoup so Python can navigate it like a tree.

### **3. Extract**

Finds all `<div class="quote">` blocks and pulls out the text.

### **4. Store**

Uses pandas to save the list of quotes into a CSV file.

---

## ⚠️ **Common Errors**

| Issue                                | Cause                      | Fix                                   |
| ------------------------------------ | -------------------------- | ------------------------------------- |
| `ModuleNotFoundError`                | Requests/BS4 not installed | Install with `pip install`            |
| `NoneType has no attribute get_text` | Element not found          | HTML structure changed or typo        |
| CSV not found                        | Wrong folder               | Check where you're running the script |
| Status code not 200                  | Website unavailable        | Retry or check URL                    |

---

## 🧩 **Challenge**

Modify the script so that it **also extracts the author name** for each quote.

Helpful hint:

```python
author = q.find("small", class_="author").get_text(strip=True)
```

Add a new column to your CSV:

```python
df = pd.DataFrame({
    "quote": quotes_list,
    "author": authors_list
})
```

---

## 📜 **License**

This project is free to use for anyone learning web scraping.

---