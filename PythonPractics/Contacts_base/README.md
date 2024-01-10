## Записная книга 
_Реализовано двумя стособами: через работу с файлом, и через список(dbase)_
### Contacts_base_file
_Вариант исполнения основанный на работе с файлом_

#### Реализованы функции:

print_menu()

create_contact(FILE_NAME)

change_contact(FILE_NAME)

find_contact(FILE_NAME)

delete_contact(FILE_NAME)

show_contact(FILE_NAME)

### Contacts_base_list
_Вариант исполнения основанный на работе со списком_


### Contacts_base_windows
_Оконная реализация записной книги, использована библионека **Tkinter**_

![window](window.png)

* Create - работает - открыват файлы
* Change - работает (выбранный контакт удаляется, заполненые поля создают новую запись)
* Find - работает в отдельном окне
* Delete - работает с окном предупреждения
* Show - работает в отдельном окне
* Save & Exit - работает с сохранением в файл после create

Структура

![structure](structure.png)
