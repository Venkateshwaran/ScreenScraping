from bs4 import BeautifulSoup
import urllib2
import requests
import re
start_url = requests.get('http://www.indiaproperty.com/chennai-property-search-allresidential-properties-for-sale-in-velachery-results')
soup = BeautifulSoup(start_url.content)
#properties = soup.findAll('a',{'class':'paddl10'})
properties = soup.findAll('a',{c for a in soup.find_all('a') for c in a.attrs.get('class', [])} )
for eachproperty in properties:
 print eachproperty['href']

