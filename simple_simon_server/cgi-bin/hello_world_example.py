#!C:\Python26\python.exe -u
#!/usr/bin/env python


import sys
sys.path.insert(0, "/users/mark/python_internet_class/thirty_minute_app")


import cgitb
cgitb.enable()



print "Content-Type:text/html"
print "<HTML>"
print "<TITLE>CGI script output</TITLE>"
print "<H1>This is my first CGI script<H1>"
print "Hello, world!"
print "</HTML>"
