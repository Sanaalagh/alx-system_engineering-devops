#!/usr/bin/python3
"""
Module to fetch the titles of the top ten hot posts for a given subreddit.
"""
import requests


def top_ten(subreddit):
    """
    Prints the titles of the top ten hot posts for a given subreddit.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {'User-Agent': 'Python:api_advanced:v1 (by /u/yourusername)'}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        posts = response.json().get('data', {}).get('children', [])
        for post in posts:
            print(post['data']['title'])
    else:
        print(None)


if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        top_ten(sys.argv[1])
