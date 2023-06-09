"""
Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto
"""

preco = float(input('Digite o preço do produto : '))

precoDesconto = (preco * 5) / 100

novoPreco = preco - precoDesconto

print('{}R$ com 5% de desconto tem um desconto de {:.2f}R$ e vai ficar : {:.2f}R$'.format(preco, precoDesconto, novoPreco))