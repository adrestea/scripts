#!/usr/bin/python3
# -*- coding: UTF-8 -*-

from tkinter import *
# import Tkinter.messagebox as messagebox


class Application(tkinter.Frame):
    def __init__(self, master=None):
        tkinter.Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        self.nameInput = tkinter.Entry(self)
        self.nameInput.pack()
        self.alertButton = tkinter.Button(self, text='Hello', command=self.hello)
        self.alertButton.pack()

    def hello(self):
        name = self.nameInput.get() or 'world'
        # messagebox.showinfo('Message', 'Hello, %s' % name)


if __name__ == '__main__':
    app = Application()
    # 设置窗口标题:
    app.master.title('Hello World')
    # 主消息循环:
    app.mainloop()
