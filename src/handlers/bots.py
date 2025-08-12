import os
import re
import subprocess
from typing import Optional

from aiogram import Bot, Router
from aiogram.filters.command import Command
from aiogram.types import Message

bots_roter = Router()

from ...config import config


@bots_roter.message(Command('bots'))
async def bots(bot: Bot, message: Optional[Message] = None) -> None:
    text = ""
    autostart_dir = "./sh-module"

    if not os.path.exists(autostart_dir):
        try:
            os.makedirs(autostart_dir, exist_ok=True)
            text += f"<b>📁 | Directory '{autostart_dir}' was created.</b>\n"
        except Exception as e:
            text += f"<b>❌ | Failed to create directory '{autostart_dir}': {e}</b>\n"
            if message:
                await message.answer(text)
            return

    for filename in os.listdir(autostart_dir):
        if re.search(r"-start\.sh$", filename):
            full_path = os.path.join(autostart_dir, filename)
            try:
                process = subprocess.Popen(
                    f"sh {full_path}",
                    stdout=subprocess.PIPE,
                    shell=True
                )
                process.daemon = True
                text += f"<b>✅ | File autostart {filename} started!</b>\n"
            except Exception:
                text += f"<b>❌ | File autostart {filename} not started!</b>\n"

    if not text.strip():
        text = "😢 | <b>File autostart not found...</b>"

    if message:
        try:
            usernames = message.from_user.mention_html()
        except Exception:
            usernames = "ROOT"
    else:
        usernames = "ROOT"

    final_text = f"🤔 | <b>{usernames} trying to run autostart tasks\n{text}</b>"

    for admin_id in config.owner:
        try:
            await bot.send_message(admin_id, final_text)
        except Exception:
            pass
