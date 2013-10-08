import urllib2
from BeautifulSoup import BeautifulSoup

opener = urllib2.build_opener()
opener.addheaders = [("User-Agent", "Mozilla/5.0")]

url = ("http://jobsearch.monsterboard.nl/browse/")

content = opener.open(url).read()
soup = BeautifulSoup(content)

soup.find(id="primaryResults")
print soup.find_all('a')
