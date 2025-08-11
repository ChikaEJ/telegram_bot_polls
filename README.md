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
TELEGRAM_BOT_TOKEN=<you [telegram token](https://developers.sber.ru/help/salutebot/telegram-integration) here>

# Ngrok (опционально)
NGROK_TUNNEL_URL=<your ngrok url here>/bot/webhook/

```
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
    1) После того как вы настроили [ngrok](https://ngrok.com/downloads/windows) на вашем компьюторе и прописали url с ngrok в .env файле,
    Выполни в терминале команду для установки вебхука:
```bash
docker-compose exec bot_app python set_webhook.py
```
    2) Если всё прошло успешно, Telegram вернёт ответ:
````
{
  "ok": true,
  "result": true,
  "description": "Webhook was set"
}
````
    6) Открываем телеграм. Находим созданного бота через поиск и нажимает /start
