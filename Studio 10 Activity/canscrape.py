## There are two TODOs for this file
## TODO-1: install 'urllib' and 'requests' packages using pip 
## TODO-2: find one more webpage that allows you to automatically scrape the data



# TODO-1: install 'urllib' and 'requests' packages
#         use pip on terminal (Mac) or command prompt (Windows)
from urllib.parse import urlparse
import urllib.robotparser

import requests


# canFetch()
# this method checks the robots.txt file of the webpage
# robots.txt file informs whether we can automatically scrape the given page
# returns "true" if we are allowed to automatically-scrape the url
def canFetch(url):

    parsed_uri = urlparse(url)
    domain = '{uri.scheme}://{uri.netloc}/'.format(uri=parsed_uri)

    rp = urllib.robotparser.RobotFileParser()
    rp.set_url(domain + "/robots.txt")
    try:
        rp.read()
        canFetchBool = rp.can_fetch("*", url)
    except:
        canFetchBool = None
    
    return canFetchBool



# store the webpage url to scrape
url = "http://dsc.ucsd.edu/node/10" 

# check whether we are automatically allowed to scrape the page, by calling canFetch()
print (canFetch(url))


# TODO-2: find one more webpage that allows you to automatically scrape the data
myurl = ""
print (canFetch(myurl))



