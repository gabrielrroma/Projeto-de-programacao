from interface import *
from datetime import *

def arquivoExiste(txt):
    try:
        a = open(txt, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True    

def criarArquivo(txt):
    try:
        a = open(txt, 'wt+')
        a.close()
    except:
        print('Erro ao criar arquivo')
    else: 
        print(f'Arquivo {txt} criado.')
        
def leitorArquivo(txt,artxt):
    try:
        a = open(txt, 'rt')
    except:
        print('Erro')
    else:
        arrumador(artxt)
        cont = 1
        for linha in a:
           dado = linha.split(';')
           dado[4] = dado[4].replace('\n','')
           text = (f'{cont} - Nome: {dado[0]:<20} Categoria: {dado[1]:<20} Valor: R$ {dado[2]:<20} Dia: {dado[3]:<20} Hora: {dado[4]:<20}') 
           print(text.center(160))
           cont += 1
        valorTotal(txt)
    finally:
        a.close()
        
def arquivoCategoria(txt,artxt):
    try:
        a = open(txt, 'rt')
    except:
        print('erro.')
    else:
        arrumador(artxt)
        while True:
            categorias = input("Categoria da transação((C)Casa, (T)Transporte, (S)Saúde, (L)Lazer, (A)Alimentação): ").upper()
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
        cont = 1    
        total = 0
        for linha in a:
            dado = linha.split(';')
            if dado[1] == categoria:
                dado[4] = dado[4].replace('\n','')
                text = (f'{cont} - Nome: {dado[0]:<20} Categoria: {dado[1]:<20} Valor: R$ {dado[2]:<20} Dia: {dado[3]:<20} Hora: {dado[4]:<20}')
                total += valorTotalCat(txt, float(dado[2]))
                print(text.center(160))
                cont += 1 
        tot = (f'Valor total: R${total}')
        print('\n', tot.center(160))       
    finally:
        a.close()             
        
def adicionarTransacao(txt,nome='',categoria='',valor=0):
    try:
        now = datetime.now()
        dia = now.strftime('%d/%m/%Y')
        hora = now.strftime('%H:%M:%S')
        
        a = open(txt, 'at')
    except:
        print('Erro.')
    else:
        try:
            a.write(f'{nome};{categoria};{valor};{dia};{hora}\n')
        except:
            print('Erro.')
        else:
            print('Novo valor adicionado')
            a.close()       
            
def removerArquivo(txt, linha):
    try:
        with open(txt, 'r') as arquivo:
            a = arquivo.readlines()
        with open(txt, 'w') as arquivo:
            for i, l in enumerate(a):
                if i != linha - 1:
                    arquivo.write(l)
    except IOError:
        print('Erro ao remover transação.')
    else:
        print('Transação removida com sucesso.')
        
def valorTotal(txt):
    try:
        a = open(txt, 'rt')
    except:
        print('Erro.')
    else:
        valorTot = 0
        for linha in a:
           dado = linha.split(';')
           valorTot += float(dado[2])
        text = (f'Valor Total R$ {valorTot}')
        print('\n',text.center(160))                   
    
def valorTotalCat(txt,dado):
    try:
        a = open(txt,'rt')
    except:
        print("Erro.") 
    else:
        return dado
               
           
                           