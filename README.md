# Интернет магазин.

## Установка:

1. Клонируйте репозиторий:
```
git clone https://github.com/DmitryPikov/onlinestore.git
```

2. Установите зависимости из poetry.lock-файла:
```
poetry install --sync
```

3. Запустите сервер Django в зависимости от вашей системы

Для Windows:
```
python manage.py runserver
```
Для Linux и MacOS:
```
python3 manage.py runserver
```

4. В браузере откройте адрес страницы:
```
http://127.0.0.1:8000/
```