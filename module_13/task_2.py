# -*- coding: cp1251 -*-

def maximum_of_two(namber_1, namber_2):
	if namber_1>namber_2:
		return namber_1
	else:
		return namber_2

def maximum_of_three (maximum_1,namber_3):
	if maximum_1>namber_3:
		return maximum_1
	else:
		return namber_3


namber_1, namber_2, namber_3=int (input(' ������� 3 ����� :')),int (input()),int (input())
namberX=int((maximum_of_two(namber_1, namber_2)))
print('������������� ����� ����� ',maximum_of_three(namberX,namber_3))
