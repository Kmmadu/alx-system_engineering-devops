#!/usr/bin/python3
"""Recursive function that queries the Reddit API and counts keyword occurrences in hot articles."""

import requests


def count_words(subreddit, word_list, after=None, word_dict=None):
    """
    Recursively fetches all hot post titles from a given subreddit and counts keyword occurrences.

    Parameters:
    - subreddit: The subreddit to query.
    - word_list: List of keywords to count.
    - after: The pagination token for the next set of results (default is None).
    - word_dict: Dictionary to count keyword occurrences (default is None).

    Returns:
    If `after` is `None`, it prints the sorted keyword counts. Otherwise, it recurses to the next page.
    """
    if word_dict is None:
        # Initialize word_dict if not already initialized
        word_dict = {word.lower(): 0 for word in word_list}

    if after is None:
        # Sort the dictionary by count (descending), then alphabetically
        sorted_words = sorted(word_dict.items(), key=lambda x: (-x[1], x[0]))
        # Print words with counts greater than zero
        for word, count in sorted_words:
            if count > 0:
                print(f"{word}: {count}")
        return  # Return at the end of recursion
    
    # Define the Reddit API endpoint with pagination
    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    user_agent = 'Python/Reddit:CountWords:v1.0 (by /u/yourusername)'
    params = {'limit': 100, 'after': after}

    try:
        # Send the GET request to fetch hot posts with pagination
        response = requests.get(url, headers={'User-Agent': user_agent}, allow_redirects=False, params=params)

        if response.status_code != 200:
            # If the subreddit is invalid or there's another error, return
            return
        
        # Parse the hot posts
        hot = response.json()['data']['children']
        next_after = response.json()['data']['after']

        # Count keyword occurrences in the title of each post
        for post in hot:
            title = post['data']['title'].lower()
            words = title.split()
            for keyword in word_dict:
                word_dict[keyword] += words.count(keyword)

        # Recursively call the function with the new "after" token
        count_words(subreddit, word_list, next_after, word_dict)

    except requests.RequestException:
        # Handle network errors or other issues
        return  # Exit if there's a request-related error

