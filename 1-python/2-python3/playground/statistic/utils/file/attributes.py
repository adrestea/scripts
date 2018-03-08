#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
a

"""

import os


class FileAttributes(object):
    def __init__(self, file_path):
        self.path = file_path
        if not os.path.isfile(file_path):
            raise Exception("file path is not available.")

    def get_mtime(self):
        return os.path.getmtime(self.path)

    def get_ctime(self):
        return os.path.getctime(self.path)

    def get_atime(self):
        return os.path.getatime(self.path)
