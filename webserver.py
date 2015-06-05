import cherrypy


def logit():
    print('Logging from {0}'.format(cherrypy.request.remote.ip))

if __name__ == '__main__':
    cherrypy.tools.logit = cherrypy.Tool('before_finalize', logit)

    from dashboard.admin.facebook import FacebookAdmin
    cherrypy.tree.mount(FacebookAdmin(), '/admin/facebook')

    cherrypy.engine.start()
    cherrypy.engine.block()
