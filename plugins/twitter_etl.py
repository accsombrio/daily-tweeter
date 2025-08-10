import tweepy
import os
from datetime import date

#etl twitter function
def run_twitter_etl():

    # API keys
    CONSUMER_KEY = os.getenv('CONSUMER_KEY')
    CONSUMER_SECRET = os.getenv('CONSUMER_SECRET')
    ACCESS_KEY = os.getenv('ACCESS_KEY')
    ACCESS_SECRET = os.getenv('ACCESS_SECRET')

    # Authenticate with the Twitter API v2
    client = tweepy.Client(
        consumer_key=CONSUMER_KEY,
        consumer_secret=CONSUMER_SECRET,
        access_token=ACCESS_KEY,
        access_token_secret=ACCESS_SECRET
    )
    # Define the tweet text

    #tweet_text = "send tweets using docker!"
    tweet_text = f"Today is {date.today().strftime('%B %d, %Y')}. Have a good day!"

    # Create the tweet
    try:
        response = client.create_tweet(text=tweet_text)
        print(f"Tweet ID: {response.data['id']}")
        print(f"Tweet Text: {response.data['text']}")
        print("tweet posted  successfully!")
        
        #retrieve twitter client user details
        #response = client.get_me()
        #print(f"Name: {response.data['name']}")
        #print(f"Username: {response.data['username']}")
        
    except tweepy.TweepyException as e:
        print(f"Error creating tweet: {e}")