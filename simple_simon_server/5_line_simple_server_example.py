from http.server import HTTPServer, CGIHTTPRequestHandler
 
port = 8080
httpd = HTTPServer((' ' , port) , CGIHTTPRequestHandler)
print("Starting simple_httpd on port: " + str(httpd. server_port) )
httpd. serve_forever()
#GET /users/mark/Python_internet_class/thirty_minute_app/time/mhs_print_time_try.py HTTP/1.1

