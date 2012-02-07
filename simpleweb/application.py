#!/usr/bin/env python
import cgi
import re
import urllib

class RequestContext(object):

    def __init__(self, environ, start_response):
        self.status = '200 OK'
        self.headers = { 'Content-Type': ['text/plain']
                       }
        self._start_response = start_response

        self.environ = environ
        self.request_method = environ.get('REQUEST_METHOD')
        self.path_info = urllib.unquote(environ.get('PATH_INFO'))
        self.cgi_vars = cgi.FieldStorage(fp = environ['wsgi.input'],
                                         environ = environ,
                                         keep_blank_values = 1)
    def start_response(self):
        # python2.7+
        #headers = [ (name, val) for val in vals
        #                for name, vals in self.headers.iteritems() ]
        headers = []
        for name, vals in self.headers.iteritems():
            for val in vals:
                headers.append( (name, val) )
        self._start_response(self.status, headers)

class application(object):

    def __init__(self, mapping = []):
        self.urlMapping = mapping

    def run(self):
        from flup.server.fcgi import WSGIServer
        return WSGIServer(self.handleRequest).run()

    def handleRequest(self, environ, start_response):
        self.ctx = RequestContext(environ, start_response)
        for (supportedMethods, regexp, handler) in self.urlMapping:
            if self.ctx.request_method not in supportedMethods.split(' '):
                continue
            m = re.match(regexp, self.ctx.path_info)
            if m is None:
                continue
            h = handler(*m.groups())
            self.ctx.start_response()
            return [h.render(),]
        self.ctx.start_response()
        return ['What happened?',]
