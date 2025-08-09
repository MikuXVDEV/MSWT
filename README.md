Я подправил твой README, исправил грамматику, форматирование, ссылки и сделал текст чуть более читаемым.

---

# MSWT (переписанная версия)

**MSWT** — бот для управления вашими сервисами через Telegram.

Переписанная версия **MSWT** с использованием:
[uv](https://github.com/astral-sh/uv), [aiogram](https://docs.aiogram.dev/) и `.env`.

---

## 📦 Рекомендованная версия Python

`3.10.16`

---

## 🚀 Установка

1. Установите **uv**:

```bash
pip install uv
```

2. Создайте виртуальное окружение:

```bash
uv venv
```

3. Активируйте окружение:

```bash
source .venv/bin/activate
```

---

## ▶ Запуск

```bash
uv run bot.py
```

Перед запуском заполните файл `.env`.
Пример настроек находится в `.env-example`.

---

## ⚙ Пример .service

Чтобы бот запускался автоматически при каждой загрузке системы, создайте `.service`-файл и поместите его в `/etc/systemd/system`:

```ini
# MSWT | Копировать в /etc/systemd/system/mswt.service
[Unit]
Description=Telegram bot
After=network.target

[Service]
ExecStart=/usr/bin/bash /home/__YourDirectory__/start-server.sh
# В start-server.sh: cd /путь/к/проекту && uv run bot.py
RestartSec=10
Restart=always

[Install]
WantedBy=multi-user.target
```

---

Хочешь, я ещё сделаю `.service` и `start-server.sh` в готовом виде, чтобы можно было просто скопировать и запустить?
Так меньше шансов ошибиться в путях.
