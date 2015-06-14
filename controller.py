import sqlite3

__author__ = 'dima'
import os

"""
контроллер - прослойка между интрефейсом и данными
"""

from engine import *

def set_day_in_semester(count):
    #метод устанавливает количество дней в семестре
    f = open('detail.txt')

    if os.stat("detail.txt").st_size == 0:
        count = str(count)
        f = open('detail.txt', 'w')
        f.write(count)
        f.close()
        return True


    else:
        create_semester(int(f.read()))


        # prepared_semester = create_semester(count)

    # f = open('detail.txt',)

def get_group():
    #метод возврящяет группы с бд

    conn = sqlite3.connect('bd_schedule')
    c = conn.cursor()
    c.execute("select num_group from groups")

    group_from_db = []
    for i in c:
        group_from_db.append(i[0])

    return group_from_db