#!/usr/bin/python3
"""
    Prints the titles of the first 10 hot posts of given subreddit
"""
import requests


def top_ten(subreddit):
    """
        Function queries Reddit API and prints the titles of
        the first 10 hot posts or prints None if subreddit doesn't exist
    """
    url = "https://api.reddit.com/r/{}?sort=hot&limit=10".format(subreddit)
    headers = {'User-Agent': 'CustomClient/1.0'}
    r = requests.get(url, headers=headers, allow_redirects=False).json()
    if 'data' in r:
        for post in r['data']['children']:
            print(post['data']['title'])
    else:
        print(None)
