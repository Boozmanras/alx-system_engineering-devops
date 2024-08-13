#!/usr/bin/python3
import requests

def recurse(subreddit, hot_list=[], after=""):
    """Returns a list of titles of all hot posts for a given subreddit."""
    url = f'https://www.reddit.com/r/{subreddit}/hot.json?after={after}'
    headers = {'User-Agent': 'Custom'}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        data = response.json().get('data', {})
        after = data.get('after', None)
        hot_list.extend([post.get('data', {}).get('title') for post in data.get('children', [])])
        if after:
            return recurse(subreddit, hot_list, after)
        return hot_list
    return None

