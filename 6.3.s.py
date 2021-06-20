import socket
import sys
import time
import errno
from multiprocessing import Process
import math


def ProcessStart(server):
	while True:
		opt=server.recv(1024).decode()

		if opt == '1':
			number, b =[float(i) for i in server.recv(2048).decode('utf-8').split('\n')]
			calculate=math.log(float(number),float(b))

		elif opt == '2':
			number = server.recv(1024).decode()
			calculate =math.sqrt(float(number))

		elif opt == '3':
			number  = server.recv(1024).decode()
			calculate = math.exp(float(number))

		elif  opt == '4':
			server.close()
			break

		server.sendall(str(calculate).encode())

if  __name__ == '__main__':
	sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	host = ''
	port = 8888

	try:
		sock.bind((host,port))
	except socket.error as e:
		print(str(e))
		sys.exit()

	sock.listen(3)
	while True:
		try:
			server,addr = sock.accept()
			print('\n Line Connected!!\n')

			proc = Process(target=ProcessStart, args=(server,))
			proc.start()
		except socket.error:
			print('error occurred!')


	sock.close()
