#!/usr/bin/python3
"""
Recursive module to fetch all titles of hot articles for a given subreddit.
"""
import requests


def recurse(subreddit, hot_list=[], after=""):
    """
    Recursively fetches all titles of hot articles for a given subreddit.
    """
    headers = {'User-Agent': 'Python:api_advanced:v1 (by /u/yourusername)'}
    url = (
        f"https://www.reddit.com/r/{subreddit}/hot.json?"
        f"limit=100&after={after}"
    )
    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        return None

    data = response.json().get('data', {})
    hot_list.extend(
        [post['data']['title'] for post in data.get('children', [])]
    )
    after = data.get('after', None)

    if after is not None:
        return recurse(subreddit, hot_list, after)
    else:
        return hot_list


if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        result = recurse(sys.argv[1])
        if result is not None:
            print(len(result))
        else:
            print("None")
