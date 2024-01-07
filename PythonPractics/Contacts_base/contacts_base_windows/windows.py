from tkinter import *
USER_NAME = "admin"
FILE_NAME = "contacts.txt"
dbase=[]


def open_file(file_name):
    with open(file_name, 'r') as file:
        lines = file.readlines()
    return lines

# Функция создания контакта
def create_contact(dbase: list):
    window_create = Tk()
    window_create.title("Создание контакта")
    window_create.geometry('400x400')
    lbl_create = Label(window_create, text="=====Создание контакта=====")
    lbl_create.grid(column=0, row=0)
    name = Entry(window_create, text="Введите имя контакта :", width=20)
    name.grid(column=0, row=1)
    t_number = Entry(window_create, text="Введите телефон :", width=20)
    t_number.grid(column=0, row=2)
    nikname = Entry(window_create, text="Введите никнейм :", width=20)
    nikname.grid(column=0, row=3)
    btn_create = Button(window_create, text="Добавить контакт", command=btn_create_press(f"{name.get()};{t_number.get()};{nikname.get()}"))
    btn_create.grid(column=0, row=4)
    window_create.quit()

def btn_create_press(str_contact:str):
    dbase.append(str_contact)
    print("Добавлен контакт"+str_contact)




def exit(dbase: list):
    with open(FILE_NAME, 'w') as file:
        file.writelines(dbase)
    window.quit()

def change_contact(dbase):
    pass

def find_contact(dbase):
    pass

def delete_contact(dbase):
    pass

def show_contact(dbase):
    pass




def pritn_button_menu():
    bnt1 = Button(window, text="Create Contact", command=create_contact(dbase), width=20)
    bnt1.grid(column=0, row=2)
    bnt2 = Button(window, text="Change Contact", command=change_contact(dbase), width=20)
    bnt2.grid(column=0, row=3)
    bnt3 = Button(window, text="Find Contact", command=find_contact(dbase), width=20)
    bnt3.grid(column=0, row=4)
    bnt4 = Button(window, text="Delete Contact", command=delete_contact(dbase), width=20)
    bnt4.grid(column=0, row=5)
    bnt5 = Button(window, text="Show Contact", command=show_contact(dbase), width=20)
    bnt5.grid(column=0, row=6)
    bnt6 = Button(window, text="Save & Exit", command=exit(dbase), width=20)
    bnt6.grid(column=0, row=7)


dbase = open_file(FILE_NAME)
window = Tk()
window.title("Контакты")
window.geometry('400x800')
lbl = Label(window, text="Всего контактов: " + str(count_contact(dbase)))
lbl.grid(column=0, row=0)
pritn_button_menu()
window.mainloop()


