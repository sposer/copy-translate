#-*- coding:utf-8 -*-
from typing import Any
import pyperclip
from time import sleep
from Config import Config

class Pyperclip():

    def __init__(self) -> None:
        self.listener = listener()
        pass

    def stop(self):
        self.listener.off()

    def listen(self) -> Any:
    #while True:
        #jianting().main()
        txt = self.listener.main()
        #print(txt)
        return txt

class listener():

    def __init__(self) -> None:
        self.config = Config().getConfig()
        self.on = True
        pass

    def off(self):
        self.on = False

    def clipboard_get(self):
        data = pyperclip.paste()
        return data
 
    def main(self):
        recent_txt = self.clipboard_get()
        while self.on:
            txt = self.clipboard_get()
            if txt != recent_txt:
                recent_txt = txt
                return recent_txt
            #sleep(0.2)
            sleep(self.config["time_interval"])