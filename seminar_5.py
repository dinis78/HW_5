import os
from traceback import print_list
from unicodedata import name
os.system("cls")

# № 2. Задайте натуральное число N. Напишите программу, 
# которая составит список простых множителей числа N.

import math
num=int(input('Введите число '))

def prime_factors (num):
  while num%2==0:            #для чётного числа
    print(2, end=' ')
    num=num/2

  for i in range(2,int(math.sqrt(num))+1):  #для нечетного числа 
    while num%i==0:
      print(i, end=' ')
      num=num/i
  if num>2:
    print(num, end=' ')
prime_factors(num)

#######################################################