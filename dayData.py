import urllib
import re
import json

symbolfile = open("symbols.txt").read()
symbolslist = filter(None, symbolfile.split("\n"))

#stock price for the symbols in the symbol list every 5 min in a day in bloomberg
for symbol in symbolslist:
    filename = "data/" + symbol +".txt"
    myfile = open(filename,"w+")
    myfile.close()

    htmlfile = urllib.urlopen("http://www.bloomberg.com/markets/api/bulk-time-series/price/" + symbol + "%3AUS?timeFrame=1_DAY")
    data = json.load(htmlfile)
    dataPoints = data[0]["price"]

    # append in the file using "a"
    myfile = open(filename,"a")

    for point in dataPoints:
        myfile.write(str(symbol+","+str(point["dateTime"])+","+str(point["value"])+"\n"))
    myfile.close
