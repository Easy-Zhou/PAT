#!/anaconda3/bin/python
# @Time    : 2019-04-26 15:22
# @Author  : zhou
# @File    : 2896_线程安全
# @Software: PyCharm
# @Description: 


import time
import threading


class ticket_db:

    def __init__(self):
        self.tickets = 5

    def get_tickets(self):
        return self.tickets

    def sell_tickets(self):
        if self.tickets > 0:
            self.tickets -= 1
            return "出票成功"
        else:
            return "无票"


def ticket_body1():
    global db, lock
    while True:
        lock.acquire()
        cnt = db.get_tickets()
        if cnt > 0:
            db.sell_tickets()
            time.sleep(1)
            print("售出第{0}张票".format(cnt))
            lock.release()
        else:
            lock.release()
            return


def ticket_body2():
    global db, lock
    while True:
        lock.acquire()
        cnt = db.get_tickets()
        if cnt > 0:
            db.sell_tickets()
            time.sleep(1)
            print("售出第{0}张票".format(cnt))
            lock.release()
        else:
            lock.release()
            return


db = ticket_db()
lock = threading.Lock()

t1 = threading.Thread(target=ticket_body1)
t1.start()

t2 = threading.Thread(target=ticket_body2)
t2.start()
