"""
Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO.

"""
from datetime import date
ano = int(input("Digite o ano : "))

if ano == 0:
    ano = date.today().year

bissexto = "não"

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    bissexto = "é"

print("O ano {}, {} bissexto !".format(ano, bissexto))
