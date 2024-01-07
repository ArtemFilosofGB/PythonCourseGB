from tkinter import Tk, Label, Entry, Button, Toplevel

dbase = []  # Предположим, что dbase был определен вне функции

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

# Создание основного окна
window = Tk()
window.title("Основное окно")
window.geometry('200x100')

# Кнопка "Создание контакта"
btn_create_contact = Button(window, text="Создание контакта", command=create_contact)
btn_create_contact.pack()

# Запуск цикла обработки сообщений основного окна
window.mainloop()
