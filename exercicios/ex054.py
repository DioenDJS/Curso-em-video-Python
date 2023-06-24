from datetime import datetime, date

"""
Crie um programa que leia o ano de nascimento de sete pessoas .No final
mostre quantas pessoas ainda não atingiram a maioridade e quantas ja são maiores
"""

today = date.today()
dataNasci = datetime.datetime(1986, 7, 22)


print(dataNasci.year)
print(today.year - dataNasci.year)
