from bs4 import BeautifulSoup
from string import punctuation, whitespace
import urllib2
import datetime
import re
import MySQLdb
today = datetime.date.today()
url="http://www.99acres.com/property-in-velachery-chennai-south-ffid?"
page=urllib2.urlopen(url)
soup = BeautifulSoup(page.read())
properties = soup.findAll('span',{'class':'blk'})[0].
for eachproperty in properties:

