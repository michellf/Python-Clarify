"""
Listas
Em outras linguagens é conhecida como Array, Vetor ou matriz...

* Dinâmica >>> Não possui tamanho fixo e não preciso informar este tamanho.
* Aceita qualquer tipo de dado.

* Sintaxe:
        [] ou list()

* SORT >>> Ordena os dados de uma lista.
* REVERSE >>> Inverte a lista.
* APPENDD >>> Atribui a lista, um elemento por vez. Podendo ser inclusive outra lista...
* INSERT >>> Atribui vários elementos, integrando à lista original.
* POP >>> Remove um valor da lista por índice.
* REMOVE >>> Remove um valor da lista por valor.
* ENUMERATE >>> Acesso à chave e valor.
* SHALLOW COPY
* CLEAR >>> Limpa a lista.
"""

# tupla = ()
# tupla2 = tuple()

# # lista sempre tem []
# # listas
# lista1=[]
# lista2 = list()
# n10 = [range(0,101,10)]               # deu errado
# n102 = list(range(0,101,10))          # deu certo - preencher uma ilsta com 10 valores de 0 até 100 
# n103 = [10,20,80,90,222,'leo',True,19.6]
# print(n10)
# print(n102)
# print(n103)

# cadastro = []  #lista declarada
# cadastro.append('Leo')

notas = [] #lista declarada
for n in range(4): notas.append(float(input('Nota: ')))

print(notas)

notas.sort()
print(notas)

notas.reverse()
print(notas)

# ***************************************
# DUAS FORMAS DE INSERIR DADOS NA LISTA::::::::::::::::::::::::::::::::::::::::::
# APPEND - INSERE NA ÚLTIMA POSICAO
# INSERT - INSERE NA POSICAO (INDICE) QUE VOCE QUISER

notas.append(4) # coloca o 4 no final da lista - INSERE NO FINAL DA LISTA
print(notas)

notas.insert(1,15) # na posicao 1 ele insere o valor 15 na lista - INSERE NA POSICAO QUE SE QUER (POSIC,VALOR)
print(notas)


# DUAS FORMAS DE REMOVER DADOS NA LISTA::::::::::::::::::::::::::::::::::::::::::
# POP PROCURA PELO ÍNDICE (POSICAO) ou DEL 
# REMOVE PROCURA O VALOR (ITEM)

notas.pop() # remove sempre o ult valor da lista 
print(notas)

notas.pop(2) # remove a posicao 2 (índice 2) da lista
print(notas)

notas.remove(8) # remove o valor (item) 8 da lista
print(notas)

del notas[3] # excluir indice(posicao) 3

# ***************************************

# VERIFICA SE TEM O VALOR 188 NA MINHA LISTA ***************************************
print(188 in notas) # true ou false existe ou nao


print ('**********')
# ENUMERATE INDICE(POSICAO) + VALOR
# SEM ENUMERATE ACESSO APENAS O VALOR SEM O INDICE
notas = [8,5,20,10]
for indice, item in enumerate(notas): 
        print(f'Na posicao {indice} temos a note: {item}')
print ('**********')
notasTeste = [8,5,20,10]
del notasTeste[3] # excluir posicao 3
print (notasTeste)


