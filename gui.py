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
        self.menubar.add_cascade(label="Настройки", menu=self.settings)

        self.root.config(menu=self.menubar)

        self.root.mainloop()

    def create_schedule(self):
        self.create_schedule_form = Toplevel()
        self.create_schedule_form.title("создание расписания")

        self.variable = StringVar(self.create_schedule_form)

        self.get_group = get_group()

        if self.get_group == False:
            messagebox.showwarning(
                "Error",
                "Ошибка, групп не найдено"
            )
            self.create_schedule_form.destroy()
            
        w = OptionMenu(self.create_schedule_form, self.variable, *self.get_group)
        w.pack()





    def setup_day_on_semester(self):

        self.form_day_semester = Toplevel()
        self.form_day_semester.title("установка дней в семетре")

        label = Label(self.form_day_semester,text="сколько дней в семестре?",width=30)
        label.pack()

        self.textDay = Entry(self.form_day_semester)
        self.textDay.insert(0,0)
        self.textDay.pack()

        self.send_button_day = Button(self.form_day_semester,text = "Ok",command = self.send_data_day)
        self.send_button_day.pack()

    def send_data_day(self):
        get_date_from_button = self.textDay.get()
        check = int(self.textDay.get())

        if check < 1:
            print("error")
        else:
            if set_day_in_semester(get_date_from_button):
                messagebox.showwarning(
                "дни",
                "добавленно"

        )
                self.form_day_semester.destroy()

start = gui()