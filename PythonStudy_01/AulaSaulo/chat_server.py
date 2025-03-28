import socket

def iniciar_servidor():
    """
    Inicia um servidor de chat que permite comunicação bidirecional com clientes.
    
    O servidor:
    - Cria um socket TCP/IP
    - Aguarda conexões na porta 12345
    - Aceita um cliente por vez
    - Permite troca de mensagens interativas
    - Mantém a conexão até que o cliente desconecte
    """
    
    # Cria um socket TCP/IP (AF_INET = IPv4, SOCK_STREAM = TCP)
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Associa o socket ao endereço localhost e porta 12345
    server.bind(('localhost', 12345))
    
    # Define o limite de conexões pendentes
    server.listen(2)
    print("Chat servidor iniciado...")

    # Loop principal do servidor - aguarda conexões indefinidamente
    while True:
        # Aceita uma nova conexão (bloqueante)
        # conn: socket para comunicação com este cliente específico
        # addr: tupla com endereço IP e porta do cliente
        conn, addr = server.accept()
        print(f"Cliente conectado: {addr}")
        
        # Loop de comunicação com o cliente atual
        while True:
            try:
                # Aguarda mensagem do cliente (bloqueante)
                # 1024 é o tamanho máximo do buffer de recepção
                msg = conn.recv(1024).decode()
                
                # Se cliente desconectou, sai do loop de comunicação
                if not msg:
                    break
                
                print(f"Cliente diz: {msg}")
                
                # Obtém resposta do usuário (servidor)
                resposta = input("Servidor diz: ")
                
                # Envia resposta ao cliente
                conn.send(resposta.encode())
                
            except:
                # Em caso de erro na comunicação, encerra conexão
                break
                
        # Fecha a conexão com o cliente atual
        conn.close()
        print("Cliente desconectado")

# Garante que o servidor só inicia se este arquivo for executado diretamente
if __name__ == "__main__":
    iniciar_servidor() 