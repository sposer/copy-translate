import os.path
import json
import sys

class Config():
    def __init__(self) -> None:
        if(os.path.isfile("config.txt")):
            self.readConfig()
        else:
            config = {}
            config["win_width"] = 160
            config["win_height"] = 90
            config["win_alpha"] = 0.8
            config["win_x"] = 0
            config["win_y"] = 0
            config["win_showTime"] = 3
            config["time_interval"] = 0.2
            config["txt_size"] = 12
            self.config = config
            self.saveConfig()
        #print(self.config)
        pass

    def saveConfig(self):
        file = open("config.txt", "w")
        print(self.config, file = file)
        file.close()

    def readConfig(self):
        file = open("config.txt", "r")
        sys.stdin = file
        self.config = eval(input())
        file.close()

    def edtConfig(self, key, value):
        self.config[key] = value
        self.saveConfig()

    def getConfig(self):
        return self.config

if(__name__ == "__main__"):
    Config()