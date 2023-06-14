"""
Faça um programa que leia uma frase pelo teclado e mostre:

> Quantas vezes aparece a letra "A"

> Em que posição ela aparece a primeira vez

> Em que posição ela aparece a ùltima vez
"""

frase = input('Digite uma frase : ')

quantasVezA = frase.upper().count('A')

tamanho = len(frase)

primeiroA = frase.upper().find("A", 0, tamanho)
ultimoA = frase.upper().rfind("A")

print('Existem {} A e o primeiro A da frase esta na posição {} e o ultimo na posição {} '.format(quantasVezA, primeiroA, ultimoA))