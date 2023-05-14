from interface import *
from manipulador import *
from time import sleep

#Definindo em uma variável qual será o arquivo para guardar transações
txt = 'saldo.txt'

if not arquivoExiste(txt):
    criarArquivo(txt)

#Menu para fazer operações
while True:
    #Função menu() para adicionar opções de escolha
    opcao = menu(['Sair','Adicionar transação','Listar transações','Listar transações por categoria'])
    
#Condição para opção desejada
    #Codição 0: Para fechar o programa
    if opcao == 0:
        print(arrumador('Fechando sistema!'))
        break
    #Condição 1: Para adicionar transações
    elif opcao == 1:
        nome = input("Digite o nome da transação: ")
        categorias = input("Categoria da transação((C)Casa, (T)Transporte, (S)Saúde, (L)Lazer, (A)Alimentação): ").upper()
        while True:
            if categorias == 'C':
                categoria = 'Casa'
                break
            elif categorias == 'T':
                categoria = 'Transporte'
                break
            elif categorias == 'S':
                categoria = 'Saúde'
                break
            elif categorias == 'L':
                categoria = 'Lazer'
                break
            elif categorias == 'A':
                categoria = 'Alimentação'
                break
            else: 
                print('Categoria não encontrada.')
                continue
        valor = input("Digite o valor da transação: ")    
        criarArquivo(txt,nome,categoria,valor)
        
    #Condição 2: Para listar todas as transações    
    elif opcao == 2:
        leitorArquivo(txt,'Lista de Transações')
        
    #Condição 3: Para listar transações por categoria    
    elif opcao == 3:
        arquivoCategoria(txt,'Lista de Transações por categoria')  
    #Caso opção desejada inexistente, roda de novo       
    else:
        print('Tente uma opção válida.')
    sleep(1)    