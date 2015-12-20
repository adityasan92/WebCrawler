#Usually websites have a additional paramters attached to the end, which is session id or variables. this code deals with that so that we dont
#get stuck in that trap(infinte loop for the spider)
import urllib
import re
from bs4 import BeautifulSoup
import urlparse

htmltext = urllib.urlopen("http://www.ndtv.com")
soup = BeautifulSoup(htmltext,"html.parser")

for tag in soup.findAll('a',href=True):
    raw = tag['href']
    hostname = urlparse.urlparse(tag['href']).hostname
    path = urlparse.urlparse(tag['href']).path
    newUrl =  "http://" + str(hostname) + str(path)
    print newUrl
