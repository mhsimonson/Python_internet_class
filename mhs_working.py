print ''' content-type: text/html <html> <head> <title> This is the title </title> </head> <body> This is the body. </body> </html> '''

 # Import modules for CGI handling 
import cgi, cgitb 
 
 # Create instance of FieldStorage
form = cgi.FieldStorage() 
 
 # Get data from field 'name' 
name = form.getvalue('name') 
 
 # Get data from field 'address' 
address = form.getvalue('address') 
 
 # Get data from field 'phone' 
phone = form.getvalue('phone') 
 
 # Get data from field 'email' 
email = form.getvalue('email') 

print ''' content-type: text/html <html> <head> <title> This is the title </title> </head> <body> <br>
    <form action="./test.cgi" method="post"> <p>
    Name: <input type="text" name="name" id="name" value=""/></p><p>
    Street Address: <input type="text" name="st_address" id="st_address" value=""/></p> <p>
    Town: <input type="text" name="town" id="town" value=""/></p> <p>
    County: <input type="text" name="county" id="county" value=""/></p> <p>
    Postcode: <input type="text" name="postcode" id="postcode" value=""/></p> <p>
    Telephone: <input type="text" name="telephone" id="telephone" value=""/></p> <p>
    Fax: <input type="text" name="fax" id="fax" value=""/></p> <p>
    Email: <input type="text" name="email" id="email" value=""/></p> <p>
    Website: <input type="text" name="website" id="website" value=""/></p> <br> <input type="submit" value="Submit" /> </form> </body> </html> ''' 
