## Тест 2. Тестовый проект магазина продуктов.
Реализованы товары, подкатегории и категории товаров.
Реализована корзина покупателей.
Авторизация по JWT-токену.
Реализация API на DRF.

#### Запуск проекта:
После клонирования проекта устанавливаем poetry:  
`pip install poetry`

Переходим а папку backend, активируем окружение, устанавливаем зависимости:  
`poetry shell`  
`poetry install`

В папке *backend/food_store/food_store* переименовываем файл *.env.sample* в *.env*, устанавливаем корректное значение SECRET_KEY.

В папке *backend/food_store* создаем миграции:  
`python manage.py makemigrations`  
`python manage.py migrate`

Создаем суперюзера:  
`python manage.py createsuperuser`

Запускаем dev-сервер:  
`python manage.py runserver`

Админка проекта по адресу:  
http://localhost:8000/admin/

Описание необходимых ручек:  
https://github.com/Vladislav-76/test-food-store/blob/main/backend/README.md

