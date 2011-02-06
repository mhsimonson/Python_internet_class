import cherrypy

## Note Control C on the DOS command line will kill server, "Kill" command in Unix

class HelloWorld:
    def index(self):
        return "Hello world!"
    index.exposed = True

cherrypy.quickstart(HelloWorld())
