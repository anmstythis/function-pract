import math
try:
    a = float(input("Введите первое число:"))
except(ValueError):
    print("Это не число.")
    proceed = str(input("Для возобновления операции введите 'y'. В ином случае введите любой другой символ:"))
    if proceed == 'y':
        a = float(input("Введите первое число:"))
oper = input("Введите операцию (примечание: ** - возведение в степень, sqrt - квадратный корень, ! - факториал, sin - синус, cos - косинус, tg - тангенс):") 
# ** - возведение в степень, sqrt - квадратный корень, ! - факториал, sin - синус, cos - косинус, tg - тангенс
c = int(a)
if oper == '+':
    b = float(input("Введите второе число:"))
    print(a + b)
elif oper == '-':
    b = float(input("Введите второе число:"))
    print(a - b)
elif oper == '*':
    b = float(input("Введите второе число:"))
    print(a * b)
elif oper == '/':
    b = float(input("Введите второе число:"))
    if b != 0:
        print(a / b)
    else:
        print("На 0 делить нельзя")
elif oper == '**':
    b = float(input("Введите второе число:"))
    print(a**b)
elif oper == 'sqrt' and a >= 0:
    print(math.sqrt(a))
elif oper == 'sqrt' and a < 0:
    print("Из такого числа корень не извлекается.")
elif oper == '!':
    if a == c and a >= 0:
        print(math.factorial(c))
    else:
        print("Факториала такого числа не существует.")
elif oper == 'sin':
    print(math.sin(a))
elif oper == 'cos':
    print(math.cos(a))
elif oper == 'tg':
    print(math.tan(a))
proceed = str(input("Для возобновления операции введите 'y'. В ином случае введите любой другой символ:"))
while proceed == 'y':
    try:
        a = float(input("Введите первое число:"))
    except(ValueError):
        print("Это не число.")
        continue
    c = int(a)
    oper = input("Введите операцию (примечание: ** - возведение в степень, sqrt - квадратный корень, ! - факториал, sin - синус, cos - косинус, tg - тангенс):") 
# ** - возведение в степень, sqrt - квадратный корень, ! - факториал, sin - синус, cos - косинус, tg - тангенс
    if oper == '+':
        b = float(input("Введите второе число:"))
        print(a + b)
    elif oper == '-':
        b = float(input("Введите второе число:"))
        print(a - b)
    elif oper == '*':
        b = float(input("Введите второе число:"))
        print(a * b)
    elif oper == '/':
        b = float(input("Введите второе число:"))
        if b != 0:
            print(a / b)
        else:
            print("На 0 делить нельзя")
    elif oper == '**':
        b = float(input("Введите второе число:"))
        print(a**b)
    elif oper == 'sqrt' and a >= 0:
        print(math.sqrt(a))
    elif oper == 'sqrt' and a < 0:
        print("Из такого числа корень не извлекается.")
    elif oper == '!':
        if a == c and a >= 0:
            print(math.factorial(c))
        else:
            print("Факториала такого числа не существует.")
    elif oper == 'sin':
        print(math.sin(a))
    elif oper == 'cos':
        print(math.cos(a))
    elif oper == 'tg':
        print(math.tan(a))
    proceed = str(input("Для возобновления операции введите 'y'. В ином случае введите любой другой символ:"))