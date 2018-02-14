#!/usr/bin/env python
#coding:utf-8       #设置python文件的编码为utf-8，这样就可以写入中文注释
'''
'''
import sys
import ConfigParser

class Config:
    def __init__(self, path):
        self.path = path
        self.cf = ConfigParser.ConfigParser()
        self.cf.read(self.path)

    def __get(self, field, key):
        result = ""
        try:
            result = self.cf.get(field, key)
        except:
            result = ""
        return result

    def __set(self, filed, key, value):
        try:
            self.cf.set(filed, key, value)
            self.cf.write(open(self.path, 'w'))
        except:
            return False
        return True

    def read_config(self, config_file_path, key, field = "DEFAULT"):
        cf = ConfigParser.ConfigParser()
        try:
            cf.read(config_file_path)
            result = cf.get(field, key)
        except:
            sys.exit(1)
        return result

    def write_config(self, config_file_path, key, value, field = "DEFAULT"):
        cf = ConfigParser.ConfigParser()
        try:
            cf.read(config_file_path)
            cf.set(field, key, value)
            cf.write(open(config_file_path,'w'))
        except:
            sys.exit(1)
        return True

if __name__ == "__main__":
    pass