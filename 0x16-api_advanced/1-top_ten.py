#!/usr/bin/python3
"""
Module to interact with the Reddit API to get top ten hot posts of a subreddit.
"""
import requests

def top_ten(subreddit):
    """ Prints the titles of the top 10 hot posts for a given subreddit. """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {'User-Agent': 'Python:top_ten_posts:v1.0 (by /u/yourusername)'}

    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code != 200:
        print("None")
        return

    data = response.json()
    posts = data.get("data", {}).get("children", [])
    if posts:
        for post in posts:
            print(post['data']['title'])
    else:
        print("None")

if __name__ == "__main__":
    # This part can be in your 1-main.py, here for demonstration:
    import sys
    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        top_ten(sys.argv[1])
