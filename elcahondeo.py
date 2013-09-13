from bs4 import BeautifulSoup
import urllib2
url="http://www.elafter.com/"
page=urllib2.urlopen(url)
soup = BeautifulSoup(page.read())
source=soup.findAll('a',{"href":True})
for sources in source:
 print sources['href']
