import socket
import threading
import time
#指定ipv4，和面向流的tcp协议
import threading

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(('127.0.0.1',9999))
s.listen(5)
print('Waiting For Connection...')
# def tcplink(sock,addr):
sock, addr = s.accept()
print('Accept new connection from %s...'%(addr,))
sock.send(b'Welcome!')
while True:
    data = sock.recv(1024)
    time.sleep(1)
    if not data or data.decode('utf-8') == 'exit':
        break
    sock.send(('Hello, %s!' % data.decode('utf-8')).encode('utf-8'))
sock.close()
print('Connection from %s closed.' % (addr,))
# while True:
#     sock,addr = s.accept()
#     t = threading.Thread(target = tcplink,args = (sock,addr))
#     t.start()