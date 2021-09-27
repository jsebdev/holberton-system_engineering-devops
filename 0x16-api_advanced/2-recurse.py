#!/usr/bin/python3
"""
Return all the hot posts of a subreddit
"""
import requests


def recurse(subreddit, hot_list=[]):
    return recurse_helper(subreddit, hot_list)


def recurse_helper(subreddit_name, hot_list=[], after=''):
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit_name)
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)\
            AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135\
            Safari/537.36 Edge/12.246'}
    payload = {'after': after}
    r = requests.get(url, headers=headers, allow_redirects=False,
                     params=payload)
    subreddit = r.json()
    if subreddit.get('message', None) == 'Not Found':
        return None
    posts = subreddit['data']['children']
    for post in posts:
        hot_list.append(post.get('data').get('title'))
    if (subreddit.get('data').get('after')):
        after = subreddit.get('data').get('after')
        return recurse_helper(subreddit_name, hot_list, after)
    return hot_list
