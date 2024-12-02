# Завдання №5. Написати обробку запиту метода GET сервером зі шляхом та параметрами в URL http://127.0.0.1:800/currency?<param>, де допустимі значення param:
# a. today - курс USD, актуальний на сьогодні
# b. yesterday - курс USD, актуальний на попередній день

from flask import Flask, request
import requests
from datetime import datetime, timedelta

app = Flask(__name__)

def get_usd_exchange_rate(start_date, end_date):
    start_str = start_date.strftime("%Y%m%d")
    end_str = end_date.strftime("%Y%m%d")
    url = f"https://bank.gov.ua/NBU_Exchange/exchange_site?start={start_str}&end={end_str}&valcode=usd&sort=exchangedate&order=desc&json"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        if data:
            return data[0]['rate']
        else:
            return None
    else:
        return None

@app.route('/currency')
def get_currency():
    param = request.args.get('param')

    if param == 'today':
        today = datetime.now()
        rate = get_usd_exchange_rate(today, today)
        if rate:
            return f"USD - {rate} (Сьогодні)"
        else:
            return "Не вдалося отримати курс валют від НБУ", 500

    elif param == 'yesterday':
        yesterday = datetime.now() - timedelta(days=1)
        rate = get_usd_exchange_rate(yesterday, yesterday)
        if rate:
            return f"USD - {rate} (Вчора)"
        else:
            return "Не вдалося отримати курс валют від НБУ", 500

    else:
        return 'Недійсний запит. Використайте "?param=today" або "?param=yesterday"', 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)


