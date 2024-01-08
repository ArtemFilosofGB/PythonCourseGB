from tkinter import Tk, Label, Entry, Button, Toplevel, scrolledtext
import os
dbase = []  # Предположим, что dbase был определен вне функции

def read_contacts_from_file():
    # Проверяем, существует ли файл
    if os.path.exists('contacts.txt'):
        # Открываем файл
        with open('contacts.txt', 'r') as f:
            # Читаем содержимое файла построчно и добавляем каждую строку в dbase
            for line in f:
                dbase.append(line.strip())
    else:
        print('Файл contacts.txt не существует.')

def write_contacts_to_file():
    # Открываем файл для записи
    with open('contacts.txt', 'w') as f:
        # Записываем каждый контакт из dbase в файл
        for contact in dbase:
            f.write(contact + '\n')
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

def show_contacts():
    create_scrollable_window()


def exit_app():
    write_contacts_to_file()
    window.destroy()

# Создание основного окна
window = Tk()
window.title("Основное окно")
window.geometry('200x100')

# Кнопка "Создание контакта"
btn_create_contact = Button(window, text="Создание контакта", command=create_contact)
btn_create_contact.pack()

# Кнопка "Показать контакты"
btn_show_contacts = Button(window, text="Показать контакты", command=show_contacts)
btn_show_contacts.pack()

# Кнопка "Выход"
btn_exit = Button(window, text="Выход", command=exit_app)
btn_exit.pack()

# Чтение контактов из файла при запуске приложения
read_contacts_from_file()

# Запуск цикла обработки сообщений основного окна
window.mainloop()
