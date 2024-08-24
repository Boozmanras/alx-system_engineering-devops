#!/usr/bin/python3
"""
This module defines a function to query the Reddit API and print the titles
of the top 10 hot posts in a given subreddit.
"""

from requests import get


def top_ten(subreddit):
    """
    Queries the Reddit API to retrieve and print the titles of the first
    10 hot posts listed for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit to query.

    Returns:
        None: If the subreddit is invalid or if
        the request fails, it prints 'None'.
    """
    if subreddit is None or not isinstance(subreddit, str):
        print("None")
        return

    # Set a custom User-Agent to avoid request blocking by Reddit
    user_agent = {'User-agent': 'Google Chrome Version 81.0.4044.129'}
    params = {'limit': 10}
    url = f'https://www.reddit.com/r/{subreddit}/hot/.json'

    # Perform the GET request to Reddit API
    response = get(url, headers=user_agent, params=params)

    try:
        # Parse the JSON response to retrieve post titles
        all_data = response.json()
        posts = all_data.get('data', {}).get('children', [])

        for post in posts:
            title = post.get('data', {}).get('title', "None")
            print(title)

    except Exception:
        print("None")
