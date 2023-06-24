"""
Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:

- Se ele ainda vai ser alistar ao serviço militar
- Se é a hora de se alistar
- Se já passou do tempo do alistamento
"""

idade = int(input("Digite sua idade : "))

if idade < 18:
    print("Você ainda vai ser alistar ao serviço militar")
elif idade == 18:
    print("É a hora de você se alistar")
else:
    print("Já passou do tempo do seu alistamento")
