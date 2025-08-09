**MSWT** — Telegram-бот для управления вашими сервисами.

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
uv run bot.py
```

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