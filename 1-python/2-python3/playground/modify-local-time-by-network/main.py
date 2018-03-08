#!/usr/bin/env python
# encoding: utf-8

# import httplib
import http.client as httplib
import logging
import subprocess
import threading

import time


def getBeijinTime():
    """
　　 获取北京时间
    """
    try:
        conn = httplib.HTTPConnection("www.beijing-time.org")
        conn.request("GET", "/time15.asp")
        response = conn.getresponse()
        print
        response.status, response.reason
        if response.status == 200:
            # 解析响应的消息
            # response.read() //在python3使用需要先转化byte-like为str
            # result = str(response.read(), encoding="utf-8")
            result = bytes.decode(response.read())
            logging.debug(result)
            data = result.split(";\r\n")
            year = data[1].split("=")[1]
            month = data[2].split("=")[1]
            day = data[3].split("=")[1]
            hrs = data[5].split("=")[1]
            minute = data[6].split("=")[1]
            sec = data[7].split("=")[1].split(";")[0]

            beijinTimeStr = "%s-%s-%s %s:%s:%s" % (year, month, day, hrs, minute, sec)
            # beijinTime = time.strptime(beijinTimeStr, "%Y-%m-%d %X")  //将str转换为time的元组
            # return beijinTime
            return beijinTimeStr
    except Exception as e:
        logging.exception("getBeijinTime except")
        return None


def syncLocalTime():
    """
    同步本地时间
    """
    logging.info("current local time is: %d-%d-%d %d:%d:%d" % time.localtime()[:6])

    beijinTime = getBeijinTime()
    if beijinTime is None:
        logging.info("get beijinTime is None, will try again in 30 seconds...")
        timer = threading.Timer(30.0, syncLocalTime)
        timer.start()
    else:
        # logging.info("get beijinTime is: %d-%d-%d %d:%d:%d" % beijinTime[:6])

        # tm_year, tm_mon, tm_mday, tm_hour, tm_min, tm_sec = beijinTime[:6]
        # import os
        # out_bytes = subprocess.check_output(['sudo', 'ls'])
        # os.system("date %d-%d-%d" % (tm_year, tm_mon, tm_mday))  # 设置日期
        # os.system("time %d:%d:%d.0" % (tm_hour, tm_min, tm_sec))  # 设置时间

        # d_val = str.format("%d-%d-%d %d:%d:%d" % (tm_year, tm_mon, tm_mday, tm_hour, tm_min, tm_sec))
        # subprocess.check_output(['sudo', 'date', '-s', d_val])
        try:
            out_bytes = subprocess.check_output(['sudo', 'date', '-s', beijinTime], timeout=5)
            logging.info("syncLocalTime complete, current local time: %d-%d-%d %d:%d:%d \n" % time.localtime()[:6])
        except subprocess.TimeoutExpired:
            logging.info("set date time out.")


if __name__ == '__main__':
    syncLocalTime()
