from bs4 import BeautifulSoup
import urllib2
url="http://www.indiaproperty.com/chennai-property-search-allresidential-properties-for-sale-in-velachery-results"
page=urllib2.urlopen(url)
soup = BeautifulSoup(page.read())
properties = soup.findAll('a',{'class':'paddl10'})
for eachproperty in properties:
    print eachproperty['href']