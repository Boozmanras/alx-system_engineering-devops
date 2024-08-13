# 0x16. API Advanced

This project involves querying the Reddit API to retrieve various information about subreddits. Below are the tasks completed:

1. **How many subs?**
   - Function: `number_of_subscribers(subreddit)`
   - Queries the Reddit API and returns the number of subscribers for a given subreddit. Returns `0` if the subreddit is invalid.

2. **Top Ten**
   - Function: `top_ten(subreddit)`
   - Queries the Reddit API and prints the titles of the first 10 hot posts listed for a given subreddit. Prints `None` if the subreddit is invalid.

3. **Recurse it!**
   - Function: `recurse(subreddit, hot_list=[])`
   - A recursive function that queries the Reddit API and returns a list containing the titles of all hot articles for a given subreddit. Returns `None` if the subreddit is invalid.

4. **Count it!**
   - Function: `count_words(subreddit, word_list)`
   - A recursive function that queries the Reddit API, parses the titles of all hot articles, and prints a sorted count of given keywords (case-insensitive).

Each task follows strict coding standards, including the use of the Requests module, PEP 8 style guide, and proper handling of HTTP requests and responses.

