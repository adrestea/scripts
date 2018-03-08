#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from queue import LifoQueue

q = LifoQueue()

for i in range(3):
    q.put(i)

while not q.empty():
    print(q.get())
