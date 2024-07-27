# TelegramTextBot
Простой телеграм бот для отправки сообщений с поддержкой нескольких аккаунтов

## Настройка

> Вся настройка производится в файле config.py

Каждый из ботов циклически выполняет действия из параметра `actions`

Доступные действия:

---

#### chat_message

```py
{"type": "chat_message", "chat_id": 12345678, "text": "Hello world!"}
```

Отправляет сообщение в чат

`chat_id` - ID чата

`text` - Сообщение

---

#### sleep

```py
{"type": "sleep", "duration": 10}
```

Приостанавливает бота

`duration` - продолжительность в секундах

## Установка

```sh
~ > git clone https://github.com/xysed/TelegramTextBot.git 
~ > cd TelegramTextBot

# Linux
~/TelegramTextBot > python3 -m venv venv
~/TelegramTextBot > source venv/bin/activate
~/TelegramTextBot > pip3 install -r requirements.txt
~/TelegramTextBot > nano config.py  # Укажите ваши API_ID и API_HASH
~/TelegramTextBot > python3 main.py

# Windows
~/TelegramTextBot > python -m venv venv
~/TelegramTextBot > venv\Scripts\activate
~/TelegramTextBot > pip install -r requirements.txt
~/TelegramTextBot > # Откройте файл config.py и укажите ваши API_ID и API_HASH
~/TelegramTextBot > python main.py
```