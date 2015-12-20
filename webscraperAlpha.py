import urllib
from bs4 import BeautifulSoup
import urlparse
import mechanize

url="http://www.twitch.tv/"
print urlparse.urlparse(url).hostname
br = mechanize.Browser()
urls = [url]
visited = [url]

while len(urls)>0:
    try:
        br.open(urls[0])
        #visited.append(urls[0])
        urls.pop(0)
        for link in br.links():
            newurl = urlparse.urljoin(link.base_url,link.url)
            hostname = urlparse.urlparse(newurl).hostname
            path = urlparse.urlparse(newurl).path
            newurl = "https://"+str(hostname) + str(path)
            #print newurl

            if newurl not in visited and urlparse.urlparse(url).hostname in newurl:
                visited.append(newurl)
                urls.append(newurl)
                print newurl
    except:
        print "error"
        urls.pop(0)

print visited
