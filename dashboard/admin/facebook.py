import cherrypy


class FacebookAdmin(object):
    @cherrypy.expose
    @cherrypy.tools.logit()
    def log(self):
        return 'Hello world - with logging'

    @cherrypy.expose
    def nolog(self):
        return 'Hello world - without logging'
