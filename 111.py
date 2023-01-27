from aiogram import Bot, Dispatcher
from aiogram.types import Message
import datetime

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

