# Завдання №2. Написати просту обробку запиту метода GET сервером. На запит повертати строку “Hello World!”

from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def handle_get():
        return 'Hello World!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
