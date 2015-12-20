from threading import Thread
import urllib
import re
import psycopg2

gmap = {}


def th(ur):
    base="https://ca.finance.yahoo.com/q?s=" +ur
    regex = '<span id="yfs_l84_[^.]*">(.+?)</span>'
    pattern = re.compile(regex)
    htmltext = urllib.urlopen(base).read()
    results = re.findall(pattern,htmltext)
    try:
        gmap[ur] = results[0]
    except:
        print "got an error"


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

conn_string = "host='localhost' dbname='postgres' user='postgres'"
conn = psycopg2.connect(conn_string)
cursor = conn.cursor()
print "Connected!\n"
query =""
for key in gmap.keys():
    print key,gmap[key]
    query = query + "INSERT INTO stock_data.symbols(symbol,lastprice) values (" + "'" + key+ "'," + gmap[key]+ ");"

cursor.execute(query)
conn.commit()
