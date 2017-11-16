class tweetBot:
    
    def __init__(self):
        #enter the corresponding information from your Twitter application:
        CONSUMER_KEY = 'QSJ8J1xwv2pfLelX8s1D8e7pN'#keep the quotes, replace this with your consumer key
        CONSUMER_SECRET = 'pwvkZBoOjr5IR5LP81T4YCbZXwmvPZqniE5PkZ39GDpuetD5cJ'#keep the quotes, replace this with your consumer secret key
        ACCESS_KEY = '921162870775148545-Cc9UaUQXIZVPjR0dMFaLyk3Vycb8qr1'#keep the quotes, replace this with your access token
        ACCESS_SECRET = 'ME7sxcS7gJXdRJDCnUzzYWiNrhyAmgCl70uSG1V3llHfa'#keep the quotes, replace this with your access token secret
        auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
        auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
        self._api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True) 
        self._username = 'macewanstats'
        self._specificsFile = 'spec.txt'        
        self._followerCount = 0
        self._followingCount = 0
        
        
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
        username = user.name
        followercount = user.followers_count
        
        print(user.followers)
        print (username, followercount)


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