# -*- coding: cp1251 -*-

kolebaniya_m=int(input('������� ��������� ���������:'))
stop_m=float(input('������� ��������� ���������: '))
count =0
while kolebaniya_m>stop_m:
    count+=1
    kolebaniya_m=float(kolebaniya_m-(kolebaniya_m*0.084))
print ('������� ��������� �������������� �����',count,'���������')