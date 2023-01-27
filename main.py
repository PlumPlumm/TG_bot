from aiogram import Bot, Dispatcher, executor, types
import datetime

TOKEN = '5899343319:AAHKzqJLAfx2GnIxdoZ0yIbd4A0FJhNjVX8'

text_path = 'text/morning_text.txt'


def read_text(path):
    text = []
    with open(path, 'r', encoding="utf-8") as f:
        for line in f:
            line = line.replace("\n", '')
            text.append(line)
    f.close()
    return text

def return_count_takeoff():
    today_data = datetime.datetime.today()
    takeoff_date = datetime.datetime(2023, 2, 26)
    return (takeoff_date - today_data).days

bot = Bot(TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def echo(message: types.Message):
    await message.answer(text='ппп')


if __name__ == '__main__':
    # executor.start_polling(dp)
    text = read_text(text_path)
    count_takeoff = return_count_takeoff()
    print(f'{text[5]}, до отъезда осталось {count_takeoff}')