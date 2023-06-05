"""
Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e seu antecessor.
"""

n = int(input('Digite o numero : '))
numSucessor = n + 1
numAntecessor = n - 1
print('O numero antecessor do numero {} é : {} \nE o numero sucessor é : {} '.format(n, numAntecessor, numSucessor))