import os
import tweepy
import requests
import pyshorteners
import praw
from time import sleep

API_KEY = os.getenv('API_KEY')
CONSUMER_KEY = os.getenv('CONSUMER_KEY')
CONSUMER_SECRET = os.getenv('CONSUMER_SECRET')
ACCESS_KEY = os.getenv('ACCESS_KEY')
ACCESS_SECRET = os.getenv('ACCESS_SECRET')
CLIENT_ID = os.getenv('CLIENT_ID')
CLIENT_SECRET = os.getenv('CLIENT_SECRET')

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

def tweet_meme(image_url, message):
	
	response = requests.get(image_url)
	file = open("temp.png", "wb")
	file.write(response.content)
	file.close()
	
	media = api.media_upload('temp.png')

	tweet = message
	post_result = api.update_status(status=tweet, media_ids=[media.media_id])

	sleep(10)

	print('tweeted ' + tweet)

reddit = praw.Reddit(client_id = CLIENT_ID,
                      client_secret = CLIENT_SECRET,
                      user_agent = "Discord Meme Bot",
                      username = "fakebot3")

subreddit = reddit.subreddit('memes')

top_5 = subreddit.top(limit = 5)
top_4 = subreddit.top(limit = 4)
top_3 = subreddit.top(limit = 3)
top_2 = subreddit.top(limit = 2)
top_1 = subreddit.top(limit = 1)
for submission in top_5:
 meme_5 = submission

for submission in top_4:
 meme_4 = submission

for submission in top_3:
 meme_3 = submission

for submission in top_2:
 meme_2 = submission

for submission in top_1:
 meme_1 = submission


s = pyshorteners.Shortener(api_key=API_KEY)

meme_1_link = s.bitly.short('https://reddit.com' + meme_1.permalink)
meme_2_link = s.bitly.short('https://reddit.com' + meme_2.permalink)
meme_3_link = s.bitly.short('https://reddit.com' + meme_3.permalink)
meme_4_link = s.bitly.short('https://reddit.com' + meme_4.permalink)
meme_5_link = s.bitly.short('https://reddit.com' + meme_5.permalink)

tweet_meme(image_url=meme_1.url, message=meme_1.title + ' ' + meme_1_link)
tweet_meme(image_url=meme_2.url, message=meme_2.title + ' ' + meme_2_link)
tweet_meme(image_url=meme_3.url, message=meme_3.title + ' ' + meme_3_link)
tweet_meme(image_url=meme_4.url, message=meme_4.title + ' ' + meme_4_link)
tweet_meme(image_url=meme_5.url, message=meme_5.title + ' ' + meme_5_link)

print('Memes Tweeted : )')
