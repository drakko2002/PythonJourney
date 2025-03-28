import socket
import time

def iniciar_cliente():
    """
    Inicia um cliente de chat que se conecta ao servidor para troca de mensagens.
    
    O cliente:
    - Conecta-se ao servidor local na porta 12345
    - Permite envio de mensagens ao servidor
    - Recebe e exibe respostas do servidor
    - Mantém conexão até que o usuário envie uma mensagem vazia
    """
    
    while True:  # Loop de tentativas de conexão
        # Cria socket TCP/IP
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        try:
            # Tenta conectar ao servidor
            client.connect(('localhost', 12345))
            print("Conectado ao servidor de chat!")

            # Loop principal de comunicação
            while True:
                try:
                    # Obtém mensagem do usuário
                    msg = input("Você diz: ")
                    
                    # Se mensagem vazia, encerra
                    if not msg:
                        return  # Sai completamente do programa
                    
                    # Envia mensagem ao servidor
                    client.send(msg.encode())
                    
                    # Recebe e exibe resposta do servidor
                    resposta = client.recv(1024).decode()
                    print(f"Servidor diz: {resposta}")
                    
                except:
                    print("Erro na comunicação com o servidor")
                    break  # Sai do loop interno
        
        except ConnectionRefusedError:
            print("\nERRO: Servidor está lotado ou não está disponível!")
            print("Tentando reconectar em 5 segundos...")
            time.sleep(5)  # Espera 5 segundos antes de tentar novamente
            continue
        
        finally:
            # Fecha conexão com servidor
            client.close()
            print("Desconectado do servidor")

# Garante que o cliente só inicia se este arquivo for executado diretamente
if __name__ == "__main__":
    iniciar_cliente() 