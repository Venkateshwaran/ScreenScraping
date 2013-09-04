from bs4 import BeautifulSoup
import urllib2
url="http://www.99acres.com/property-in-velachery-chennai-south-ffid?"
page=urllib2.urlopen(url)
soup = BeautifulSoup(page.read())
properties=soup.findAll('a',{'class':'f15'})
for eachproperty in properties:
 print eachproperty['href'], eachproperty.string
