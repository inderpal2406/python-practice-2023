"""Module to send top news as desktop notification"""

# Import modules.

import requests  # First install requests using pip.

# Initiate variables with global scope.

# RSS Feeds are an easy way to stay up to date with your favorite websites,
# such as blogs or online magazines. If a site offers an RSS feed, you get
# notified whenever a post goes up, and then you can read a summary or the whole post.

# RSS is a web feed that allows users and applications to access updates to
# websites in a standardized, computer-readable format.

# RSS: Really Simple Syndication.

RSS_FEED_URL = "http://www.hindustantimes.com/rss/topnews/rssfeed.xml"

new_uel = "https://www.hindustantimes.com/feeds/rss/top-news/rssfeed.xml"

# Define functions.

def load_RSS_feed():
    """Function to load RSS feed"""


def main():
    """First function to be called"""
    load_RSS_feed()
