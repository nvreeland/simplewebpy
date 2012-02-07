#!/usr/bin/env python
import simpleweb as web

class hello(web.template):
    def __init__(self, name):
        web.ctx.headers['Content-Type'] = 'text/html'
        self.setValue('Title', 'Hello World from simplewebpy')
        if name:
            self.setValue('Name', name)
        else:
            self.setValue('Name', 'World')

urls =  [ ('GET POST',  '/(.*)',    hello)
        ]

app = web.application(urls)

if __name__ == '__main__':
    app.run()
