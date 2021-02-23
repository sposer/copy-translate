#-*- coding:utf-8 -*-
from os import close, times
import tkinter as tk
from Pyperclip import Pyperclip
import threading
from Translate import Translate
from Config import Config
from time import sleep

class Start():

    #初始化
    def __init__(self, txt = ""):#内容
        self.txt = txt
        self.pyperclip = Pyperclip()
        startListen(self)


    def show(self):
        #print(threading.current_thread().getName())
        if(self.txt == None): return

        txt = Translate(self.txt)#__init__不能返回数据？
        txt = txt.doPost()

        root = tk.Tk()
        root.title('复制翻译')
        root.geometry("%sx%s+%s+%s" % (self.config["win_width"], self.config["win_height"], self.config["win_x"], self.config["win_y"]))
        """ width=self.config["win_width"], height=self.config["win_height"] """
        text = tk.Text(root, undo=True, font=("微软雅黑",self.config["txt_size"]))

        text.insert("insert", txt)
        
        text.pack()
        
        root.overrideredirect(1)                 # 去除窗口边框
        root.wm_attributes("-alpha", self.config["win_alpha"])        # 透明度(0.0~1.0)
        root.wm_attributes("-toolwindow", True)  # 置为工具窗口(没有最大最小按钮)
        root.wm_attributes("-topmost", True)     # 永远处于顶

        #监听右键拖动
        move = lambda event : OnMotion(event, root)
        stMove = lambda event : StopMove(event, root)
        root.bind("<ButtonPress-3>", StartMove) #监听左键按下操作响应函数
        root.bind("<ButtonRelease-3>", stMove) #监听左键松开操作响应函数
        root.bind("<B3-Motion>", move)  #监听鼠标移动操作响应函数
        #root.bind("<KeyPress>", myquit)

        #倒计时关闭
        """ timeToClose = lambda root: timeToClose(root)
        t = threading.Thread(target = timeToClose, args=[root, ])
        t.start()
        t.join() """
        timer = threading.Timer(self.config["win_showTime"], timeToClose, args=(root,))
        timer.setDaemon(threading.currentThread())
        timer.start()

        #监听关闭
        close = lambda event: closeAWin(root,)
        root.bind("<Double-Button-1>", close)

        #监听焦点
        """ focusin = lambda event: self.pyperclip.stop()
        root.bind("<FocusIn>", focusin)

        focusout = lambda event: startListen
        root.bind("<FocusOut>", focusout) """
        root.mainloop()
        root.destroy()


def startListen(self):
    while True:
        self.config = Config().getConfig()
        txt = self.pyperclip.listen()
        if(is_contain_chaos(self.txt) == False):
            self.txt = txt
            thread = threading.Thread(target = self.show, args=())
            thread.setDaemon(threading.currentThread())
            thread.start()
            #startListen(self)


def is_contain_chaos(keyword):
    try:
        keyword.encode("gb2312")
    except UnicodeEncodeError:
        return True
    return False


def closeAWin(root):
    #root.destroy()能关闭窗口，但阻塞了计时器线程导致不能关闭
    root.quit()
    root.update()

def timeToClose(root):
    closeAWin(root)


""" def app_lost_focus(self, event):
    if self.focus_get() != self.menu:
        self.destroy_menu(event) """


""" def onGo():
  print("go")

goBtn = tk.Button(text="测试",command=onGo,fg='blue',font=("黑体",10))
goBtn.pack()
 """

def StartMove(event):
    global x, y
    x = event.x
    y = event.y
 
def StopMove(event, root):
    global x, y
    x = None
    y = None
    c = Config()
    c.edtConfig("win_x", root.winfo_x())
    c.edtConfig("win_y", root.winfo_y())
 
def OnMotion(event, root):
    global x, y
    deltax = event.x - x
    deltay = event.y - y
    root.geometry("+%s+%s" % (root.winfo_x() + deltax, root.winfo_y() + deltay))
    root.update()
    #print(event.x,event.y,root.winfo_x(),root.winfo_y(),root.winfo_width(),root.winfo_height())


""" def myquit(*args):
    e = tk.Event()
    print(e)
    event = args[0]
    print(event) """


if __name__ == '__main__':
    Start()