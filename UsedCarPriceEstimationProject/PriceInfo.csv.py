import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://www.pakwheels.com/used-cars/search/-/mk_suzuki/md_wagon-r/ct_karachi/ct_lahore/ct_rawalpindi"
response = requests.get(url)

soup = BeautifulSoup(response.content, 'html.parser')

listings = soup.find_all('div', class_='price-details generic-dark-grey')

prices = []
# prices
for listing in listings:
    abc = listing.get_text(strip=True)
    prices.append(abc)
    print(abc)


info = soup.select("ul.search-vehicle-info-2")

all_data = []

for ul in info:
    car_name = ul.find_previous("h3").get_text(strip=True)
    car_name = car_name.split("for Sale")[0].strip()
    info = [li.get_text(strip=True) for li in ul.select("li")]
    all_data.append([car_name, *info])

    # print(car_name)
    # print(*info)

# df = pd.DataFrame(
#     all_data, columns=["Car Name", "Year", "KM", "Type", "CC", "Transmission","Prices"]
# )
# df.to_csv("data.csv", mode="a", header=True, index=False)
# print(df)


zipped_value_name = list(zip(all_data, prices))

final_list = []
for row in zipped_value_name:
    final_list.append(row)
    print(row)

import csv

with open('numbers.csv', 'w', newline='') as csvfile:
    fieldnames = ['col1', 'col2']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for i, j in zip(all_data, prices):
        writer.writerow({'col1': i, 'col2': j})


#
# print('done')
# # df = pd.DataFrame(
# #     all_data + prices, columns=["Car Name", "Year", "KM", "Type", "CC", "Transmission","Prices"]
# # )
# df = pd.DataFrame(
#     final_list= final_list
# )
# df.to_csv("data.csv", mode="a", header=True, index=False)
# print(df)
# print('done again')
