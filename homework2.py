len  = int(input('длина списка: '))

list = []
listres = []

last = len - 1
first = 0

i = 0

while i != len:
    s = int(input('элемент списка №' + str(i + 1) + ': '))
    list.append(s)
    i += 1
i = 0

while i != (len + 1) // 2:
    k = list[first] * list[last]
    listres.append(k)
    first += 1
    last -= 1
    i += 1

print(listres)