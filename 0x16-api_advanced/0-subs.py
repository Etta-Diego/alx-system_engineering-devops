#!/usr/bin/python3
import requests
"""This script contains function that queries the Reddit API"""

def number_of_subscribers(subreddit):
    """Returns the number of total subscribers for a given subreddit"""

    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    header = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=header, allow_redirects=False)
    if response.status_code == 200:
        data = response.json()
        total_subscribers = data['data']['subscribers']
        return total_subscribers
    else:
        return 0
