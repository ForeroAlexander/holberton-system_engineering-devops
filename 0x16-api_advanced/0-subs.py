#!/usr/bin/python3
"""File with a function that return the number of subs of a subreddit
"""

import requests


def number_of_subscribers(subreddit):
    """function that queries the Reddit API and returns the
       number of subscribers"""
    URL = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {'User-Agent': 'URL'}
    response = requests.get(URL, headers=headers)
    if response.status_code == 404:
        return 0
    data = response.json().get('data')
    subs = data.get('subscribers')
    return subs
