# -*- coding: cp1251 -*-

def preobrazovanme(namber):
    i=0
    if namber<1:

     while(True):
      namber=namber*10
      
      i=i+1
      if namber>=1:
          break
      
    print ('Формат плавающей точки: x =',round(namber,2),'*10**',i*-1)
    if namber>1:
        while(True):
            namber=namber/10
            
            i=i+1
            if namber<10:
             break
      
    print ('Формат плавающей точки: x =',round(namber,2),'*10**',i)

    return namber

    

nam=float(input(' введите число : '))
preobrazovanme(nam)
