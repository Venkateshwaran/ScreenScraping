from bs4 import BeautifulSoup
import urllib2
url="http://rediff.com/"
page=urllib2.urlopen(url)
soup = BeautifulSoup(page.read())
source=soup.findAll('script',{"src":True})
for sources in source:
 print sources['src']
