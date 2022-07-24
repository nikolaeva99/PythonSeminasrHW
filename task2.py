'''
Задача 1. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
Пример:
6782 -> 23
0,56 -> 11
'''
#Первое решение
# stroka = input()
# sum = 0
# for i in stroka:
#     if i != '.':
#         sum = sum + int(i)
# print(sum)


#Второе решение
# stroka = input()
# sum = 0
# for i in stroka:
#     if i.isdigit():
#         sum = sum + int(i)
# print(sum)


'''
number = float(input('Input number: '))
result = int(0)
if number>1:
    while number>1:
        sum = int(number%10)
        result = result + sum
        number = number/10
else:
    while (number *10) % 10 == 0:
        sum1 = int(number%10)
        result = result + sum1
        number = number*10

print (result)
'''

'''
Задача 2. Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N. Факториал
5! = 120
'''
'''
number = int(input('Input number: '))
result = int(1)
for i in range (1, number+1):
    result = result*i
print(result)
'''
'''
Задача 3. Задана последовательность натуральных чисел, завершающаяся числом 0. 
Требуется определить значение второго по величине элемента в этой последовательности, 
то есть элемента, который будет наибольшим, если из последовательности удалить наибольший элемент.
Пример:
1
7
9
0
Вывод:
7
'''
'''
def FinfSecondMax (arr):
    count = 0
    for i in arr:
        max = arr[i]
        if arr[i] == max:
            max == arr[i]
            count += 1
        if count == 2:
            return f'Second max is: {arr[i]}'
  

a = [1, 3, 34, 6, 876, 0]
print(FinfSecondMax(a))
'''

