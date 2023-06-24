"""
Crie um programa que leia um nũmero inteiro
e mostre na tela se ele é PAR ou IMPAR
"""

num = int(input("Digite um numero : "))

numParImpar = "PAR" if num % 2 == 0 else "IMPAR"

print("O numero {} é {} !".format(num, numParImpar))