"""
Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para 
o usuario tentar descobrir qual foi o número escolhido pelo computador .
O programa deverá escrever na tela se o usuário venceu ou perdeu
"""
import random
from time import sleep

numEscolhidoCPU = random.randint(0, 5)
print("-"*50)
print("Computador escolhendo um numero entre 0 e 5")
print("-"*50)
numEscolhidoUsuario = int(input('Escolha um numero entre 0 e 5 : '))
print("PROCESSANDO... ")
sleep(2)

resultado = "acertou" if numEscolhidoCPU == numEscolhidoUsuario else "errou"

print("Você {} o numero escolhido pela cpu foi {} !".format(resultado, numEscolhidoCPU))
