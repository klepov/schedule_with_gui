# coding=utf-8
from tkinter import *
from tkinter.filedialog import asksaveasfilename, askopenfilename
# import unittest
#from scrolledtext import ScrolledText

"""
filename='TESTLOL.txt'
fin=open(filename,'r')
l1list=fin.readline()
"""


def filesave(self):
    pass


def fileopen():
    s=Toplevel(root)


def proizv_circle_open(self):
    pass


def proizv_circle_new():
    c=Toplevel(root)
    c.geometry("1024x768")
    menubar = Menu(c)
    menubar.add_cascade(label="Назад", command=c.destroy)
    c.config(menu=menubar)
    def entro():
        o10.delete(0,END)
        o11.delete(0,END)
        o12.delete(0,END)
        o13.delete(0,END)
        o14.delete(0,END)
        o15.delete(0,END)
        o16.delete(0,END)
        o17.delete(0,END)
        o18.delete(0,END)
        o19.delete(0,END)
    Label(c, text="Коэффициент оборота по приему(Кпр)",bg='yellow').grid(row=9)
    Label(c, text="Ч(прин)").grid(row=10)
    Label(c, text="Ч(оп)").grid(row=11)
    o10 = Entry(c,bg='red')
    o11 = Entry(c,bg='green')
    o12 = Entry(c,bg='green')
    o10.grid(row=9, column=1)
    get_o10 = o10.get()
    o11.grid(row=10, column=1)
    o12.grid(row=11, column=1)

    Label(c, text="Коэффициент оборота по увольнению(Кув)",bg='yellow').grid(row=12)
    Label(c, text="Ч(ув)").grid(row=13)
    Label(c, text="Ч(оп)").grid(row=14)
    o13 = Entry(c,bg='red')
    o14 = Entry(c,bg='green')
    o15 = Entry(c,bg='green')
    o13.grid(row=12, column=1)
    o14.grid(row=13, column=1)
    o15.grid(row=14, column=1)
    Label(c, text="Коэффициент общего оборота(Коб)",bg='yellow').grid(row=15)
    Label(c, text="Ч(прин)").grid(row=16)
    Label(c, text="Ч(ув)").grid(row=17)
    Label(c, text="Ч(сп)").grid(row=18)
    o16 = Entry(c,bg='red')
    o17 = Entry(c,bg='green')
    o18 = Entry(c,bg='green')
    o19 = Entry(c,bg='green')
    o16.grid(row=15, column=1)
    o17.grid(row=16, column=1)
    o18.grid(row=17, column=1)
    o19.grid(row=18, column=1)

    def otvet():
        o10.delete(0,END)
        o13.delete(0,END)
        o16.delete(0,END)


        chislo7 = o11.get()
        chislo8 = o12.get()
        chislo7 = int(chislo7)
        chislo8 = int(chislo8)
        c4 =chislo7/chislo8
        o10.insert(0,c4)

        chislo9 = o14.get()
        chislo10 = o15.get()
        chislo9 = int(chislo9)
        chislo10 = int(chislo10)
        c5 =chislo9/chislo10
        o13.insert(0,c5)

        chislo11 = o17.get()
        chislo12 = o18.get()
        chislo13 = o19.get()
        chislo11 = int(chislo11)
        chislo12 = int(chislo12)
        chislo13 = int(chislo13)
        c6 =(chislo11-chislo12)/chislo13
        o16.insert(0,c6)
    #
    # """
    # >>> p = proizv_circle_new()
    # >>> p.otvet()
    # >>> p.chislo7(10)
    # >>> p.chislo8(2)
    # >>> p = chislo7/chislo8
    #
    # 5
    #
    # """
    # '''
    # >>> pit = proizv_circle_new(5 , 4)
    # >>> pit.entro
    # 5
    # >>> pit.otvet
    # 4
    # >>> Pit = proizv_circle_new(0 , 0)
    # >>> Pit.LeftX()
    # Идем влево
    # >>> Pit.DownY()
    # Идем вниз
    # >>> Pit.X
    # -1
    # >>> Pit.Y
    # -1
    # '''




    def saveall():
        get_o10 = o10.get()
        op10 = str(get_o10)
        print(op10)
        f = open('detail.txt', 'w')
        f.write(get_o10)
        f.close()

    Button(c, text='Вычислить', command=otvet).grid(row=20, column=1, pady=4)
    Button(c, text='Стереть', command=entro).grid(row=20, column=4, pady=4)
    Button(c, text='Сохранить', command=saveall).grid(row=20, column=3)


    # if __name__ == "__main__":
    #     import doctest
    #     doctest.testmod(verbose=True)

