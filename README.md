# sky django avito

Данная программа - это сервер для сайта, который выдает информацию из базы данных в виде JSON.
Доступные адреса (поддерживаются методы: get и post):
* /ad/
* /cat/

После последнего знака '/' можно написать определенный id для получения конкретного объекта.


## Как установить

Для этого проекта требуются следующие пакеты Python:

- django >= 4.1.7

Эти зависимости можно установить с помощью следующей команды:

```bash
pip install poetry
poetry install
```


## Запуск

Для запуска программы наберите команду:

```bash
./manage.py runserver
```

После этого локальный сервер будет доступен по адресу: `http://127.0.0.1:8000`


# Подготовка базы данных

Программа работает с DBMS (СУБД) SQLite.\
Изначально все данные хранятся в папке 'datasets\' в csv-формате.
Чтобы перевести данные в базу данных, необходимо перед первым запуском запустить команды:

```
python utils.py
./manage.py loaddata ./datasets/ads.json
./manage.py loaddata ./datasets/categories.json
./manage.py makemigrations
./manage.py migrate
```


## Цель проекта

Код написан в образовательных целях. [skypro]().


docker run -p 5432:5432 --name django_avito_postgres -e POSTGRES_PASSWORD=postgres -d postgres
python ./tools/convert.py
или загрузить csv в DB напрямую, только поменять в ad.csv колунку is_published TRUE FALSE 1 0

./manage.py loaddata ./datasets/location.json
./manage.py loaddata ./datasets/user.json
./manage.py loaddata ./datasets/user_location.json
./manage.py loaddata ./datasets/category.json
./manage.py loaddata ./datasets/ad.json
