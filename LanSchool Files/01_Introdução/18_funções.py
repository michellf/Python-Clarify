# """
# FUNÇÔES
# Uma forma de organizar o código e garantir que ele 
# possa ser reutilizado. Ideal que cada função seja 
# responsável por uma tarefa...
# """

# Função diz oi
# Função canta parabéns
# Função soma 2 valores

def diz_oi():
    print('oi ')

def parabens():
    print('Parabéns para você')

def soma():
    diz_oi()
    parabens()
    a = 10
    b = 20
    print(f'Somando {a} com {b}, temos {a + b}')
    
soma()



