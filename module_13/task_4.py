# -*- coding: cp1251 -*-
def count_numbers(first_n):
     first_num_count = 0
     temp = first_n
     while temp > 0:
        first_num_count += 1
        temp = temp // 10
     return first_num_count
def change_number (first_n,first_num_count):
    last_digit = first_n % 10
    first_digit = first_n // 10 ** (first_num_count - 1)
    between_digits = first_n % 10 ** (first_num_count - 1) // 10
    first_n = last_digit * 10 ** (first_num_count - 1) + between_digits * 10 + first_digit
   
    return first_n

def main ():
    first_n = int(input("������� ������ �����: "))
    num_count=count_numbers(first_n)

    if num_count<3:
        print("� ������ ����� ������ ��� ����.")
    else :
     first_n=change_number (first_n,num_count)
     print('��������� ������ �����:', first_n)


    second_n = int(input("\n������� ������ �����: "))
    
    l_num_count=count_numbers(second_n)
    if l_num_count<4:
         print("�� ������ ����� ������ ������ ����.")
    else :
     second_n=change_number (second_n,l_num_count)
     print('��������� ������ �����:', second_n)
     print('\n����� �����:', first_n + second_n)

main()