## Описание проекта

**Foodgram** — это веб-приложение для публикации рецептов, составления списка покупок и отслеживания любимых блюд. Пользователи могут создавать собственные рецепты, добавлять их в избранное, подписываться на других авторов и формировать список необходимых ингредиентов для покупок.

## Запуск проекта с помощью Docker

1. **Клонируйте репозиторий:**
    ```bash
    git clone https://github.com/AlexanderBultsev/foodgram-st.git
    cd foodgram-st
    ```

2. **Создайте файл `.env` и настройте переменные окружения по примеру:**
    ```bash
    # Настройки базы данных PostgreSQL
    POSTGRES_DB=db
    POSTGRES_USER=user
    POSTGRES_PASSWORD=password
    DB_HOST=db
    DB_PORT=5432

    # Настройки для Django
    DJANGO_SECRET_KEY=your-secret-key
    DJANGO_DEBUG=True
    DJANGO_ALLOWED_HOSTS=localhost,127.0.0.1
    ```

3. **Постройте и запустите контейнеры:**
    ```bash
    docker-compose up --build -d
    ```

4. **(Опционально) Создайте суперпользователя:**
    ```bash
    docker-compose exec backend python manage.py createsuperuser
    ```

6. **Откройте проект в браузере:**
    ```
    http://127.0.0.1/
    ```

---
