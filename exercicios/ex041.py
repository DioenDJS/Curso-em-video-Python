"""
A Confederação Nacional de natação precisa de um programa que leia o ano
de nascimento de um atleta e mostre sua categoria, de acordo com a idade:

- Até 9 anos : Mirim
- Até 14 anos : Infantil
- Até 19 anos : Junior
- Até 20 anos : Sênior
- Acima : Master
"""

idade = int(input("Digite a idade do atleta : "))
categoria = ""

if idade <= 9:
    categoria = "Mirim"
elif idade > 9 and idade <= 14:
    categoria = "Infantil"
elif idade > 14 and idade <= 19:
    categoria = "Junior"
elif idade > 19 and idade <= 20:
    categoria = "Sênior"
else:
    categoria = "Master"

print("O atleta esta na faixa de idade da catedotia {}, {} anos !".format(categoria, idade))
