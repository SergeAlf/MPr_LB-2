# Завдання №3. Написати просту обробку запиту метода GET сервером зі шляхом та параметрами в URL, наприклад http://127.0.0.1:8000/currency?today.
# Повертати статичне значення курса валют, наприклад “USD - 41,5”.  Для flask отримати параметри запиту за допомогою request.args.get(), для bottle -  request.query()

from flask import Flask, request

app = Flask(__name__)

@app.route('/currency')
def get_currency():
    today = request.args.get('today')

    if today is not None:
        return 'USD – 41,5'
    else:
        return 'Недійсний запит, відсутній параметр "today"', 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