def stoim_pokaz_open(self):
    pass


def stoim_pokaz_new():
    c=Toplevel(root)
    c.geometry("1024x768")
    menubar = Menu(c)
    menubar.add_cascade(label="Назад", command=c.destroy)
    c.config(menu=menubar)

    def entro():
        o20.delete(0,END)
        o21.delete(0,END)
        o22.delete(0,END)
        o23.delete(0,END)
        o24.delete(0,END)
        o25.delete(0,END)
        o26.delete(0,END)
        o27.delete(0,END)
        o28.delete(0,END)
        o29.delete(0,END)
    Label(c, text="Производительность труда - натуральный метод(ПТнат)",bg='yellow').grid(row=0,column=2)
    Label(c, text="В").grid(row=1,column=2)
    Label(c, text="ч-ч").grid(row=2,column=2)
    o20 = Entry(c,bg='red')
    o21 = Entry(c,bg='green')
    o22 = Entry(c,bg='green')
    o20.grid(row=0, column=3)
    o21.grid(row=1, column=3)
    o22.grid(row=2, column=3)

    Label(c, text="Производительность труда  - стоимостной метод(ПТстоим)",bg='yellow').grid(row=3,column=2)
    Label(c, text="V").grid(row=4,column=2)
    Label(c, text="Ч(ппп)").grid(row=5,column=2)
    o23 = Entry(c,bg='red')
    o24 = Entry(c,bg='green')
    o25 = Entry(c,bg='green')
    o23.grid(row=3, column=3)
    o24.grid(row=4, column=3)
    o25.grid(row=5, column=3)
    Label(c, text="Производительность труда - трудовой метод(Те)",bg='yellow').grid(row=6,column=2)
    Label(c, text="ч-ч").grid(row=7,column=2)
    Label(c, text="В").grid(row=8,column=2)
    o26 = Entry(c,bg='red')
    o27 = Entry(c,bg='green')
    o28 = Entry(c,bg='green')
    o26.grid(row=6, column=3)
    o27.grid(row=7, column=3)
    o28.grid(row=8, column=3)

    def otvet():
        o20.delete(0,END)
        o23.delete(0,END)
        o26.delete(0,END)
        chislo16 = o21.get()
        chislo17 = o22.get()
        chislo16 = int(chislo16)
        chislo17 = int(chislo17)
        c8 =chislo16/chislo17
        o20.insert(0,c8)

        chislo18 = o24.get()
        chislo19 = o25.get()
        chislo18 = int(chislo18)
        chislo19 = int(chislo19)
        c9 =chislo18/chislo19
        o23.insert(0,c9)

        chislo20 = o27.get()
        chislo21 = o28.get()
        chislo20 = int(chislo20)
        chislo21 = int(chislo21)
        c10 =chislo20-chislo21
        o26.insert(0,c10)


    Button(c, text='Вычислить', command=otvet).grid(row=20, column=3, pady=4)
    Button(c, text='Стереть', command=entro).grid(row=20, column=4, pady=4)
    Button(c, text='Сохранить', command=onSave).grid(row=20, column=5)



