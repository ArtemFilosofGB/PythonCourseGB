## Записная книга 
### Contacts

#### Реализованы функции:
```commandline
print_menu()
```
Выводит меню работы с записной книжкой

~~~
create_contact(FILE_NAME)
~~~
Создаёт ноавый контакт в диалоге imput
~~~
change_contact(FILE_NAME)
~~~
Изменение созданного контакта
~~~
find_contact(FILE_NAME)
~~~
Поиск по записной книжке
~~~
delete_contact(FILE_NAME)
~~~
Удаление контакта по заданному имени (используется в функции change_contact(FILE_NAME))
~~~
show_contact(FILE_NAME)
~~~
Выводит записную книгу (Используется внутри change_contact(FILE_NAME) и delete_contact(FILE_NAME))

~~~
count_contact(file_name=FILE_NAME):
~~~
Выводит количество записей в записной книге
