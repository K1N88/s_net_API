# s_net_API

API для социальной сети по публикации личных дневников. 

### Технологии:

- Python
- Django
- DjangoRestFramework
- JWT

### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/K1N88/s_net_API.git
```

```
cd s_net_API
```

Cоздать и активировать виртуальное окружение:

```
python -m venv venv
```

```
venv/scripts/activate
```

Установить зависимости из файла requirements.txt:

```
python -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python manage.py migrate
```

Запустить проект:

```
python manage.py runserver
```

Пример запроса на Получение публикаций:

```
GET /api/v1/posts/
```

Пример запроса на Добавление комментария:

```
POST /api/v1/posts/{post_id}/comments/
{
  "text": "string"
}
```