def proizv_vozm_okno():
    a=Toplevel()
    a.geometry("1024x768")
    def entro():
        o1.delete(0,END)
        o2.delete(0,END)
        o3.delete(0,END)
        o4.delete(0,END)
        o5.delete(0,END)
        o6.delete(0,END)
        o7.delete(0,END)
        o8.delete(0,END)
        o9.delete(0,END)



    Label(a, text="Численность средне-списочная(Чсп)",bg='yellow').grid(row=0)
    Label(a, text="Сумма Ч(сп)").grid(row=1)
    Label(a, text="Д(к)").grid(row=2)
    o1 = Entry(a,bg='red')
    o2 = Entry(a,bg='green')
    o3 = Entry(a,bg='green')
    #for i  in range(20):
     #   o2 += o2
    #@print (o2)

    o1.grid(row=0, column=1)
    o2.grid(row=1, column=1)
    o3.grid(row=2, column=1)
    Label(a, text="Численность средне-явочная(Чяв)",bg='yellow').grid(row=3)
    Label(a, text="Сумма Ч(яв)").grid(row=4)
    Label(a, text="Д(р)").grid(row=5)
    o4 = Entry(a,bg='red')
    o5 = Entry(a,bg='green')
    o6 = Entry(a,bg='green')
    o4.grid(row=3, column=1)
    o5.grid(row=4, column=1)
    o6.grid(row=5, column=1)
    Label(a, text="Численность фактически работающих(Чфр)",bg='yellow').grid(row=6)
    Label(a, text="Сумма Ч(фр)").grid(row=7)
    Label(a, text="Д(р)").grid(row=8)
    o7 = Entry(a,bg='red')
    o8 = Entry(a,bg='green')
    o9 = Entry(a,bg='green')
    o7.grid(row=6, column=1)
    o8.grid(row=7, column=1)
    o9.grid(row=8, column=1)

    def otvet():
        o1.delete(0,END)
        o4.delete(0,END)
        o7.delete(0,END)
        chislo1 = o2.get()
        chislo2 = o3.get()
        chislo1 = int(chislo1)
        chislo2 = int(chislo2)
        c1 =chislo1//chislo2
        o1.insert(0,c1)

        chislo3 = o5.get()
        chislo4 = o6.get()
        chislo3 = int(chislo3)
        chislo4 = int(chislo4)
        c2 =chislo3//chislo4
        o4.insert(0,c2)

        chislo5 = o8.get()
        chislo6 = o9.get()
        chislo5 = int(chislo5)
        chislo6 = int(chislo6)
        c3 =chislo5//chislo6
        o7.insert(0,c3)



    Button(a, text='Сохранить', command=onSave).grid(row=20, column=3)
    Button(a, text='Вычислить', command=otvet).grid(row=20, column=2, pady=4)
    Button(a, text='Стереть', command=entro).grid(row=20, column=4, pady=4)



def proizv_vozm_open(self):
    pass


def proizv_vozm_new(self):
    pass


def cenoobr_open(self):
    pass


