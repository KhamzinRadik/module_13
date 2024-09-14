# -*- coding: cp1251 -*-

def count_number_len(x):
    count = 1
    while x > 9:
        count += 1
        x //= 10
     return count
    
print(count_number_len(5))