# Задача №49. Решение в группах
# Создать телефонный справочник с
# возможностью импорта и экспорта данных в
# формате .txt. Фамилия, имя, отчество, номер
# телефона - данные, которые должны находиться
# в файле.
# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в
# текстовом файле
# 3. Пользователь может ввести одну из
# характеристик для поиска определенной
# записи(Например имя или фамилию
# человека)
# 4. Использование функций. Ваша программа
# не должна быть линейной


# Открыть файл
# сохранить файл
# Создание контакта
# Изм контакт
# Найти контакт
# Удалить контакт
# показать контакт
# выход
#
# menu
def cls():
    print('\n' * 100)


FILE_NAME = "contacts.txt"


def print_menu():
    print("=" * 30)
    print("1. Create contact")
    print("2. Change contact")
    print("3. Find contact")
    print("4. Delete contact")
    print("5. Show contact")
    print("6. Exit")
    print("=" * 30)


def create_contact(file_name):
    print("=====Создание контакта=====")
    name = input("Введите имя контакта :")
    t_number = input("Введите телефон :")
    nikname = input("Введите никнейм :")
    string = f"{name};{t_number};{nikname}\n"
    with open(file_name, 'a') as data:
        data.writelines(string)
    print("Добавлен контакт",string)


def change_contact(file_name):
    # переписать с искользованием функции поска в функции изменения
    # использовать функцию удаления для изменения
    print("=====Изменение контакта=====")
    with open(file_name, 'r') as data:
        for line in data:
            print(line, end="")
    name = input("Введите имя контакта;")
    t_number = input("Введите телефон;")
    nikname = input("Введите никнейм;")
    string = f"{name};{t_number};{nikname}\n"
    with open(file_name, 'a') as data:
        data.writelines(string)


def find_contact(file_name,name=""):
    print("=====Поиск контакта=====")
    if name == "":
        name = input("Строка поиска: ")
    with open(file_name, 'r') as data:
        for line in data:
            if name.lower() in line.lower():
                print(line)
        else:
            print("Контакт не найден")


def show_contact(file_name):
    print("=====Cписок контактов=====")
    print("Колличество контактов - ", count_contact())
    with open(file_name, 'r') as data:
        for line in data:
            print(line, end="")
          #  lines = data.readlines()
    #     print(lines,"***********")
    # return lines

def read_file_lines(file_name):
    with open(file_name, 'r') as file:
        lines = file.readlines()
    return lines

def delete_contact(file_name):
    print("=====Удаление контакта=====")
    lines = read_file_lines(file_name)  # return list
    print("Внимание происходит удаление контакта! \'0\' для отмены")
    name = input("Введите имя контакта: ")
    if name == '0':
        print("Отмена")
        return 0
find_contact(FILE_NAME, name)

    with open(FILE_NAME, "r") as file:
        lines = file.readlines()
    del lines[1]
    with open(FILE_NAME, "w") as file:
        file.writelines(lines)



def count_contact(file_name=FILE_NAME):
    with open(file_name, 'r') as fp:
        for count, line in enumerate(fp):
            pass
    return count + 1


# функция отчистки консоли


def main():
   # print("Колличество контактов - ", count_contact())
    while True:
        print_menu()
        user_choice = int(input())
        # "1. Create contact"
        if user_choice == 1:
            create_contact(FILE_NAME)
        # "2. Change contact"
        elif user_choice == 2:
            change_contact(FILE_NAME)
        # "3. Find contact"
        elif user_choice == 3:
            find_contact(FILE_NAME)
        # "4. Delete contact"
        elif user_choice == 4:
            delete_contact(FILE_NAME)
        # "5. Show contact"
        elif user_choice == 5:
            show_contact(FILE_NAME)
        # "6. Exit"
        elif user_choice == 6:
            break


if __name__ == '__main__':
    main()
    print("Good bye!")
