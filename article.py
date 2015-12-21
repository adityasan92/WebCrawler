import nltk
import urllib
from bs4 import BeautifulSoup
from readability.readability import Document
import mechanize

url="http://www.firstpost.com/world/bernie-sanders-apologises-to-hillary-clinton-for-data-breach-in-us-campaign-2552954.html"

br = mechanize.Browser()
br.set_handle_robots(False)
br.addheaders = [('User-agent', 'Firefox')]

html = br.open(url).read()
readable_article = Document(html).summary()
readable_title = Document(html).short_title()

soup = BeautifulSoup(readable_article,"lxml")

final_article = soup.text

links = soup.findAll('img', src=True)

print final_article.encode("cp437", "ignore")
