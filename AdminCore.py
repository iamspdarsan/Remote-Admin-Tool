import socket
from tarfile import NUL

class Admin:


    def __init__(self):
        self.incomingSocket=False
        self.clientAddress=False
        self.recdata=False

    def start_server(self,address,port,nofclis):
        '''@arguments
            address(0.0.0.0), port (numeric) , number of clients(numeric)'''
        try:
            soc=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            soc.bind((address,port))
            soc.listen(nofclis)
            soc.settimeout(15)
            print("Listening")
            self.incomingSocket,self.clientAddress=soc.accept()
            print("Incoming Connnection from "+ self.clientAddress[0])
        except:
            print('timeout')

    def command_executer(self,command):
        '''Incoming socket (Socket object), Command(String)'''
        self.incomingSocket.send(command.encode())
        self.recdata=self.incomingSocket.recv(20024)
        self.txtwriter(self.recdata.decode())

    
    def txtwriter(self,data,file='D:/admindat'):
        with open(file,'w')as outfile:
            outfile.write(data)

