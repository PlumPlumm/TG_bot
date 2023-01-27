from aiogram import Bot, Dispatcher

from core.settings import settings


async def send_message_takeoff(bot: Bot):
    await bot.send_message(settings.bots.admin_id, 'Привет')
