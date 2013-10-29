from string import punctuation, whitespace
import urllib2
import datetime
import re
import MySQLdb
from bs4 import BeautifulSoup as Soup

today = datetime.date.today()
html = urllib2.urlopen("http://www.99acres.com/property-in-velachery-chennai-south-ffid").read()

soup = Soup(html)
re_digit = re.compile('(\d+)')

for division in soup.find_all('div',{'class':'sT'}):

	part1 = division.find('a',title=re.compile('Bedroom'))
	finalpart1 = today, "," + "http://99acres.com" + part1 ['href'] + "," , part1.string + "," + ",".join(re.findall("'([a-zA-Z0-9,\s]*)'",part1['onclick']))
	part2 = division.find('span',{'class':'blk'}).find('b').text.strip()
	part3 = re.findall(re_digit,division.find('i',{'class':'blk'}).text.strip())
	
	print finalpart1, part2, part3 
