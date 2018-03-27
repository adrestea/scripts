#!/usr/bin/env python
# -*- coding: utf-8 -*-
import datetime
import time


class DateEx:
    def __init__(self, str_form=None, str_to=None, format_from=None, format_to=None):
        # def __init__(self, str_form=None, str_to=None, time_stamp=0, format_from="%Y-%m-%d %H:%M:%S",
        # format_to="%Y/%m/%d %H:%M:%S"):
        self.time_stamp = -1
        self.str_from = str_form
        self.format_from = format_from
        self.str_to = str_to
        self.format_to = format_to

    def __init__(self, str, format):
        self.__init__(str_form=str, format_from=format)

    def __init__(self):
        pass

    def set_time_stamp(self, time_stamp):
        self.time_stamp = time_stamp

    def str_to_other_str(self):
        # def str_to_other_str(self, str_from, format_from='%Y-%m-%d %H:%M:%S'):
        """
        将默认的"%Y-%m-%d %H:%M:%S"格式转换为时间数组, 如:"2013-10-10 23:40:00"
        """
        if self.str_from is None or self.format_from is None:
            raise Exception("string is none.")
        timeArray = time.strptime(self.str_from, self.format_from)
        return timeArray

    def str_to_other_style(self):
        # def str_to_other_style(self, str_from, format_from="%Y-%m-%d %H:%M:%S", format_to="%Y/%m/%d %H:%M:%S"):
        """
        :return: 更改事件字符串格式, 如"2013-10-10 23:40:00" 改为 "2013/10/10 23:40:00"
        思路:先转换为时间数组,然后转换为其他格式
        """
        if self.str_from is None or self.format_from is None or self.format_to is None:
            raise Exception("string is none.")
        timeArray = self.str_to_other_str(self.str_from, self.format_from)
        otherStyleTime = time.strftime(self.format_to, timeArray)
        return otherStyleTime

    def str_to_stamp(self):
        # def str_to_stamp(self, str_from, format_from="%Y-%m-%d %H:%M:%S", format_to="%Y/%m/%d %H:%M:%S"):
        """
        将format_from的格式转换为format_to的格式类型
        """
        if self.str_from is None or self.format_from is None or self.format_to is None:
            raise Exception("string is none.")

        timeArray = time.strptime(self.str_from, self.format_from)
        otherStyleTime = time.strftime(self.format_to, timeArray)
        return otherStyleTime

    def stamp_to_str(self):
        """
        :return: 返回日期事件格式
        """
        # stamp = 1381419600
        if self.time_stamp == -1:
            raise Exception("string is none.")
        timeArray = time.localtime(self.time_stamp)
        otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
        return otherStyleTime

    def stamp_to_str_ex(self, time_stamp):
        # timeStamp = 1381419600
        if self.time_stamp:
            raise Exception("string is none.")
        dateArray = datetime.datetime.utcfromtimestamp(self.time_stamp)
        otherStyleTime = dateArray.strftime("%Y-%m-%d %H:%M:%S")
        return otherStyleTime

    def get_current_time(self):
        """
        :return: 返回當前的时间
        """
        # 获得当前时间时间戳
        timeStamp = int(time.time())
        return self.stamp_to_str(timeStamp)

    def get_current_time_ex(self, format_to="%Y-%m-%d %H:%M:%S"):
        """
        :return: 返回當前的时间
        """
        now = datetime.datetime.now()
        otherStyleTime = now.strftime(format_to)
        return otherStyleTime

    def get_date_before(self, days_ago=0):
        """
        注:timedelta()的参数有:days,hours,seconds,microseconds
        :return:
        """
        days_ago = (datetime.datetime.now() - datetime.timedelta(days=days_ago))
        timeStamp = int(time.mktime(days_ago.timetuple()))
        return self.stamp_to_str(timeStamp)

    def get_date_to_datetime(self):
        """
        注：将字符串日期转换为datetime后可以很高效的进行统计操作，因为转换为datetime后，可以通过datetime.timedelta()方法来前后移动时间，效率很高，而且可读性强。
        :return: 返回datetime对象
        """
        # 给定日期字符串，直接转换为datetime对象
        # dateStr = '2013-10-10 23:40:00'
        if self.date_str is None:
            raise Exception("string is none.")
        datetimeObj = datetime.datetime.strptime(self.date_str, "%Y-%m-%d %H:%M:%S")
        return datetimeObj

    def get_time_different(self):
        """
        :return: 两个时间之间相隔的秒
        """
        # from_time = datetime.datetime(2014, 12, 4, 1, 59, 59)
        # to_time = datetime.datetime(2014, 12, 4, 3, 59, 59)
        if self.str_to is None or self.str_from is None:
            raise Exception("string is none.")
        return (self.str_to - self.str_from).total_seconds()


if __name__ == "__main__":
    de = DateEx()
    pass
