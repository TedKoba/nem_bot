from bot.args_twitter_keys import (
    access_token,
    access_token_secret,
    api_key,
    api_secret
)
import requests
from requests_oauthlib import OAuth1Session

twitter = OAuth1Session(
    access_token,
    access_token_secret,
    api_key,
    api_secret
)


def tweet(text):
    url = 'https://api.twitter.com/1.1/statuses/update.json'
    params = {'status': text}
    return twitter.post(url, params=params)
