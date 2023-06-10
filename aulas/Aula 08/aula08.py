"""
Trabalhando com Módulos
"""
# import math
from math import sqrt, floor

""" modulos: assim como algumas linguagens de programação que tem pacotes e bibliotecas são conjuntos de funcionalidades 
empacotadas e disponibilizadas para antender certas necessidades 

- Adicionamos este modulos atraves de um comando 'import' e em python temos duas formas para fazer isso 

 * import math : Neste caso iremos importar toda a biblioteca contendo todas as funções
 
 * from math import sqrt, floor : Neste caso estamos pegando apenas as funções 
 sqrt -> calcula a raiz quadrada 
 floor -> arredonda o valor de um numero pra baixo
"""

num = int(input("Digite um numero : "))

raiz = sqrt(num)

print("A raiz quadrada de {} é {}".format(num, floor(raiz)))
