len  = int(input('длина списка: '))

min = 1
max = 0

list = []
i = 0

while i != len:
    s = float(input('элемент списка №' + str(i + 1) + ' (пишите числа через .): '))
    list.append(s)
    i += 1

i = 0

while i != len:
    q = list[i] % 1
    if q < min:
        min = q
    if q > max:
        max = q
    i += 1


res = max - min

print(res)
