import datetime
today = datetime.date.today()
print today


import re
import urllib2
from bs4 import BeautifulSoup as Soup

html = urllib2.urlopen("http://www.99acres.com/property-in-velachery-chennai-south-ffid").read()
soup = Soup(html)

re_digit = re.compile('(\d+)')
for div in soup.find_all('div', {'class': 'sT_disc grey'}):
    try:
        project = div.find('span').find('b').text.strip()
    except:
        project = 'No project'
    area = re.findall(re_digit, div.find('i', {'class': 'blk'}).text.strip())

    print ", ".join([project] + area)