import csv
import random as random


def select_sorted(sort_columns='high', order='desc', limit=50, filename='dump.csv'):
    def quicksort(lst):
        if len(lst) <= 1:
            return lst
        else:
            q = random.choice(lst)
            s_nums = []
            m_nums = []
            e_nums = []
            for i in range(len(lst)):
                if lst[i][sort_columns] < q[sort_columns]:
                    s_nums.append(lst[i])
                elif lst[i][sort_columns] > q[sort_columns]:
                    m_nums.append(lst[i])
                else:
                    e_nums.append(lst[i])

            return quicksort(s_nums) + e_nums + quicksort(m_nums)

    with open('all_stocks_5yr.csv', "r") as f:
        reader = list(csv.DictReader(f))

        sort = quicksort(reader)

    with open(filename, 'w') as file:
        file.write('date, open, high, low, close, volume, Name\n')
        for i in range(int(limit)):
            file.write(
                f'{sort[i]["date"]}, {sort[i]["open"]}, {sort[i]["high"]}, {sort[i]["low"]}, {sort[i]["close"]}, {sort[i]["volume"]}, {sort[i]["Name"]}\n')

    return sort


select_sorted(sort_columns='volume', order='desc', limit=50, filename='dump.csv')
