import requests
from bs4 import BeautifulSoup

url = "https://www.pakwheels.com/used-cars/search/-/mk_suzuki/md_wagon-r/ct_karachi/ct_lahore/ct_rawalpindi"
response = requests.get(url)

soup = BeautifulSoup(response.content, 'html.parser')

listings = soup.find_all('div', class_='price-details generic-dark-grey')

# prices
for listing in listings:
    abc = listing.get_text(strip=True)
    print(abc)


