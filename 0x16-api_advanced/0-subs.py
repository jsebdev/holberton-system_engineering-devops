#!/usr/bin/python3
"""
Return the number of subscribers of a subreddit
"""
import requests


def number_of_subscribers(subreddit):
    url = 'https://www.reddit.com/r/{:s}/about.json'.format(subreddit)
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)\
            AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135\
            Safari/537.36 Edge/12.246'}
    r = requests.get(url, headers=headers, allow_redirects=False)
    subreddit = r.json()
    if subreddit.get('message', None) == 'Not Found':
        return 0
    return subreddit['data'].get('subscribers', 0)
