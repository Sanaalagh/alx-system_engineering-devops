#!/usr/bin/python3
"""
Recursive function to count and sort keywords in the titles of hot articles from a subreddit.
"""
import requests


def count_words(subreddit, word_list, after='', counts={}):
    """
    Queries the Reddit API, counts occurrences of keywords in hot articles' titles.
    """
    headers = {'User-Agent': 'Python:api_advanced:v1 (by /u/yourusername)'}
    url = (
        f"https://www.reddit.com/r/{subreddit}/hot.json?limit=100&after={after}"
    )
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code != 200:
        if counts:
            print_sorted_counts(counts)
        return

    data = response.json().get('data', {})
    for post in data.get('children', []):
        title = post['data']['title'].lower()
        for word in word_list:
            word_lower = word.lower()
            # Count occurrences of word in title
            counts[word_lower] = counts.get(word_lower, 0) + title.count(word_lower)

    after = data.get('after', None)
    if after is not None:
        count_words(subreddit, word_list, after, counts)
    elif counts:
        print_sorted_counts(counts)


def print_sorted_counts(counts):
    """
    Prints the counts of words sorted by frequency and alphabetically.
    """
    sorted_counts = sorted(
        ((key, value) for key, value in counts.items() if value > 0),
        key=lambda x: (-x[1], x[0])
    )
    for word, count in sorted_counts:
        print(f"{word}: {count}")


if __name__ == "__main__":
    import sys
    if len(sys.argv) < 3:
        print("Usage: {} <subreddit> <list of keywords>".format(sys.argv[0]))
        print("Ex: {} programming 'python java javascript'".format(sys.argv[0]))
    else:
        result = count_words(sys.argv[1], [x for x in sys.argv[2].split()])
