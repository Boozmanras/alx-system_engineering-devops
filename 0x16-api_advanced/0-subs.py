#!/usr/bin/python3
"""
This module defines a function to query the Reddit API.
"""

from requests import get


def number_of_subscribers(subreddit):
    """
    Queries the Reddit API to retrieve the total number of subscribers
    for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit to query.

    Returns:
        int: The number of subscribers for the subreddit, or 0 if
             the subreddit is invalid or the request fails.
    """
    if subreddit is None or not isinstance(subreddit, str):
        return 0

    user_agent = {'User-agent': 'Google Chrome Version 81.0.4044.129'}
    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    
    response = get(url, headers=user_agent)

    try:
        all_data = response.json()
        return all_data.get('data', {}).get('subscribers', 0)
    except Exception:
        return 0
