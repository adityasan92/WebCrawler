import urllib
from bs4 import BeautifulSoup
import urlparse
import mechanize

# replicating a browser
br = mechanize.Browser()
url="http://www.ndtv.com"

br.open(url)

for link in br.links():
    newurl = urlparse.urljoin(link.base_url,link.url)
    hostname = urlparse.urlparse(newurl).hostname
    path = urlparse.urlparse(newurl).path
    newurl = "http://"+str(hostname) + str(path)
    print newurl
