import requests
import pandas as pd
from bs4 import BeautifulSoup



def scrape_data(url):
    all_data = []

    for page in range(1, 3):
        page_url = f"{url}&page={page}"
        soup = BeautifulSoup(requests.get(page_url).content, "html.parser")
        listings = soup.select("ul.search-vehicle-info-2")


        for ul in listings:
            car_name = ul.find_previous("h3").get_text(strip=True)
            car_name = car_name.split("for Sale")[0].strip()
            info = [li.get_text(strip=True) for li in ul.select("li")]
            all_data.append([car_name, *info])

    return all_data


# Scrape data for the first URL
url1 = "https://www.pakwheels.com/used-cars/search/-/mk_suzuki/md_alto/ct_karachi/ct_lahore/ct_rawalpindi"
data1 = scrape_data(url1)

# Write the data to the CSV file
df = pd.DataFrame(
    data1, columns=["Car Name", "Year", "KM", "Type", "CC", "Transmission"]
)
df.to_csv("data.csv", mode="a", header=True, index=False)

# Scrape data for the second URL
url2 = "https://www.pakwheels.com/used-cars/search/-/mk_suzuki/md_wagon-r/ct_karachi/ct_lahore/ct_rawalpindi"
data2 = scrape_data(url2)

# Append the data to the CSV file
df = pd.DataFrame(
    data2, columns=["Car Name", "Year", "KM", "Type", "CC", "Transmission"]
)
df.to_csv("data.csv", mode="a", header=False, index=False)

# Scrape data for the third URL
url3 = "https://www.pakwheels.com/used-cars/search/-/mk_suzuki/ct_karachi/ct_lahore/ct_rawalpindihttps:/ct_rawalpindi/md_swift/"
data3 = scrape_data(url3)

# Append the data to the CSV file
df = pd.DataFrame(
    data3, columns=["Car Name", "Year", "KM", "Type", "CC", "Transmission"]
)
df.to_csv("data.csv", mode="a", header=False, index=False)

print('Done!')
