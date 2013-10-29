from bs4 import BeautifulSoup
from string import punctuation, whitespace
import urllib2
import datetime
import re
url="http://www.99acres.com/property-in-velachery-chennai-south-ffid?"
page=urllib2.urlopen(url)
soup = BeautifulSoup(page.read())
pdate = soup.findAll('i', {'class':'pdate'})
for eachdate in pdate:
 print re.sub('(\s{2,})', ' ', eachdate.text)
