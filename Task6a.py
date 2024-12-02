# Завдання №6. Написати обробку методу POST веб-сервером. У тілі повідомлення передавати текстові дані. Зберегти ці дані на сервері:
# a. у файл

from flask import Flask, request

app = Flask(__name__)

@app.route('/save', methods=['POST'])
def save_to_file():
    data = request.data.decode('utf-8')

    if data:
        with open('data.txt', 'a') as file:
            file.write(data + '\n')
        return "Дані були успішно збережені у файл «data.txt»", 200
    else:
        return "Немає даних", 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
