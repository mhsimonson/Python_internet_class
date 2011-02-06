import cherrypy

##class OnePage(object):
##    def index(self):
##        return "one page!"
##    index.exposed = True
 
class HelloWorld(object):
    def index(self):
        return "<strong>hello world!</strong>"
    index.exposed = True
 
cherrypy.quickstart(HelloWorld())
