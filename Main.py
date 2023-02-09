


# negative for revolutionary or positive for reactionary
# scale of 0-10 based on how passionate? 


#input : twitter username -> twitter api to get all their tweets -> pass it through our model to predict revolutionary or reactionary

###

import tweepy

# Replace with your own API credentials
consumer_key = "your_consumer_key"
consumer_secret = "your_consumer_secret"
access_token = "your_access_token"
access_token_secret = "your_access_token_secret"

# Authenticate to the Twitter API
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# Create an API client
api = tweepy.API(auth)

# Search for political tweets containing the hashtag "#politics"
tweets = api.search(q="#politics", count=100)

# Print the text of each tweet
for tweet in tweets:
    print(tweet.text)


###
