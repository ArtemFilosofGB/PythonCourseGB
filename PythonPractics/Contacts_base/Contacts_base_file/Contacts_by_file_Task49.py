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
    print("1. Создание")
    print("2. Изменение")
    print("3. Поиск") #done
    print("4. Удаление") #done
    print("5. Показать книгу")#done
    print("6. Выход")#done
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
    show_contact(file_name)
    name = input("Введите имя контакта для изменения: ")
    t_number = input("Введите телефон;")
    nikname = input("Введите никнейм;")
    string = f"{name};{t_number};{nikname}\n"
    delete_contact(file_name, name)
    with open(file_name, 'a') as data:
        data.writelines(string)


def find_contact(file_name,name=""):
    print("=====Поиск контакта=====")
    if name == "":
        name = input("Строка поиска: ")
    with open(file_name, 'r') as data:
        for line in data:
            if name.lower() in line.lower():
                print(line, end="")
        else:
            print("Контакт не найден")


def show_contact(file_name):
    print("=====Cписок контактов=====")
    print("Колличество контактов - ", str(count_contact()))
    with open(file_name, 'r') as data:
        for line in data:
            print(line, end="")


def read_file_lines(file_name):
    with open(file_name, 'r') as file:
        lines = file.readlines()
    return lines

def delete_contact(file_name, name=""):
    print("=====Удаление контакта=====", name)
    lines = read_file_lines(file_name)  # return list
    show_contact(file_name)
    print("Внимание происходит удаление контакта! \'0\' для отмены")
    if name == "":
        name = input("Введите имя контакта: ")
        if name == '0':
            print("Отмена")
            return 0
    with open(file_name, 'w') as file:
        for line in lines:
            if name not in line:
                file.write(line)


def count_contact(file_name=FILE_NAME):
    with open(file_name, 'r') as fp:
        for count, line in enumerate(fp):
            pass
    return count + 1


# функция отчистки консоли


def main():
    print("Колличество контактов - ", count_contact())
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
            print("Good bye!")
            break


if __name__ == '__main__':
    main()

