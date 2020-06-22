
from socket import *
#远程修改学习中！！！！！！

"""
author:chj
email:497847023@qq.com
time:2020-6-15
env:python3.7
socket and Process exercise
"""
user = {}


def do_login(sock, name,addr):
    if name in user:
        sock.sendto(b"Fail",addr)
        return
    else:
        sock.sendto(b"OK", addr)
        msg = "欢迎 %s进入聊天室"%name
        for i in user:
            sock.sendto(msg.encode(),user[i])
    user[name]=addr


def do_chat(sock, name,content):
    msg = "%s : %s" % (name, content)
    for i in user:
        if name != i:
            sock.sendto(msg.encode(),user[i])


def do_quit(sock, name):
    del user[name]  # 从字典中删除用户
    msg = "%s 退出聊天室" % name
    # 通知其他人
    for i in user:
        sock.sendto(msg.encode(), user[i])


def do_request(sock):
    while True:
        data,addr = sock.recvfrom(2048)
        msg =data.decode.split(" ",2)
        if msg[0]=="L":
            do_login(sock,msg[1],addr)
        if msg[0]=="C":
            do_chat(sock,msg[1],msg[2])
        if msg[0]=="Q":
            do_quit(sock,msg[1])




def main():
    sock = socket(AF_INET,SOCK_DGRAM)
    sock.bind(('0.0.0.0',8888))
    do_request(sock)

if __name__ == '__main__':
    main()
