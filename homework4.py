number = int(input('ваше число в десятичной системе счисления: '))
a = False
res = ''

while a == False:
    if number != 0:
        res += str(number % 2)
        number = number // 2
    else: 
        a = True

res = res [::-1]

print('ваше число в двоичной системе счисления: ' + str(res))