from tkinter import Tk, Label, Entry, Button, Toplevel, scrolledtext

USER_NAME = "admin"
FILE_NAME = "contacts.txt"
dbase = []


def open_file(file_name):
    try:
        with open(file_name, 'r') as file:
            lines = file.readlines()
    except Exception as e:
        print(e)
        print("Не удалось открыть файл")
        with open(file_name, 'a') as file:
            lines = []
    return lines


# Функция создания контакта
def create_contact():
    def btn_create_press():
        # Получаем данные из полей ввода
        name_value = name.get()
        t_number_value = t_number.get()
        nikname_value = nikname.get()

        # Формируем строку контакта и добавляем в базу данных контактов
        contact_str = f"{name_value};{t_number_value};{nikname_value}\n"
        dbase.append(contact_str)

        # Для отладки: печатаем содержимое dbase
        print(f'Добавлен контакт: {contact_str}')
        print(dbase)

        # Закрываем всплывающее окно
        window_create.destroy()
        show_contacts_in_window()

    # Создание всплывающего окна
    window_create = Toplevel(window)
    window_create.title("Создание контакта")
    window_create.geometry('400x200')

    # Метка описания
    lbl_create = Label(window_create, text="=====Создание контакта=====")
    lbl_create.pack()

    # Поля ввода на форме создания контакта
    name = Entry(window_create, width=40)
    name.pack()
    t_number = Entry(window_create, width=40)
    t_number.pack()
    nikname = Entry(window_create, width=40)
    nikname.pack()

    # Кнопка добавления контакта
    btn_create = Button(window_create, text="Добавить контакт", command=btn_create_press)
    btn_create.pack()


def exit():
    try:
        with open(FILE_NAME, 'w') as file:
            file.writelines(dbase)
    except Exception as e:
        print(e)
        print("Не удалось сохранить данные в файл")
    print("Завершение работы программы")
    # window.quit()


def change_contact():
    def btn_change_press():
        def btn_change_ok_press():
            print(f"Контакт {line} изменен на {name_to_change_ent.get()} {number_to_change_ent.get()} {nikname_to_change_ent.get()}")
            dbase.remove(line)
            dbase.append(f"{name_to_change_ent.get()};{number_to_change_ent.get()};{nikname_to_change_ent.get()}\n")
            show_contacts_in_window()
            window_changre.destroy()


        name_to_change = name_change.get()
        lbl_change_press =Label(window_changre, text=f"Поиск контакта {name_to_change}")
        lbl_change_press.pack()
        for line in dbase:
            if name_to_change in line:
                name_to_change_ent = Entry(window_changre, width=40)
                name_to_change_ent.pack()
                name_to_change_ent.insert(0, line)
                number_to_change_ent = Entry(window_changre, width=40)
                number_to_change_ent.pack()
                nikname_to_change_ent = Entry(window_changre, width=40)
                nikname_to_change_ent.pack()
                btn_change_ok = Button(window_changre, text="Изменить", command=btn_change_ok_press)
                btn_change_ok.pack()
                btn_change_cancel = Button(window_changre, text="Отмена", command=window_changre.destroy)
                btn_change_cancel.pack()

    window_changre = Toplevel(window)
    window_changre.title("Изменение контакта")
    window_changre.geometry('400x200')

    name_change= Entry(window_changre, width=40)
    name_change.pack()

    btn_change = Button(window_changre, text="Изменить контакт", command=btn_change_press)
    btn_change.pack()



def find_contact():
    def btn_find_press():
        # Получаем данные из полей ввода
        name_find_value = name_find.get()
        for line in dbase:
            if name_find_value in line:
                lbl_find['text'] = "Найден контакт: " + line
                print("Найден контакт: ", line, end="")
        else:
            print("Контакт не найден")

    # Создание всплывающего окна
    window_find = Toplevel(window)
    window_find.title("Поиск контакта")
    window_find.geometry('300x100')

    # Метка описания
    lbl_find = Label(window_find, text="=====Поиск контакта=====")
    lbl_find.pack()

    # Поля ввода
    name_find = Entry(window_find, width=40)
    name_find.pack()
    find_btn = Button(window_find, text="Поиск", command=btn_find_press)
    find_btn.pack()


