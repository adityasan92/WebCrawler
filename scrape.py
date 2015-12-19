import urllib
import re

htmltext= urllib.urlopen("https://www.google.ca/finance/getprices?q=AAPL&x=NASD&i=120&p=25m&f=c&df=cpct&auto=1&ts=1450510581558&ei=wQh1Vrm9HdeVjAGc56nwBg").read()

print htmltext.split()[len(htmltext.split()) -1]
#regex = '<span id="ref_[^.]*_l">(.+?)</span>'
#pattern = re.compile(regex)

#results = re.findall(pattern,htmltext)

#print results
