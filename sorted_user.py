import csv
import pandas as pd
from turtle import pd
from distlib.compat import raw_input


def cache(k):
    cache = {}

    def wrapper(*args, **kwargs):
        key = tuple(f'{k}, {args}, {kwargs}')
        if key not in cache:
            cache[key] = k(*args, **kwargs)
        return cache[key]

    return wrapper


@cache
def select_sorted():
    sort_columns = raw_input('сортировка по цене открытия(1), закрытия(2), максиму(3), минимум(4), обьём(5):') or 'high'
    if sort_columns == '1':
        sort_columns = 'open'
    elif sort_columns == '2':
        sort_columns = 'close'
    elif sort_columns == '3':
        sort_columns = 'high'
    elif sort_columns == '4':
        sort_columns = 'low'
    elif sort_columns == '5':
        sort_columns = 'volume'

    order = raw_input('порядок по убыванию (1) / возрастанию (2):') or 'desc'
    if order == '1':
        order = 'desc'
    elif order == '2':
        order = 'asc'

    limit = raw_input('ограничение выборки (50):') or '50'
    filename = raw_input('Название файла для сохранения результата (dump.csv):') or 'dump.csv'

    return select_sorted(order, limit, filename)


def select_sorted_func(sort_columns='high', order='desc', limit=50, filename='dump.csv'):
    with open('all_stocks_5yr.csv', "r") as f:
        reader = list(csv.DictReader(f))
    df = pd.DataFrame(reader)

    if order == 'desc':
        sort_d = df.sort_value(sort_columns, ascending=False)
    else:
        sort_d = df.sort_value(sort_columns)

    a = sort_d.to_dict('records')

    with open(filename, "w") as file:
        file.write('date, open, high, close, volume, Name\n')
        for i in range(int(limit)):
            file.write(
                f'{sort[i]["date"]}, {sort[i]["open"]}, {sort[i]["high"]}, {sort[i]["low"]}, {sort[i]["close"]}, {sort[i]["volume"]}, {sort[i]["Name"]}\n')

    return sort_d


def get_by_date():
    date = raw_input('Дата в формате yyyy-mm-dd [all]:') or 'all'
    name = raw_input('Тикер [all]:') or 'all'
    filename = raw_input('Файл [result.csv]:') or 'result.csv'

    get_by_date_func(date, name, filename)


def get_by_date_func(date="2017-08-08", name="PCLN", filename='result.csv'):
    with open('dump.csv', "r") as file:
        reader = list(csv.DictReader(file))

    new = []

    for i in reader:
        if i.get('Name') == name and i.get('date') == date:
            new.append(i)

        for i in reader:
            if date != 'all' and name != 'all' and i.get('Name') == name and i.get('date') == date:
                new.append(i)
            elif date == 'all' and name == 'all':
                new.append(i)
            elif date != 'all' and name != 'all' and i.get('date') == date:
                new.append(i)
            elif date == 'all' and name != 'all' and i.get('Name') == name:
                new.append(i)
        with open(filename, "w") as file:
            file.write(f'{new} \n')


get_by_date_func(date="2017-08-08", name="PCLN", filename='result.csv')
