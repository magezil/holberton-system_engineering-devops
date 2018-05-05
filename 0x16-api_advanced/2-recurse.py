#!/usr/bin/python3
"""
    Returns list of titles of hot articles
"""
import requests


def recurse(subreddit, hot_list=[], after=""):
    """
        Recursive function to query Reddit API for given subreddit

        Returns a list of titles of all hot articles,
        or None if invalid subreddit
    """
    url = "https://api.reddit.com/r/{}?sort=hot".format(subreddit)
    if after:
        url = "{}&after={}".format(url, after)
    headers = {'User-Agent': 'CustomClient/1.0'}
    r = requests.get(url, headers=headers, allow_redirects=False)
    if r.status_code != 200:
        return None
    r = r.json()
    if 'data' in r:
        data = r['data']
        if not data['children']:
            return hot_list
        hot_list += [post['data']['title'] for post in data['children']]
        if not data['after']:
            return hot_list
        recurse(subreddit, hot_list, data['after'])
        if hot_list[-1] is None:
            del hot_list[-1]
        return hot_list
    else:
        return None
