from aiogram import Bot, Dispatcher, executor, types

TOKEN = '5899343319:AAHKzqJLAfx2GnIxdoZ0yIbd4A0FJhNjVX8'

morning_text_path = 'text/morning_text.txt'
night_text_path = 'text/night_text.txt'

def read_text(path):
    text = []
    with open(path, 'r', encoding="utf-8") as f:
        for line in f:
            line = line.replace("\n", '')
            text.append(line)
    f.close()
    return text

bot = Bot(TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def echo(message: types.Message):
    await message.answer(text='ппп')

if __name__ == '__main__':
    # executor.start_polling(dp)
    print(read_text(night_text_path))