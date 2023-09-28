"""
Vamos iniciar um programa que receba:
 nome = str(input('Digite seu nome)).title()
 idade
 peso
 altura

Retorne o IMC do usuário.

IMC =   Peso
      --------
       Altura²
"""


nome = str(input('Digite seu nome: ')).title()
idade = int(input(f'{nome}, agora sua idade: '))
peso = float(input('Peso: '))
altura = float(input('Altura: '))

imc = float(peso/altura**2)

print(f'{nome}, seu IMC retornou: {imc}')
print(f'{nome}, seu IMC retornou: {imc:.2f}')
print(f'{nome}, seu IMC retornou: {round(imc,2)}')
