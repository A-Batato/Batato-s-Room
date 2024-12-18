# Вводим три целых числа
a = int(input())
b = int(input())
c = int(input())

# Сравниваем числа
if a >= b:
    if a >= c:
        print(a)  # a наибольшее
    else:
        print(c)  # c наибольшее
else:
    if b >= c:
        print(b)  # b наибольшее
    else:
        print(c)  # c наибольшее1
