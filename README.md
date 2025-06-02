Простое Django приложение для интеграции с платежной системой Stripe.

## Установка и запуск

### Локальный запуск:

1. Клонируйте репозиторий
2. Создайте виртуальное окружение:
   ```bash
   python -m venv venv
   source venv/bin/activate  #Linux/Mac
   venv\Scripts\activate     #Windows
   ```
3. Установите зависимости:
   ```bash
   pip install -r requirements.txt
   ```
4. Скопируйте `.env.example` в `.env` и заполните переменные окружения
5. Выполните миграции:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```
6. Создайте суперпользователя:
   ```bash
   python manage.py createsuperuser
   ```
7. Запустите сервер:
   ```bash
   python manage.py runserver
   ```

### Запуск с Docker:

```bash
docker compose up --build -d

docker compose exec web python manage.py migrate
docker compose exec web python manage.py createsuperuser
```

## Использование

1. Перейдите в админку `/admin/` и создайте товары
2. Откройте страницу товара `/item/{id}/`
3. Нажмите кнопку "Buy" для перехода к оплате Stripe

## API Endpoints

- `GET /item/{id}/` - страница товара
- `GET /buy/{id}/` - создание Stripe Checkout Session
- `GET /success/` - страница успешной оплаты

## Инструкции по запуску:

1. **Получите Stripe ключи:**
   - Зарегистрируйтесь на stripe.com
   - В тестовом режиме получите publishable и secret ключи

2. **Настройте окружение:**
   - Скопируйте `.env.example` в `.env`
   - Заполните Stripe ключи и другие переменные

3. **Запустите проект:**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   python manage.py createsuperuser
   python manage.py runserver