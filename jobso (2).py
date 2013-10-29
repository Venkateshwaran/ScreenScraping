from string import punctuation, whitespace
import urllib2
import datetime
import re
from bs4 import BeautifulSoup 

today = datetime.date.today()
html = urllib2.urlopen("http://finance.yahoo.com/q/is?s=IBM+Income+Statement&annual" ).read()

soup = BeautifulSoup(html)
table = soup.find("table", attrs={'class':'yfnc_tabledata1'})
rows = table.findAll('tr')

for row in rows:
    cols = row.findAll('td')
    i=0
    for col in cols:
        i+=1
        print col.string
        print "________________________", i