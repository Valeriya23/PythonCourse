with open ('C:/Users/lerok/Downloads/rosalind_subs (1).txt','r') as file:
    c=file.read()
c=c.split()
a=c[0]
b=c[1]
d=[]
for i in range (len(a)):
    if a[i:i+len(b)]==b:
        d.append(i+1)
print(d)
