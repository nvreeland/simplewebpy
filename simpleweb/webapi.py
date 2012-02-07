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
        self.headers = { 'Content-Type': 'text/plain' }

    def init(self, env, start_response):
        self.env = env
        self._start_response = start_response

        self.method = env.get('REQUEST_METHOD')
        self.path_info = urllib.unquote(env.get('PATH_INFO'))
        self.cgi_vars = cgi.FieldStorage(fp = env['wsgi.input'],
                                         environ = env,
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
ctx.__doc__ = """
A `storage` object containing various information about the request:

`env`
    : A dictionary containg the standard WSGI environment variables.

`method`
    : The HTTP request method.

### Response Data

`status` (default: "200 OK")
    : The status code used in the response.

`headers`
    : A dictionary storing response headers.  Key is the header name, Value is the header value.  If Value is a list, the header is sent, one for each element.
"""
