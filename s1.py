import socket
import threading
import os
import time


HOST = '147.139.204.33'  
PORT = 50001

#HOST2 = '149.129.247.202'  
#PORT2 = 50007

#5Dragon
#HOST = '149.129.237.172'  
#PORT = 50001

#FAFAFA
#HOST = '149.129.225.106'  
#PORT = 50004

#HOST = '127.0.0.1'
#PORT = 8081  

def readtoken():
    with open("t1.txt", "r") as file:
        first_line = file.readline()
    return first_line

def gentoken(line):
    n = 2
    token = [line[i:i+n] for i in range(0, len(line), n)]
    token1=[]
    for i in range(0,8):
        if i == 4 or i == 5 or i == 6 or i == 7:
            token1.append("00")
        else:
            token1.append(token[i])
    for i in range(4,12):
        token1.append(token[i])

    token2=[]
    for i in range(12,28):
        token2.append(token[i])

    btoken1 = ''.join(map(str, token1))
    btoken2 = ''.join(map(str, token2))
    return [btoken1, btoken2]

def auth(client_socket, token1, token2):
    b = b'\x03\x00\x00L\x03\x00\x00\x00\xa0\xff\x00\x00\x00\x00\x00\x00'
    b += bytes.fromhex(token1)
    b += bytes.fromhex(token2)
    b += b'\x00\x00\x00\x00\x00\x00\x00\x00V1.01\x00\x00\x00'
    b += b'\x00\x00\x00\x00\x00`\x01\x00\x02\x00\x00\x00'
    client_socket.send(b)
    data = client_socket.recv(1024)
    print('Received', repr(data))

def client_program(client_socket):
    #message = input(" -> ")  # take input
    #while message.lower().strip() != 'exit':
    while True:
        time.sleep(0.4)
        #BasicSPin180
        #bs = b'\x03\x00\x00 \x03\x00\x00\x00\x11\xa0\x00\x00\x00\x00\x00\x00'
        #bs += b"\x00\x00\x00\x00\x01\x00\x00\x00\x12\x00\x00\x00\x10'\x00\x00"

        #BasicSPin80
        #bs = b'\x03\x00\x00 \x03\x00\x00\x00\x11\xa0\x00\x00\x00\x00\x00\x00'
        #bs += b"\x00\x00\x00\x00\x01\x00\x00\x00\x08\x00\x00\x00\x10'\x00\x00"

        #BasicSPin1760
        #bs += b'\x03\x00\x00 \x03\x00\x00\x00\x11\xa0\x00\x00\x00\x00\x00\x00'
        #bs += b"\x00\x00\x00\x00\x02\x00\x00\x00X\x00\x00\x00\x10'\x00\x00"
        
        #BasicSPin4400
        #bs += b'\x03\x00\x00 \x03\x00\x00\x00\x11\xa0\x00\x00\x00\x00\x00\x00'
        #bs += b"\x00\x00\x00\x00\x05\x00\x00\x00X\x00\x00\x00\x10'\x00\x00"

        #FreeGame80
        #bs = b'\x03\x00\x00 \x03\x00\x00\x00\x11\xa0\x00\x00\x00\x00\x00\x00'
        #bs += b"\x01\x00\x00\x00\x01\x00\x00\x00\x08\x00\x00\x00\x10'\x00\x00"
        
        #FreeGame17
        #bs = b'\x03\x00\x00 \x03\x00\x00\x00\x11\xa0\x00\x00\x00\x00\x00\x00'
        #bs += b"\x01\x00\x00\x00\x0f\x00\x00\x00X\x00\x00\x00\x10'\x00\x00"
        
        #FreeGame13
        bs = b'\x03\x00\x00 \x03\x00\x00\x00\x11\xa0\x00\x00\x00\x00\x00\x00'
        bs += b"\x01\x00\x00\x00\x0f\x00\x00\x00X\x00\x00\x00\x10'\x00\x00"

        client_socket.send(bs)  # send message
        data = client_socket.recv(1024)
        print('Received', repr(data))
        #message = input(" -> ")  # again take input
    client_socket.close()  # close the connection

if __name__ == '__main__':
    token = readtoken()
    gentoken = gentoken(token)
    client_socket = socket.socket()  # instantiate
    client_socket.connect((HOST, PORT))  # connect to the server
    auth(client_socket, gentoken[0], gentoken[1])
    #client_program(client_socket)
    N = 1
    threads = [threading.Thread(target=client_program, args=[client_socket]) for i in range(N)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()
