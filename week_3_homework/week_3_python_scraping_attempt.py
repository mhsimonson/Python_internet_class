## Overall summary:
## =================
## Tired and disappointed.  Thought I had this down.  Fought it for some 4+ hours tonight, and just couldn't get it all
## Took some 2-3 just to figure out how to navigate the table portion of the webpage - finally got that
## No idea how at this point how to pull the links from the "intro" section of the webpage before iterating through the table
## Tried for another hour to get Python to make a directory.  No dice.  At least got the PDF versions of the links recognized thanks to
## a user tip on the class mailing list.
## Finally tried to at least get the links pulled from the table, and followed...and getting a Forbidden 403 error trying to get to the
## Wikipedia Internet Protocol Suite link
## So, sorry, another incomplete - MHS 2_1_11

## Useful Links:
## =============

# Working through blog example from http://thepcspy.com/read/scraping-websites-with-python/
# Also great tutorial video on YouTube http://www.youtube.com/watch?v=Ap_DlSrT-iE&feature=channel
# Troubleshooting KeyError: href bombout:  http://stackoverflow.com/questions/2502120/trying-to-grab-just-absolute-links-from-a-webpage-using-beautifulsoup

## =================================
## Notes from Sunday work session

## Works ***** Don't mess with it

##for link in soup.findAll('a', attrs={'href': re.compile("http://")}):
##    print link.text
##    print link['href']
##    print
## Suggestions on next steps from Brian:
##     1st loop over table rows
##     so it proceeds one row at a time
## To create directories - research os, os.path for commands


import urllib2
from BeautifulSoup import BeautifulSoup
import re
import os, pprint

url = 'http://briandorsey.info/uwpython/Internet_Programming_in_Python.html'
source = urllib2.urlopen(url)

soup=BeautifulSoup(source)
my_table=soup.table

## ======================================================================================
## attempts at trying to get Python to make a directory...nothing worked. Error messages included:
## WindowsError: [Error 123] The filename, directory name, or volume label syntax is incorrect
## Quick Google search revealed possible Registry problems...?

##os.mkdir('c:\python26\temp')
##current_dir = os.getcwd()
##sub_dirs = os.walk(current_dir)
##print 'Current directory:', current_dir
##output_dir = raw_input('Enter the directory where you want a temp directory made to store files scraped from the website links:\n')
##if os.path.isdir(output_dir):
##    print "Putting a temp directory there"
##    print output_dir
##    print '\temp'
##    os.mkdir(output_dir+'\temp')
##else:
##    raise ValueError, 'No such directory...exiting'


week=0

for row in my_table.findAll("tr"):
    x=row.findNext("td")
    if x.text.isdigit():
        week=int(x.text)
        
    for cell in row.findAll("td"):

## It finds everything, but I get a 403 Forbidden error trying to go to one of the links.
        
        for link in cell.findAll('a', attrs={'href': re.compile("://")}):  # "htt" in re.compile returns the BlueBoxGroup https link
            print link.text
            print link['href']
            follow_url=link['href']
            source=urllib2.urlopen(follow_url)
            follow_soup = str(BeautifulSoup(source))

## Did not complete - found the PDFs, but couldn't get the statement right to go to them
            
        for link in cell.findAll('a', attrs={'href': re.compile(".pdf")}):  # "htt" in re.compile returns the BlueBoxGroup https link
            follow_url=link['http://briandorsey.info/uwpython/'+'href']
            source=urllib2.urlopen(follow_url)
            follow_soup = str(BeautifulSoup(source))
            print link.text
            print link['href']
            
## Control code to break at week 1's list

    if week==1:
        break

## Section that worked on Sunday:
## ============================

##        follow_url = link['href']
##        source = urllib2.urlopen(follow_url)
##        follow_soup = str(BeautifulSoup(source))
##        links_content.append(follow_soup)



## Dumping Ground - Internet pastes, failed attempts, etc
## ======================================================

#data = str(soup.findAll('pre', limit=1))
##data = replace(data,'[<pre>','')
##data = replace(data,'</pre>]','')
##file_location = '/Users/location_edit_this'
##file_name = file_location + 'usd_aus.csv'
##file = open(file_name,"w")
##file.write(data)
##file.close()

#    week=0
#    if str(item.text).isdigit():
#            week=item.text
#            print "Week ",week
    #link_extractor(soup.table)
    
        #print cell
        #if cell.text.isdigit():
        #    week=int(cell.text)
        #print week
        #print cell.text        

#paraText = soup.find(text='This is paragraph ')
#ParaText.findNextSiblings('b')
##soup.find(tableTag).findNext('td').li
##
##def RepresentsInt(s):
##    try: 
##        int(s)
##        return True
##    except ValueError:
##        return False
#def link_extractor(page_section):

##for link in soup.findall('a', attrs={'href': re.compile("//")}):  # "htt" in re.compile returns the BlueBoxGroup https link
##    print link.text
##    print link['href']
##        follow_url = link['href']
##        source = urllib2.urlopen(follow_url)
##        follow_soup = str(BeautifulSoup(source))
##        links_content.append(follow_soup)
##        break  # Testing break flow
##
##print links_content

## Works ***** Don't mess with it
##for link in soup.findAll('a', attrs={'href': re.compile("http://")}):
##    print link.text
##    print link['href']
##    print

##soup_table = BeautifulSoup(input_page_data)
##my_table=soup.table
##print my_table
    
##
##for x in links:
###    title = x.contents[0].string
##    print x
##    print x.contents
##    print x.contents[0]
##    link = x['href']
##    print '%s\n' % (link)

#for link in soup.findAll('a'):
#    print link['href'].startswith('/')
#        link['href']= 'http://www.foobarinc.com'+link['href']

##for row in soup.table('tr'):
##    soup.table.findNext('td')
##    x=tablerow.findNextSiblings('td')
##    print x
##    if str(x.text).isdigit():
##        week = x.text
##        print week

##from BeautifulSoup import BeautifulSoup
##import urllib,string,csv,sys,os
##from string import replace
##
##date_s = '&date1=01/01/08'
##date_f = '&date=11/10/08'
##fx_url = 'http://www.oanda.com/convert/fxhistory?date_fmt=us'
##fx_url_end = '&lang=en&margin_fixed=0&format=CSV&redirected=1'
##cur1,cur2 = 'USD','AUD'
##fx_url = fx_url + date_f + date_s + '&exch=' + cur1 +'&exch2=' + cur1
##fx_url = fx_url +'&expr=' + cur2 +  '&expr2=' + cur2 + fx_url_end
##data = urllib.urlopen(fx_url).read()
##soup = BeautifulSoup(data)
##data = str(soup.findAll('pre', limit=1))
##data = replace(data,'[<pre>','')
##data = replace(data,'</pre>]','')
##file_location = '/Users/location_edit_this'
##file_name = file_location + 'usd_aus.csv'
##file = open(file_name,"w")
##file.write(data)
##file.close()
