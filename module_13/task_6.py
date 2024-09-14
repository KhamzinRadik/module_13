# -*- coding: cp1251 -*-
def indepht (x):
    return x**3-3*x**2-12*x+5

danger=0
while danger<=0 or danger>4 :

    danger=float(input('Введите максимально допустимый уровень опасности:'))
print (abs(indepht(danger)))