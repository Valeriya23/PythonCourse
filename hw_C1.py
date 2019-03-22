a=input('Введите числа через пробел: ')
b=[int(symbol) for symbol in a.split()]
for i in range (1, len(b)):
    if b[i-1]<b[i]:
        print(b[i])