def cenoobr_new():
    c=Toplevel(root)
    c.geometry("1024x768")
    menubar = Menu(c)
    menubar.add_cascade(label="Назад", command=c.destroy)
    c.config(menu=menubar)
    def entro():
        o23.delete(0,END)
        o24.delete(0,END)
        o25.delete(0,END)
        o26.delete(0,END)
        o27.delete(0,END)
        o28.delete(0,END)
        o29.delete(0,END)
        o30.delete(0,END)
        o31.delete(0,END)
        o32.delete(0,END)
        o33.delete(0,END)
        o30.delete(0,END)
        o31.delete(0,END)
        o32.delete(0,END)
        o33.delete(0,END)
        o34.delete(0,END)
        o35.delete(0,END)
        o36.delete(0,END)
        o37.delete(0,END)
        o38.delete(0,END)
        o39.delete(0,END)
    Label(c, text="Абсолютный прирост",bg='yellow').grid(row=9,column=2)
    Label(c, text="ПТ(отч)").grid(row=10,column=2)
    Label(c, text="ПТ(прош)").grid(row=11,column=2)
    o23 = Entry(c,bg='red')
    o24 = Entry(c,bg='green')
    o25 = Entry(c,bg='green')
    o23.grid(row=9, column=3)
    o24.grid(row=10, column=3)
    o25.grid(row=11, column=3)

    Label(c, text="Темп роста производительности труда(ТрПТ)",bg='yellow').grid(row=12,column=2)
    Label(c, text="ПТ(отч)").grid(row=13,column=2)
    Label(c, text="ПТ(прош)").grid(row=14,column=2)
    o26 = Entry(c,bg='red')
    o27 = Entry(c,bg='green')
    o28 = Entry(c,bg='green')
    o26.grid(row=12, column=3)
    o27.grid(row=13, column=3)
    o28.grid(row=14, column=3)

    Label(c, text="Темп прироста производительности труда(ТприрПТ)",bg='yellow').grid(row=19,column=2)
    Label(c, text="ТрПТ").grid(row=20,column=2)
    o29 = Entry(c,bg='red')
    o30 = Entry(c,bg='green')
    o31 = Entry(c,bg='green')
    o29.grid(row=19, column=3)
    o30.grid(row=20, column=3)
    o31.grid(row=21, column=3)

    Label(c, text="Сдельная заработная плата",bg='red').grid(row=10,column=9)
    Label(c, text="N").grid(row=11, column=9)
    Label(c, text="Rст").grid(row=12, column=9)
    o32 = Entry(c,bg='red')
    o33 = Entry(c,bg='green')
    o34 = Entry(c,bg='green')
    o32.grid(row=10, column=10)
    o33.grid(row=11, column=10)
    o34.grid(row=12, column=10)

    def otvet():
         chislo16 = o24.get()
         chislo17 = o25.get()
         chislo16 = int(chislo16)
         chislo17 = int(chislo17)
         c8 =chislo16/chislo17
         o23.insert(0,c8)

         chislo18 = o27.get()
         chislo19 = o28.get()
         chislo18 = int(chislo18)
         chislo19 = int(chislo19)
         c9 =chislo18/chislo19
         o26.insert(0,c9)

         chislo20 = o30.get()
         chislo21 = o31.get()
         chislo20 = int(chislo20)
         chislo21 = int(chislo21)
         c10 =chislo20-chislo21
         o29.insert(0,c10)

         chislo25 = o33.get()
         chislo26 = o34.get()
         chislo25 = int(chislo25)
         chislo26 = int(chislo26)
         c12 = chislo25*chislo26
         o32.insert(0,c12)
    Button(c, text='Вычислить', command=otvet).grid(row=40, column=1, sticky=W, pady=5)
    Button(c, text='Стереть', command=entro).grid(row=40, column=2, sticky=W, pady=5)
    Button(c, text='Сохранить', command=onSave).grid(row=20, column=3)


def Help():
    c = Toplevel(root)
    # text = open('test.txt', 'r', encoding = 'utf8')
    # textt=text.read()
    # T=Text(spr)
    # T.insert(END, textt)



def ZP(self):
    pass


def onSave():
    filename=asksaveasfilename()
    if filename:
        alltext=self.gettext()
        open(filename, 'w').write(alltext)



def onOpen():
    filename=askopenfilename()
    if filename:
        alltext = open(filename, 'r').read()
        self.settext(alltext)




def window2():
    a2 = Toplevel(root)
    a2.title('Форма')
    a2.geometry("1024x768")
    menubar1 = Menu(a2)
    menubar1.add_cascade(label="Назад", command=a2.destroy)  # Темы
    a2.config(menu=menubar1)


    def Entro():

        o38.delete(0,END)
        o39.delete(0,END)
        o40.delete(0,END)
        o41.delete(0,END)
        o42.delete(0,END)
        o43.delete(0,END)
        o44.delete(0,END)



    """fields = 'сумма Ч(сп)', 'Д(к)', 'сумма Ч(яв)', 'Д(р)', 'сумма Ч(фр)', 'Ч(прин)', 'Ч(оп)'
    def fetch(entries):
        for entry in entries:
            print('Input => "%s"' % entry.get())


    def makeform(root, fields):
        entries = []
        for field in fields:
            row = Frame(a2)  # создать новый ряд
            lab = Label(row, width=10, text=field)  # добавить метку, после ввода
            ent = Entry(row, width=15)
            row.pack(side=TOP, fill=X)  # прикрепить к верхнему краю
            lab.pack(side=LEFT)
            ent.pack(side=LEFT,  fill=X)  # растянуть по горизонтали
            entries.append(ent)
        return entries
    ents = makeform(a2, fields)
    a2.bind('<Return>', (lambda event: fetch(ents)))
    Button(a2, text='Fetch',
           command=(lambda: fetch(ents))).pack(side=LEFT)

"""



