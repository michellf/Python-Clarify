# """
# Primeiro passo para leitura, é abrir o arquivo, para isto usamos
# a função OPEN(nomeArquivo).
# O parâmetro é o nome ou caminho do arquivo.

# O arquivo deve existir, caso contrário retornará erro FileNotFound.

# Open apenas abre o arquivo, para ler seu conteúdo é necessário usarmos
# a função nomeArquivo.read()
# Por padrão o Open abre com o parâmetro r(read)
# """

# criando um arquivo txt
# a -> adc w -> sub r -> leitura (pode ser suprimido)
# tratamento de erro

# Exercício de aula: criar um todo (lista de tarefas)

# sempre digitar open e close antes para nao esquecer de fechar
# open()
# close()

#  The argument mode points to a string beginning with one of the following
#  sequences (Additional characters may follow these sequences.):

#  ``r''   Open text file for reading.  The stream is positioned at the
#          beginning of the file.

#  ``r+''  Open for reading and writing.  The stream is positioned at the
#          beginning of the file.

#  ``w''   Truncate file to zero length or create text file for writing.
#          The stream is positioned at the beginning of the file.

#  ``w+''  Open for reading and writing.  The file is created if it does not
#          exist, otherwise it is truncated.  The stream is positioned at
#          the beginning of the file.

#  ``a''   Open for writing.  The file is created if it does not exist.  The
#          stream is positioned at the end of the file.  Subsequent writes
#          to the file will always end up at the then current end of file,
#          irrespective of any intervening fseek(3) or similar.

#  ``a+''  Open for reading and writing.  The file is created if it does not
#          exist.  The stream is positioned at the end of the file.  Subse-
#          quent writes to the file will always end up at the then current
#          end of file, irrespective of any intervening fseek(3) or similar.

# try: 
#     # se nao encontrar o arquivo, cria
#     # escreve linha no arquivo
#     with open('./base/teste.txt','a', encoding='utf8') as arquivo:
#         arquivo.write('\nEstou só testando...')
#         print(arquivo)

#     # escrita no arquivo
#     with open('./base/teste.txt','w', encoding='utf8') as arquivo:
#         arquivo.write('\nEstou só testandoxxxxx...')

#     # leitura de arquivo
#     with open('comando Git.txt','r', encoding='utf8') as arquivo:
#         texto = arquivo.read()

#     print(texto)

#     # copia arquivo para maiusculo
#     with open('comando Git maiusculo.txt','a', encoding='utf8') as arquivo:
#         arquivo.write(texto.upper())
# except FileNotFoundError:
#     print('Arquivo nao encontrato')
# except FileExistsError:
#     print('Arquivo nao encontrato por que nao existe')
# finally: #vai ser executado independente do que ocorra - dando erro ou nao dando.
#     print('volte sempre')
# #exemplo tratamento de erros

# import pandas as pd
# # leitura de excel

# dados = pd.read_excel('nomearquivo.xlsx')
# # to_excel - dataframe converte para tabela

# Exercício de aula: criar um arquivo (lista de tarefas)
# funcao
# tratamento de erro

def todo():
    while True:
        try: 
            menu = int(input('[1]INSERE \n[2]VISUALIZA\n[3]SAIR\nOpção: '))
            match menu:
                case 1:
                    try:
                        with open('./base/task.txt','a', encoding='utf8') as arquivo:
                            tarefa = str(input('Tarefa: '))
                            arquivo.write('\n Tarefa: ')
                            arquivo.write(f'{tarefa}\n')
                    except FileNotFoundError:
                        print('Não encontrado')
                case 2:
                    try:
                        with open('./base/task.txt','r', encoding='utf8') as arquivo:
                            print(arquivo.read())
                    except FileNotFoundError:
                        print('Não encontrado')
                case 3:
                    print()
                    break
                case _:
                    print('Opção inválida')
                    break
        
        except ValueError:
            print('Dígito inválido.')
  
todo()
            


