# Дипломный проект от SkyPro. 
# Django-приложение “Образовательные модули”

## Описание.

### Написать небольшой проект на Django и Django Rest Framework с моделью "Образовательные модули". В них есть:
    порядковый номер
    название
    описание

## Задача.

### При создании проекта нужно:

    1. реализовать для модели (моделей) все методы CRUD
    2. Полностью покрыть автоматизированными юнит-тестами все модели, сериализаторы, виды.

## Требуемый стэк

    Python 3.11, Docker, Django, PostgreSQL, ORM, MVT/MTV, FBV/CBV, Serliazers, Viewset/Generic, 
    Tests, Git, Readme, PEP8, Swagger

## В проекте используется Unittest

    - python manage.py test

## Для подсчета покрытия тестами использовался специальный пакет Coverage

    - coverage run --source='.' manage.py test
    - coverage report!

![img_3.png](screen%2Fimg_3.png)

![img.png](screen%2Fimg.png)


# Для запуска проекта локально Вам потребуется:

### Установите систему контроля версий GIT с учетом вашей OS.

        - Windows:
            https://git-scm.com/download/win
        - Unix 
            sudo apt update (обновление системы)
            sudo apt install git-all

        - Убедиться что все установлено:
            git --version

### Создайте и скопируйте проект в директорию:

        - git clone git@github.com:rusov63/Skypro.Graduation_project.git

### Для запуска приложения необходимо настроить виртуальное окружение и установить все необходимые зависимости:

    Команда для Windows:
        - python -m venv venv
        - venv\Scripts\activate
        - pip install -r requirement.txt

    Команда для Unix:
        - python3 -m venv venv
        - source venv/bin/activate 
        - pip install -r requirements.txt

### Для работы с переменными окружениями необходимо заполнить файл:

        - env.examples

### Для заполнения моделей данными необходимо выполнить следующую команду:

        - python manage.py fill

### Для создания административной панели:

        - python manage.py createsuperuser

### Для запуска проекта:

    Команда для Windows:
        - python manage.py runserver

    Команда для запуска админ. панели    
        - http://127.0.0.1:8000/admin/

### Документация проекта: http://127.0.0.1:8000/swagger/