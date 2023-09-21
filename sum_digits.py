def sum_digits(number):
    a = 0
    while number > 0:
        a += number % 10
        number = int(number / 10)
    return a
num = 123456
print("Сумма цифр числа ", num, ":", sum_digits(num))
