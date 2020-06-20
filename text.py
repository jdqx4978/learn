import threading
from time import sleep
import os
#线程执行函数
# a = 1
# def music():
#     for i in range(3):
#         sleep(2)
#         print(os.getpid(),"播放：张伟变身")
#     global a
#     print(a)
#     a=1000
# t = threading.Thread(target=music)
# t.start()
# for i in range(3):
#     sleep(1)
#     print(os.getpid(),"向松大变身")
# t.join()
# print(a)

#线程2
def fun(sec,name):
    print("张伟是傻逼")
    sleep(sec)
    print("%s执行完毕"%name)
jobs=[]
for i in range(10):
    t=threading.Thread(target=fun,args=(2,),kwargs={"name":'T%d'%i})
    jobs.append(t)
    t.start()
[i.join() for i in jobs]