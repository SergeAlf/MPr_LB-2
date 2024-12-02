# Завдання №6. Написати обробку методу POST веб-сервером. У тілі повідомлення передавати текстові дані. Зберегти ці дані на сервері:
# b. у sqlite3 базі даних

import sqlite3
from flask import Flask, request

app = Flask(__name__)

def init_db():
    conn = sqlite3.connect('data.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS data (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            content TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

@app.route('/save', methods=['POST'])
def save_to_db():
    data = request.data.decode('utf-8')

    if data:
        conn = sqlite3.connect('data.db')
        cursor = conn.cursor()
        cursor.execute('INSERT INTO data (content) VALUES (?)', (data,))
        conn.commit()
        conn.close()
        return "Дані були успішно збережені у файл «data.db»", 200
    else:
        return "Немає даних", 400

if __name__ == '__main__':
    init_db()
    app.run(host='0.0.0.0', port=8000)
