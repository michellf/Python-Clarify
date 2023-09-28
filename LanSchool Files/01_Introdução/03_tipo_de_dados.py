"""
Python possui o que chamamos de tipagem fraca.

STRING por padrão, sempre estará entre
    ' ' aspas simples
    " " aspas duplas
    ''' ''' aspas simples triplas
    E aspas duplas trilas, como esta que cerca este comentário.
"""
# Fatiamento de String
# Metodos (podem ser utilizados na mesma construção.)
# Número inteiro - int | ex: 123 65 98 90
# Float >>> Números reais/ decimais separados por . e não ,
# correto
# errado
# Booleano >>> 2 constantes - Verdadeiro (True) e falso (false).

# String (Texto) → str
# nome = str(input('Digite seu nome: ')).title()

dado = '     LeONarDO   AlVes    '
print(dado.lower()) # letras minúsculas
print(dado.upper()) # letras maiúsculas
print(dado.title()) # 1º letra maiúscula em cada palavra
print(dado.capitalize()) # 1º letra maiúscula só da 1º palavra

print(len(dado)) # Conta caracteres na cadeia
print(len(dado.strip()))
print(dado.strip().count(' '))

print(dado.replace('a', '10'))


# Inteiro (int)
numero = 10
print(numero * 100)
idade = int(input('Idade: ')) 
# Float (float)
altura = 1.83
alt = float(input('Altura: '))
# Booleano Bolean Bool (bool)
status = True 
status = False
print('a' in 'Maria')


''
""
'''
ggjgj
'''
"""
hgjhgh
"""
# jghg