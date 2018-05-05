#!/usr/bin/python3
"""
    Finds number of subscribers for given subreddit account,
    or 0 if invalid subreddit
"""
import requests


def number_of_subscribers(subreddit):
    """
        Sends a query to Reddit API

        Returns the number of subscribers for given subreddit
    """
    url = "https://api.reddit.com/r/{}/about".format(subreddit)
    headers = {'User-Agent': 'CustomClient/1.0'}
    r = requests.get(url, headers=headers, allow_redirects=False)
    if r.status_code != 200:
        return 0
    r = r.json()
    if 'data' in r:
        return r['data']['subscribers']
    else:
        return 0
