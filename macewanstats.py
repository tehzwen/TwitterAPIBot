
 
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
        
        self.TWEET = Button(self, text = "Send tweet from file", command = sendTweet)
        
        self.TWEET.pack({"side": "top"})
        
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
        t.getFollowerCounts()
        followercount = t._followerCount
        currentFollowers = t.discoverFollowers(t._username)
        print (currentFollowers)
        
        while waiting:
            print ("waiting")
    
            time.sleep(1)
            t.getFollowerCounts()
            newFollowers = t._followerCount
            
            if newFollowers > followercount:
                print ("We have a new follower")
                newFollowersSet = t.discoverFollowers(t._username)
                difference = newFollowersSet.difference(currentFollowers)
                for user in difference:
                    t.followSomeone(user)
                    print ("I followed", user)
                followercount = t._followerCount
            
        print ("bot is ready")
    
    thread1 = threading.Thread(target= runBot)
    thread1.start()
    
def sendTweet():
    filename = filedialog.askopenfilename()
    t = tweetBot()
    t.writeTweet(filename)
    print ("tweet sent")


   
def main():
    
    root = Tk()
    app = Application(root)
    if app.BOT:
        print ("ran the bot")
    app.mainloop()
    root.destroy()
    
main()
    
