from random import randint
"""
Desenvolva um programa que leia seis numeros inteiros e mostre a soma aponas daqueles que forem pares.
Se o valor digitado for impar desconsidere-o
"""
soma = 0
for num in range(1, 7):
    numero = randint(1, 100)
    if numero % 2 == 0:
        soma += numero
    print(numero)
print(f'Soma dos valore pares {soma}')