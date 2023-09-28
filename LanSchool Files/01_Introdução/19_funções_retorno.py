# Com retorno
# com mais de 1 retorno
# Desafio de aula: Cara ou Coroa

# """
# FUNÇÔES
# Uma forma de organizar o código e garantir que ele 
# possa ser reutilizado. Ideal que cada função seja 
# responsável por uma tarefa...
# """

# Função diz oi
# Função canta parabéns
# Função soma 2 valores

# def diz_oi():
#     return 'Oi'

# def parabens():
#     print('Parabéns para você')

# def soma():
#     a = 10
#     b = 20
#     return a+ b

# # print(soma()*10) 
# # print(f'Somando {a} com {b}, temos {a + b}')

from random import random, randint
# print(random()) # 0 e 1
# print()
# print(randint(1,10))

# def teste():
#     dado = 1

#     if dado >= 5:
#         return 'É maior que 5'
#     else:
#         return 'É menor que 5'

def cara_coroa():
    
    if randint(1,2) == 1:
        print(randint(1,2)) #gera num aleatorios de 1 a 2
    if random() >= 0.5 :
        return 'Cara'
    return 'Coroa'

print(cara_coroa())