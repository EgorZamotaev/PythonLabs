from datetime import datetime, timedelta
from tkinter import *

times = [("Час", 1), ("День", 2), ("Минута", 3)]

def count(date_birth):
    date_birth = date_birth.split("/")
    date_birth = datetime(int(date_birth[2]), int(date_birth[1]), int(date_birth[0]))
    now_date = datetime.now()
    lived = now_date - date_birth
    ave_death = 26333
    death_date = date_birth + timedelta(days=ave_death)
    rest_of_life = death_date - now_date
    return lived, rest_of_life

def select():
    l = language.get()
    date_birth=edit_field.get()
    lived = count(date_birth)[0]
    rest_of_life = count(date_birth)[1]
    print(date_birth, lived)
    x = "прожито "
    y = "осталось "
    if l == 1:
        x += str(int(lived.total_seconds()) // 3600)
        sel.config(text=x)
        y += str(int(rest_of_life.total_seconds()) // 3600)
        sel2.config(text=y)
    elif l == 2:
        x += str(int(lived.days))
        sel.config(text=x)
        y += str(int(rest_of_life.days))
        sel2.config(text=y)
    elif l == 3:
        x += str(int(lived.total_seconds()) // 60)
        sel.config(text=x)
        y += str(int(rest_of_life.total_seconds()) // 60)
        sel2.config(text=y)



root = Tk()
root.title("Задание 4")
root.geometry("300x280")

header = Label(text="Введите дату рождения (дд/мм/гггг)", padx=15, pady=10)
header.grid(row=0, column=0, sticky=W)

edit_field = Entry(root, width=30)
edit_field.grid(row=1, column=0, sticky=W)

language = IntVar()

row = 2
for txt, val in times:
    Radiobutton(text=txt, value=val, variable=language, padx=15, pady=10, command=select) \
        .grid(row=row, sticky=W)
    row += 1

sel = Label(padx=15, pady=10)
sel.grid(row=row, sticky=W)
sel2 = Label(padx=15, pady=10)
sel2.grid(row=row+1, sticky=W)
root.mainloop()


