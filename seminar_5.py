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


# x=int(100)
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
        
        
    
#     c= random.randint(1,28)
#     if 56<x<84:
#         c=5
#     elif x<=56:
#         c=x-29
#     elif x<=28:
#         c=x  
#     print('Ходит БОТ', c) 
#     while  c>x: 
#         c= random.randint(1,2) 
#     x=x-c    
        

#     print('Остаток конфет', x)
#     if x==0:
#         print('БОТ ВЫИГРАЛ!!!' )
#         break
    
#########################################################

# №3.Создайте программу для игры в ""Крестики-нолики"".

maps = [1,2,3,    #поле
        4,5,6,
        7,8,9]
victori =[[0,1,2], #победные комбинации
        [3,4,5],
        [6,7,8],
        [0,3,6],
        [1,4,7],
        [2,5,8],
        [0,4,8],
        [2,4,6]]
 
def print_maps():       #вывод поля 
    print(maps[0], end = " ")  
    print(maps[1], end = " ")
    print(maps[2])
 
    print(maps[3], end = " ")
    print(maps[4], end = " ")
    print(maps[5])
 
    print(maps[6], end = " ")
    print(maps[7], end = " ")
    print(maps[8])    
 

def step_maps(step,symbol):
    ind = maps.index(step)
    maps[ind] = symbol
 
def get_result():   # показываем ход игры
    win = ""
 
    for i in victori:
        if maps[i[0]] == "X" and maps[i[1]] == "X" and maps[i[2]] == "X":
            win = "X"
        if maps[i[0]] == "O" and maps[i[1]] == "O" and maps[i[2]] == "O":
            win = "O"   
             
    return win
 
game_over = False
player1 = True
 
while game_over == False:
 
    print_maps()
    if player1 == True:    #ход игроков
        symbol = "X"
        step = int(input("Игрок 1, ваш ход: "))
    else:
        symbol = "O"
        step = int(input("Игрок 2, ваш ход: "))
 
    step_maps(step,symbol) 
    win = get_result() 
    if win != "":
        game_over = True
    else:
        game_over = False
    player1 = not(player1)              
print_maps()
print("Победил", win)

    
###########################################################################
