"""Module to send top news as desktop notification"""

####################################################################################
# Note: This code is tested from home laptop.
# It may need additional changes if the machine on which this code is executed is
# connected to VPN or behind a proxy server.
####################################################################################

# Import modules.

import requests  # First install requests using pip.
import xml.etree.ElementTree as ET

# Initiate variables with global scope.

# RSS Feeds are an easy way to stay up to date with your favorite websites,
# such as blogs or online magazines. If a site offers an RSS feed, you get
# notified whenever a post goes up, and then you can read a summary or the whole post.

# RSS is a web feed that allows users and applications to access updates to
# websites in a standardized, computer-readable format.

# RSS: Really Simple Syndication.

# RSS: RSS(Rich Site Summary, often called Really Simple Syndication) uses a family of
# standard web feed formats to publish frequently updated informationlike blog entries,
# news headlines, audio, video. RSS is XML formatted plain text.

#RSS_FEED_URL = "http://www.hindustantimes.com/rss/topnews/rssfeed.xml"  # Old URL
#RSS_FEED_URL = "https://www.hindustantimes.com/feeds/rss/top-news/rssfeed.xml"  # This didn't give any headline. So, we switched to science RSS feed as below.
RSS_FEED_URL = "https://www.hindustantimes.com/feeds/rss/science/rssfeed.xml"

# Define functions.

def parse_XML(xml_data):
    """Function to parse XML format data received from RSS feed"""


def load_RSS_feed():
    """Function to load RSS feed"""
    #url1 = "https://api.github.com/users/inderpal2406"
    #url2 = "https://www.google.com"
    # Above both URLs work without requirement for any verify and headers parameters in requests.get()
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0'}
    #headers = {"User-Agent":"Mozilla/5.0"}  # It may work with just this much header as well.
    #response = requests.get(RSS_FEED_URL,headers=headers)  # It works with this without need of verify argument.
    # headers is a dict var. This var can be named anything.
    # headers for API requests can be passed as a dictionary in request module of python.
    # key is such a dict is the header type and value is the value for the header type.
    # A good article on understanding headers and query parameters:
    # https://www.torocloud.com/blog/using-query-parameters-and-headers-in-rest-api-design
    #######################################################################################
    # But we try to supply SSL certificates as well in the request. To supply same, we follow below procedure.
    # Got to target website in browser, export complete chain of SSL certificates in Base64
    # encoded pem file. Supply this file in verify argument of the request. Downloading only one
    # certificate in the chain, in base64 encoded pem file, won't work. Complete chain is needed.
    # When we export after viewing the cert in chrome browser, it gives option to save complete
    # chain of certs in base64 format of .pem file. Select that option.
    # Otherwise we need to export each certificate separately and then combine them into one 
    # pem file as shown on website: https://levelup.gitconnected.com/solve-the-dreadful-certificate-issues-in-python-requests-module-2020d922c72f
    cert_path = ".\\www-hindustantimes-com-chain.pem"  # This pem file can be named as anything.
    response = requests.get(RSS_FEED_URL,headers=headers,verify=cert_path)
    #print(response.status_code)
    #print(response.text)
    #print(response.content)  # content is in bytes.
    ######################################################################################
    # Write response.content to a file.
    filename = ".\\topnewsfeed.xml"
    file_object = open(filename,"wb")
    file_object.write(response.content)
    file_object.close()
    #return response.content  # Needs to be uncommented at the end.
    filename2 = ".\\testdata.xml"
    tree = ET.parse(filename2)
    root = tree.getroot()
    print(root.tag, root.attrib)
    for child in root:
        print(child.tag, child.attrib)

def main():
    """First function to be called"""
    rss_data = load_RSS_feed()
    # For XML parsing:
    # https://www.geeksforgeeks.org/xml-parsing-python/
    #newsitems = parse_XML(rss_data)

# Call main() when the script is executed.

if __name__ == "__main__":
    main()
