import os
from traceback import print_list
from unicodedata import name
os.system("cls")

# 1#. Напишите программу, удаляющую из текста
# все слова, содержащие "абв".


text_my = 'самозабвенен мой друг, журнар абвгдейка'

text_my = list(filter(lambda x: 'абв' not in x, text_my.split()))
my = " ".join(text_my)
print(my)

