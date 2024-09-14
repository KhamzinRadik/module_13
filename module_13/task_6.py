# -*- coding: cp1251 -*-

def root(f,a,b,d):
    fa=f(a)
    fb=f(b)
    if fa*fb<0:
        while abs(a-b)>d:
            c=0.5*(a+b)
            fc=f(c)
            if fc*fa<0:
                b=c
                fb=fc
            else:
                a=c
                fa=fc
        return 0.5*(a+b)
    else:
        return None
        
d=float(input("d="))        
print(root(lambda x: x**3 - 3*x**2 - 12*x + 10,0,4,d))
