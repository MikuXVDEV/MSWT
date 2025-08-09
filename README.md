Вот переработанный и структурированный README, чтобы было понятно и удобно шаг за шагом:

---

# MSWT (переписанная версия)

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

# 🛠 Автоматический запуск с systemd

Для того, чтобы бот запускался автоматически при старте системы, создайте systemd unit-файл.

### Пример `mswt.service`:

```ini
# Копировать в /etc/systemd/system/mswt.service
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