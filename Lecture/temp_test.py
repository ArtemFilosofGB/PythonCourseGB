def delete_contact(lst, name=""):
    if name == "":
        name = input("Введите имя контакта: ")
    for name_in_lst in lst:
        if name_in_lst == name:
            lst.remove(name)

lst=[]
str="qqwe 234 asd"
lst.append(str)
str="ssss 234 aaa"
lst.append(str)

print(lst)
delete_contact(lst,"ssss 234 aaa")
print("deleted",lst)