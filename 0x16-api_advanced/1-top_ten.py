#!/usr/bin/python3
"""
Return the number of subscribers of a subreddit
"""
import requests


def top_ten(subreddit):
    url = 'https://www.reddit.com/r/{:s}/hot.json'.format(subreddit)
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)\
            AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135\
            Safari/537.36 Edge/12.246'}
    r = requests.get(url, headers=headers, allow_redirects=False)
    subreddit = r.json()
    if subreddit.get('message', None) == 'Not Found':
        return None
    posts = subreddit['data']['children']
    for i, posts in enumerate(posts):
        if (i < 10):
            print(posts['data']['title'])
        else:
            break
