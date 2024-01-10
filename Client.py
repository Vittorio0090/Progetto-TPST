import socket

# Creazione del socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connessione al server
server_address = ('localhost', 12345)
client_socket.connect(server_address)

# Invio di dati al server
message = "Ciao, server!"
client_socket.sendall(message.encode())

# Chiusura del socket
client_socket.close()
