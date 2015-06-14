from tkinter import messagebox
from controller import *
from tkinter import *

class gui():

    def __init__(self):
        self.root = Tk()



        self.main_menu = Menu(self.root)

        self.setting = Menu(self.main_menu, tearoff=0)
        self.setting.add_command(label = "дни для семестра",command = self.setup_day_on_semester)
        self.main_menu.add_cascade(label = "настройки",menu=self.setting)

        self.root.config(menu = self.main_menu)
        self.root.mainloop()



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