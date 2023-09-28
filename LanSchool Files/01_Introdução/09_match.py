"""
Estrutura condicionais mais utilizada em menus,
funciona semelhante ao escolhaCaso do portugol
e switch case no java por exemplo...
"""
# Calculadora

''' 
Conclua o exemplo inserindo: 
    multiplicar, dividir e resto da divisão.
'''
menu = int(input('[1]SOMAR\n[2]SUBTRAIR\n[3]MULTIPLICAR\n[4]DIVIDIR\nOpção: '))
numero1 = int(input('Digite o Primeiro Número: '))
numero2 = int(input('Digite o Segundo Número: '))

match menu:
    case 1:
        print('somando...')
        result = numero1 + numero2
    case 2:
        print('substraindo')
        result = numero1 - numero2
    case 3:
        print('multiplicando')
        result = numero1 * numero2
    case 4:
        print('dividindo')
        result = numero1 / numero2
    case _: #escolheu um número não declarado
        print('opção inválida')
        
print(f'resultado: {result}')

