#!/usr/bin/python3
"""
a function that queries the Reddit API and returns the number of subscribers (not active users, total subscribers) for a given subreddit.
"""
import requests


def number_of_subscribers(subreddit):
    headers = {'User-Agent': 'My User Agent 1.0'}
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json().get("data").get('subscribers')
    else:
        return 0
