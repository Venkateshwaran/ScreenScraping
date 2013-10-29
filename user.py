import urllib2 
from bs4 import BeautifulSoup

url='http://www.jbhifi.com.au/computers/laptop-notebook/'
req=urllib2.Request(url,headers={'User-Agent':'Mozilla/5.0 (Windows NT 5.1)          AppleWebKit/537.36 (KHTML, like Gecko) Chrome/29.0.1547.76 Safari/537.36'})
webpage=urllib2.urlopen(req)
content=webpage.read()
soup=BeautifulSoup(content)
x=soup.find("div",attrs={'id':'content'})
print str(x)[:100]