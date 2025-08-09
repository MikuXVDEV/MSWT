# MSWT (переписанная версия)

Переписанная версия **MSWT** с использованием: [uv](https://github.com/astral-sh/uv) [aiogram](https://docs.aiogram.dev/) и  `.env` для хранения конфигурации и токенов.

## 📦 Рекомендованная версия Python
`3.10.16`

## 🚀 Установка
```bash
pip install uv && uv venv && source .venv/bin/activate
```
## Запуск
```bash
uv run bot.py
```

Перед запуском, заполните .env. Пример в .env-example



## Пример сервиса:
```bash
# MSWT | Copy to /etc/systemd/system
[Unit]
Description=Telegram bot
After=network.target
[Service]
ExecStart=/usr/bash /home/__YourDirectory__/start-server.sh  # In start-server write "cd (you directory) && uv run bot.py"
RestartSec=10
Restart=always
[Install]
WantedBy=multi-user.target
```





