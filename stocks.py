import urllib
import re

symbolfile = open("symbols.txt")

symbolslist = filter(None, symbolfile.read().split("\n"))

print symbolslist

i=0

while i<len(symbolslist):
    url = "https://ca.finance.yahoo.com/q?s=" + symbolslist[i]
    htmlfile = urllib.urlopen(url)
    htmltext = htmlfile.read()
    regex = '<span id="yfs_l84_[^.]*">(.+?)</span>'
    pattern = re.compile(regex)
    price = re.findall(pattern,htmltext)
    print "the price of", symbolslist[i], " is ", price
    i = i +1
