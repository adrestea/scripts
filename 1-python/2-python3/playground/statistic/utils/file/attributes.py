#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
a

"""
import datetime
import os

from playground.statistic.utils.date.date import DateEx


class FileAttributes(object):
    def __init__(self, file_path):
        self.path = file_path
        if not os.path.isfile(file_path):
            raise Exception("file path is not available.")

    def get_mtime_display(self):
        m_time = self.get_mtime_stamp()
        m_time_started = datetime.datetime.strptime(m_time, '%a %b  %d %H:%M:%S %Y')
        return m_time_started

    def get_mtime_stamp(self):
        return os.path.getmtime(self.path)

    def get_ctime_stamp(self):
        c_time = os.path.getctime(self.path)
        return c_time

    def get_atime_stamp(self):
        return os.path.getatime(self.path)

    def get_mtime(self):
        dateEx = DateEx(time_stamp=self.get_mtime_stamp())
        return dateEx.stamp_to_str()

    def get_ctime(self):
        dateEx = DateEx()
        dateEx.set_time_stamp(self.get_ctime_stamp())
        return dateEx.stamp_to_str()

    def get_atime(self):
        dateEx = DateEx(time_stamp=self.get_atime_stamp())
        return dateEx.stamp_to_str()
