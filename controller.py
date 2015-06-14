import sqlite3

__author__ = 'dima'
import os

"""
контроллер - прослойка между интрефейсом и данными
"""
from engine import *

class controller():
    def set_day_in_semester(self,count):
        #метод устанавливает количество дней в семестре
        f = open('detail.txt')

        if os.stat("detail.txt").st_size == 0:
            count = str(count)
            f = open('detail.txt', 'w')
            f.write(count)
            f.close()
            return True


        else:
            self.semester = engine.create_semester(int(f.read()))


    def add_group(self,id):
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

    def get_group(self):
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


    def get_objects(self):
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

    def start_engine(self,group_name,*objects_group):
        f = open('detail.txt')
        self.count_day = engine.create_semester(int(f.read()))
        self.group_name = group_name
        self.object_group = objects_group

        prepair = engine.create_schedule("32",self.count_day,self.object_group)
        engine.compare_date_with_schedule(prepair)

engine = generate()