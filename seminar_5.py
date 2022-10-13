
import os
from traceback import print_list
from unicodedata import name
os.system("cls")

# 1#. Напишите программу, удаляющую из текста
# все слова, содержащие "абв".


# text_my = 'самозабвенен мой друг, журнар абвгдейка'

# text_my = list(filter(lambda x: 'абв' not in x, text_my.split()))
# my = " ".join(text_my)
# print(my)    

####################################################

# №2.  Создайте программу для игры с конфетами человек против человека.
#Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. 
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. 
# Все конфеты оппонента достаются сделавшему последний ход. 
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
#a) Добавьте игру против бота
#b) Подумайте как наделить бота ""интеллектом""

# import random


# x=int(1021)
# print('Остаток конфет', x)

# while x>0:
     

#     a=int(input('Игрок №1 введите число от 1 до 28 '))
#     while a>28 or a<=0 or a>x:
#         a=int(input('Игрок №1 введите число от 1 до 28 '))
#     x=x-a
#     print('Остаток конфет', x)  
#     if x==0:
#         print('Игрок №1 ВЫИГРАЛ!!!') 
#         break 

#     # b=int(input('Игрок №2 введите число от 1 до 28 '))
#     # while b>28 or b<=0 or b>x:
#     #     b=int(input('Игрок №2 введите число от 1 до 28 '))
#     # x=x-b    
#     # print('Остаток конфет', x)
#     # if x==0:
#     #     print('Игрок №2 ВЫИГРАЛ!!!' )
#     #     break
        
    ## игра бота против игрока №1    
    
#     c= 29-a
#     elif x<=56:
#         c=x-29
#     elif x<=28:
#         c=x  
#     print('Ходит БОТ', c) 
#     x=x-c    
        

#     print('Остаток конфет', x)
#     if x==0:
#         print('БОТ ВЫИГРАЛ!!!' )
#         break
    
#########################################################

# №3.Создайте программу для игры в ""Крестики-нолики"".

# maps = [1,2,3,    #поле
#         4,5,6,
#         7,8,9]
# victori =[[0,1,2], #победные комбинации
#         [3,4,5],
#         [6,7,8],
#         [0,3,6],
#         [1,4,7],
#         [2,5,8],
#         [0,4,8],
#         [2,4,6]]
 
# def print_maps():       #вывод поля 
#     print(maps[0], end = " ")  
#     print(maps[1], end = " ")
#     print(maps[2])
 
#     print(maps[3], end = " ")
#     print(maps[4], end = " ")
#     print(maps[5])
 
#     print(maps[6], end = " ")
#     print(maps[7], end = " ")
#     print(maps[8])    
 

# def step_maps(step,symbol):
#     ind = maps.index(step)
#     maps[ind] = symbol
 
# def get_result():   # показываем ход игры
#     win = ""
 
#     for i in victori:
#         if maps[i[0]] == "X" and maps[i[1]] == "X" and maps[i[2]] == "X":
#             win = "X"
#         if maps[i[0]] == "O" and maps[i[1]] == "O" and maps[i[2]] == "O":
#             win = "O"   
             
#     return win
 
# game_over = False
# player1 = True
 
# while game_over == False:
 
#     print_maps()
#     if player1 == True:    #ход игроков
#         symbol = "X"
#         step = int(input("Игрок 1, ваш ход: "))
#     else:
#         symbol = "O"
#         step = int(input("Игрок 2, ваш ход: "))
 
#     step_maps(step,symbol) 
#     win = get_result() 
#     if win != "":
#         game_over = True
#     else:
#         game_over = False
#     player1 = not(player1)              
# print_maps()
# print("Победил", win)

    
###########################################################################


# #4. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

# with open('encod.txt','w') as enc:
#     enc.write ('WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW')

def rle_encode (data):            # кодируем текст
    encoding = ''
    prev_char = ''
    count = 1
    if not data:
        return ''
    for char in data:
        if char != prev_char:
            if prev_char:
                encoding += str(count) + prev_char
            count=1
            prev_char=char
        else:
            count+=1
    else:
        encoding+=str(count) + prev_char
        return encoding        

with open ('encod.txt', 'r') as enc:  # открываем из файла текст
    file=enc.readline()
    print(file)
    encoded_val = rle_encode(file)   
print(encoded_val)

with open('encoded.txt','w') as ened:  # отправляем в файл закодированный текст
    ened.write(encoded_val)
    

def rle_decode(data):   # раскодируем текст
    decode = ''
    count = ''
    for char in data:
        if char.isdigit():
            count += char
        else:
            decode += char * int(count)
            count = ''
    return decode

with open ('encoded.txt', 'r') as ened:  # открываем из файла закодированный текст
    file_1=ened.readline()
    print(file_1)
    decoded_val = rle_decode(file_1)   
print(decoded_val)


     

