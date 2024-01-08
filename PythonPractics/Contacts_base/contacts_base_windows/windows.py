from tkinter import Tk, Label, Entry, Button, Toplevel, scrolledtext
USER_NAME = "admin"
FILE_NAME = "contacts.txt"
dbase=[]


def open_file(file_name):
    with open(file_name, 'r') as file:
        lines = file.readlines()
    return lines

# Функция создания контакта
def create_contact():
    def btn_create_press():
        # Получаем данные из полей ввода
        name_value = name.get()
        t_number_value = t_number.get()
        nikname_value = nikname.get()

        # Формируем строку контакта и добавляем в базу данных контактов
        str_contact = f"{name_value};{t_number_value};{nikname_value}"
        dbase.append(str_contact)

        # Для отладки: печатаем содержимое dbase
        print(f'Добавлен контакт: {str_contact}')
        print(dbase)

        # Закрываем всплывающее окно
        window_create.destroy()

    # Создание всплывающего окна
    window_create = Toplevel(window)
    window_create.title("Создание контакта")
    window_create.geometry('400x200')

    # Метка описания
    lbl_create = Label(window_create, text="=====Создание контакта=====")
    lbl_create.pack()

    # Поля ввода
    name = Entry(window_create, width=40)
    name.pack()
    t_number = Entry(window_create, width=40)
    t_number.pack()
    nikname = Entry(window_create, width=40)
    nikname.pack()

    # Кнопка добавления контакта
    btn_create = Button(window_create, text="Добавить контакт", command=btn_create_press)
    btn_create.pack()





def exit(dbase: list):
    with open(FILE_NAME, 'w') as file:
        file.writelines(dbase)
    #window.quit()

def change_contact(dbase):
    pass

def find_contact(dbase):
    pass

def delete_contact(dbase):
    pass

def show_contacts():
    create_scrollable_window()
def create_scrollable_window():
    # Создание всплывающего окна для отображения контактов
    window_contacts = Toplevel(window)
    window_contacts.title("Список контактов")
    window_contacts.geometry('400x200')

    # Многострочное поле с вертикальным ползунком прокрутки
    txt_contacts = scrolledtext.ScrolledText(window_contacts, width=40, height=10)
    txt_contacts.pack()
    # Заполнение многострочного поля данными из dbase
    for contact in dbase:
        txt_contacts.insert('end', contact + '\n')


def count_contact(dbase):
    return len(dbase)



def pritn_button_menu():
    bnt1 = Button(window, text="Create Contact", command=create_contact, width=20)
    bnt1.grid(column=0, row=2)
    bnt2 = Button(window, text="Change Contact", command=change_contact(dbase), width=20)
    bnt2.grid(column=0, row=3)
    bnt3 = Button(window, text="Find Contact", command=find_contact(dbase), width=20)
    bnt3.grid(column=0, row=4)
    bnt4 = Button(window, text="Delete Contact", command=delete_contact(dbase), width=20)
    bnt4.grid(column=0, row=5)
    bnt5 = Button(window, text="Show Contact", command=show_contacts, width=20)
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


