from aiogram import Bot, Dispatcher
import asyncio
import logging
import datetime
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from core.handlers import apsched

from core.handlers.basic import get_start
from core.settings import settings


async def start_bot(bot: Bot):
    # await bot.send_message(settings.bots.admin_id, text='Бот запущен')
    pass

async def stop_bot(bot: Bot):
    await bot.send_message(settings.bots.admin_id, text='Бот остановлен')


async def start():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - [%(levelname)s] - %(name)s - "
               "(%(filename)s).%(funcName)s(%(lineno)d) - %(message)s"
    )
    bot = Bot(token=settings.bots.bot_token)
    dp = Dispatcher()
    scheduler = AsyncIOScheduler()
    scheduler.add_job(
        apsched.send_message_takeoff, trigger='cron',
        args=(bot,), hour=10, minute=0, second=0,
        start_date=datetime.datetime.now()
    )
    dp.startup.register(start_bot)
    dp.shutdown.register(stop_bot)

    dp.message.register(get_start)

    try:
        scheduler.start()
        await dp.start_polling(bot)
    finally:
        await bot.session.close()



def main():
    asyncio.run(start())


if __name__ == '__main__':
    main()
