def calculator():
    a = float(input("Первое число: "))
    op = input("Оператор (+, -, *, /): ")
    b = float(input("Второе число: "))

    if op == '+':
        result = a + b
    elif op == '-':
        result = a - b
    elif op == '*':
        result = a * b
    elif op == '/':
        result = a / b if b != 0 else "Ошибка: деление на 0"
    else:
        result = "Неизвестный оператор"

    print("Результат:", result)

calculator()