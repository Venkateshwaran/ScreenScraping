from string import punctuation, whitespace
import urllib2
import datetime
import re
from bs4 import BeautifulSoup as Soup

today = datetime.date.today()
html = urllib2.urlopen("http://www.99acres.com/property-in-thoraipakkam-chennai-south-ffid?").read()

soup = Soup(html)
print "INSERT INTO `property` (`date`,`Url`,`Rooms`,`place`,`PId`,`Phonenumber1`,`Phonenumber2`,`Phonenumber3`,`Typeofperson`,` Nameofperson`,`typeofproperty`,`Sq.Ft`,`PerSq.Ft`,`AdDate`,`AdYear`)"
print 'VALUES'
re_digit = re.compile('(\d+)')
properties = soup.findAll('a', title=re.compile('Bedroom'))

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
  print ' ('
  print today,","+ (a['href'] if a else '`NULL`')+",", (a.string if a else 'NULL, NULL')+ "," +",".join(re.findall("'([a-zA-Z0-9,\s]*)'", (a['onclick'] if a else 'NULL, NULL, NULL, NULL, NULL, NULL')))+","+ ", ".join([project] + area),","+pdates+""
  print ' ), '