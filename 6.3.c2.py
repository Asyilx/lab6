import socket
import sys
import time
import math
import errno

C= socket.socket()
host = '192.168.56.104'
port = 8888

try:
        C.connect((host,port))
        print (' Line Successfull Connected! ')
except socket.error as e:
        print (str(e))

loop = True

while loop:
        print ('\n Welcome to math calculator python ')
        print (' 1. Logarithmic (Log)')
        print (' 2. Square Root ')
        print (' 3. Exponential')
        print (' 4. Exit ')

        ans = input ('\n Enter your choice : ')
        C.send(ans.encode())

        if ans == '1':
                print ('\n [+] Log Function ')
                number = input('\n Enter Number : ')
                b = input('\n Enter base : ')
                C.sendall(str.encode('\n'.join([str(number), str(b)])))
                total = C.recv(1024)
                print ('Asnwer for log'+ number +'base'+ b +' : '+str(total.decode()))

        elif ans == '2':
                root = True
                while root:
                        print ('\n [+] Square Root Function ')
                        number = input ('\n Enter Number : ')
                        if float(number) <  0:
                                print('\n Negative Number Cant Be Square Root')
                        else:
                                root = False
                                C.send(number.encode())
                        total = C.recv(1024)

                print ('Answer for square root '+number+' : '+str(total.decode()))

        elif ans == '3':
                print ('\n [+] Exponential')
                number = input ('\n Enter Number : ')
                C.send(number.encode())
                total = C.recv(1024)
                print ('Answer for exponent is'+number+' : '+str(total.decode()))

        elif ans == '4':
                C.close()
                sys.exit()
        else:
                 print ('\n Invalid input please try again !')
                 input ( '\n Press Enter to Continue .. ')

