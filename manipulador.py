from interface import *

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
           dado[2] = dado[2].replace('\n','')
           print(f'{cont} - Nome: {dado[0]:<33} Categoria: {dado[1]:<33} Valor: {dado[2]:<33}') 
           cont += 1
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
        for linha in a:
            dado = linha.split(';')
            if dado[1] == categoria:
                dado[2] = dado[2].replace('\n','')
                print(f'{cont} - Nome: {dado[0]:<33} Categoria: {dado[1]:<33} Valor: {dado[2]:<33}') 
                cont += 1
    finally:
        a.close()             
        
def adicionarTransacao(txt,nome='',categoria='',valor=0):
    try:
        a = open(txt, 'at')
    except:
        print('Erro.')
    else:
        try:
            a.write(f'{nome};{categoria};{valor}\n')
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