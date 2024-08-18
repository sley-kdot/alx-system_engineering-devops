#!/usr/bin/python3
"""
a function that queries an API endpoint
"""
import requests
from sys import argv


def top_ten(subreddit):
    subreddit = argv[1]
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    params = {"limit": 10}
    res = requests.get(url, params=params)
    if res.status_code == 200:
        data = res.json()
        var = []
        for k, v in data.items():
            if k == "data":
                var = v["children"]
                for i in range(len(var)):
                    print(var[i]["data"].get("title"))
    else:
        print(None)
