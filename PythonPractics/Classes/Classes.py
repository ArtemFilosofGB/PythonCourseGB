class Human:
    def __init__(self, name: str, age: int, work: str) -> None:
        self.name = name
        self.age = age
        self.work = work
    def __str__(self):
        return f"Имя:{self.name}, возраст: {self.age} лет, работает в  {self.work}"

    def working(self):
        print(f"{self.name} начал работать в {self.work}")

hum_1 = Human("Artem", 18, "IT")
hum_1.age=39
print(hum_1)
print(type(hum_1))
hum_1.working()