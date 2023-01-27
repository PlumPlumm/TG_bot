from aiogram import Bot, Dispatcher

from core.handlers.read_text import return_message_takeoff
from core.settings import settings

text_path = '..\..\\text\morning_text.txt'

async def send_message_takeoff(bot: Bot):
    await bot.send_message(chat_id=-801176317 ,text=return_message_takeoff())