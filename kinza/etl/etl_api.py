# ETL with API

import requests

url = "https://api.apilayer.com/exchangerates_data/latest?base=EUR&apikey=VBBmj4YcycSXaVMpm4wk8tAgphoEiuTh"

response = requests.get(url)

text = response.text

print(text[:100]) # Print the first 100 characters of the response text
