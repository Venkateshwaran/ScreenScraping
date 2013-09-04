from bs4 import BeautifulSoup
import urllib2
import re
url="http://www.99acres.com/property-in-velachery-chennai-south-ffid?"
page=urllib2.urlopen(url)
soup = BeautifulSoup(page.read())
properties = soup.findAll('a', title=re.compile('Bedroom'))
for eachproperty in properties:
 print eachproperty['href']+",", eachproperty.string
