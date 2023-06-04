"""
Crie um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possiveis sobre ele.
"""

value = input('Digite algo entre um numero ou letra podendo ser ambos junto : ')

print('O tipo primmitivo do valor digitado é : ', type(value))
print('O valor digitado e um numero : {} '.format(value.isnumeric()))
print('O valor digitado e um espaço vazio : ', value.isspace())
print('O valor digitado e uma letra : ', value.isalpha())
print('O valor digitado contem letra e numero : ', value.isalnum())
print('O valor foi digitado é um digito numerico : ', value.isdigit())
print('O valor digitado esta com todas as letras maiúsculas  : ', value.isupper())
print('O valor digitado esta com todas as letras minusculas  : ', value.islower())
print('O valor digitado esta capitalizada  : ', value.istitle())
