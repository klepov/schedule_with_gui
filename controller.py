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


def add_group(id):
    try:

        conn = sqlite3.connect('bd_schedule')
        c_group = conn.cursor()
        c_group.execute("insert into groups values(NULL,%s)" % (id))

        conn.commit()
        conn.close()

        return True

    except sqlite3.OperationalError:
        return False
        # prepared_semester = create_semester(count)

    # f = open('detail.txt',)

def get_group():
    #метод возврящяет группы с бд
    a = 2
    try:
        conn = sqlite3.connect('bd_schedule')
        c = conn.cursor()
        c.execute("select num_group from groups")

        checking = conn.cursor()
        checking.execute("select num_group from groups")



        # Если пустой ответ - выходим
        check = checking.fetchall()
        if len(check) == 0:
            return False

        else:
            # иначе формируем список и возвращяем его
            group_from_db = []

            for i in c:
                group_from_db.append(i[0])

            return group_from_db

    except sqlite3.OperationalError:
        return False


def get_objects():
    # метод возврящяет группы с бд

    a = 2
    try:
        conn = sqlite3.connect('bd_schedule')
        object_in_db = conn.cursor()
        object_in_db.execute("select name,hours from objects_prog")


        # Если пустой ответ - выходим
        if a == 0:
            return False

        else:
            # иначе формируем список и возвращяем его
            object_from_db = []

            for i in object_in_db:
                object_from_db.append(i[0])

            return object_from_db

    except sqlite3.OperationalError:
        return False
