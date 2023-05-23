# Variaveis para nome de arquivo
saldocsv = 'saldo.csv'
transacoescsv = 'transacoes.csv'

# Função para mostrar o saldo
def saldo(saldo):
    osaldo = open(saldo,'rt')
    valor = osaldo.read()
    return float(valor)

# Função para leitura de número inteiro com tratamento de erro
def leitorInteiros(txt):
    while True:
        try:
            n = int(input(txt))
        except (ValueError, TypeError):
            print("Digite um número inteiro válido!")
            continue
        except KeyboardInterrupt:
            print('Cancelando operações!')
            return 0
        else:
            return n
        
# Funções para arrumar menu
def linha(tam = 80):
    return '=-' * tam

def arrumador(txt):
    print(linha())
    print(txt.center(160))
    print(linha())
        
def menu(lista):
    arrumador('Sistema de Rastreamento de Despesas Pessoais.')
    print('Saldo:', saldo('saldo.csv'))
    cont = 0
    for item in lista:
        print(f'{cont} - {item}')
        cont += 1
    opcMenu = leitorInteiros('Que opção deseja acessar?: ')
    return opcMenu    
        
                