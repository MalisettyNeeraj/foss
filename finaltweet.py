import tweepy 
consumer_key ="b5iZZKHqWKO6tKmd4BO65AnDI"
consumer_secret ="wZcY5QP0nMFrXwjsXLDOQLmuMa4lxuiI0G6UxHVJ28nv9Wncnt"
access_token ="1053149916434849793-1UmvMzbFTl8qM9MvtyNVmUbZtEpL7Z"
access_token_secret ="rQoGAx3sk2BaNBX0OFLw5gw7r8Xq6fojFOHYmjnEsKnYM "
auth = tweepy.OAuthHandler(consumer_key, consumer_secret) 
auth.set_access_token(access_token, access_token_secret) 
api = tweepy.API(auth) 
api.update_status(status ="hello")