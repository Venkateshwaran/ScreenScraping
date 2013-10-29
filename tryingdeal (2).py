from string import punctuation, whitespace
import urllib2
import datetime
import re
import MySQLdb
from bs4 import BeautifulSoup as Soup

today = datetime.date.today()
html = urllib2.urlopen("http://www.99acres.com/property-in-velachery-chennai-south-ffid").read()

soup = Soup(html)
print "INSERT INTO Property (URL,Rooms, Place, Phonenumber1,Phonenumber2,Phonenumber3,Typeofperson, Name)"
print "VALUES ("
re_digit = re.compile('(\d+)')
pdate = soup.findAll('i', {'class':'pdate'})
properties = soup.findAll('a', title=re.compile('Bedroom'))
for eachproperty in properties:
# title = today,","+"http:/"+ eachproperty['href']+",", eachproperty.string+"," +",".join(re.findall("'([a-zA-Z0-9,\s]*)'", eachproperty['onclick'])) 
for eachdate in pdate:
		pdates = re.sub('(\s{2,})', ' ', eachdate.text)
for div in soup.find_all('div', {'class': 'sT_disc grey'}):
		try:
			project = div.find('span').find('b').text.strip()
		except:
			project = 'No project'	
		area = re.findall(re_digit, div.find('i', {'class': 'blk'}).text.strip())

		print today,","+"http:/"+ eachproperty['href']+",", eachproperty.string+"," +",".join(re.findall("'([a-zA-Z0-9,\s]*)'", eachproperty['onclick']))+","+ ", ".join([project] + area),","+pdates
print ")"