def delete_contact():
    def btn_delete_press():
        def btn_alert_delete_press():
            dbase.remove(line)
            alert_delete.destroy()
            print("Контакт удален")
            lbl_delete['text'] = "Контакт удален {}".format(line)
            show_contacts_in_window()

        # Получаем данные из полей ввода
        name_delete_value = name_delete.get()
        print(name_delete_value)
        for line in dbase:
            print(line)
            if name_delete_value in line:
                alert_delete = Toplevel(window_delete)
                alert_delete.title(f"Удалить {line} ?")
                alert_delete.geometry('300x100')

                btn_alert_delete = Button(alert_delete, text="Удалить", command=btn_alert_delete_press)
                btn_alert_delete.pack()
                btn_alert_cancel = Button(alert_delete, text="Отмена", command=alert_delete.destroy)
                btn_alert_cancel.pack()
        else:
            print("Контакт не найден")
            lbl_delete['text'] = "Контакт не найден"
        # window_delete.destroy()

    window_delete = Toplevel(window)
    window_delete.title("Удаление контакта")
    window_delete.geometry('300x100')

    #метка на форме удаления
    lbl_delete = Label(window_delete, text="=====Удаление контакта=====")
    lbl_delete.pack()

    #поля ввода на форме удаления
    name_delete = Entry(window_delete, width=40)
    name_delete.pack()

    #кнопка удаления контакта
    delete_btn = Button(window_delete, text="Удалить", command=btn_delete_press)
    delete_btn.pack()



def show_contacts():
    create_scrollable_window()
    print(dbase)


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


def console_out():
    print(dbase)
def show_contacts_in_window():
    lbl = Label(window, text="Всего контактов: " + str(count_contact(dbase)))
    lbl.grid(column=0, row=0)
    list_contacts.delete('1.0', 'end')
    for contact in dbase:
        list_contacts.insert('end', contact + '\n')


dbase = open_file(FILE_NAME)
window = Tk()
window.title("Контакты")
window.geometry('345x740')
lbl = Label(window, text="")
lbl.grid(column=0, row=0)

# Кнопки
bnt1 = Button(window, text="Create Contact", command=create_contact, width=40)
bnt1.grid(column=0, row=2)
bnt2 = Button(window, text="Change Contact", command=change_contact, width=40)
bnt2.grid(column=0, row=3)
bnt3 = Button(window, text="Find Contact", command=find_contact, width=40)
bnt3.grid(column=0, row=4)
bnt4 = Button(window, text="Delete Contact", command=delete_contact, width=40)
bnt4.grid(column=0, row=5)
bnt5 = Button(window, text="Show Contact", command=show_contacts, width=40)
bnt5.grid(column=0, row=6)
bnt6 = Button(window, text="Save & Exit", command=exit, width=40)
bnt6.grid(column=0, row=7)
bnt7 = Button(window, text="console out", command=console_out, width=40)
bnt7.grid(column=0, row=8)


#отображение контактов на главном экране
list_contacts = scrolledtext.ScrolledText(window, width=40, height=30)
list_contacts.grid(column=0, row=9)

#Заполнение многострочного поля данными из dbase
show_contacts_in_window()

lbl_bottom=Label(window, text="Рабочая база {}".format(FILE_NAME))
lbl_bottom.grid(column=0, row=10)

lbl_bottom2=Label(window, text="Данные сохраняются только после корректного выхода")
lbl_bottom2.grid(column=0, row=11)

# Запуск цикла
window.mainloop()

# Когда же эта прогшрамма заработает как надо!!!!
# Когда же эта прогшрамма заработает как надо!!!!
