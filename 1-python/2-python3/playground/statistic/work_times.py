#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-
"""
a
"""

import os
import threading
import time
from enum import Enum, unique

from playground.statistic.utils.file.attributes import FileAttributes

# MAX_OUT_TIMES = 5
MAX_OUT_TIMES = 2
# DEFAULT_SLEEP_TIME = 10
DEFAULT_SLEEP_TIME = 2
cmd_notify = {"inotifywait": "inotify-tools"}
event_file = ".event"
thread_monitor = None
isDebug = True
lock = threading.Lock()


@unique
class Status(Enum):
    Init = -1
    Working = 0
    Leaved = 1
    Timeout = 2


class WatchDog(object):

    def __init__(self, cmd):
        self.__m_time_lasted = None
        self.__lasted_status = Status.Working
        self.name = cmd
        if isDebug:
            print()
        self.__event_file_path = os.sep.join([os.getcwd(), event_file])
        if not os.path.exists(self.__event_file_path):
            os.mknod(self.__event_file_path)
        self.file_attributes = FileAttributes(self.__event_file_path)

    def is_support_installed(self):
        if not self.__is_binary_installed():
            print("Application is not install, please install follow first:\n\n"
                  "       $ sudo apt-get install", cmd_notify.get(self.name))
            return False
        else:
            print("Application is installed.")
            return True

    def start_to_monitor(self):
        global thread_monitor
        if isDebug:
            print("begin to monitor input folder.")
        # start to monitor input system.
        thread_input_monitor = threading.Thread(target=self.__to_input_monitor, name="monitor input system thread")
        threads = [thread_input_monitor]

        # start to monitor file status.
        thread_file_monitor = threading.Thread(target=self.__to_file_monitor, name="monitor file modify time thread")
        threads.append(thread_file_monitor)

        for t in threads:
            t.setDaemon(True)
            t.start()
            print(t.getName())
            t.join()

    @staticmethod
    def __sleep(sleep_time=DEFAULT_SLEEP_TIME):
        time.sleep(sleep_time)

    @staticmethod
    def __write_flag():
        print("--------write somethings ...")

    def __to_file_monitor(self):
        if isDebug:
            print("[__to_file_monitor]:\t")
        self.is_file_running = True
        out_times = 0
        status = Status.Init  # 需要强制第一次写入数据
        while True:
            # m_time = self.file_attributes.get_mtime()
            # m_time_started = datetime.datetime.strptime(m_time, '%a %b  %d %H:%M:%S %Y')
            m_time_started = self.file_attributes.get_mtime()
            if self.__m_time_lasted is None:
                self.__m_time_lasted = m_time_started
                self.__write_flag()
                self.__sleep()
                continue
            # f = (m_time_started - self.__m_time_lasted).seconds
            f = (m_time_started - self.__m_time_lasted)
            if isDebug:
                print("%s:\tstart:%f\t\t end:%f\t\tf:%f" % (
                    time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), m_time_started, self.__m_time_lasted, f),
                      end='')
            if f > 1:
                out_times = 0
                self.__m_time_lasted = m_time_started
                status = Status.Working
            else:
                if out_times >= MAX_OUT_TIMES:
                    # If out_times is greater than the value then determined status is leave.
                    status = Status.Leaved
                else:
                    status = Status.Timeout
                out_times = out_times + 1
            # write pipe flag
            if isDebug:
                print("\t\tout_times:%d\t\tstatus:%s\t\t lasted_status:%s" % (out_times, status, self.__lasted_status))
            if self.__lasted_status != status and status != Status.Timeout:
                self.__lasted_status = status
                self.__write_flag()
            self.__sleep()

    def __to_input_monitor(self):
        cmd = " ".join(["inotifywait", "-m", "/dev/input", ">", event_file])
        if isDebug:
            print("[__to_input_monitor]:\t", cmd)
        os.popen(cmd)
        self.is_input_running = True

    def __is_binary_installed(self):
        output = os.popen(" ".join(["which", self.name])).readlines()
        if len(output):
            return True
        return False


def main():
    global thread_monitor
    app = WatchDog("inotifywait")
    if not app.is_support_installed():
        if isDebug:
            print("exit because support application is not installed.")
        exit(1)
    app.start_to_monitor()
    exit(0)


if __name__ == "__main__":
    main()
