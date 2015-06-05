import cherrypy
from dashboard.lib.cherrypy import Jinja2TemplatePlugin, Jinja2Tool
from jinja2 import Environment, PrefixLoader, PackageLoader


if __name__ == '__main__':
    # Hook up the Jinja templating
    env = Environment(loader=PrefixLoader({
        'admin': PackageLoader('dashboard.admin'),
    }))
    Jinja2TemplatePlugin(cherrypy.engine, env=env).subscribe()
    cherrypy.tools.template = Jinja2Tool()

    # Hook up the URL tree
    from dashboard.admin.facebook import FacebookAdmin
    cherrypy.tree.mount(FacebookAdmin(), '/admin/facebook')

    cherrypy.engine.start()
    cherrypy.engine.block()
