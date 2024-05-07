#!/usr/bin/python3
"""Queries the Reddit API to return the number of subscribers for a given subreddit."""

import requests


def number_of_subscribers(subreddit):
    """
    Returns the number of subscribers for the given subreddit.
    If the subreddit is invalid, returns 0.
    """
    # Reddit API endpoint for subreddit information
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)

    # Custom User-Agent to avoid "Too Many Requests" and comply with Reddit API policies
    user_agent = 'Python/Reddit:SubCount:v1.0 (by /u/yourusername)'
    
    try:
        # Send a GET request to fetch the subreddit information
        response = requests.get(url, headers={'User-Agent': user_agent}, allow_redirects=False)
        
        if response.status_code == 200:
            # If successful, return the number of subscribers
            return response.json()['data']['subscribers']
        else:
            # If not successful (e.g., subreddit does not exist), return 0
            return 0
    except requests.RequestException:
        # If there's a network issue or other request-related error, return 0
        return 0

