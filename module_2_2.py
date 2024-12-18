first = int(input('First:'))
second = int(input('Second:'))
third = int(input('Third:'))

unique_numbers = {first, second, third}

if len(unique_numbers) == 1:
    print(3)
elif len(unique_numbers) == 2:
    print(2)
else:
    print(0)