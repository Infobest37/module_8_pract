class NumberProcessor:
    """Создаем клас при котором идет проверка списка в котором имееться  строки и проверяем список
    если встроке есть не целые числа тога выводим ошибку"""
    def list_number(self, numbers):
        for i in numbers:
            try:
                if not isinstance(i,(float, int)):
                    raise print("Число не целое")
                print(f"Обработака числа: {i}")

            except TypeError:
                print("Ошибка")


numbers = [1, 2.5, 'три', 4, 'пять', 6, 7,"6"]
processor = NumberProcessor()
processor.list_number(numbers)

