from lib.interface import *
from lib.manipulador import *
from time import sleep

txt = 'saldo.txt'

if not arquivoExiste(txt):
    criarArquivo(txt)


while True:
    opcao = menu(['Sair','Adicionar transação','Listar transações','Listar transações por categoria'])
    if opcao == 0:
        print(arrumador('Fechando sistema!'))
        break
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
    elif opcao == 2:
        leitorArquivo(txt,'Lista de Transações')
    elif opcao == 3:
        print('3')     
    else:
        print('Tente uma opção válida.')
    sleep(1)    