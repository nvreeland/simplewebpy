#!/usr/bin/env python
import re
import webapi as web

__all__ = [
    'application',
    ]

class application(object):

    def __init__(self, mapping = []):
        self.urlMapping = mapping

    def run(self):
        from flup.server.fcgi import WSGIServer
        return WSGIServer(self.handleRequest).run()

    def handleRequest(self, environ, start_response):
        web.ctx.init(environ, start_response)
        for (supportedMethods, regexp, widget) in self.urlMapping:
            if web.ctx.method not in supportedMethods.split(' '):
                continue
            m = re.match(regexp, web.ctx.path_info)
            if m is None:
                continue
            try:
                web.ctx.doc.widgets.insert(0, widget(*m.groups()))
                response = web.ctx.doc.render()
                web.ctx.status = '200 OK'
                web.ctx.headers['Content-Type'] = 'text/html'
            except:
                import traceback
                web.ctx.status = '500 Internal Server Error'
                web.ctx.headers['Content-Type'] = 'text/plain'
                response = traceback.format_exc()
            web.ctx.start_response()
            return [response,]
        # No request handler!
        # 404 Not found
        web.ctx.status = '404 Not Found'
        web.ctx.headers['Content-Type'] = 'text/plain'
        web.ctx.start_response()
        return ['Not found',]
