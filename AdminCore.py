import socket


class Admin:

    def __init__(self):
        pass

    def connect_server(self,address,port):
        self.socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.socket.connect((address,port))
 

    def command_executer(self,command):
        self.socket.send(command.encode())
        self.recdata=self.socket.recv(20024)
        self.txtwriter(self.recdata.decode())
    
    def txtwriter(self,data,file='D:/admindat'):
        with open(file,'w')as outfile:
            outfile.write(data)
