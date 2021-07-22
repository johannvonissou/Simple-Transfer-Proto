import socket

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.bind(('', 6666))

socket.listen(1)
print("[I] En attente d'un client ...")
client, address = socket.accept()
print("[I] Connection faite avec", address)

f = open("delivery.dat", 'wb')

data = 1
while data:
    data = client.recv(2048)
    f.write(data)

print("[I] Echange terminé avec succès.")

client.close()
socket.close()
