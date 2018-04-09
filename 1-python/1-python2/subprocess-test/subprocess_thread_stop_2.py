import threading, inspect, ctypes
from time import ctime,sleep

def _async_raise(tid, exctype):
    """raises the exception, performs cleanup if needed"""
    tid = ctypes.c_long(tid)
    if not inspect.isclass(exctype):
        exctype = type(exctype)
    res = ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, ctypes.py_object(exctype))
    if res == 0:
        raise ValueError("invalid thread id")
    elif res != 1:
        # """if it returns a number greater than one, you're in trouble,
        # and you should call it again with exc=NULL to revert the effect"""
        ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, None)
        raise SystemError("PyThreadState_SetAsyncExc failed")

def stop_thread(thread):
    _async_raise(thread.ident, SystemExit)

class TestThread(threading.Thread):
    def run(self):
        print("TestThread begin at ", ctime())
        while True:
            print("TestThread going...")
            sleep(10)
        print("TestThread end at ", ctime())

if __name__ == "__main__":
    t = TestThread()
    t.start()
    sleep(1)
    stop_thread(t)
    print("t status is :%s"% t.isAlive())
    print("stoped")
