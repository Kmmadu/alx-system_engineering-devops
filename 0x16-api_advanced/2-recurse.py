#!/usr/bin/python3
"""Recursive function that queries the Reddit API to return a list of all hot post titles for a given subreddit."""

import requests


def recurse(subreddit, hot_list=None, after=None):
    """
    Recursively fetches all hot post titles from a given subreddit.

    Parameters:
    - subreddit: The subreddit to query.
    - hot_list: A list of hot post titles (default is None).
    - after: The pagination token for the next set of results (default is None).

    Returns:
    A list of hot post titles, or None if the subreddit is invalid or there's an error.
    """
    if hot_list is None:
        hot_list = []

    # Reddit API endpoint for hot posts, with pagination
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    
    # Custom User-Agent to comply with Reddit API policies
    user_agent = 'Python/Reddit:Recurse:v1.0 (by /u/yourusername)'
    
    # Set limit to 100 to reduce recursion depth
    params = {'limit': 100}
    if after:
        params['after'] = after

    try:
        # Make the GET request to the Reddit API
        response = requests.get(url, headers={'User-Agent': user_agent}, allow_redirects=False, params=params)

        if response.status_code == 200:
            # Parse the JSON data
            data = response.json()
            
            # Add the titles of the hot posts to the list
            for post in data['data']['children']:
                hot_list.append(post['data']['title'])
            
            # Get the "after" token to check if there's more data
            after = data['data']['after']
            
            if after:
                # Recursively call if there's another page
                return recurse(subreddit, hot_list, after)
            else:
                # No more data, return the list of titles
                return hot_list
        else:
            # If the subreddit is invalid or there's another error, return None
            return None

    except requests.RequestException:
        # Handle network errors or other request-related exceptions
        return None

