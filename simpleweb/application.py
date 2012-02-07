#!/usr/bin/env python
import webapi as web
import re

class application(object):

    def __init__(self, mapping = []):
        self.urlMapping = mapping

    def run(self):
        from flup.server.fcgi import WSGIServer
        return WSGIServer(self.handleRequest).run()

    def handleRequest(self, environ, start_response):
        web.ctx.init(environ, start_response)
        for (supportedMethods, regexp, handler) in self.urlMapping:
            if web.ctx.request_method not in supportedMethods.split(' '):
                continue
            m = re.match(regexp, web.ctx.path_info)
            if m is None:
                continue
            try:
                h = handler(*m.groups())
            except:
                import traceback
                web.ctx.headers = {'Content-Type': 'text/plain'}
                web.ctx.start_response()
                return [traceback.format_exc(),]
            else:
                web.ctx.start_response()
                return [h.render(),]
        # No request handler!
        # 404 Not found
        web.ctx.status = '404 Not Found'
        web.ctx.headers = {'Content-Type': 'text/plain'}
        web.ctx.start_response()
        return ['Not found',]
