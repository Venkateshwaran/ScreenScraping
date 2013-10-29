from bs4 import BeautifulSoup
import urllib2
import csv
import re
number = 1
for i in xrange(0,38):
    page = urllib2.urlopen("http://www.sfap.org/klsfaprep_search?page={}&type=1&strname=&loc=&op=Lancer%20la%20recherche&form_build_id=form-72a297de309517ed5a2c28af7ed15208&form_id=klsfaprep_search_form" .format(i))
    soup = BeautifulSoup(page.read())
    print number,","
    print '\n'
    for eachuniversity in soup.findAll('div',{'class':'field-item odd'}):
	 	
		print re.sub(r'\s+',' ',''.join(eachuniversity.findAll(text=True)).encode('utf-8')),',',
		#print ''.join(eachuniversity.findAll(text=True)).encode('utf-8').strip(),',', 
    print '\n'
    number = number + 1
#print >> f, 'Filename:', some.csv  # or f.write('...\n')
#f.close()

