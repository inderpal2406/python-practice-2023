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

new_url = "https://www.hindustantimes.com/feeds/rss/top-news/rssfeed.xml"

# Define functions.

def load_RSS_feed():
    """Function to load RSS feed"""


def main():
    """First function to be called"""
    load_RSS_feed()


# Got to target website in browser, export complete chain of SSL certificates in Base64
# encoded pem file. Supply this file in verify argument of the request. Downloading only one
# certificate in the chain, in base64 encoded pem file, won't work. Complete chain is needed.
# When we export after viewing the cert in chrome browser, it gives option to save complete
# chain of certs in base64 format of .pem file. Select that option.
# Otherwise we need to export each certificate separately and then combine them into one 
# pem file as shown on website: https://levelup.gitconnected.com/solve-the-dreadful-certificate-issues-in-python-requests-module-2020d922c72f


url1 = "https://api.github.com/users/inderpal2406"
url2 = "https://www.google.com"
# Above both URLs work without requirement for any verify and headers parameters in requests.get()


url = "https://www.hindustantimes.com/feeds/rss/top-news/rssfeed.xml"
cert_path = "C:\\Users\\isaini\\Downloads\\server.pem"  # server.pem can be named as anything.
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0'}
#headers = {"User-Agent":"Mozilla/5.0"}  # It may work with just this much header as well.

# headers is a dict var. This var can be named anything.
# headers for API requests can be passed as a dictionary in request module of python.
# key is such a dict is the header type and value is the value for the header type.
# A good article on understanding headers and query parameters:
# https://www.torocloud.com/blog/using-query-parameters-and-headers-in-rest-api-design


import requests
#response = requests.get(url)  # SSL cert related error.
#response = requests.get(url,verify=cert_path)  # Access denied error. HTTP response as 401. 
# Required headers as some websites don't response without headers parameters.
response = requests.get(url,headers=headers,verify=cert_path)
print(response.status_code)
print(response.text)
print(response.content)  # content is in bytes.

# Above code worked initially. But later started giving below error:
# Firewall Authentication. You must authenticate to use this service.
# Need to check. Maybe we need to pass auth parameter in requests.get()

