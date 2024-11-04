import requests
import json

# URL, на который будет отправлен webhook
webhook_url = 'https://webhook-test.com/686dc11e992b3e1804d220be29c13406'

# Данные, которые мы хотим отправить
data = {
    'event': 'new_order',
    'order_id': 12345,
    'customer_name': 'Иван Иванов',
    'total_amount': 100.00
}

# Преобразуем данные в JSON-формат
json_data = json.dumps(data)

# Отправляем POST-запрос на webhook URL
response = requests.post(webhook_url, data=json_data, headers={'Content-Type': 'application/json'})

# Проверяем ответ от сервера
if response.status_code == 200:
    print('Webhook успешно отправлен!')
else:
    print(f'Ошибка при отправке webhook: {response.status_code}')
    print(f'Ответ от сервера: {response.text}')