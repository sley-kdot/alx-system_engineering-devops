#!/usr/bin/python3
"""
a function that queries an API endpoint
"""
import requests
from sys import argv


def number_of_subscribers(subreddit):
    subreddit = argv[1]
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    res = requests.get(url)
    if res.status_code == 200:
        data = res.json()
        result = data["data"].get("subscribers")
        return result
    else:
        return 0
