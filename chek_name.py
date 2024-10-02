class InvalidNameError(Exception):
    pass
class User:
    def set_name(self, name):
        try:
            if any(char.isdigit() for char in name):

                """Давайте разберем строчку if any(char.isdigit() for char in name): шаг за шагом:
                  Это цикл, который проходит по каждому символу строки name.
                  Например, если name = "Алексей123", то цикл пройдет через каждый символ: 'А', 'л', 'е', 'к', 'с', 'е', 'й', '1', '2', '3'.
                  char.isdigit():
                  Метод .isdigit() проверяет, является ли символ числом.
                  Например, '1'.isdigit() вернет True, потому что '1' — это число.
                  Если символ — буква, пробел или другой нечисловой символ, то .isdigit() вернет False.
                  for char in name (внутри any()):
                  Мы создаем генератор, который по очереди проверяет каждый символ в строке name с помощью char.isdigit().
                  any():

                  Функция any() возвращает True, если хотя бы одно из условий внутри генератора истинно (то есть хотя бы один символ — это цифра)."""

                raise InvalidNameError(f"Имя не должно содержать цифр: {name}")
            self.name = name
        except InvalidNameError as e:
            print(f"Ошибка: {e}")


u = User()
u.set_name("Александр")  # Ожидаемый результат: корректное имя
u.set_name("Александр123")


