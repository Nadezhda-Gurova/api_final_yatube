## Проект «API для Yatube»
### Описание
API блога Yatube на Django REST Framefork. Предоставляет возможность 
обрабатывать различные типы запросов: GET, POST, PATCH, PUT, DEL.

### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/Nadezhda-Gurova/api_final_yatube.git
```

```
cd api_final_yatube
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv env
```

```
source env/bin/activate
```

```
python3 -m pip install --upgrade pip
```

Установить зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python3 manage.py migrate
```

Запустить проект:

```
python3 manage.py runserver
```

###Примеры 
####Запрос
```http://127.0.0.1:8000/api/v1/posts/```
####Ответ
```
[
{
"id": 0,
"author": "string",
"text": "string",
"pub_date": "2019-08-24T14:15:22Z",
"image": "string",
"group": 0
}
]
```
####Запрос
```http://127.0.0.1:8000/api/v1/groups/```
####Ответ
```
[
  {
    "user": "string",
    "following": "string"
  }
]
```

