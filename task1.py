#Задача 1.
'''Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
Пример:
- 6 -> да
- 7 -> да
- 1 -> нет'''
'''
dayNumber = int(input ('Input day number: '))
if dayNumber > 7 or dayNumber < 0:
    print ('Input correct number!')
else:
    if dayNumber == 6 or dayNumber == 7: 
        print ('It`s weekend! ')
    else:
        print('It is not weekend :( ')
'''
#Задача 2
#Напишите программу для проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

#Задача 3
'''Напишите программу, которая принимает на вход координаты точки (X и Y),
причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится 
эта точка (или на какой оси она находится).
Пример:
- x=34; y=-30 -> 4
- x=2; y=4-> 1
- x=-34; y=-30 -> 3'''
'''
x = int(input('Input X coordinate: '))
y = int(input('Input Y coordinate: '))

if x == 0 or y == 0:
    print ('Input non-zero!')
else:
    if x > 0 and y > 0:
        print('It`s I coordinate quarter')
    if x > 0 and y < 0:
        print('It`s II coordinate quarter')
    if x < 0 and y < 0:
        print('It`s III coordinate quarter')
    if x < 0 and y > 0:
        print('It`s IV coordinate quarter')
'''
#Задача 4
#Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).
'''
quarter = int(input('Input number of coordinate quarter: '))

if quarter < 0 or quarter > 4:
    print ('Input correct number! ')
else:
    if quarter == 1:
        print ('x > 0, y > 0')
    if quarter == 2:
        print ('x > 0, y < 0')
    if quarter == 3:
        print ('x < 0, y < 0')
    if quarter == 4:
        print ('x < 0, y > 0')
'''
#Задача 5
'''Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
Пример:
- A (3,6); B (2,1) -> 5,09
- A (7,-5); B (1,-1) -> 7,21'''

xA = int(input('Input Ax coordinate: '))
yA = int(input('Input Ay coordinate: '))
xB = int(input('Input Bx coordinate: '))
yB = int(input('Input By coordinate: '))

from math import sqrt
result = round(sqrt((xB-xA)*(xB-xA)+(yB-yA)*(yB-yA)), 3)
print(result)