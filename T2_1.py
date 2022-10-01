# 1. Напишите программу, которая принимает на вход вещественное число и
# показывает сумму его цифр.
# in -> out
# - 6782 -> 23
# - 0.67 -> 13
# - 198.45 -> 27

N = input('Введите вещественное число: ')
print(type(N))
sum = 0
for i in N:
     if i != '.':
         sum += int(i)
print(sum)

# без работы с методами строк

N=float(input())
sum=0
ind=len(str(N))-2
N*=10**ind
while N:
    sum+=N%10
    N//=10
print(int(sum))



