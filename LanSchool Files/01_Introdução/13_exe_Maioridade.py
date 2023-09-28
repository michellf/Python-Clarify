"""
 Faça um programa que leia ano de nascimento de 5 pessoas e no final
 mostre quantas pessoas já atingiram a maioridade e para aquelas que
 ainda atingiram, mostre a média em anos que faltam para chegarem a maior idade.
"""

from datetime import date

qtde = 5 #quantidade de datas nasc digitadas
ano  = somaAno = somaMenor = 0
status = ''
# anoAtu = 2023
anoAtu = date.today().year

for cont in range(qtde):
    ano = (int(input('Digite o ano de nascimento: ')))
    if (anoAtu - ano) >= 18:
        print("Maior de Idade - Nascido no ano: ", ano)
    elif (anoAtu - ano) < 18:
        print("Menor de Idade - Nascido no ano: ", ano)
        status = 'Menor'
        somaMenor = somaMenor+1 #qtde de menores de idade
        somaAno += (anoAtu - ano) #soma das idades
    else:
        'Inválido'

if status != '':
    print("Média Ano para maioridade é: ",int(somaAno)/int(somaMenor))
