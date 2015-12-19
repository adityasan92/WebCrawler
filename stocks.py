import urllib
import re

symbolslist = ["aapl","spy","goog","nflx"]
i=0

while i<len(symbolslist):
    url = "https://ca.finance.yahoo.com/q?s=" + symbolslist[i]
    htmlfile = urllib.urlopen(url)
    htmltext = htmlfile.read()
    regex = '<span id="yfs_l84_'+ symbolslist[i] +'">(.+?)</span>'
    pattern = re.compile(regex)
    price = re.findall(pattern,htmltext)
    print "the price of", symbolslist[i], " is ", price
    i = i +1
