numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
# Создаем пустые списки для простых и непростых чисел
primes = []
not_primes = []

# Перебираем каждый элемент из списка numbers
for num in numbers:
    if num < 2:  # Число 1 и отрицательные числа не являются простыми
        continue

    is_prime = True  # Предполагаем, что число простое

    # Вложенный цикл для проверки на делимость
    for divisor in range(2, int(num**0.5) + 1):  # Проверяем делители до корня из num
        if num % divisor == 0:  # Если num делится на divisor
            is_prime = False  # Число не простое
            break  # Выходим из цикла, так как нашли делитель

    # В зависимости от значения is_prime добавляем число в соответствующий список
    if is_prime:
        primes.append(num)
    else:
        not_primes.append(num)

# Выводим списки на консоль
print("Primes:", primes)
print("Not Primes:", not_primes)