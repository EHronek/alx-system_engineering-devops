#!/usr/bin/python3
'''function top_ten returns top ten posts for a given subreddit'''
import requests
import sys


def top_ten(subreddit):
    ''' functionm to return the top ten posts for a given subreddit'''
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {'User-Agent': 'MyBot/0.0.1'}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            data = response.json()
            posts = data['data']['children']
            for post in posts:
                print(post['data']['title'])
        else:
            print(None)
    except requests.RequestException:
        print(None)
