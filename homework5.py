k = int(input('ваше число: '))

i = 0

list = []
listotr = [0, 1]

fst = 0
snd = 1

raspred = 1

while i != k:
    i += 1
    if raspred == 1:
        fst = fst - snd
        raspred = 2
        listotr.append(fst)
    elif raspred == 2:
        snd = snd - fst 
        raspred = 1
        listotr.append(snd)



while i != 0:
    list.append(listotr[i])
    i -= 1

list.append(0)
list.append(1)

i = 1

fst = 0
snd = 1

raspred = 1

while i != k:
    i += 1
    if raspred == 1:
        fst = fst + snd
        raspred = 2
        list.append(fst)
    elif raspred == 2:
        snd = snd + fst 
        raspred = 1
        list.append(snd)

print(list)
