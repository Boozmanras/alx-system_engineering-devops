#!/usr/bin/python3
import requests

def count_words(subreddit, word_list, counts={}, after=None):
    """Prints a sorted count of given keywords from all hot posts in a subreddit."""
    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    headers = {'User-Agent': 'Mozilla/5.0'}
    params = {'after': after}
    response = requests.get(url, headers=headers, params=params, allow_redirects=False)
    if response.status_code == 200:
        data = response.json().get('data', {})
        after = data.get('after', None)
        titles = [post.get('data', {}).get('title').lower() for post in data.get('children', [])]
        for word in word_list:
            word_lower = word.lower()
            if word_lower in counts:
                counts[word_lower] += sum(title.split().count(word_lower) for title in titles)
            else:
                counts[word_lower] = sum(title.split().count(word_lower) for title in titles)
        if after is not None:
            return count_words(subreddit, word_list, counts, after)
        sorted_counts = sorted(counts.items(), key=lambda item: (-item[1], item[0]))
        for word, count in sorted_counts:
            if count > 0:
                print(f"{word}: {count}")
    return

