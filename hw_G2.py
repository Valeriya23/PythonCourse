import itertools as it
a=2
def simple_numbers():
    yield a
    D={}
    for i in it.count(3,2):
        p=D.pop(i,0)
        if p!=0:
            x=i+p
            while x in D: x+=p
            D[x]=p
        else:
            yield i
            D[i*i]=2*i
#Пример использования:
b=0
b=list(it.islice(simple_numbers(),b,b+10))
print(b)
