#!/usr/bin/python3
"""Makes requests recursively
"""

import requests


def recurse(subreddit, hot_list=[], after=0):
    """Makes requests recursively
    """

    usr = 'Opera/9.80 (X11; Linux i686; U; ru) Presto/2.8.131 Version/11.11'
    usrAg = {'User-Agent': usr}

    # URL that is goin to be used for the request
    url = 'https://www.reddit.com/r/{}/hot.json?after={}'.format(subreddit,
                                                                 after)

    response = requests.get(url, headers=usrAg)
    json_r = response.json()

    if response.status_code == 404:
        return None
    else:
        for post in json_r['data']['children']:
            hot_list.append(post['data']['title'])
        new_after = json_r['data']['after']
        if new_after is None:
            return hot_list
        return recurse(subreddit, hot_list, new_after)
