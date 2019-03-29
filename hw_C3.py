a=input('введите предложение: ')
b=a.split()
c=b[0]
for i in b:
    if len(i)<len(c):
        c=i
print(len(c))
