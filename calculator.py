import math
def calc():
    while(True):
        try:
            a = float(input("Введите первое число:"))
        except (ValueError):
             print("Это не число.")
             continue
        c = int(a)
        oper = input("Введите операцию (примечание: ** - возведение в степень, sqrt - квадратный корень, ! - факториал, sin - синус, cos - косинус, tg - тангенс):") 
        if oper == "+" or oper == "-" or oper == "*" or oper == "/" or oper == "**":
            try:
                b = float(input("Введите второе число:"))
            except (ValueError):
                print("Это не число.")
                continue
            if oper == "+":
                print(a + b)
            elif oper == "-":
                print(a - b)
            elif oper == "*":
                print(a * b)
            elif oper == "/":
                try:
                    print(a / b)
                except (ZeroDivisionError):
                    print("На 0 делить нельзя")
            elif oper == "**":
                print(a ** b)
        elif oper == "sqrt":
            try:
                print(math.sqrt(a))
            except (ValueError):
                print("Из такого числа корень не извлекается.")
        elif oper == "!":
            try:
                print(math.factorial(c))
            except (ValueError):
                print("Факториала такого числа не существует.")
        elif oper == 'sin':
            print(math.sin(a))
        elif oper == 'cos':
            print(math.cos(a))
        elif oper == 'tg':
            print(math.tan(a))
calc()
