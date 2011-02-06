#!/usr/bin/env python
# Only for Unix

import time
import datetime
import cgi


#print Content-type:text/html\r\n\r\n
#print "Content-type:text/html"
print '<html>'
print '<head>'
print ' ***** output from print_time_mhs.py *****'
print '</head>'
print '<p>'
print '<body>'
print 
print '<h1> <strong> The current time is: <strong> </h1>'
print
print 
print datetime.datetime.now()
print
print
print '</body>'
print '</html>'


#print "Here is the time: %s" % time.time()
#print "and again: %s" % datetime.datetime.now()


