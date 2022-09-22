#!/usr/bin/python3
"""
Task 2 - 0x16. API advanced
"""

import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    Recursive function that queries the Reddit API and
    returns a list containing the titles of all hot articles
    for a given subreddit. If no results are found for
    the given subreddit, the function should return None.
    """

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)\
    AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'}
    params = {'after': after}
    response = requests.get(url, headers=headers,
                            params=params, allow_redirects=False)
    if response.status_code == 200:
        posts = response.json().get('data').get('children')
        for post in posts:
            hot_list.append(post.get('data').get('children'))
        after = response.json().get('data').get('after')
        if after is None:
            return (hot_list)
        else:
            return (recurse(subreddit, hot_list, after))
    else:
        return (None)