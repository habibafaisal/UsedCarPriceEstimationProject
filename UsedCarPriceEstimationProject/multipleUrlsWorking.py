import requests
from bs4 import BeautifulSoup
import pandas as pd

# define the URLs to scrape
urls = ["https://www.pakwheels.com/used-cars/search/-/mk_suzuki/md_alto/md_cultus/md_wagon-r/md_swift/?page=",
        # "https://www.pakwheels.com/used-cars/search/-/mk_toyota/md_corolla/?page=",
        # "https://www.pakwheels.com/used-cars/search/-/mk_honda/md_civic/?page="
        ]

all_data = []

# loop through each URL and page, and scrape the data
for url in urls:
    for page in range(1, 400):
        full_url = url + str(page)
        response = requests.get(full_url)
        soup = BeautifulSoup(response.content, 'html.parser')

        listings = soup.find_all('div', class_='price-details generic-dark-grey')
        pricesList = []
        for listing in listings:
            price_string = listing.get_text(strip=True)
            try:
                # try to extract the numeric value from the price string
                price = float(price_string.replace("PKR", "").replace("lacs", "").replace(" ", ""))
            except ValueError:
                # if the value is not numeric, replace it with "N/A"
                price = "N/A"
            pricesList.append(price)

        citiesListing = soup.select('ul.search-vehicle-info')
        citiesList = []

        for ul in citiesListing:
            citiesString = ul.get_text(strip=True)
            print(citiesString)
            citiesList.append(citiesString)

            # try:
            #     print('working')
            #     cities = (li.get_text(strip=True) for li in ul.select("li"))
            # except ValueError:
            #     print('not working')
            #     price = "N/A"
            # print("============================================================")
            # print(cities)


        info = soup.select("ul.search-vehicle-info-2")
        for i, ul in enumerate(info):
            car_name = ul.find_previous("h3").get_text(strip=True)
            car_name = car_name.split("for Sale")[0].strip()
            car_info = [li.get_text(strip=True) for li in ul.select("li")]
            all_data.append([car_name, *car_info, pricesList[i],citiesList[i]])
            # print(all_data)

# create a pandas dataframe and save the data to a CSV file
df = pd.DataFrame(
    all_data, columns=["Car Name", "Year", "KM", "Type", "CC", "Transmission", "Price", "Cities"]
)
df.to_csv("finalData.csv", mode="a", header=True, index=False)
print('Scraping completed and data saved to finalData.csv.')
# print(df)
print(citiesList)