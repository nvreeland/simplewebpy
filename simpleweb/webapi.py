#!/usr/bin/env python
import cgi
import urllib

__all__ = [
    'RequestContext',
    'ctx',
]

class RequestContext(object):

    def __init__(self):
        self.status = '200 OK'
        self.headers = { 'Content-Type': ['text/plain'] }
        self._start_response = None
        self.environ = None

    def init(self, environ, start_response):
        self.environ = environ
        self._start_response = start_response

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
            if isinstance(vals, list):
                for val in vals:
                    headers.append( (name, val) )
            else:
                headers.append( (name, vals) )
        self._start_response(self.status, headers)

ctx = context = RequestContext()