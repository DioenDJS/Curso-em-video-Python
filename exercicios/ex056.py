"""
Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No fianl
do programa mostre :

> A média de idade do Grupo

> Qual é o nome do homem mais velho

> Quantas mulheres têm menos de 20 anos

"""

pessoa = dict()
listaPessoas = []
comparaIdade = 0
nomeHomemMaisVelho = ''
somaDaMediaDeIdadeGrupo = 0
quantidadedeMulheresComMaisDeVinteAnos = 0

for p in range(4):
    print('-' * 5 + f'{p+1}ª PESSOA' + '-' * 5)
    nome = str(input("Digite o nome da pessoa : ")).strip()
    idade = int(input("Digite a idade da pessoa : "))
    sexo = str(input("Digite o sexo da pessoa : "))

    pessoa = {"nome": nome, "idade": idade, "sexo": sexo}
    listaPessoas.append(pessoa.copy())

for i in range(len(listaPessoas)):
    somaDaMediaDeIdadeGrupo += listaPessoas[i]['idade']
    if "M" == listaPessoas[i]["sexo"]:
        if listaPessoas[i]['idade'] > listaPessoas[i-1]['idade']:
            comparaIdade = listaPessoas[i]['idade']
            nomeHomemMaisVelho = listaPessoas[i]['nome']
            print(nomeHomemMaisVelho)

    if "F" == listaPessoas[i]["sexo"] and 20 > listaPessoas[i]["idade"]:
        quantidadedeMulheresComMaisDeVinteAnos += 1

media = float(somaDaMediaDeIdadeGrupo / len(listaPessoas))
print(f'media {media}')
print(f'A idade do homem mais velho na lista é {comparaIdade} !')
print(f'O homem mais velho tem {comparaIdade} e se chama {nomeHomemMaisVelho}')
print(f'Quantas mulheres tem mais de 20 anos {quantidadedeMulheresComMaisDeVinteAnos} !')
print(listaPessoas)