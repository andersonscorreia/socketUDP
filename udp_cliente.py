# Importando a biblioteca socket
import socket

# Definindo as constantes do programa
HOST        = 'localhost'   # Definindo o IP do servidor
PORT        = 60000         # Definindo a porta
CODE_PAGE   = 'utf-8'       # Definindo a página de código de caracteres
BUFFER_SIZE = 512           # Definindo o tamanho do buffer

# Criando o socket UDP
udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    # Solicitando uma mensagem ao usuário
    mensagem_ida = input('Digite a mensagem (\h -- Ajuda): ')
    # Convertendo a mensagem digitada de string para bytes
    mensagem_ida = mensagem_ida.encode(CODE_PAGE)
    # Enviando a mensagem ao servidor      
    udp_socket.sendto(mensagem_ida, (HOST, PORT))
    
    if mensagem_ida.decode(CODE_PAGE).upper() == '\Q': break
    

    # Recebendo echo do servidor
    data_retorno, ip_retorno = udp_socket.recvfrom(BUFFER_SIZE)
    mensagem_volta = data_retorno.decode(CODE_PAGE)
    print (f'Echo recebido {ip_retorno}: {mensagem_volta} ')

# Fechando o socket
udp_socket.close()
