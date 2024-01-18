#!/usr/bin/python3
"""number of subscribers for a given subreddit"""
from requests import get


def number_of_subscribers(subreddit):
    """Queries Reddit API and returns the
    number of subscribers for subreddit"""

    if subreddit is None or not isinstance(subreddit, str):
        return 0

    api_url = f"https://www.reddit.com/r/{subreddit}/about.json"
    user_agent = {'User-agent': 'Google Chrome Version 81.0.4044.129'}

    response = get(api_url, headers=user_agent, allow_redirects=False)
    if response.status_code != 200:
        return 0

    results = response.json()
    try:
        return results['data']['subscribers']

    except Exception:
        return 0
