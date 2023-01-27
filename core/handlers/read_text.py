import datetime


def calc_count_takeoff():
    today_data = datetime.datetime.today()
    takeoff_date = datetime.datetime(2023, 2, 26)
    return (takeoff_date - today_data).days


def return_message_takeoff():
    # text = []
    # with open('..\\..\\text\morning_text.txt', 'r', encoding="utf-8") as f:
    #     for line in f:
    #         line = line.replace("\n", '')
    #         text.append(line)
    # f.close()

    return f'Доброе утро, осталось {calc_count_takeoff()} дней'



