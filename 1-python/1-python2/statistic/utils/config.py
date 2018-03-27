#!/usr/bin/env python
# coding:utf-8
import sys
import ConfigParser


class Config:
    def __init__(self, path):
        self.path = path
        self.cf = ConfigParser.ConfigParser()
        self.cf.read(self.path)
        # print(self.cf.sections())

    # def __get(self, field, key):
    #     result = ""
    #     try:
    #         result = self.cf.get(field, key)
    #     except:
    #         result = ""
    #     return result
    #
    # def __set(self, filed, key, value):
    #     try:
    #         self.cf.set(filed, key, value)
    #         self.cf.write(open(self.path, 'w'))
    #     except:
    #         return False
    #     return True

    def read_config(self, key, field="DEFAULT"):
        # cf = ConfigParser.ConfigParser()
        result = None
        try:
            # cf.read(self.path)
            result = self.cf.get(field, key)
        except:
            print("value is None")
        return result

    def write_config(self, key, value, field="DEFAULT"):
        # cf = ConfigParser.ConfigParser()
        try:
            # cf.read(self.path)
            self.cf.set(field, key, value)
            self.cf.write(open(self.path, 'w'))
        except Exception as e:
            print("value is None")
        return True

    def sections(self):
        # cf = ConfigParser.ConfigParser()
        return self.cf.sections()

    def items(self, section):
        return self.cf.items(section)

    def remove_option(self, section, key):
        self.cf.remove_option(section, key)

    def remove_section(self, section):
        self.cf.remove_section(section)

    def add_section(self, section):
        self.cf.add_section(section)


if __name__ == "__main__":
    pass
