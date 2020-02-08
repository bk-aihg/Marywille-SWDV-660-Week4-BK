import socket                
  
s = socket.socket()          
port = 9500                
s.bind(('', port))         
s.listen(5)      

conn, addr = s.accept()  
with conn:
	while True:
		data = conn.recv(1024)
		if not data:
			break
		elif data == b"Hello":
			conn.sendall(b"Hi")
		else:
			conn.sendall(b"Goodbye")
			conn.close()
			
