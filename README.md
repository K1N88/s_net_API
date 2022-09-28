# api_final_yatube

### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/K1N88/api_final_yatube.git
```

```
cd api_final_yatube
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
