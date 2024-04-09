#!/usr/bin/python3
""" number of subscribers for a given subreddit"""
import requests


def number_of_subscribers(subreddit):
    """queries the Reddit API and returns number of subscribers"""
    if subreddit is None or not isinstance(subreddit, str):
        return 0

    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    headers = {'User-Agent': 'subreddit_subscriber_counter/0.1'}

    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200 and 'data' in response.json() and 'subscribers' in response.json()['data']:
            return response.json()['data']['subscribers']
        else:
            return 0
    except Exception as e:
        print(f"An error occurred: {e}")
        return 0
