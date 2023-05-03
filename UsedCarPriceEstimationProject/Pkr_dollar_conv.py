from currency_converter import CurrencyConverter
c = CurrencyConverter()
print(c.convert(100, 'EUR', 'USD'))
# print('rates')
# print(c.convert(100, 'PKR', 'USD'))

from forex_python.converter import CurrencyRates
Ac = CurrencyRates()
print(Ac.get_rates('USD'))

# working one


import requests


def pkr_to_usd(amount):
    # Get the current exchange rate from Open Exchange Rates API
    response = requests.get("https://openexchangerates.org/api/latest.json?app_id=09ac8c09dee6454a99f68fa54e589af9")
    rates = response.json()["rates"]
    pkr_rate = rates["PKR"]
    print(pkr_rate)
    usd_rate = rates["USD"]

    # Convert PKR to USD
    # usd_amount = amount / pkr_rate * usd_rate
    usd_amount = amount * pkr_rate #slightly changing

    return usd_amount

print(pkr_to_usd(500))