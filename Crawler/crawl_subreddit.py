#! /usr/bin/python3

import praw


reddit = praw.Reddit('crawler')


for submission in reddit.subreddit('all').hot(limit=10):
    print(submission.title)
