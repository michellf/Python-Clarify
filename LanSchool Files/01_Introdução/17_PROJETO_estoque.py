# """
# Cadastre 3 produtos no estoque, cada produto precisa ter:
# - nome
# - preço
# - data e hora que foi cadastrado
# - Nome do Funcionário

# Em seguida, permita que os produtos sejam visualizados.
# """
# # lista com dicionãrio dentro
# # lista ESTOQUE com todos os produtos - quero ter um dicionário (para cada produto) dentro da lista
# estoque = []

# for cont in range(3):
#     produto = dict(
#         nome = str(input('Nome do produto: ')),
#         preco = float(input('Preco: '))
#     )
#     estoque.append(produto)
# # print('\n')
# # lista.append (dicionario)

# #for produto in estoque: # cada produto é um dicionário
# #    print (produto)
# # print('\n')
# for produto in estoque: # cada produto é um dicionário
#                         # [ {} {} {} ] (listas com dicionários)
#    # for chave, valor in produto:
#     for chave, valor in produto.items():
#         print(f'{chave} | {valor}')
#     print()




from datetime import datetime

estoque = []

menu = int(input('1| cadastrar \n2| Visualizar\n3| Sair\nOopção: '))

while True: 

    match menu:
            case 1:
                    produto = dict(
                            nome_produto = str(input('Nome: ')).title(),
                            preco = float(input('Preço: R$ ')),
                            nome_funcionario = str(input('Funcionãrio: ')).title(),
                            dt_cadastro = datetime.now().strftime('%d.%m.%Y | %H:%M')
                                                        
                    )
                    estoque.append(produto)

            case 2: # Visualizando o estoque [ {} {} {} ] dicionário dentro de lista
                print(estoque)
                for prod in estoque:
                    print(f'\nProduto: {i+1}')
                    for chave, valor in p.items():
                        print(f'{chave} → {valor}') 
                    print()
            case 3:
                break
            case _:
                print('Opção Inválida')

