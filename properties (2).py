from bs4 import BeautifulSoup
from string import punctuation, whitespace
import urllib2
import datetime
import re
import MySQLdb
#db = MySQLdb.connect(host="scraping.db.9131598.hostedresource.com", user="scraping", passwd="Semester12#", db="scraping")
today = datetime.date.today()
url="http://www.99acres.com/property-in-velachery-chennai-south-ffid?"
print "INSERT INTO Property (URL,Rooms, Place, Phonenumber1,Phonenumber2,Phonenumber3,Typeofperson, Name)"
print "VALUES "
page=urllib2.urlopen(url)
soup = BeautifulSoup(page.read())
properties = soup.findAll('a', title=re.compile('Bedroom'))
for eachproperty in properties:
 final = today,","+"http:/"+ eachproperty['href']+",", eachproperty.string+"," +",".join(re.findall("'([a-zA-Z0-9,\s]*)'", eachproperty['onclick'])) 
 print final
 #print ")"