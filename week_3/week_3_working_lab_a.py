import urllib2
from BeautifulSoup import *
import sys
import re
import string
# Why can't you use 'import BeautifulSoup' here, instead of 'from...import' structure?

search_url='http://briandorsey.info/uwpython/Internet_Programming_in_Python.html'

req = urllib2.Request(search_url)
response = urllib2.urlopen(req)
html = response.read()

#print html
soup = BeautifulSoup(html)
#print soup

x=str(soup.findAll(text=True))
print type(x)

word_list=[]
for word in x.split():
    word_clean=word.strip(string.punctuation + string.whitespace)            
    word_list.append(word_clean.lower())
print word_list

#word_list.find("jan")

months=[
    'jan',
    'feb',
    'mar',
    'apr'
    ]

#print x
    
