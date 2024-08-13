#!/usr/bin/python3
import requests

def count_words(subreddit, word_list, hot_list=[], after="", counts={}):
    """Prints a sorted count of given keywords from all hot posts in a subreddit."""
    url = f'https://www.reddit.com/r/{subreddit}/hot.json?after={after}'
    headers = {'User-Agent': 'Custom'}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        data = response.json().get('data', {})
        after = data.get('after', None)
        hot_list.extend([post.get('data', {}).get('title') for post in data.get('children', [])])
        if after:
            return count_words(subreddit, word_list, hot_list, after, counts)
        for word in word_list:
            count = sum([title.lower().split().count(word.lower()) for title in hot_list])
            if count > 0:
                counts[word.lower()] = counts.get(word.lower(), 0) + count
        sorted_counts = sorted(counts.items(), key=lambda item: (-item[1], item[0]))
        for word, count in sorted_counts:
            print(f"{word}: {count}")
    return


