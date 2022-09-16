import random

res = 0
list = []
i = 0
len = random.randint(3,15)
print(len)

while i != len:
    list.append(random.randint(1, 15))
    i += 1

print(list)

i = 1
while i < len:
    res = res + list[i]
    i += 2

print(res)