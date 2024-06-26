#!/usr/bin/python3
"""This script contains function that queries the Reddit API"""

import requests

def number_of_subscribers(subreddit):
    """Returns the number of total subscribers
    for a given subreddit"""

    response = requests.get(
            "https://www.reddit.com/r/{}/about.json".format(subreddit),
            headers={"User-Agent": "Mozilla/5.0"},
            )

    if response.status_code == 200:
        data = response.json()
        total_subscribers = data['data']['subscribers']
        return total_subscribers
    else:
        return 0
