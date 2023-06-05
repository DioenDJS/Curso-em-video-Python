"""
Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto
"""

preco = float(input('Digite o preço do produto : '))

precoDesconto = (5 / 100) * preco

novoPreco = preco - precoDesconto

print('{}R$ com 5% de desconto tem um desconto de {}R$ e vai ficar : {}R$'.format(preco, precoDesconto, novoPreco))