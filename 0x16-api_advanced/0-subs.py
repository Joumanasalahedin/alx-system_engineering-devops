#!/usr/bin/python3
""" number of subscribers for a given subreddit"""
import requests


def number_of_subscribers(subreddit):
    """queries the Reddit API and returns number of subscribers"""
    if subreddit is None or not isinstance(subreddit, str):
        return 0

    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    headers = {'User-Agent': 'Google Chrome Version 81.0.4044.129'}

    response = requests.get(url, headers=headers)
    try:
        return response.json()['data']['subscribers']
    except Exception:
        return 0
