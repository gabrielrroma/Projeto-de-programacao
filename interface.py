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
        
def linha(tam = 80):
    return '=-' * tam

def arrumador(txt):
    print(linha())
    print(txt.center(160))
    print(linha())
    
def menu(lista):
    arrumador('Sistema de Rastreamento de Despesas Pessoais.')
    cont = 0
    for item in lista:
        print(f'{cont} - {item}')
        cont += 1
    opcMenu = leitorInteiros('Que opção deseja acessar?: ')
    return opcMenu    
        
                