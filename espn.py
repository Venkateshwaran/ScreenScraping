#!/usr/bin/env python
# -*- coding: utf-8 -*- 
import urllib2
from bs4 import BeautifulSoup

f = open('homeattendance.txt', 'w')

for number in range (2006, 2012):
 link = "http://espn.go.com/nhl/attendance/_/year/&#8221 + str(number)"
 page = urllib2.urlopen(link)
 soup = BeautifulSoup(page)
 table = soup.find('table')
 for row in table.find_all('tr', { 'class' : ['oddrow' , 'evenrow']}):
   col = row.find_all('td')
   team = col[1].string
   attendance = col[4].string
   capacity = col[5].string
   f.write(team + '\t' + str(number) + 't' + attendance + '\t' + capacity + '\n')
f.close()