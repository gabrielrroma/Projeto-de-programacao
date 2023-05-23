from interface import *
from datetime import *

# Variaveis para nome de arquivo
saldocsv = 'saldo.csv'
transacoescsv = 'transacoes.csv'

# Função para leitura de categoria por sua primeira letra
def categoria():
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
    return categoria        

# Função para mostrar saldo
def saldo(saldo):
    osaldo = open(saldo,'rt')
    valor = osaldo.read()
    return float(valor)

# Função para checar existencia de um arquivo
def arquivoExiste(txt):
    try:
        a = open(txt, 'rt', encoding='utf-8')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True    

# Cria arquivo caso não exista
def criarArquivo(txt):
    try:
        a = open(txt, 'wt+', encoding='utf-8')
        a.close()
    except:
        print('Erro ao criar arquivo')
    else: 
        print(f'Arquivo {txt} criado.')

# Leitor de arquivo para organização de dados do arquivo        
def leitorArquivo(txt,artxt):
    try:
        a = open(txt, 'rt', encoding='utf-8')
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
        
# Mesmo que leitorArquivo() porém com filtro de categoria        
def arquivoCategoria(txt,artxt):
    try:
        a = open(txt, 'rt', encoding='utf-8')
    except:
        print('erro.')
    else:
        arrumador(artxt)
        cat = categoria()
        cont = 1    
        total = 0
        for linha in a:
            dado = linha.split(';')
            if dado[1] == cat:
                dado[4] = dado[4].replace('\n','')
                text = (f'{cont} - Nome: {dado[0]:<20} Categoria: {dado[1]:<20} Valor: R$ {dado[2]:<20} Dia: {dado[3]:<20} Hora: {dado[4]:<20}')
                total += valorTotalCat(txt, float(dado[2]))
                print(text.center(160))
                cont += 1 
        tot = (f'Valor total: R${total:.2f}')
        print('\n', tot.center(160))       
    finally:
        a.close()             
        
# Cria transação para adicionar ao arquivo dividindo por (nome,categoria,valor,data,hora)        
def adicionarTransacao(txt,nome='',categoria='',valor=0):
    nsaldo = saldo(saldocsv)
    if nsaldo < float(valor):
        print('Você não tem dinheiro pra essa transação.')
    else:        
        try:
            now = datetime.now()
            dia = now.strftime('%d/%m/%Y')
            hora = now.strftime('%H:%M:%S')
            
            a = open(txt, 'at', encoding='utf-8')
        except:
            print('Erro.')
        else:
                try:
                    a.write(f'{nome};{categoria};{valor};{dia};{hora}\n')
                except:
                    print('Erro.')
                else:    
                    nsaldo -= float(valor)
                    b = open(saldocsv, 'wt')
                    b.write(str(nsaldo))
                    print('Novo valor adicionado')
                    b.close()
                    a.close()       
          
# Remove trasação do arquivo com escolha de opção            
def removerArquivo(txt, linha):
    try:
        with open(txt, 'r', encoding='utf-8') as arquivo:
            a = arquivo.readlines()
        with open(txt, 'w') as arquivo:
            for i, l in enumerate(a):
                if i != linha - 1:
                    arquivo.write(l)
    except IOError:
        print('Erro ao remover transação.')
    else:
        print('Transação removida com sucesso.')

# Mostra saldo total       
def valorTotal(txt):
    try:
        a = open(txt, 'rt', encoding='utf-8')
    except:
        print('Erro.')
    else:
        valorTot = 0
        for linha in a:
           dado = linha.split(';')
           valorTot += float(dado[2])
        text = (f'Valor Total R$ {valorTot}')
        print('\n',text.center(160))                   

# Mostra valor total filtrado por categoria    
def valorTotalCat(txt,dado):
    try:
        a = open(txt,'rt',encoding='utf-8')
    except:
        print("Erro.") 
    else:
        return float(f'{dado:.2f}')
               
# Atualiza o valor do saldo                
def adicionarSaldo():
    try:
        a = open('saldo.csv', 'rt')
        total = float(a.read())
    except:
        print('Erro')
    else:        
        N = float(input("Digite o valor a ser adicionado: "))
        total += N
        total = (f'{total:.2f}')
        a.close()
        a = open('saldo.csv', 'wt')
        a.write(total)
    finally:
        print('Valor adicionado com sucesso!')
        a.close()

# Modifica trasação do arquivo        
def alterarTransacao(txt, linha, novo_nome, nova_categoria):
    try:
        with open(txt, 'r', encoding='utf-8') as arquivo:
            linhas = arquivo.readlines()

        if linha >= 1 and linha <= len(linhas):
            linhas[linha-1] = f'{novo_nome};{nova_categoria};{linhas[linha-1].split(";")[2]};{linhas[linha-1].split(";")[3]};{linhas[linha-1].split(";")[4]}'

            with open(txt, 'w', encoding='utf-8') as arquivo:
                arquivo.writelines(linhas)

            print('Transação alterada com sucesso.')
        else:
            print('Número de linha inválido.')
    except IOError:
        print('Erro ao alterar transação.')            