from socket import *
from select import *

# 　创建好监听套接字
sockfd = socket()
sockfd.bind(("0.0.0.0", 8888))
sockfd.listen(5)
sockfd.setblocking(False)

p = poll()
map = {}
p.register(sockfd, POLLIN)
map[sockfd.fileno()] = sockfd
while True:
    events = p.poll()
    for fd, event in events:
        if fd == sockfd.fileno():
            connfd, addr = map[fd].accept()
            print("Connect from", addr)
            connfd.setblocking(False)
            p.register(connfd, POLLIN)
            map[connfd.fileno()] = connfd
        elif event == POLLIN:
            data = map[fd].recv(1024)
            if not data:
                p.unregister(fd)
                map[fd].close()
                del map[fd]
                continue
            print(data.decode())
            map[fd].send(b'ok')
