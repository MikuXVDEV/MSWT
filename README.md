**MSWT** — Telegram-бот для управления вашими сервисами.


|| используется pyenv, потому start-server.sh не будет работать, если вы не установите его||

Эта версия переписана с использованием:
[uv](https://github.com/astral-sh/uv), [aiogram](https://docs.aiogram.dev/) и `.env` для удобства конфигурации.

---

## 📦 Рекомендованная версия Python

`3.10.16`

---

## 🚀 Установка и настройка

### 1. Установите `uv`

```bash
pip install uv
```

### 2. Создайте виртуальное окружение

```bash
uv venv
```

### 3. Активируйте виртуальное окружение

```bash
source .venv/bin/activate
```

---

## ⚙ Конфигурация

Перед запуском заполните файл `.env`
Пример настроек можно найти в `.env-example`.

---

## ▶ Запуск бота

```bash
uv run -m MSWT
```
---

# Задачи (TASK's)

В боте есть механизм для запуска **тасков** — фоновых задач, которые выполняет бот.
Например, можно делать регулярные бэкапы базы данных и отправлять их вам в Телеграм.

## Как добавить свою задачу [пример]

1. Создайте файл с задачей в папке `src/handlers/tasks`. Например: `BackupBD.py`.

2. В этом файле создайте **асинхронную функцию** с именем `start_task`, которая принимает один аргумент — объект бота `bot` типа `Bot` из aiogram.

```python
from aiogram import Bot
import asyncio

async def start_task(bot: Bot) -> None:
    while True:
        try:
            # Здесь логика вашей задачи, например бэкап базы
            await run_mongodump(...)
        except Exception as e:
            # Обработка ошибок
            print(f"Ошибка в задаче: {e}")
        await asyncio.sleep(10000)  # пауза перед следующим запуском
```

3. При старте бота автоматически найдутся все такие задачи и будут запущены параллельно.

---

# Сервисы

После первого запуска бота в корне проекта автоматически создаётся папка `sh-module`.
В эту папку нужно помещать ваши `.sh`-скрипты (юниты).

**Важно:**
Имя файла должно заканчиваться на `-start.sh`, например: `МоёНазвание-start.sh`.
Если в названии отсутствует суффикс `-start.sh`, бот не сможет обнаружить и запустить ваш юнит.

---

### Пример простого юнита — `hello-start.sh`:

```bash
#!/bin/bash
echo 'Привет, мир!'
```

---

### Пример для запуска telegram-бота:
```bash
#!/bin/bash
cd /home/miku/dev/MSWT || exit 1
source .venv/bin/activate
uv run bot.py
```

# 🛠 Автоматический запуск с systemd

Для того, чтобы бот запускался автоматически при старте системы, создайте systemd unit-файл.

### Пример `mswt.service`:

```ini
[Service]
ExecStart=/ПУТЬ_К_MSWT/start-server.sh
RestartSec=10
Restart=always
Type=simple

[Install]
WantedBy=multi-user.target
```

### Важные шаги:

1. Дайте права на выполнение скриптам:

```bash
chmod +x /ПУТЬ_К_MSWT/restart-daemon.sh
chmod +x /ПУТЬ_К_MSWT/start-server.sh
```

2. Скопируйте unit-файл в systemd:

```bash
sudo cp mswt.service /etc/systemd/system
```

3. Перезагрузите конфигурацию systemd:

```bash
sudo systemctl daemon-reload
```

4. Включите и сразу запустите сервис:

```bash
sudo systemctl enable mswt.service --now
```

---