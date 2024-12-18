# Вводим количество команд
N = int(input())

# Вычисляем максимальное количество победителей
if N % 2 == 0:
    max_winners = N // 2
else:
    max_winners = (N // 2) + 1

# Выводим результат
print(max_winners)