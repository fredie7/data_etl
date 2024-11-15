import requests
from bs4 import BeautifulSoup as bs
import pandas as pd

#list of URL's for each page.
pages = []

# Loop through the first 5 pages.
for page_number in range(1, 5):
    url_start = 'https://www.centralcharts.com/en/price-list-ranking/ALL/asc/ts_36-uk-stocks--qc_1-alphabetical-order?p='
    url = url_start + str(page_number)
    pages.append(url)

# Get the <th> tag contents for the header.
webpage = requests.get(pages[0])
soup = bs(webpage.text, 'html.parser')
stock_table = soup.find('table', class_='tabMini tabQuotes')
th_tag_list = stock_table.find_all('th')

headers = []
for each_tag in th_tag_list:
    title = each_tag.text
    headers.append(title)

new_headers = []
for header in headers:
    if header not in ('Cap.', 'Issued Cap.', ''):
        new_headers.append(header)
headers = new_headers
uk_stock_data = pd.DataFrame(columns = headers)


# Loop through each page.
for page in pages:
    webpage = requests.get(page)
    soup = bs(webpage.text, 'html.parser')

    if soup.find('table'):
        stock_table = soup.find('table', class_='tabMini tabQuotes')
        tr_tag_list = stock_table.find_all('tr')

        for each_tr_tag in tr_tag_list[1:]:
            td_tag_list = each_tr_tag.find_all('td')

            row_values = []
            for each_td_tag in td_tag_list[0:7]:
                new_value = each_td_tag.text.strip()
                row_values.append(new_value)

            uk_stock_data.loc[len(uk_stock_data)] = row_values

# Switch data types and sort by the trading volume
uk_stock_data[['Financial instrument', 'Current price', 'Change(%)', 'Open','High', 'Low']] = \
    uk_stock_data[['Financial instrument', 'Current price', 'Change(%)', 'Open', 'High', 'Low']] \
    .astype(str)

uk_stock_data.replace({'Current price': {',':'', '-':'1'},
                  'Change(%)': {',':'', '-':'1', '%':''},
                  'Open': {',':'', '-':'1'},
                  'High': {',':'', '-':'1'},
                  'Low': {',':'', '-':'1'},
                  'Volume': {',':'', '-':'1'}
}, regex=True, inplace=True)

uk_stock_data[['Current price', 'Change(%)', 'Open', 'High', 'Low', 'Volume']] = \
    uk_stock_data[['Current price', 'Change(%)', 'Open', 'High', 'Low', 'Volume']]. \
    apply(pd.to_numeric)

uk_stock_data = uk_stock_data.sort_values(by=['Volume'], ascending=False)
uk_stock_data.rename(columns={'change(%)': 'percentage_change'}, inplace=True)


uk_stock_data.columns = uk_stock_data.columns.str.lower().str.replace(" ", "_")
uk_stock_data.rename(columns={'change(%)': 'percentage_change'}, inplace=True)

# Save the data to a CSV file.
uk_stock_data.to_csv('uk_stock_data.csv', index=False)
print(uk_stock_data.head())