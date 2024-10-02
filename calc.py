



class SimpleCalculator:
    ''' Создали конкулятор который в последствии еще при желании можно отладить он может принимать
    вырожения в терминале и с помощью цикла while создовать постоянный колькулятор пока не напишешь ключевое
    слово'''
    def calc(self, expression):
        # Ожидаем, что числа разделены пробелами: "число оператор число"
        valu_1, operator, valu_2 = expression.split(" ")
        valu_1 = int(valu_1)  # Преобразуем первое число в int
        valu_2 = int(valu_2)  # Преобразуем второе число в int
        print(expression.split())
        #Выполняем операцию в зависимости от оператора
        if operator == "+":
            expression = valu_1 + valu_2
        elif operator == "-":
            expression = valu_1 - valu_2
        elif operator == "*":
            expression = valu_1 * valu_2
        elif operator == "/":
            if valu_2 == 0:
                raise ZeroDivisionError("Деление на ноль невозможно")
            expression = valu_1 / valu_2
        else:
            raise ValueError("Неверный оператор")
        return expression






s = SimpleCalculator()

while True:

    line = input("Введите выражение (или 'exit' для выхода): ")
    try:
        if line.lower() == "exit":
            break
        result_1 = s.calc(line)
        if result_1 is not None:
           print(f"Результат: {result_1}")
    except ValueError as e:
        if "unpack" in e.args[0]:
            print(f"Нехватает одного числа для выполнения вырожения")
        else:
            print(f"Значение не может быть строкой {e}")



