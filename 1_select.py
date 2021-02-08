import socket
from select import select

to_monitor = []

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
server.bind(('localhost',5000))

server.listen()
def accept_connction(server):
	client_socket, addr = server.accept()
	print('Connection from:',addr)

	to_monitor.append(client_socket)


def send_massege(client_socket):	

	print('befor recv()')

	request = client_socket.recv(4096)

	if request: 
		response = 'Hellow wirls\n'.encode()
		client_socket.send(response)
	else:
		client_socket.close()


def event_loop():
	while True:

		ready_to_read, _, _= select(to_monitor,[], [])#read ,write, errors  
		print(select(to_monitor,[], []))
		for sock in ready_to_read:
			if sock is server:
				accept_connction(sock)
			else:
				send_massege(sock)

if __name__ == '__main__':
	to_monitor.append(server)
	event_loop()