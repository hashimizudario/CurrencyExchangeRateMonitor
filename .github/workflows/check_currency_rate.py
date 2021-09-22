import requests
import argparse

parser = argparse.ArgumentParser(description='Exchange Currencies.')
parser.add_argument('-k', type=str, help='access key of currencylayer.com')
parser.add_argument('-s', type=str, help='source currency, default CNY', default="CNY")
parser.add_argument('-t', type=str, help='target currency, default CAD', default="CAD")
args = parser.parse_args()

access_key = args.k
# TODO: use github actions secrets
source_currency = args.s
target_currency = args.t
default_data_head = "USD"
# currencylayer.com api free account only provides USD based currency exchange rates
url = "http://api.currencylayer.com/live?" + "access_key=" + access_key
response = requests.get(url=url)
data = response.json()
currency_exchange_rate = data["quotes"][default_data_head+source_currency]/data["quotes"][default_data_head+target_currency]
print(currency_exchange_rate)