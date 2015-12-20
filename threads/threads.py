from threading import Thread
import urllib
import re

def th(ur):
    base="https://ca.finance.yahoo.com/q?s=" +ur
    regex = '<span id="yfs_l84_[^.]*">(.+?)</span>'
    pattern = re.compile(regex)
    htmltext = urllib.urlopen(base).read()
    results = re.findall(pattern,htmltext)
    print results

symbolfile = open("symbols.txt").read()
symbolslist = filter(None, symbolfile.split("\n"))

print symbolslist

threadlist =[]

for u in symbolslist:
    t = Thread(target=th,args=(u,))
    t.start()
    threadlist.append(t)

for b in threadlist:
    b.join()
