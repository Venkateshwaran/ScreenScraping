from bs4 import BeautifulSoup
import urllib2
i = 0
for i in xrange(0,38):
	#page=urllib2.urlopen("http://www.sfap.org/klsfaprep_search?page={}&type=1&strname=&loc=&op=Lancer%20la%20recherche&form_build_id=form-72a297de309517ed5a2c28af7ed15208&form_id=klsfaprep_search_form" %i) 
	page=urllib2.urlopen("http://www.sfap.org/klsfaprep_search?page={}&type=1&strname=&loc=&op=Lancer%20la%20recherche&form_build_id=form-72a297de309517ed5a2c28af7ed15208&form_id=klsfaprep_search_form".format(i))
	soup = BeautifulSoup(page.read())
#universities=soup.findAll('div',{'class':'field-item odd'})
	for eachuniversity in soup.findAll('div',{'class':'field-item odd'}):
 #print eachuniversity['href']+","+eachuniversity.string.encode('utf-8').strip()
 #print eachuniversity.string if eachuniversity  else ''
 		print ''.join(eachuniversity.findAll(text=True)).encode('utf-8')
	print ',\n'












