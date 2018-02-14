#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# FileName: pickle-object-to-file.py


import pickle
import pprint


def save_object():
    # 使用pickle模块将数据对象保存到文件
    data1 = {'a': [1, 2.0, 3, 4 + 7j],
             'b': ('string', u'Unicode string'),
             'c': None}

    ist = [1, 2, 3]

    output = open('data.pkl', 'wb')

    # Pickle dictionary using protocol 0.
    pickle.dump(data1, output)

    # Pickle the list using the highest protocol available.
    pickle.dump(ist, output, -1)

    output.close()


def load_object():
    # 使用pickle模块从文件中重构python对象
    pkl_file = open('data.pkl', 'rb')

    data1 = pickle.load(pkl_file)
    pprint.pprint(data1)

    data2 = pickle.load(pkl_file)
    pprint.pprint(data2)

    pkl_file.close()


if __name__ == '__main__':
    save_object()
    load_object()
