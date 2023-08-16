from bs4 import BeautifulSoup
import requests


r = requests.get('https://www.cursbnr.ro/')
class GetRates:
    def get_rates():
        if r.ok:
            soup = BeautifulSoup(r.content, 'lxml')
            currency_table = soup.find('div', class_='table-responsive')
            currency_data = currency_table.find_all('tr')
            currency, value = [], []
            for item in currency_data:
                if item.find('td'):
                    currency.append(item.find('td').text)
                    values = item.find_all('td')
                    value.append(values[2].text)

            data = dict(zip  (currency, value))
           
