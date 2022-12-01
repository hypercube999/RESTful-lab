import requests


# Перед запуском этой программы запустить main.py!
if __name__ == '__main__':
    HOST = "localhost"
    PORT = 8080

    # Выполняем GET запрос к нашему сервису по URL /sum,
    # передавая 2 параметра: числа a=10 и b=20.
    # Выводим статус-код ответа и ответ сервера на печать
    response = requests.get(f"http://{HOST}:{PORT}/sum", params={"a": 10, "b": 20})
    print(f"Status code: {response.status_code}")
    print(f"Response body: {response.text}")
