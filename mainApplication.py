import tweepy, time, sys, json, os
from tkinter import *
from tkinter import filedialog
import threading
import os
from TweetBot import *


class Application(Frame):
    
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()
    
    def createWidgets(self):
        
        self.QUIT = Button(self)
        self.QUIT["text"] = "QUIT"
        self.QUIT["fg"] = "red"
        self.QUIT["command"] = exitApp
        
        self.QUIT.pack({"side": "right"})
        
        self.BOT = Button(self)
        self.BOT['text'] = "Start bot"
        self.BOT['fg'] = "black"
        self.BOT["command"] = mainActivity
        
        self.BOT.pack({"side": "left"})

        self.USERNAMETOSEARCH = Entry(self, bd=5)
        self.USERNAMETOSEARCH.pack(side = BOTTOM)
        
        self.TWEET = Button(self, text = "Send tweet from file", command = sendTweet)
        self.TWEET.pack({"side": "top"})

        self.USEARCH = Button(self, text = "Search for user", command = lambda: getTweetsFrom(self.USERNAMETOSEARCH.get()))
        self.USEARCH.pack({"side": "top"})
        
    def createStop(self):
        self.STOP = Button(self)
        self.STOP["text"] = "Stop Bot"
        self.STOP["command"] = stopBot
        self.STOP.pack({"side": "bottom"})

        
def stopBot():
    t = tweetBot()
    print ("currently waiting for command")
        
def exitApp():
    os._exit(1)
        
def mainActivity():
    
    def runBot():
        waiting = True
        t = tweetBot()
        print ("bot is ready")
    
    thread1 = threading.Thread(target= runBot)
    thread1.start()
    
def sendTweet():
    filename = filedialog.askopenfilename()
    t = tweetBot()
    t.writeTweet(filename)
    print ("tweet sent")

def getTweetsFrom(val):
    t = tweetBot()
    t.getUserTweets(val, 50)
    t.getWordFrequency()

    fontSize = 24
    biggestVal = t._frequencyDict[0][1]

    for key,value in t._frequencyDict:
        if value > 10:
            if value < biggestVal:
                fontSize -= 1
                biggestVal = value
            #print(key)
            label = Label(None, text=key, font=('Times', fontSize),fg='black')
            label.pack()

def main():
    root = Tk()
    root.geometry("500x500")
    app = Application(root)

    if app.BOT:
        print ("ran the bot")
    app.mainloop()
    root.destroy()
    
main()
    
