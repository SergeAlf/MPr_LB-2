# Завдання №4. Обробка заголовків запиту. В залежності від значення параметру заголовку “Content-Type” (application/json чи application/xml) повертати json чи xml документ.
# У разі відсутності - повертати звичайний текст. Для flask отримати заголовки за допомогою request.headers.get, для bottle - request.get_header[].

from flask import Flask, request, jsonify, Response

app = Flask(__name__)

@app.route('/currency')
def get_currency():
    content_type = request.headers.get('Content-Type')

    currency_data = {
        "currency": "USD",
        "rate": "41,5"
    }

    if content_type == 'application/json':
        return jsonify(currency_data)

    elif content_type == 'application/xml':
        xml_response = f"""<?xml version="1.0" encoding="UTF-8"?>
<currency>
    <name>USD</name>
    <rate>41,5</rate>
</currency>"""
        return Response(xml_response, content_type='application/xml')

    else:
        return "USD - 41,5"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
