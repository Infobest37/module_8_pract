def c(line):
    valu_1, operations, valu_2 = line.split(" ")
    valu_1 = int(valu_1)
    valu_2 = int(valu_2)
    # if operations == "+":
    #     print(f"Результат: {valu_1 + valu_2}")
    # if operations == "-":
    #     print(f"Результат: {valu_1 - valu_2}")
    # if operations == "*":
    #     print(f"Результат: {valu_1 * valu_2}")
    # if operations == "/":
    #     print(f"Результат: {valu_1 / valu_2}")
    # if operations == "//":
    #     print(f"Результат: {valu_1 // valu_2}")
    # if operations == "%":
    #     print(f"Результат: {valu_1 % valu_2}")


Lines = 0
with open('test.txt', 'r') as file:
    for line in file:
        Lines += 1
        try:
          c(line)
        except ValueError as e:
            if "unpack" in e.args[0]:
              print(f"Возникла ошибка в распаковки в строке: {Lines}, такого типа {e.args}")

            else:
                print(f"Другая ошибка {e}")