def window():
    class ScrolledText(Frame):
        def __init__(self, parent=None, text='', file=None):
            Frame.__init__(self, parent)
            self.pack(expand=YES, fill=BOTH)  # make me expandable
            self.makewidgets()
            self.settext(text, file)

        def makewidgets(self):
            sbar = Scrollbar(self)
            text = Text(self, relief=SUNKEN)
            sbar.config(command=text.yview)  # xlink sbar and text
            text.config(yscrollcommand=sbar.set)  # move one moves other
            sbar.pack(side=RIGHT, fill=Y)  # pack first=clip last
            text.pack(side=LEFT, expand=YES, fill=BOTH)  # text clipped first
            self.text = text

        def settext(self, text='', file=None):
            if file:
                text = open(file, 'r').read()
            self.text.delete('1.0', END)  # delete current text
            self.text.insert('1.0', text)  # add at line 1, col 0
            self.text.mark_set(INSERT, '1.0')  # set insert cursor
            self.text.focus()  # save user a click

        def gettext(self):  # returns a string
            return self.text.get('1.0', END + '-1c')  # first through last

    if len(sys.argv) > 1:
        st = ScrolledText(file=sys.argv[1])  # filename on cmdline
    else:
        st = ScrolledText(text='Words\ngo here')  # or not: two lines

    def show(event):
        print(repr(st.gettext()))  # show as raw string

    root.bind('<Key-Escape>', show)  # esc = dump text
    Label(root, text='Помощь', bg='Orange').pack()



'''    Button(self, text=”Bye”, command=self.quit).grid(row=0 , column = 2)

def Edit(self):
    Label(self,
              text = "Имя: "
              ).grid(row = 1, column = 0, sticky = W)
        self.person_ent = Entry(self)
        self.person_ent.grid(row = 1, column = 1, sticky = W)
person = self.person_ent.get()
'''
root = Tk()
root.title("Добро пожаловать")
root.geometry("1024x768")
menubar = Menu(root)
filemenu = Menu(menubar)
filemenu.add_command(label="Открыть", command=onOpen)
filemenu.add_command(label="Сохранить", command=onSave)
filemenu.add_command(label='Новое окно', command=proizv_vozm_okno)
filemenu.add_command(label="Выход", command=root.destroy)
menubar.add_cascade(label="Производственные возможности", menu=filemenu)
root.config(menu=menubar)

Proizv_circle = Menu(menubar)
Proizv_circle.add_command(label="Открыть", command=onOpen)
Proizv_circle.add_command(label="Новый", command=proizv_circle_new)
Proizv_circle.add_command(label="Сохранить", command=onSave)
menubar.add_cascade(label="Производственный цикл", menu=Proizv_circle)
root.config(menu=menubar)

stoim_pokaz = Menu(menubar)
stoim_pokaz.add_command(label="Открыть", command=onOpen)
stoim_pokaz.add_command(label="Новый", command=stoim_pokaz_new)
stoim_pokaz.add_command(label="Сохранить", command=onSave)
menubar.add_cascade(label="Стоимостные показатели", menu=stoim_pokaz)
root.config(menu=menubar)

cenoobr = Menu(menubar)
cenoobr.add_command(label="Открыть", command=onOpen)
cenoobr.add_command(label="Новый", command=cenoobr_new)
cenoobr.add_command(label="Сохранить", command=onSave)
menubar.add_cascade(label="Ценообразование", menu=cenoobr)
root.config(menu=menubar)



ZP = Menu(menubar)
# Label(root, text='Форма и системы оплаты', bg='orange').pack()
ZP.add_command(label="Форма", command=window2)
menubar.add_cascade(label="Тест", menu=ZP)

Help = Menu(menubar)
Help.add_command(label="Дополнительная информация", command=onOpen)
Help.add_command(label="Блокнот", command=window)
menubar.add_cascade(label="Помощь", menu=Help)
root.config(menu=menubar)

root.config(menu=menubar)

#Label(root, text='Бобёр', bg='orange').pack()
root.mainloop()
# unittest.main()
if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
