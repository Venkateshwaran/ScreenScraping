import csv
import urllib2

import BeautifulSoup


def getPageText(url, filename):
    data = urllib2.urlopen(url).read()
    bs = BeautifulSoup.BeautifulSoup(data, convertEntities=BeautifulSoup.BeautifulSoup.HTML_ENTITIES)
    with open(filename, 'w') as f:
        writer = csv.writer(f)
        for adli in bs.findAll('div',attrs={'class':'tads'}):
        	alink = adli.find('a')
        	aspan = adli.find('span', attrs={'class':'ac'})
        for li in bs.findAll('li', attrs={'class':'g'}):
            sLink = li.find('a')
            sSpan = li.find('span', attrs={'class':'st'})

            writer.writerow([sLink['href'], sSpan, alink['href'], aspan])

def main():
    urls = ['http://192.168.1.200/coimbatore/3BHK_flats_inCoimbatore.html_%94201308110608%94.html',
'http://192.168.1.200/coimbatore/3BHK_flats_inCoimbatore.html_%94201308110608%94.html.html',
'http://192.168.1.200/coimbatore/3BHK_flats_inCoimbatore.html_%94201308120627%94.html     ',
'http://192.168.1.200/coimbatore/3BHK_flats_inCoimbatore.html_%94201308120627%94.html.html',
'http://192.168.1.200/coimbatore/3BHK_flats_inCoimbatore.html_%94201308150654%94.html     ',
'http://192.168.1.200/coimbatore/3BHK_flats_inCoimbatore.html_%94201308150654%94.html.html',
'http://192.168.1.200/coimbatore/3BHK_flats_inCoimbatore.html_%94201308160607%94.html     ',
'http://192.168.1.200/coimbatore/3BHK_flats_inCoimbatore.html_%94201308160607%94.html.html',
'http://192.168.1.200/coimbatore/3BHK_flats_inCoimbatore.html_%94201308170605%94.html     ',
'http://192.168.1.200/coimbatore/3BHK_flats_inCoimbatore.html_%94201308170605%94.html.html',
'http://192.168.1.200/coimbatore/3BHK_flats_inCoimbatore.html_%94201308200621%94.html     ',
'http://192.168.1.200/coimbatore/3BHK_flats_inCoimbatore.html_%94201308200621%94.html.html',
'http://192.168.1.200/coimbatore/3BHK_flats_inCoimbatore.html_%94201308210629%94.html     ',
'http://192.168.1.200/coimbatore/3BHK_flats_inCoimbatore.html_%94201308210629%94.html.html',
'http://192.168.1.200/coimbatore/3BHK_flats_inCoimbatore.html_%94201308220609%94.html     ',
'http://192.168.1.200/coimbatore/3BHK_flats_inCoimbatore.html_%94201308220609%94.html.html',
'http://192.168.1.200/coimbatore/3BHK_flats_inCoimbatore.html_%94201308230602%94.html     ',
'http://192.168.1.200/coimbatore/3BHK_flats_inCoimbatore.html_%94201308230602%94.html.html',
'http://192.168.1.200/coimbatore/3BHK_flats_inCoimbatore.html_%94201308240602%94.html     ',
'http://192.168.1.200/coimbatore/3BHK_flats_inCoimbatore.html_%94201308240602%94.html.html',
'http://192.168.1.200/coimbatore/3BHK_flats_inCoimbatore.html_%94201308250605%94.html     ',
'http://192.168.1.200/coimbatore/3BHK_flats_inCoimbatore.html_%94201308250605%94.html.html',
'http://192.168.1.200/coimbatore/3BHK_flats_inCoimbatore.html_%94201308260608%94.html     ',
'http://192.168.1.200/coimbatore/3BHK_flats_inCoimbatore.html_%94201308260608%94.html.html',
'http://192.168.1.200/coimbatore/3BHK_flats_inCoimbatore.html_%94201308270607%94.html     ',
'http://192.168.1.200/coimbatore/3BHK_flats_inCoimbatore.html_%94201308270607%94.html.html',
'http://192.168.1.200/coimbatore/3BHK_flats_inCoimbatore.html_%94201308280603%94.html     ',
'http://192.168.1.200/coimbatore/3BHK_flats_inCoimbatore.html_%94201308280603%94.html.html',
'http://192.168.1.200/coimbatore/3BHK_flats_inCoimbatore.html_%94201308290602%94.html     ',
'http://192.168.1.200/coimbatore/3BHK_flats_inCoimbatore.html_%94201308290602%94.html.html',
'http://192.168.1.200/coimbatore/3BHK_flats_inCoimbatore.html_%94201308300605%94.html     ',
'http://192.168.1.200/coimbatore/3BHK_flats_inCoimbatore.html_%94201308300605%94.html.html',
'http://192.168.1.200/coimbatore/3BHK_flats_inCoimbatore.html_%94201308310605%94.html     ',
'http://192.168.1.200/coimbatore/3BHK_flats_inCoimbatore.html_%94201308310605%94.html.html',
'http://192.168.1.200/coimbatore/3BHK_flats_inCoimbatore.html_%94201309010603%94.html     ',
'http://192.168.1.200/coimbatore/3BHK_flats_inCoimbatore.html_%94201309010603%94.html.html',
'http://192.168.1.200/coimbatore/3BHK_flats_inCoimbatore.html_%94201309020602%94.html     ',
'http://192.168.1.200/coimbatore/3BHK_flats_inCoimbatore.html_%94201309020602%94.html.html',
'http://192.168.1.200/coimbatore/3BHK_flats_inCoimbatore.html_%94201309030602%94.html     ',
'http://192.168.1.200/coimbatore/3BHK_flats_inCoimbatore.html_%94201309030602%94.html.html',
'http://192.168.1.200/coimbatore/3BHK_flats_inCoimbatore.html_%94201309040602%94.html     ',
'http://192.168.1.200/coimbatore/3BHK_flats_inCoimbatore.html_%94201309040602%94.html.html',
'http://192.168.1.200/coimbatore/3BHK_flats_inCoimbatore.html_%94201309050602%94.html     ',
'http://192.168.1.200/coimbatore/3BHK_flats_inCoimbatore.html_%94201309050602%94.html.html',
'http://192.168.1.200/coimbatore/3BHK_flats_inCoimbatore.html_%94201309060602%94.html     ',
'http://192.168.1.200/coimbatore/3BHK_flats_inCoimbatore.html_%94201309060602%94.html.html',
'http://192.168.1.200/coimbatore/3BHK_flats_inCoimbatore.html_%94201309070602%94.html     ',
'http://192.168.1.200/coimbatore/3BHK_flats_inCoimbatore.html_%94201309070602%94.html.html',
'http://192.168.1.200/coimbatore/3BHK_flats_inCoimbatore.html_%94201309080603%94.html     ',
'http://192.168.1.200/coimbatore/3BHK_flats_inCoimbatore.html_%94201309080603%94.html.html',
'http://192.168.1.200/coimbatore/3BHK_flats_inCoimbatore.html_%94201309090603%94.html     ',
'http://192.168.1.200/coimbatore/3BHK_flats_inCoimbatore.html_%94201309090603%94.html.html',
'http://192.168.1.200/coimbatore/3BHK_flats_inCoimbatore.html_%94201309100602%94.html     ',
'http://192.168.1.200/coimbatore/3BHK_flats_inCoimbatore.html_%94201309100602%94.html.html',
'http://192.168.1.200/coimbatore/3BHK_flats_inCoimbatore.html_%94201309110602%94.html     ',
'http://192.168.1.200/coimbatore/3BHK_flats_inCoimbatore.html_%94201309110602%94.html.html',
'http://192.168.1.200/coimbatore/3BHK_flats_inCoimbatore.html_%94201309120603%94.html     ',
'http://192.168.1.200/coimbatore/3BHK_flats_inCoimbatore.html_%94201309120603%94.html.html',
'http://192.168.1.200/coimbatore/3BHK_flats_inCoimbatore.html_%94201309130603%94.html     ',
'http://192.168.1.200/coimbatore/3BHK_flats_inCoimbatore.html_%94201309130603%94.html.html',
'http://192.168.1.200/coimbatore/3BHK_flats_inCoimbatore.html_%94201309140602%94.html     ',
'http://192.168.1.200/coimbatore/3BHK_flats_inCoimbatore.html_%94201309140602%94.html.html',
'http://192.168.1.200/coimbatore/3BHK_flats_inCoimbatore.html_%94201309210606%94.html'

    ]
    for i, url in enumerate(urls, 1):
        getPageText(url, '3BHK_flats_inCoimbatore {}.csv'.format(i))

if __name__=="__main__":
    main()    

