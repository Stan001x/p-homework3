import random
size = int(input('Введите количество элементов списка: '))
num = int(input('Введите число для проверки его наличия в списке: '))
count = 0
my_list = [random.randint(0,10) for _ in range(size)]
print(my_list)
for i in range(size - 1):
    if num == my_list[i]:
        count += 1
print(f'число {num} встречается {count} раз')
if count == 0:
    min = abs(num - my_list[0])
    for i in range(size - 1):
        if abs(num - my_list[i]) < min:
            min = abs(num - my_list[i])
            near = my_list[i]
    
    print(f'Ближайшее число: {near}')
