# api_for_blog
Разработано приложение API для сайта-блога.
Учебный проект, мой код в директории - /yatube_api

### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:
```
git clone https://github.com/paveliglin89/api_final_yatube.git
cd api_final_yatube
```

Cоздать и активировать виртуальное окружение:
```
python3 -m venv env
source venv/Scripts/activate
```

Установить зависимости из файла requirements.txt:
```
python3 -m pip install --upgrade pip
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
