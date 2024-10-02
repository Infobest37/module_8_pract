class Person:
    """ Создаем клас который проверяет возраст при котором он не должен быть
    равен отрицательному значению"""
    def __init__(self, name):
        self.name = name
        self.age = "Неправельный возраст"

    def set_age(self,age):
        try:
           if age < 0:
               raise print("Возраст не может быть отрицательным")
           self.age = age
        except TypeError as e:
                print(f"Ошибка {e}")



p = Person("Иван")
p.set_age(24)
print(f"Возраст {p.name}: {p.age}")