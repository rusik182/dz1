# <Задание 4>
# Напишите программу, которая будет преобразовывать десятичное число в двоичное.

# Пример:
# 45 => 101101
# 3 => 11
# 2 => 10

x = int(input('Введите десятичное число: '))
 
y = ''
 
while x > 0:
    y = str(x % 2) + y
    x = x // 2
 
print(y)