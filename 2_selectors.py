import socket
import selectors

selector = selectors.DefaultSelector()

def server():
	server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	server.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
	server.bind(('localhost',5000))
	server.listen()

	selector.register(fileobj=server, events=selectors.EVENT_READ, data=accept_connction)
def accept_connction(server):
	
	client_socket, addr = server.accept()
	selector.register(fileobj=client_socket, events=selectors.EVENT_READ, data=send_massege)
	print('Connection from:',addr)



def send_massege(client_socket):	

	print('befor recv()')

	request = client_socket.recv(4096)

	if request: 
		response = 'Hellow wirls\n'.encode()
		client_socket.send(response)
	else:
		selector.unregister(client_socket)
		client_socket.close()


def event_loop():
	while True:
		events = selector.select() #(key,evens - чтение и ли запись)
		# SelectorKye -  

		for key, _ in events:
			callback = key.data
			callback(key.fileobj)

if __name__ == '__main__':
	server()
	event_loop()
# особенность этого примера то что мы регистрировали сокеты вместе с сопровождающими данными 
# В данном случае 