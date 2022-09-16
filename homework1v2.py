import random

res = 0
list = []
i = 0
len = int(input('длина списка: '))

while i != len:
    s = int(input('элемент списка №' + str(i + 1) + ': '))
    list.append(s)
    i += 1

print(list)

i = 1
while i < len:
    res = res + list[i]
    i += 2

print(res)