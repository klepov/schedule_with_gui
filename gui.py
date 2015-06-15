from tkinter import messagebox
from controller import *
from tkinter import *

class gui():

    def __init__(self):
        self.root = Tk()

        self.menubar = Menu(self.root)

        self.schedule = Menu(self.menubar, tearoff=0)
        self.schedule.add_command(label="создать", command=self.create_schedule)
        self.menubar.add_cascade(label="Расписание", menu=self.schedule)
        # ---------------------------------------------------------------
        self.settings = Menu(self.menubar, tearoff=0)
        self.settings.add_command(label="установка дней в семестре", command=self.setup_day_on_semester)
        self.settings.add_command(label="добавить группу", command=self.add_group)
        self.menubar.add_cascade(label="Настройки", menu=self.settings)

        self.root.config(menu=self.menubar)
        self.textArea = Text()
        self.textArea.pack()
        self.root.mainloop()

    def create_schedule(self):
        self.create_schedule_form = Toplevel()
        self.create_schedule_form.title("создание расписания")

        self.variable = StringVar(self.create_schedule_form)

        self.variable_objects = StringVar(self.create_schedule_form)

        self.get_group = adapter.get_group()
        self.get_objects = adapter.get_objects()
        if self.get_group == False or self.get_objects == False:
            messagebox.showwarning(
                "Error",
                "Ошибка, групп не найдено или нет предметов"
            )
            self.create_schedule_form.destroy()

        w = OptionMenu(self.create_schedule_form, self.variable, *self.get_group)
        object_for_group = OptionMenu(self.create_schedule_form, self.variable_objects, *self.get_objects)

        w.pack()
        object_for_group.pack()

        self.send_engine = Button(self.create_schedule_form,text = "создать",command = self.send_engine_controller)
        self.send_engine.pack()

    def send_engine_controller(self):
        self.good = adapter.start_engine(32,['philosof', 24],['python', 25])

        for i in self.good:
            if  'weekend' == self.good:
                self.textArea.insert("\n")
                continue
                print("lol")
        self.textArea.insert(1.0, self.good)





    def setup_day_on_semester(self):
        """
        устанавливает количество дней в семестре
        :return:
        """
        self.form_day_semester = Toplevel()
        self.form_day_semester.title("установка дней в семетре")

        label = Label(self.form_day_semester,text="сколько дней в семестре?",width=30)
        label.pack()

        self.textDay = Entry(self.form_day_semester)
        self.textDay.insert(0,0)
        self.textDay.pack()

        self.send_button_day = Button(self.form_day_semester,text = "Ok",command = self.send_data_day)
        self.send_button_day.pack()

    def add_group(self):
        """
        ввод группы
        :return:
        """
        self.form_add_group = Toplevel()
        self.form_add_group.title("добавление новых групп")
        label = Label(self.form_add_group, text="Номер группы")
        label.pack()
        self.num_group = Entry(self.form_add_group)
        self.num_group.pack()

        self.send_button_group = Button(self.form_add_group, text="добавить", command=self.add_group_control)
        self.send_button_group.pack()

    def add_group_control(self):

        self.get_group_from_button = int(self.num_group.get())
        check = int(self.num_group.get())

        if check < 0:
            print("error")
        else:
            if adapter.add_group(self.get_group_from_button):
                messagebox.showwarning(
                    "группа",
                    "добавленно"

                )
                self.form_add_group.destroy()

    def send_data_day(self):
        """
        добавление в файл дни
        :return:
        """
        get_date_from_button = self.textDay.get()
        check = int(self.textDay.get())

        if check < 1:
            print("error")
        else:
            if adapter.set_day_in_semester(get_date_from_button):
                messagebox.showwarning(
                "дни",
                "добавленно"

        )
                self.form_day_semester.destroy()

adapter = controller()
start = gui()

# создание контроллера
