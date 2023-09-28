"""
Print:
    Função responsável por imprimir informações no console
Input:
    Função responsável por entrada de dados 
"""

# print('Olá, mundo!')
nome = input('Digite seu nome: ')
# print(nome)
# print formatado (Menos usual)
print('Bom dia,', nome, ', legal te conhecer...')
print('Bom dia,' + nome + ', legal te conhecer...')
print('Bom dia {} legal te conhecer...'.format(nome))

# Fstring (Mais usual)
print(f'Bom dia {nome}, legal te conhecer...')