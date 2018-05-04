#!/usr/bin/python3
"""
    Finds number of subscribers for given subreddit account, 0 if invalid subreddit
"""
import requests


def number_of_subscribers(subreddit):
    """
        Sends a query to Reddit API
        
        Returns the number of subscribers for given subreddit
    """
    url = "http://api.reddit.com/r/{}/about".format(subreddit)
    headers = {'User-Agent': 'CustomClient/1.0'}
    r = requests.get(url, headers=headers).json()
    if 'data' in r:
        return r['data']['subscribers']
    else:
        return 0
