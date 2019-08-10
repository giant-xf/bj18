import sys
import time
import gevent
from gevent import socket,monkey
#这句话一定要写，代表把以下代码按照gevent中的功能来运行
#只要是延时操作，都在这里进行了修改重写，必须要调用gevent中的功能
monkey.patch_all()

def handle_request(conn):
    while True:
        data = conn.recv(1024)
        if not data:
            conn.close()
            break
        print("recv:", data)
        conn.send(data)
def server(port):
    s = socket.socket()
    s.bind(('', port))
    s.listen(5)
    while True:
        cli, addr = s.accept()
        gevent.spawn(handle_request, cli)
if __name__ == '__main__':
    server(7788)