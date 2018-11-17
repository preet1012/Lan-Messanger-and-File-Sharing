import socket
import os
import subprocess      #starts the shell

def transfer(s,path):
    if os.path.exists(path):
        f=open(path,'rb')
        packet=f.read(1024)
        while packet:
            s.sendall(packet)
            packet=f.read(1024)
        s.sendall(b'Done')
        f.close()

    else:
        s.send('Unable to find the file')

def connect():
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.connect(('127.0.0.1',8080))
    while True:
        command=s.recv(1024)
        command=command.decode('utf-8')
        
        if (command == '1'):
            print(command)
        
            s.sendall(b"Ready to chat")
            while True:
                x=s.recv(1024)
    
                print(x)
                if (x == 'bye'):
                    print('he is dead')
                    break
                data = input("Enter")
                s.sendall(data.encode())
                
        elif 'terminate' in command :
            s.close()
            break

        elif (command == '2'):
            print("Do you want to share files--Press [1(yes) or 2(no)]")
            m = int(input("Enter"))
            if (m == 1):
                s.sendall(b"Ready for file transfer")
                while True:
                    x=s.recv(1024)
                    x=x.decode()
                    if 'grab' in x:
                        grab,path=x.split('*')
                        try:
                            transfer(s,path)
                        except Exception(e):
                            s.sendall(str(e))
                            pass
            else:
                s.sendall(b"Not authorized")
                
                    
        else:
            s.sendall(b"Invalid Command")
            



def main():
    connect()
main()
