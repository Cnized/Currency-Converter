import os
import json
import requests

url = "https://v6.exchangerate-api.com/v6/76d4bf7e0ac1cbc286461dd7/latest/USD"

API = os.environ['Exchangerate_API_KEY']
params = {
    "apikey": API
}   
response = requests.get(url, params=params)
data = response.json()

rates = data['conversion_rates']

def currency_convertor(amount, from_currency, to_currency):
    if from_currency != 'USD':
        amount = amount * (rates[to_currency] / rates[from_currency])
    else:
        amount = amount * rates[to_currency]
        
    return amount

while True:
    print("Select from available currencies: ")
    for x in rates.keys():
        print(x)
    from_currency = input("From Currency: ").upper()
    to_currency = input("To Currency: ").upper()
    amount = float(input("Amount: "))
    converted_amount = currency_convertor(amount, from_currency, to_currency)
    print(f"{amount} {from_currency} = {converted_amount} {to_currency}")
    again = input("Do you want to convert another amount? (yes/no): ").lower()
    if again != 'yes':
        break
