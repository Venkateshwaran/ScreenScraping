from string import punctuation, whitespace
import urllib2
import datetime
import re
import MySQLdb
import csv
from bs4 import BeautifulSoup as Soup
news_url = "http://www.thestar.com/feeds.articles.news.gta.rss" # Toronto Star RSS Feed

news_rss = urllib2.urlopen(news_url)
news = news_rss.read()
news_rss.close()
soup = Soup(news)

titles = soup.findAll('title')
links = soup.findAll('link')

for link in links:
    link = link.contents    # I want the url without the <link> tags
i=0
news_stuff = []
for item in titles:
    if item.text == "TORONTO STAR | NEWS | GTA":    # These have <title> tags and I don't want them; just skip 'em.
        pass
    else:
        news_stuff.append((item.text, links[i]))    # Here's a news story.  Grab it.

i = 0
for thing in news_stuff:
    print '<a href="' 
    print thing[1]
    print '"target="_blank">' 
    print thing[0]
    print '</a><br/>'
    i += 1