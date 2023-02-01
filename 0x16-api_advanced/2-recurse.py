#!/usr/bin/python3
""" 100-count
    Function to count words in all hot posts of a given Reddit subreddit."""
import requests

def recurse(subreddit, hot_list=[], after=None):
    headers = {
        'User-Agent': 'MyBot/0.0.1'
    }
    params = {
        'limit': 100,
        'after': after
    }
    response = requests.get(f'https://www.reddit.com/r/{subreddit}/hot.json', headers=headers, params=params)
    if response.status_code == 200:
        data = response.json()
        after = data['data']['after']
        for post in data['data']['children']:
            hot_list.append(post['data']['title'])
        if after:
            return recurse(subreddit, hot_list, after)
        else:
            return hot_list
    else:
        return None

