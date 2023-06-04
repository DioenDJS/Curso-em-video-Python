"""
Tipos Primitivos e saida de dados
"""

# Valor de n1 neste caso vai ser uma string
n1 = input('Digite um valor')
print(type(n1))
print(type(int(n1))) # convertendo para um valor int

# Neste caso a conversão esta sendo feito no valor de entrada no input
n2 = int(input('Digite um valor : '))
print(type(n2))

# convertendo o valor n1 pra inteiro e somando os valores
soma = n2 + int(n1)

#print('A soma entre ', n2,' e ', n1, ' vale : ', soma)
print('A soma entre {} e {} vale : {}'.format(n1, n2, soma))

n3 = float(input('Digite um numero : '))
print(n3)
