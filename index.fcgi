#!/usr/bin/env python
import simpleweb

class hello(simpleweb.template):
    def __init__(self, name):
        app.ctx.headers['Content-Type'] = ['text/plain']
        self.setValue('Title', 'Hello World from simplewebpy')
        if name:
            self.setValue('Name', name)
        else:
            self.setValue('Name', 'World')

urls =  [ ('GET POST',  '/(.*)',    hello)
        ]

app = simpleweb.application(urls)

if __name__ == '__main__':
    app.run()

