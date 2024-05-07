#!/usr/bin/python3
"""
Module to fetch the number of subscribers for a given subreddit.
"""
import requests


def number_of_subscribers(subreddit):
    """
    Returns the number of subscribers for a given subreddit.
    """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {'User-Agent': 'Python:api_advanced:v1 (by /u/yourusername)'}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        return response.json().get('data', {}).get('subscribers', 0)
    else:
        return 0


if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        print("{:d}".format(number_of_subscribers(sys.argv[1])))
