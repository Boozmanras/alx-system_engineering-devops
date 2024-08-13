#!/usr/bin/python3
import requests

def recurse(subreddit, hot_list=[], after=None):
    """Returns a list of titles of all hot posts for a given subreddit."""
    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    headers = {'User-Agent': 'Mozilla/5.0'}
    params = {'after': after}
    response = requests.get(url, headers=headers, params=params, allow_redirects=False)
    if response.status_code == 200:
        data = response.json().get('data', {})
        after = data.get('after', None)
        hot_list.extend([post.get('data', {}).get('title') for post in data.get('children', [])])
        if after is not None:
            return recurse(subreddit, hot_list, after)
        return hot_list
    return None

