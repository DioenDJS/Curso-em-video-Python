"""
Desenvolva uma logica que leia o peso e a altura de uma pessoa, calcule
seu IMC e mostre seu status de acordo com a tabela abaixo:

- Abaixo de 18.5: Abaixo do peso
- Entre 18.5 e 25: Peso ideal
- Entre 25 até 30: sobrepeso
- Entre 30 até 40: Obesidade
- Acima de 40: Obesidade mórbida
"""
import math

peso = float(input("Digite o peso : "))
altura = float(input("Digite o altura : "))

imc = peso / altura ** 2
if imc < 18.5:
    msg = "abaixo do peso"
elif imc >= 18.5 and imc < 25:
    msg = "com peso ideal"
elif imc >= 25 and imc < 30:
    msg = "abaixo do peso"
elif imc >= 30 and imc < 40:
    msg = "com obesidade"
elif imc >= 40:
    msg = "com obesidade mórbida"

print("Você esta {} !".format(msg))
