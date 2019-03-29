print('a^2+b*x+c=0')
a=input('введите а: ')
b=input('введите b: ')
c=input('введите c: ')
if not a.isdigit():
    print('Введите число')
    quit()
if not b.isdigit():
    print('Введите число')
    quit()
if not c.isdigit():
    print('Введите число')
    quit()
a=float(a)
b=float(b)
c=float(c)
D=(b**2)-4*a*c
if D<0:
    print('D<0, ответа нет')
elif D:
    x1=(-b+(D**(1/2)))/2*a
    x2=(-b-(D**(1/2)))/2*a
    print(x1)
    print(x2)
