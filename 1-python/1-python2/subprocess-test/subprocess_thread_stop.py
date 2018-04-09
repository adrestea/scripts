import threading
import inspect
import ctypes 
from time import ctime,sleep

def _async_raise(tid, exctype):
    """raises the exception, performs cleanup if needed"""
    print("enter _async_raise    TIME:", ctime())
    if not inspect.isclass(exctype):
        exctype = type(exctype)
    res = ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, ctypes.py_object(exctype))
    if res == 0:
#        raise ValueError("invalid thread id")
        pass
    elif res != 1:
        # """if it returns a number greater than one, you're in trouble, 
        # and you should call it again with exc=NULL to revert the effect"""
        ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, None)
#        raise SystemError("PyThreadState_SetAsyncExc failed")
    print("kill end...    TIME:", ctime())

def stop_thread(thread):
    _async_raise(thread.ident, SystemExit)

def downloadCodes():
    print("downloadCodes start...    TIME:", ctime())
    sleep(10)
    print("downloadCodes end...    TIME:", ctime())

if __name__ == '__main__':
    print("main enter...    TIME:", ctime())
    dtown = threading.Thread(target=downloadCodes)
    dtown.setDaemon(True)
    dtown.start()
    sleep(3)
    stop_thread(dtown)
#    dtown.join()
    if not dtown.isAlive():
        dtown.start()
#    dtown.join()
    print("main end...    TIME:", ctime())
