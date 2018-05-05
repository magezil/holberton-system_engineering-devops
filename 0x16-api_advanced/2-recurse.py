#!/usr/bin/python3
"""
    Returns list of titles of hot articles
"""
import requests


def recurse(subreddit, hot_list=[], last_id=None):
    """
        Recursive function to query Reddit API for given subreddit

        Returns a list of titles of all hot articles,
        or None if invalid subreddit
    """
    url = "https://api.reddit.com/r/{}?sort=hot".format(subreddit)
    if last_id is not None:
        url = "{}&after=t3_{}".format(url, last_id)
        last_id = None
    headers = {'User-Agent': 'CustomClient/1.0'}
    r = requests.get(url, headers=headers, allow_redirects=False).json()
    if 'data' in r:
        for post in r['data']['children']:
            hot_list.append(post['data']['title'])
            last_id = post['data']['id']
        if last_id is not None:
            hot_list.append(recurse(subreddit, hot_list, last_id))
        return hot_list
    else:
        return None
