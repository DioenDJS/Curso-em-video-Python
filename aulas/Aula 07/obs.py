"""
Obs: curiosidades em formtação de strings
"""
nome = input('Qual é o seu nome : ')
print('Prazer em te conhecer {}!'.format(nome))

#Formatando o valor pra entrar dentro de 20 caracteres
print('Prazer em te conhecer {:20}!'.format(nome))

#Formatando o valor centralizando dentro de 20 caracteres
print('Prazer em te conhecer {:^20}!'.format(nome))

#Formatando o valor a direita dentro de 20 caracteres
print('Prazer em te conhecer {:>20}!'.format(nome))

#Formatando o valor centralizando dentro de 20 caracteres de asteristicos
print('Prazer em te conhecer {:*^20}!'.format(nome))