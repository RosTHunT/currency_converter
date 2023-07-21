import requests


class ApiDataFetcher:
    def __init__(self, api_url):
        self.api_url = api_url

    def get_data(self):
        try:
            response = requests.get(self.api_url)

            if response.status_code == 200:
                data = response.json()
                return data

            else:
                print(f"Помилка запиту. Код відповіді: {response.status_code}")
                return None

        except requests.exceptions.RequestException as e:
            print(f"Помилка під час виконання запиту: {e}")

            return None


api_url = 'https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json'
data_fetcher = ApiDataFetcher(api_url)
data = data_fetcher.get_data()

data_fetcher = ApiDataFetcher(api_url)


if data:
    print("Отримані дані:")
    for d in data:
        if d['cc'] == 'USD' or d['cc'] == 'EUR' or d['cc'] == 'PLN' or d['cc'] == 'XAU' or d['cc'] == 'XAG':
            if d['cc'] == 'XAU' or d['cc'] == 'XAG':
                print(f" Валюта: {d['txt']} {d['cc']}, Курс: {d['rate']} грн/1 кг {d['cc']}, дата: {d['exchangedate']}")
            else:
                print(f" Валюта: {d['txt']} {d['cc']}, Курс: {d['rate']} грн/1 {d['cc']}, дата: {d['exchangedate']}")

else:
    print("Не вдалося отримати дані з API.")
