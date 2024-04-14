#!/usr/bin/python3
"""Titles of the first 10 hot posts listed in a subreddit"""
from requests import get


def top_ten(subreddit):
    """Queries Reddit API and prints the titles of the first 10 hot posts in a subreddit."""
    if not subreddit or not isinstance(subreddit, str):
        print('Invalid subreddit')
        return

    api_url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    user_agent = {'User-agent': 'my-app/0.0.1'}
    params = {'limit': 10}

    response = get(api_url, headers=user_agent,
                   params=params, allow_redirects=False)
    if response.status_code != 200:
        print(f"Failed to get data: status code {response.status_code}")
        return

    try:
        results = response.json()
        data = results['data']['children']
        for post in data:
            print(post['data']['title'])
    except Exception as e:
        print(f"Error parsing JSON: {e}")
