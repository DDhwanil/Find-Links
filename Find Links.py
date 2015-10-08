from annobrowser import *
from BeautifulSoup import BeautifulSoup
import os,re
ab=annobrowser()
ab.anonymize()
url=raw_input('Enter url (In form of http:// or https://) :http')
url='http'+url

try:
    page=ab.open(url).read()
    lk=re.compile('href="(.*?)"')
    li=lk.findall(page)
    print '\nBY regx'
    for o in li:
        print o
except Exception, e:
    if 'HTTP Error 403: Forbidden' in str(e):
        print "Firewall Block or Url not accessible"

try:
    page=ab.open(url).read()
    soup=BeautifulSoup(page)
    li=soup.findAll(name='a')
    print '\n BY BeautifulSoup'
    for l in li:
        if l.has_key('href'):
            print l['href']
except Exception, e:
    if 'HTTP Error 403: Forbidden' in str(e):
        print "Firewall Block or Url not accessible"
