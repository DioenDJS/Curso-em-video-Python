"""
Faça um programa que leia um numero inteiro e diga se ele é ou nao um numero primo
"""

num = int(input('Digite o numero : '))
countPrimo = 0

for n in range(1, num + 1):
    print(n)
    if num % n == 0:
        countPrimo += 1
msg = "não é primo" if countPrimo > 2 else "é primo"
print(f'{num} {msg} !')
