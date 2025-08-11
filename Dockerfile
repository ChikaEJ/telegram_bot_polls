FROM python:3.13

RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    netcat-openbsd \
 && rm -rf /var/lib/apt/lists/*

ENV PYTHONUNBUFFERED=1

WORKDIR /usr/src/app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["python", "telegram_bot_polls/manage.py", "runserver", "0.0.0.0:8000"]

COPY entrypoint.sh /usr/src/app/entrypoint.sh

RUN chmod +x /usr/src/app/entrypoint.sh

ENTRYPOINT ["/usr/src/app/entrypoint.sh"]