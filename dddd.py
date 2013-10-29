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
for eachweb in soup.findAll('div',{'id':'center_col'}):
	a = eachweb.find('a')
	alink = eachweb.find('span',{'class':'ac'})
	olink = eachweb.find('span',{'class','st'})
	print a['href'][7:] + "," , p.sub('', str(alink)[1:-1]).replace('.','\n') + "," , olink
	