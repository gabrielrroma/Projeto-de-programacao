#Importando funções do código de outros arquivos na mesma pasta
from interface import *
from manipulador import *
import os
os.system('cls')

#Importando a função Sleep
from time import sleep

#Definindo em uma variável qual será o arquivo para guardar transações
txt = 'transacoes.csv'

if not arquivoExiste(txt):
    criarArquivo(txt)

#Menu para fazer operações
while True:
    
    #Função menu() para adicionar opções de escolha
    opcao = menu(['Sair','Adicionar transação','Listar transações','Listar transações por categoria','Remover transações','Modificar transação','Adicionar ao saldo'])
    
#Condição para opção desejada

    #Codição 0: Para fechar o programa
    if opcao == 0:
        arrumador('Até logo!')
        break
    
    #Condição 1: Para adicionar transações
    elif opcao == 1:
        arrumador('Adicionar transação')
        nome = input("Digite o nome da transação: ")
        cat = categoria()
        valor = input("Digite o valor da transação: ")    
        adicionarTransacao(txt,nome,cat,valor)
        
    #Condição 2: Para listar todas as transações    
    elif opcao == 2:
        leitorArquivo(txt,'Lista de Transações')
        
    #Condição 3: Para listar transações por categoria    
    elif opcao == 3:
        arquivoCategoria(txt,'Lista de Transações por categoria')
        
    #Condição 4: Removedor de transações    
    elif opcao == 4:
        leitorArquivo(txt, 'Remover arquivo')
        n = int(input('Digite a transação que deseja remover: '))
        removerArquivo(txt, n)
        
    #Condição 5: Modificador de transações            
    elif opcao == 5:
        leitorArquivo(txt,'Modificador de transação')
        n = int(input('Que transação da lista deseja modificar?'))
        nomeNovo = input('Digite o novo nome: ')
        cat = categoria()
        alterarTransacao(txt,n,nomeNovo,cat)
        
    #Condição 6: Adicionar débito a conta    
    elif opcao == 6:
        arrumador('Adicionar saldo')
        adicionarSaldo()    
            
    #Caso opção desejada inexistente, roda de novo       
    else:
        print('Tente uma opção válida.')
        
    sleep(1)
