import threading
import socket
import time
import sys
import os

if len(sys.argv) != 3:
    print("[!] Erreur, usage : ./stp_send.py <ip> <file>")
    sys.exit(1)
else:
    ip = sys.argv[1]
    file = sys.argv[2]

size = os.path.getsize(file)
active = True
done = 0


def time_left():
    last_done = 0
    first = True
    while active:
        time.sleep(1)
        if first:
            last_done = done
            first = False
        if active:
            print("[I] {perc}% effectués, ({speed} Mio/sec)"
                  .format(perc=round(done / size, 3) * 100, speed=round(last_done / 1000000, 3)))
            last_done = done - last_done


print("[I] Taille du fichier :", size)
f = open(file, 'rb')

print("[I] Connection à {} ...".format(ip))
socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.connect((ip, 6666))
print("[!] Connection réussie !")

t = threading.Thread(target=time_left)
t.start()

data = 1
while data:
    data = f.read(2048)
    socket.send(data)
    done += 2048

active = False
print("[I] Transfert terminé avec succès.")
t.join()

socket.close()
