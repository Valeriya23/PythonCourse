def save_func_name(func):
    def dr_func(*args, **kwargs):
        result=func(*args,**kwargs)
        return result
        file1= open(func._name_+'.txt','w')
        file1.write(str(func(*args,**kwargs)))
        file1.close()
    return dr_func
#Пример использования:
@save_func_name
def add(a,b):
    return (a+b)
print (add(2,3))
