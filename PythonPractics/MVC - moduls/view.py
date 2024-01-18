import text
import controller
import model
def main_menu():
    for n, item in enumerate(text.main_menu):
        if n==0:
            print(item)
        else:
            print(f"\t{n}. {item}")
    while True:
        choice = input("Выберите пункт меню: ")
        if choice.isdigit() and 0 < int(choice) < len(text.main_menu):
            return int(choice)
        else:
            print(f"Введите пункт меню от 1 до  {len(text.main_menu)-1}")

def show_contacts(p_book: dict[int,list[str]]):
    max_size =list(lambda x: len(max(x, key=len)),map(list(zip(*p_book.values()))))
    print(max_size)
    # if len(p_book) == 0:
    #     print("Телефонная книга пуста")
    # else:
    #     for key in p_book:
    #         print(key, p_book[key])

    if p_book:
        for n,contact in p_book.items():
            print(f"{n} {contact[0]} {contact[1]} {contact[2]}")
        else:
            print(text.empty_phone_book)
    # for n,contact in p_book.items():
    #     if choice == 3:
    #         print(f"{n} {contact[0]} {contact[1]} {contact[2]}")
    #     else:
    #         print(f"{n} {contact[0]} {contact[1]}")

def print_massage(message: str):
    print('\n' + message)

def add_contact(message: list[str]):
    for mes in message:
        contact.append(input(mes))


def imput_data(message: str)->str:
    return f'{message}'