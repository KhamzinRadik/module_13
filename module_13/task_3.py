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




N,K=int(input('������� 2 ����� :')),input()
int_N=flip_over(N)
print('������ ����� ��������:',int_N)
int_K=flip_over(K)
print('������ ����� ��������:',int_K)
print ('�����:',int_N+int_K)