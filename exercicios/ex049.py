"""
Refaça o DESAFIO 009 mostrando a tabuada de um numero que o usuario escolher só que agora
utilizando um laço for
"""
num = int(input('Digite um numero : '))

for i in range(11):
  if i < 10:
    print('{} x {:2} = {}'.format(num, i, (i * num)))
  else:
    print('{} x {} = {}'.format(num, i, (i * num)))

