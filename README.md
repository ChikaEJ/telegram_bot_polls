# 📊 Telegram Poll Bot (Django + Native Telegram Bot API)

Этот проект — пример Telegram-бота для проведения опросов на Django **без сторонних Telegram-библиотек** (используется `requests`).

## 🚀 Возможности

- Команда `/start` — регистрация пользователя в БД.
- Команда `/poll` — отправка последнего созданного опроса из админки.
- Обработка ответов (`poll_answer`) через Webhook.
- Подсчёт завершённых опросов и сохранение выбранных вариантов.
- Интерфейс в Django Admin для создания опросов.

---

## 📦 Стек технологий

- **Python** 3.13
- **Django** 5.2.5
- **PostgreSQL**
- **Docker + Docker Compose**
- **Ngrok** (для локального тестирования вебхука)

---

## 🔧 Установка и запуск

### 1. Клонируем репозиторий
```bash
git clone git@github.com:ChikaEJ/telegram_bot_polls.git
cd telegram_bot_polls
```
### 2. Настройка .env
    
    - Создай файл .env в корне проекта и укажите:
```
# Django
DJANGO_SECRET_KEY=django-insecure-your-secret-key
DJANGO_DEBUG=True
DJANGO_ALLOWED_HOSTS=localhost,127.0.0.1,<your ngrok or webhook registered domain(example: https://3d4fcdaeaccd.ngrok-free.app)>
DJANGO_CSRF_TRUSTED_ORIGINS=<your ngrok or webhook registered domain(example: https://3d4fcdaeaccd.ngrok-free.app)>,

# Database
POSTGRES_DB=botdb
POSTGRES_USER=botuser
POSTGRES_PASSWORD=botpass
POSTGRES_HOST=db
POSTGRES_PORT=5432

# Telegram
TELEGRAM_BOT_TOKEN=YOUR_TELEGRAM_BOT_TOKEN 

# Ngrok (опционально)
NGROK_AUTHTOKEN=your-ngrok-authtoken

```
    [Инструкция по созданию бота](https://developers.sber.ru/help/salutebot/telegram-integration)
### 3. Docker Compose запуск
```bash
docker-compose up --build
```
    Это поднимет:

    * Django backend (bot_app)

    * PostgreSQL (db)

    * ngrok (ngrok) — проброс для вебхука

### 4. Миграции и суперпользователь
    После первого запуска:
```bash
docker-compose exec bot_app python telegram_bot_polls/manage.py migrate
docker-compose exec bot_app python telegram_bot_polls/manage.py createsuperuser

```
### 5. Настройка вебхука
    1) После запуска контейнеров открой в браузере панель управления ngrok:
        http://localhost:4040
        (этот порт проброшен в docker-compose.yml)
    2) На странице Status найди значение Forwarding вида:
        "https://3d4fcdaeaccd.ngrok-free.app -> web:8000"
    3) Скопируй этот HTTPS-адрес (начинается с https:// и заканчивается на .ngrok-free.app).
    4) Выполни в терминале команду для установки вебхука, подставив свой токен бота и скопированный адрес:
```bash
curl -X POST "https://api.telegram.org/bot<YOUR_BOT_TOKEN>/setWebhook" \
     -H "Content-Type: application/json" \
     -d '{"url": "<NGROK_PUBLIC_URL>/bot/webhook/"}'
```
    ⚠️ Обязательно укажите слэш в конце URL.
    
    5) Если всё прошло успешно, Telegram вернёт ответ:
````
{
  "ok": true,
  "result": true,
  "description": "Webhook was set"
}
````
    6) Открываем телеграм. Находим созданного бота через поиск и нажимает /start
