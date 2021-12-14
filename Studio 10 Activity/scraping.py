## There are three TODOs for this file
## TODO-1: install 'bs4' package using pip
## TODO-2: Show the scraped text
## TODO-3: Grab all the "li" tags then print them out one "li" item per line


import requests

## TODO-1: install 'bs4' package using pip
from bs4 import BeautifulSoup


# store the webpage url to scrape
url = "http://dsc.ucsd.edu/node/10" 


r = requests.get(url)    
urlText = r.text


# Print the first 10000 characters of the webpage
## TODO-1: compare whether urlText is identical to the source code of the url
Nchars = 10000
print(urlText[:Nchars]) 
print("\n\n... " + str(len(urlText)-Nchars) + " additional characters")


soup = BeautifulSoup(urlText, 'html.parser')


## TODO-2: Show the scraped text
## hint) search get_text() on the beautifulsoup documentation
##       https://beautiful-soup-4.readthedocs.io/en/latest/


print(soup.get_text())



## TODO-3: Grab all the "li" tags then print them out one "li" item per line
## hint1) search find_all() on the beautifulsoup documentation. 
## hint2) you would want to use for loop to print one "li" item at a time

for link in soup.find_all("li"):
    print(link)


# optional TODO: get_text() is still not quite readable.  You can use soup.stripped_strings
#for string in soup.stripped_strings:
#    print(string)