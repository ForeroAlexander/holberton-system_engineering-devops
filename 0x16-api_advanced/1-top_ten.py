#!/usr/bin/python3
""" Function To Ten post file
"""

import requests


def top_ten(subreddit):
    """Write a function that queries the Reddit API and prints
        the titles of the first 10 hot posts listed for a given subreddit."""
    url = "https://www.reddit.com/r/{}/hot.json?limit=10"
    headers = {'User-Agent': 'URL'}
    response = requests.get(url.format(subreddit), headers=headers)
    if response.status_code == 404:
        print("None")
    else:
        post = response.json().get('data')
        children = post.get('children')
        for posts in children:
            print(posts.get('data').get('title'))
