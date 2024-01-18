class Contact:
    def __init__(self, name: str, phone: str, comment: str):
        self.name = name
        self.phone = phone
        self.comment = comment
    def to_str(self, sep: str = ';'):
        return f'{self.name}{sep}{self.phone}{sep}{self.comment}'


phone_book= {}
path = 'phones.txt'
SEPARATOR = ';'
def open_file():
    global phone_book
    with open(path, 'r', encoding='UTF-8') as file:
        for line in file:
            file = list(map(lambda x: x.strip().split(SEPARATOR), file.readlines()))
            #strip() - удаляет пробелы в начале и в конце строки

    phone_book ={}
    return phone_book
def save_file():
    pass

def next_id():
    global phone_book
    return (max(phone_book.keys()) + 1) if phone_book else 1

def new_contact(contact: list[str]):
    global phone_book
    phone_book[next_id()] = contact

def new_contact_added_successfully():
    pass

def find_contact(word: str)->dict[int,list[str]]:
    global phone_book
    result={}
    for u_id, contact in phone_book.items():
        if word in ' '.join(contact):
            result[u_id]=contact
    return result

def change_contact(c_id: int, c_contact: list[str]):
    global phone_book
    phone_book[c_id] = c_contact