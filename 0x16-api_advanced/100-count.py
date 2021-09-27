#!/usr/bin/python3
"""
Return all the hot posts of a subreddit
"""
import re
import requests


def count_words(subreddit, word_list):
    counter = count_words_helper(subreddit, word_list)
    counter = sorted(counter.items(), key=lambda k: k[1], reverse=True)
    for word in counter:
        if word[1] == 0:
            break
        print('{}: {}'.format(word[0], word[1]))


def count_words_helper(subreddit_name, word_list, after='', counter={}):
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
        title = post.get('data').get('title')
        for w in word_list:
            matches = re.findall(r'(?:(?<=\s)|(?<=^))({})(?=(\s|$))'.format(w),
                                 title, re.IGNORECASE)
            matches = len(matches)
            if counter.get(w):
                counter[w] += matches
            else:
                counter[w] = matches
    if (subreddit.get('data').get('after')):
        after = subreddit.get('data').get('after')
        return count_words_helper(subreddit_name, word_list, after, counter)
    return counter
