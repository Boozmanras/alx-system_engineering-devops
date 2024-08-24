#!/usr/bin/python3
"""Module for querying the number of subscribers for a given subreddit."""

import requests


def number_of_subscribers(subreddit):
    """
    Queries the Reddit API to retrieve the number of subscribers for a given subreddit. Args:
        subreddit (str): The name of the subreddit to query
    Returns:
        int: The number of subscribers if the subreddit exists, otherwise 0.
    """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "My-User-Agent"}

    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code >= 300:
        return 0

    return response.json().get("data", {}).get("subscribers", 0)
