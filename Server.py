import socket

# Creazione del socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Associazione all'indirizzo e alla porta desiderati
server_address = ('localhost', 12345)
server_socket.bind(server_address)

# In attesa di connessioni
server_socket.listen(1)
print("In attesa di connessioni...")

# Accettazione della connessione
connection, client_address = server_socket.accept()
print("Connessione da", client_address)

# Ricezione e stampa dei dati
data = connection.recv(1024)
print("Dati ricevuti:", data.decode())

# Chiusura della connessione
connection.close()
