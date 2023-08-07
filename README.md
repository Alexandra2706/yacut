# YaCut

### Описание
Проект YaCut — это сервис укорачивания ссылок. Его назначение — ассоциировать длинную пользовательскую ссылку с короткой, которую предлагает сам пользователь или предоставляет сервис.

Ключевые возможности сервиса:
- генерация коротких ссылок и связь их с исходными длинными ссылками,
- переадресация на исходный адрес при обращении к коротким ссылкам.

### Установка. Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone git@github.com:Alexandra2706/yacut.git
```

```
cd yacut
```

Cоздать и активировать виртуальное окружение:

```
python -m venv venv
```

* Если у вас Linux/macOS

    ```
    source venv/bin/activate
    ```

* Если у вас windows

    ```
    source venv/scripts/activate
    ```

Установить зависимости из файла requirements.txt:

```
python -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```
Создать и заполнить файл .env:
```
FLASK_APP = yacut
FLASK_ENV = development
FLASK_DEBUG=1
DATABASE_URI=sqlite:///db.sqlite3
SECRET_KEY=YOUR_SECRET_KEY
```

Выполнить миграции:
```
flask db init
flask db migrate -m "короткое сообщение"
flask db upgrade
```
Запустить проект:
```
flask run
```
Проект будет доступен по адресу: http://127.0.0.1:5000

### Использованные технологии

- Python 3.11
- Flask 2.0.2
- Sqlalchemy 1.4.29
- Wtforms 3.0.1
- Flask-migrate 3.0.1
- Jinja2 3.0.3

### Автор

Александра Гаврилова