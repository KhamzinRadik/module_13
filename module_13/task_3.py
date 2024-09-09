# -*- coding: cp1251 -*-
def flip_over (a):
 str_a=str(a)
 a=str(a)
 count=len(str(a))
 a=''
 for i in range (count-1,-1,-1):  
     a+=str_a[i]
 a=int(a)
 return a




N,K=int(input('Введите 2 числа :')),input()
int_N=flip_over(N)
print('Первое число наоборот:',int_N)
int_K=flip_over(K)
print('Второе число наоборот:',int_K)
print ('Сумма:',int_N+int_K)