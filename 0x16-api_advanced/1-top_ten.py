#!/usr/bin/python3
"""Module containing the function to fetch top 10 hot posts from a given subreddit."""

import requests
import sys


def top_ten(subreddit):
    """
    Prints the titles of the first 10 hot posts from a given subreddit.
    If the subreddit is invalid, prints None.
    """
    # Define the custom User-Agent for Reddit API compliance
    user_agent = {'User-Agent': 'Python/Reddit:TopTen:v1.0 (by /u/yourusername)'}

    try:
        # Send the request to fetch the top 10 hot posts for the given subreddit
        response = requests.get(
            f'https://www.reddit.com/r/{subreddit}/hot.json?limit=10',
            headers=user_agent,
            allow_redirects=False,
        )

        # Check if the request was successful
        if response.status_code != 200:
            print(None)  # Invalid subreddit or other issue
            return

        # Extract the data and ensure it's in the expected format
        data = response.json()
        if 'data' in data and 'children' in data['data']:
            # Print the titles of the first 10 hot posts
            for post in data['data']['children']:
                print(post['data']['title'])
        else:
            print(None)  # If the data structure is not as expected

    except requests.RequestException:
        # If there's a network error or other issues, print None
        print(None)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        top_ten(sys.argv[1])
    else:
        print("Usage: {} <subreddit>".format(sys.argv[0]))

