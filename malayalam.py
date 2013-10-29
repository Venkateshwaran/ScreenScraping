import os
from urllib import urlopen
from bs4 import BeautifulSoup
url= "http://www.mathrubhumi.com/sports/story.php?id=397111"
raw = urlopen(url).read()
soup = BeautifulSoup(raw)
article = soup.get_text