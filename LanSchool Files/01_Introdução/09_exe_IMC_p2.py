import time
from datetime import datetime
from pytz import timezone

"""
Agora vamos finalizar o IMC gerando uma saída
personalizada para o usuário de acordo com a
tabela:
______________________________________________
| Menor que 18.5      | Abaixo do peso       |
| Entre 18.5 - 24.9   | Peso Normal          |
| Entre 25.0 - 29.9   | Excesso de peso      |
| Entre 30.0 - 34.9   | Obesidade classe I   |
| Entre 35.0 - 39.9   | Obesidade classe II  |
| Maior ou igual 40.0 | Obesidade classe III |
----------------------------------------------

Mostre também a data deste resultado.
"""

# utilizando a Lib PYTZ
dthr = datetime.now()
hora = dthr.strftime('%H:%M')

nome = str(input('Digite seu nome: ')).title()
idade = int(input(f'{nome}, agora sua idade: '))
peso = float(input('Peso: '))
altura = float(input('Altura com . separando decimais: '))

imc = float(peso/altura**2)

print(f'{nome}, seu IMC retornou: {imc}')
print(f'{nome}, seu IMC retornou: {imc:.2f}')
print(f'{nome}, seu IMC retornou: {round(imc,2)}')

print(f'Hora: {hora}')

if imc < 18.5:
    print('Abaixo do peso.{imc}')
elif imc >= 18.59 and imc < 25:
    print('Peso Normal')
elif imc >= 25 and imc < 30:
    print('Excesso de Peso')
elif imc >= 30 and imc < 35:
    print('Obesidade Classe 1')
elif imc >= 35 and imc < 40:
    print('Obesidade Classe 2')
elif imc >= 40:
    print('Obesidade Classe 3')
else:
    print('Inválido')



