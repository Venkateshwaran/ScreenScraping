from string import punctuation, whitespace
import urllib2
import datetime
import re
from bs4 import BeautifulSoup as Soup
import csv
today = datetime.date.today()
html = urllib2.urlopen("http://192.168.1.200/coimbatore/3BHK_flats_inCoimbatore.html_%94201308110608%94.html").read()

soup = Soup(html)
p = re.compile(r'<.*?>')
aslink = soup.findAll('span',attrs={'class':'ac'})
for li in soup.findAll('li', attrs={'class':'g'}):
    sLink = li.find('a')
    sSpan = li.find('span', attrs={'class':'st'})
    print sLink['href'][7:] , "," + p.sub('', str(sSpan)).replace('.','')
for adli in soup.findAll('div',attrs={'id':'rhs_block'}):
	adlink = adli.find('a')
	print adlink['href']
print p.sub('', str(aslink)[1:-1]).replace('.','\n')


#for ads in soup.findAll('div',{'id':'tads'}):

 
