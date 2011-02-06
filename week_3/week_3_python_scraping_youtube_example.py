# Also great tutorial video on YouTube http://www.youtube.com/watch?v=Ap_DlSrT-iE&feature=channel

import urllib2
from BeautifulSoup import BeautifulSoup
import re

url = 'http://briandorsey.info/uwpython/Internet_Programming_in_Python.html'
source = urllib2.urlopen(url)

soup=BeautifulSoup(source)


#print source.read()
find_link = re.compile('<link rel.*href=(.*)"/>') 

link_list = []




#for i in list:
#   print find_link[i]
   

