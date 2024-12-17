my_string=str(input("Введите текст: "))
print(my_string, "Количество символов в строке:", len(my_string)) #Вывод строки и подсчет количества знаков
print(my_string.upper()) #Строка в верхнем регистре
print(my_string.lower()) #Строка в нижнем регистре
print(''.join(my_string.split())) #Строка без пробелов между словами
print(my_string[0]) #Первый знак строки
print(my_string[-1]) #Последний знак строки


