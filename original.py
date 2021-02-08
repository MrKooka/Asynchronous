import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
server.bind(('localhost',5000))

server.listen()

while True:
#Метод .accept заморозил скрипт ,он жет вхожящего подключения
#до тех пор по не будет входящего подключения
#другими словами, метод accept() блокирующая функция, блокирует выполнение скриптa 
	print('Before .accept()')
	# принимает входящие данные 
	# если с сервера что то пришло , то метод accept() 
	# возращает кортеж где , первый это сокет клиента а второй это адрес 
	client_socket, addr = server.accept()
	print('Connection from:',addr)
	# этот цикл мониторит входящие сообщения 
	while True:
		print('befor recv()')

		request = client_socket.recv(4096)

		if not request:
			break 
		else:
			response = 'Hellow wirls\n'.encode()
			# rкодируем строку в байти, метод encode() кодирует в байты по умолчанию
			client_socket.send(response)


	print('Вне внутреннего цикла')
	client_socket.close()