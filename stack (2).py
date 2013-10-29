from urllib import urlopen
optionsUrl = 'http://www.moneycontrol.com/commodity/'
optionsPage = urlopen(optionsUrl)
from bs4 import BeautifulSoup
soup = BeautifulSoup(optionsPage)
print soup.findAll(text='MCX')