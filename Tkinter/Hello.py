from tkinter import *

root = Tk()
root.geometry("300x250+400+200")

root.update_idletasks()
print(root.geometry())  # "300x250+400+200"
label = Label(text="Hello") # создаем текстовую метку
label.pack()    # размещаем метку в окне

root.mainloop()
