# Importando a biblioteca socket e sys
import sys, socket, os
from datetime import datetime
 
# Definindo as constantes do programa
HOST        = ''            # Definindo o IP do servidor
PORT        = 60000         # Definindo a porta
CODE_PAGE   = 'utf-8'       # Definindo a página de código de caracteres
BUFFER_SIZE = 512           # Definindo o tamanho do buffer

# Criando o socket UDP
udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
 
# Vincular o socket a tupla (host, port)
udp_socket.bind((HOST, PORT)) 
 
print(f'\nSERVIDOR ATIVO: {udp_socket.getsockname()}')
print('\nRecebendo Mensagens...\n\n')

listArquivos = os.listdir('server_files')
dictArquivos = {}
for i in listArquivos:
    dictArquivos.update({i:os.path.getsize('server_files\\'+i)}) 

arquivosTamanho =''
for i,j in dictArquivos.items():
    arquivosTamanho = arquivosTamanho+i+' --- '+str(j)+'\n'
mensagensLog = []
try:
    while True:
        # Recebendo os dados do cliente
        mensagem, ip_cliente = udp_socket.recvfrom(BUFFER_SIZE)
        # Convertendo a mensagem recebida de bytes para string
        mensagem = mensagem.decode(CODE_PAGE)
        # Imprimindo a mensagem recebida 
        
        mensagensLog.append([datetime.today().strftime('%Y-%m-%d %H:%M'),ip_cliente[0], mensagem,]) 
        
        if mensagem.upper() == '\\H': 
            print(f'\nMandando Ajuda Para {ip_cliente} ...\n')
            mensagem_volta = '\n --Listas de Comando-- \n \\f -- Listar Arquivos \n \\d:nome_arquivo -- Efetua o Download do Arquivo \n \\u:nome_arquivo -- Efetua o Upload do Arquivo \n \\q -- Sair do Cliente \n'                
            udp_socket.sendto(mensagem_volta.encode(CODE_PAGE), ip_cliente)
        
        # Mensagem de desconexão 
        elif mensagem.upper() == '\\Q':
            print(f'\nO {ip_cliente} SE DESCONECTOU DO SERVIDOR...\n')
        
        elif mensagem.upper() == '\\M':            
            print(f'\nO {ip_cliente} Enviando Lista de Mensagens...\n')
            mensagem_volta = '\n'
            for i in mensagensLog:
                mensagem_volta = mensagem_volta+i[0]+', '+i[1]+', '+i[2]+'\n'
                        
            udp_socket.sendto(mensagem_volta.encode(CODE_PAGE), ip_cliente)
            
        # Mandando lista de Arquivos  
        elif mensagem.upper() == '\\F':
            print(f'\nMandando Lista De Arquivos Para {ip_cliente} ...\n')
            mensagem_volta = '\n\n--Listas de Arquivos--\n'+arquivosTamanho                
            udp_socket.sendto(mensagem_volta.encode(CODE_PAGE), ip_cliente)
        
        # Fazendo Download do Arquivo
        elif '\\D:' in mensagem.upper():
            print(f'\n Efetua o Download do Arquivo... {ip_cliente} ...\n')
            mensagem_volta = '\nAinda em Construção... '
            udp_socket.sendto(mensagem_volta.encode(CODE_PAGE), ip_cliente)
        
        # Fazendo Download do Upload        
        elif '\\U:' in mensagem.upper():
            print(f'\n Efetua o Upload do Arquivo... {ip_cliente} ...\n')
            mensagem_volta = '\nAinda em Construção... '
            udp_socket.sendto(mensagem_volta.encode(CODE_PAGE), ip_cliente)
        
        else:
            print(f'{ip_cliente}->  {mensagem}')
            # Devolvendo uma mensagem (echo) ao cliente
            mensagem_volta = 'DEVOLVENDO... ' + mensagem
            udp_socket.sendto(mensagem_volta.encode(CODE_PAGE), ip_cliente)
except:
    print(f'\nERRO: {sys.exc_info()[0]}')
finally:    
    # Fechando o socket
    udp_socket.close()

