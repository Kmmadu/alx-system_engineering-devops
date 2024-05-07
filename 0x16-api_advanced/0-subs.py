#!/usr/bin/python3
"""Module to query and return the number of subscribers for a given Reddit subreddit."""

import requests


def number_of_subscribers(subreddit):
    """Return the total number of subscribers on a given subreddit."""
    # Set a custom User-Agent for compliance with Reddit API policies
    headers = {"User-Agent": "Python/Reddit:Subs:v1.0 (by /u/yourusername)"}
    
    # Endpoint to get subreddit information
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    
    try:
        # Fetch data from the Reddit API
        response = requests.get(url, headers=headers, allow_redirects=False)
        
        if response.status_code == 200:
            # If successful, extract the number of subscribers
            data = response.json()
            return data['data'].get('subscribers', 0)  # Return 0 if key doesn't exist
        else:
            # If the status code is not 200, return 0
            return 0

    except requests.RequestException:
        # Handle network errors or other request-related issues
        return 0  # If there's an error, return 0

