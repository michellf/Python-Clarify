"""
Dicionários - Em outras linguagens, conhecido como MAPA.

Sintaxe
exemplo1 = {}
exemplo2 = dict()

Aceita qualquer tipo de dado.
As chaves não podem ser repetidas.
"""
tupla1 = ()
tupla2 = tuple()

lista1 = []
lista2 = list()

dicionario1 = {}
dicionario2 = dict()

# dicionários nao importa a posicao, minha chave é o br por exemplo abaixo.
# paises = {chave: valor}
paises1 = {'br':'Brasil'}
paises2 = dict(
        br = 'Brasil',
        py = 'Paraguai',
        ar = 'Argentina')

print(paises1)
print(paises2['ar'])

# inserir novos dados no dicionario
paises2['us'] = 'Estados Unidos'

produtos = dict(
        nome = 'notebook xyz',
        preco = '4000',
        categoria = 'eletronicos')
print('Produtos: ', produtos)

produtos['preco'] = '5000' # substituiu valor de preco  PRECO
produtos['preco2'] = '5000' # se nao existe o indice, cria ao final  PRECO2

print('Produtos: ', produtos)

# atualiza e se nao existir, insere update.
produtos.update({'preco': '6000'})
print('Produtos: ', produtos)





