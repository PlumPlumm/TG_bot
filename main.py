from aiogram import Bot, Dispatcher, executor, types

TOKEN = '5899343319:AAHKzqJLAfx2GnIxdoZ0yIbd4A0FJhNjVX8'

bot = Bot(TOKEN)
dp = Dispatcher(bot)

TEXT = []
with open("message_text.txt", 'r', encoding="utf-8") as f:
    for line in f:
        line = line.replace("\n", '')
        TEXT.append(line)

@dp.message_handler(commands=['start'])
async def echo(message: types.Message):
    await message.answer(text='ппп')

if __name__ == '__main__':
    # executor.start_polling(dp)
    print(TEXT)