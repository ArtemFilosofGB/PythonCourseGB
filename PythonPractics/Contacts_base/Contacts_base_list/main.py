# программа телефонна книга


USER_NAME = "admin"
FILE_NAME = "contacts.txt"


# функции открвания файла на изменение
def open_file(file_name):
    with open(file_name, 'r') as file:
        lines = file.readlines()
    return lines


def count_contact(dbase: list):
    return len(dbase)


# Функция создания контакта
def create_contact(dbase: list):
    print("=====Создание контакта=====")
    name = input("Введите имя контакта :")
    t_number = input("Введите телефон :")
    nikname = input("Введите никнейм :")
    contact_str = f"{name};{t_number};{nikname}\n"
    dbase.append(contact_str)
    print("Добавлен контакт", contact_str)


# функция выхода и записи в файл
def exit(dbase: list):
    with open(FILE_NAME, 'w') as file:
        file.writelines(dbase)


# функция вывода меню
def print_menu():
    print("1. Создание контакта")
    print("2. Изменение контакта")
    print("3. Поиск контакта")
    print("4. Удаление контакта")
    print("5. Показать контакты")
    print("6. Выход")


def show_contact(dbase: list):
    print("=====Cписок контактов=====")
    print("Колличество контактов - ", str(len(dbase)))
    for line in dbase:
        print(line, end="")


def change_contact(dbase):
    print("=====Изменение контакта=====")
    show_contact(dbase)
    name = input("Введите имя контакта для изменения: ")
    t_number = input("Введите телефон;")
    nikname = input("Введите никнейм;")
    string = f"{name};{t_number};{nikname}\n"
    for name in dbase:
        if name == name:
            dbase.remove(name)
            dbase.append(string)
        else:
            print("Контакт не найден")


def find_contact(dbase: list):
    show_contact(dbase)
    print("=====Поиск контакта=====")
    print("Внимание происходит поиск контакта! \'0\' для отмены")
    name = input("Строка поиска: ")
    if name == '0':
        print("Отмена")
        return 0
    else:
        for line in dbase:
            if name in line:
                print("Найден контакт: ", line, end="")
            else:
                print("Контакт не найден")
                # find_contact(dbase)


def delete_contact(dbase: list, name=""):
    print("=====Удаление контакта=====", name)
    show_contact(dbase)
    print("Внимание происходит удаление контакта! \'0\' для отмены")
    if name == "":
        name = input("Введите имя контакта: ")
        if name == '0':
            print("Отмена")
            return 0
    for line in dbase:
        if name in line:
            dbase.remove(line)
            print(f"Контакт {line} удален")
            return 1
    else:
        print("Контакт не найден")


def main():
    dbase = open_file(FILE_NAME)
    # print(dbase)
    print("Колличество контактов - ", count_contact(dbase))
    # 3show_contact(dbase)
    while True:
        print_menu()
        user_choice = int(input())
        # "1. Create contact"
        if user_choice == 1:
            create_contact(dbase)
        # "2. Change contact"
        elif user_choice == 2:
            change_contact(dbase)
        # "3. Find contact"
        elif user_choice == 3:
            find_contact(dbase)
        # "4. Delete contact"
        elif user_choice == 4:
            delete_contact(dbase)
        # "5. Show contact"
        elif user_choice == 5:
            show_contact(dbase)
        # "6. Exit"
        elif user_choice == 6:
            exit(dbase)
            print("Good bye!")
            break


if __name__ == '__main__':
    main()
