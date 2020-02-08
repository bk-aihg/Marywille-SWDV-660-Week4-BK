import socket

HOST = '127.0.0.1'  
PORT = int(input("Enter the server port number to connect to : "))

data = input("Enter the message to send to the server : ")
data = data.encode()

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(data)
    data_server = s.recv(1024)

print(data_server.decode('ascii'))
