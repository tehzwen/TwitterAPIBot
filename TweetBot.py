import tweepy, time, sys, json, os
from wordFrequencyCounter import *
import json

class tweetBot:
    
    def __init__(self):

        with open('apiKeys.json') as f:
            data = json.load(f)

        #enter the corresponding information from your Twitter application:
        CONSUMER_KEY = data["CONSUMER_KEY"]#keep the quotes, replace this with your consumer key
        CONSUMER_SECRET = data["CONSUMER_SECRET"]#keep the quotes, replace this with your consumer secret key
        ACCESS_KEY = data["ACCESS_KEY"]#keep the quotes, replace this with your access token
        ACCESS_SECRET = data["ACCESS_SECRET"]#keep the quotes, replace this with your access token secret
        auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
        auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
        self._api = tweepy.API(auth, retry_count=5, retry_delay=60) 
        self._username = 'tehzwen'
        self._specificsFile = 'spec.txt'        
        self._followerCount = 0
        self._followingCount = 0
        self._rawTweetTexts = []
        self._fixedTweetTexts = []
        self._frequencyDict = {}
        
        
    def getinitData(self):
        file = open(self._specificsFile)
        followers = file.readlines(1)
        following = file.readlines(2)
        print (followers)
        
    def getFollowerCounts(self):
        user = self._api.get_user(self._username)
        self._followerCount = user.followers_count
        self._followingCount = user.friends_count
        
        #print(self._followerCount)
        #print(self._followingCount)
        
        #return self._followerCount, self._followingCount

    def discoverallFollowed(self, val):
        x = self._api.friends(val)
        usernames = set()
        for followed in x:
            usernames.add(followed.screen_name)
            
        return usernames
        #print (x)
        
    def discoverFollowers(self, val):
        followerList = self._api.followers(val)
        usernames = set()
        for follower in followerList:
            usernames.add(follower.screen_name)
            
        return usernames
    
    def searchUser(self, val):
        user = self._api.get_user(val)
        status = user.status
        username = user.name
        followercount = user.followers_count
        print (status)
        
    def getUserTweets(self, user, numOfTweets):
        
        try:
            for pages in tweepy.Cursor(self._api.user_timeline, id=user, tweet_mode='extended').pages(numOfTweets):      

                for page in pages:
                    #print(page._json["full_text"])
                    self._rawTweetTexts.append(page._json["full_text"])
        
        except tweepy.TweepError:
            print("WAIT BBITCH")


    def getWordFrequency(self):
        for tweet in self._rawTweetTexts:
            fixedPunctVal = removePuncuation(tweet, "realDonaldTrump")
            if (len(fixedPunctVal) > 0):
                self._fixedTweetTexts.append(fixedPunctVal)

        self._frequencyDict = countFrequency(self._fixedTweetTexts)
        #print(self._frequencyDict)


    def unfollowSomeone(self, val):
        try:
            self._api.destroy_friendship(val)
        except:
            print ("User not found!")
            return
        return
    
    def followSomeone(self, val):
        try:
            self._api.create_friendship(val)
        except:
            print ("User not found!")
            return
        return


    def writeTweet(self, file):
        filename=open(file,'r')
        f=filename.readlines()
        filename.close()
        
        f = ''.join(f)
        
        count = 0
        for char in f:
            count += 1
        
        print (count)
        
        if count > 140:
            print ("The message is too long for a tweet!")
            return    
        
        else:
            self._api.update_status(f)
            
    def exit(self):
        file = open(self._specificsFile, 'w')
        fullString = "followers:", ",", str(self._followerCount), ",", "following:", ",", str(self._followingCount)
        file.writelines(fullString)
        file.close()
        
        os._exit(1)
