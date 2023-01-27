from aiogram import Bot, Dispatcher, executor, types

TOKEN = '5899343319:AAHKzqJLAfx2GnIxdoZ0yIbd4A0FJhNjVX8'

bot = Bot(TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def echo(message: types.Message):
    await message.answer(text='ппп')

if __name__ == '__main__':
    executor.start_polling(dp)