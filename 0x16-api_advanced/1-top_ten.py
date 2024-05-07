#!/usr/bin/python3
"""Fetches the titles of the first 10 hot posts from a given subreddit."""

import requests


def top_ten(subreddit):
    """Prints the titles of the first 10 hot posts for a given subreddit."""
    # Define the URL with a limit of 10 hot posts
    url = 'https://www.reddit.com/r/{}/hot.json?limit=10'.format(subreddit)

    # Custom User-Agent to comply with Reddit API policies
    user_agent = 'Python/Reddit:TopTen:v1.0 (by /u/yourusername)'

    try:
        # Send the GET request to Reddit
        response = requests.get(url, headers={'User-Agent': user_agent}, allow_redirects=False)

        if response.status_code == 200:
            # If the response is successful, get the data
            data = response.json()
            # Iterate through the top 10 hot posts and print their titles
            for post in data['data']['children']:
                print(post['data']['title'])
        else:
            # If the response is not 200, it likely means the subreddit doesn't exist
            print(None)

    except requests.RequestException:
        # If there's a network error or other issues, print None
        print(None)

