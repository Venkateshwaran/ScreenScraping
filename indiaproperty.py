from bs4 import BeautifulSoup
import urllib2
import requests
start_url = requests.get('http://www.indiaproperty.com/chennai-property-search-allresidential-properties-for-sale-in-velachery-results')
soup = BeautifulSoup(start_url.content)
properties = soup.findAll('a',{'class':'paddl10'})
for eachproperty in properties:
 print re.findall("'([a-zA-Z0-9,\s]*)'", eachproperty['onclick'])