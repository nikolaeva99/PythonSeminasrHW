
'''
Задайте список из нескольких чисел. Напишите программу, 
которая найдёт сумму элементов списка, стоящих на 
нечётной позиции.
Пример:
- [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
'''

# def SumNumbers (arr):
#     sum = 0
#     for i in range(len(arr)):
#         if i % 2 != 0:
#             sum = arr[i] + sum
#     return sum


# list_1 = [2, 3, 5, 9, 3]
# print(SumNumbers(list_1))


# for i in range(1, len(arr), 2):
#     sum = sum + arr[i]
'''
Напишите программу, которая найдёт произведение 
пар чисел списка. Парой считаем первый и последний 
элемент, второй и предпоследний и т.д.
Пример:
- [2, 3, 4, 5, 6] => [12, 15, 16];
- [2, 3, 5, 6] => [12, 15]
'''


# array_1 = [2, 3, 4, 5, 6]
# for i in range(int(round(len(array_1)/ 2 + 0.000001))):
#     result = array_1[i]*array_1[len(array_1)- i - 1]
#     print(result)

    




  



'''
Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между 
максимальным и минимальным значением дробной части элементов.
Пример:
- [1.1, 1.2, 3.1, 5, 10.01] => 0.19
'''

# list_1=[1.1, 1.2, 3.1, 5, 10.01]
# list_1 = [x for x in list_1 if type(x) == float]
# list_1_float = list()
# for i in list_1:
#     list_1_float.append(round(i - int(i), 5))
# print(max(list_1_float)- min(list_1_float))


#print(round(list_1[0] % 1), 3)
'''
Напишите программу, которая будет преобразовывать 
десятичное число в двоичное.
Пример:
- 45 -> 101101
- 3 -> 11
- 2 -> 10
'''
# stroka = ' '
# n = int(input('number: '))
# while n > 0:
#     stroka = str(n % 2) + stroka
#     n //= 2
# print(stroka)



# or 
# stroka = stroka + str(n % 2) 
#     n //= 2
# print(stroka[::-1])
'''
*5. Задайте число. Составьте список чисел Фибоначчи, 
в том числе для отрицательных индексов.
*Пример:*
- для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, -3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] [Негафибоначчи]
'''
'''
k = int(input())
a0 = 0
a1 = 1
a2 = 1
arr = []
for i in range(k):
    arr.append(a0)
    a2 = a1 + a0
    a0 = a1
    a1 = a2
arr.append(a0) 
arr1 = list()
for i in range(len(arr)):
    if i % 2 == 0:
        arr1.append(arr[i]* (-1))
    else:
        arr1.append(arr[i])
#arr1 = [arr[i] * (-1) for i in range(0, len(arr), 2) if i % 2 == 0]   было
print(arr1[len(arr1):1:-1]+arr)
'''
