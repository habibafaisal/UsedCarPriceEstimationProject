import requests
from bs4 import BeautifulSoup
import pandas as pd


url = "https://www.pakwheels.com/used-cars/search/-/mk_suzuki/md_wagon-r/ct_karachi/ct_lahore/ct_rawalpindi"
response = requests.get(url)

soup = BeautifulSoup(response.content, 'html.parser')

listings = soup.find_all('div', class_='price-details generic-dark-grey')
pricesList = []
# prices
for listing in listings:
    prices = listing.get_text(strip=True)
    # print(prices)
    pricesList.append(prices)


info = soup.select("ul.search-vehicle-info-2")

all_data = []

for ul in info:
    car_name = ul.find_previous("h3").get_text(strip=True)
    car_name = car_name.split("for Sale")[0].strip()
    info = [li.get_text(strip=True) for li in ul.select("li")]
    all_data.append([car_name, *info])


df = pd.DataFrame(
    all_data, columns=["Car Name", "Year", "KM", "Type", "CC", "Transmission"]
)
df.to_csv("data.csv", mode="a", header=True, index=False)

aa = pd.read_csv("data.csv")

print(prices)
aa.insert(6, column = "Prices", value = pricesList)

print('work')
print(aa)
aa.to_csv("finalData.csv", mode="a", header=True, index=False)
print('workingg')
