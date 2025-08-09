
--

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



## restart_daemon.sh - для перезапуска сервиса
содержимое:
systemctl restart mswt
И дайте разрешение на запуск
chmod +x ~/restart_daemon.sh


start-server.sh
python3 bot.py
sh start-server.sh


