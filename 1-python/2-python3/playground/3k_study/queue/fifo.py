#!/usr/bin/env python3
# -*- coding: utf-8 -*-



"""
使用queue可以设置是否在get的时候block

"""
import threading
from queue import Queue


class BlockQueue(object):
    def __init__(self):
        self.q = Queue()

    def add(self, num):
        self.q.put(num)

    def print(self):
        while True:
            val = self.q.get(block=True)
            if val == "quit":
                exit()
            print("get---> ", val)

    def inp(self):
        while True:
            val = input("input a number:")
            self.q.put(val)
            if val == "quit":
                exit()

    def run(self):
        t = threading.Thread(target=self.print)
        t.setDaemon(True)
        t.start()

        d = threading.Thread(target=self.inp)
        d.setDaemon(True)
        d.start()
        t.join()
        d.join()


if __name__ == "__main__":
    b = BlockQueue()
    b.run()
