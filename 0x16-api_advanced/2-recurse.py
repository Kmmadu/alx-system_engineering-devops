#!/usr/bin/python3
"""Contains recursive function to fetch all hot post titles from a given subreddit."""
import requests


def recurse(subreddit, hot_list=None, after="", count=0):
    """Returns a list of titles of all hot posts for a given subreddit."""
    if hot_list is None:
        hot_list = []  # Initialize hot_list if it's None

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {
        "User-Agent": "0x16-api_advanced:project:v1.0.0 (by /u/firdaus_cartoon_jr)"
    }
    params = {
        "after": after,
        "count": count,
        "limit": 100
    }
    try:
        response = requests.get(url, headers=headers, params=params, allow_redirects=False)

        if response.status_code != 200:
            # If the status code indicates an error, return None
            return None

        results = response.json().get("data")
        after = results.get("after")
        count += results.get("dist")

        # Add the titles of hot posts to hot_list
        for child in results.get("children"):
            hot_list.append(child.get("data").get("title"))

        if after:
            # If there's more data, recursively call the function with the new "after"
            return recurse(subreddit, hot_list, after, count)

        # If there's no more data, return the list of hot post titles
        return hot_list

    except requests.RequestException:
        # If there's a network error or other request-related error, return None
        return None

