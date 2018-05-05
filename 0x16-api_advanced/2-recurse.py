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
    headers = {'User-Agent': 'CustomClient/1.0'}
    r = requests.get(url, headers=headers, allow_redirects=False)
    if r.status_code != 200:
        return None
    r = r.json()
    if 'data' in r:
        fill_list(r['data']['children'], hot_list)
        if not r['data']['children']:
            return hot_list
        last_id = r['data']['children'][-1]['data']['id']
        hot_list.append(recurse(subreddit, hot_list, last_id))
        if hot_list[-1] is None:
            del hot_list[-1]
        return hot_list
    else:
        return None


def fill_list(posts, hot_list):
    """
        Recursively fill hot_list from given data
    """
    if not posts:
        return hot_list
    hot_list.append(posts[0]['data']['title'])
    fill_list(posts[1:], hot_list)
    return hot_list
