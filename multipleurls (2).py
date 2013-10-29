from string import punctuation, whitespace
import urllib2
import datetime
import re
from bs4 import BeautifulSoup as Soup
import csv
today = datetime.date.today()
#html = urllib2.urlopen("http://www.99acres.com/property-in-velachery-chennai-south-ffid").read()
#print "INSERT INTO `property` (`date`,`Url`,`Rooms`,`place`,`PId`,`Phonenumber1`,`Typeofperson`,` Nameofperson`,`typeofproperty`,`Sq.Ft`,`PerSq.Ft`,`AdDate`,`AdYear`)"
#print 'VALUES'
for locality in "velachery-chennai-south", "thoraipakkam-chennai-south", "madipakkam-chennai-south", "kalapatti-coimbatore":
 html =urllib2.urlopen("http://www.99acres.com/property-in-" + locality + "-ffid")
 soup = Soup(html)
 
 re_digit = re.compile('(\d+)')
 #properties = soup.findAll('a', title=re.compile('Bedroom'))
 for eachproperty in soup.findAll('div', {'class':'sT'}):
 	a      = eachproperty.find('a', title=re.compile('Bedroom'))
 	pdate  = eachproperty.find('i', {'class':'pdate'})
 	pdates = re.sub('(\s{2,})', ' ', pdate.text)
 	div    = eachproperty.find('div', {'class': 'sT_disc grey'})
 	try:
 		project = div.find('span').find('b').text.strip()
 	except:
   		project = 'NULL'        
 	area = re.findall(re_digit, div.find('i', {'class': 'blk'}).text.strip())
 	#print "(" , today,","+ (a['href'] if a else '`NULL`')+",", (a.string.replace(' Bedroom','') if a else '')+ "," +",".join(re.findall("'([a-zA-Z0-9,\s]*)'", a['onclick']) if a else '')+","+ ", ".join([project] + area),","+pdates+"", "),"
 	print today,","+ (a['href'] if a else '`NULL`')+",", (a.string.replace(' Bedroom','') if a else '')+"," + ",".join((re.findall("'([a-zA-Z0-9,\s]*)'", a['onclick']))[0].split(",")[:1] if a else '')+","+ ", ".join([project] + area),","+pdates
