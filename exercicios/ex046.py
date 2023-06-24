"""
faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos
de artificio.indo de 10 até 0, com uma pausa de segundo entre eles.
"""
from time import sleep

for count in range(10, 0, -1):
    print(count)
    sleep(1)
print("BUM! BUM! BUM! ")
