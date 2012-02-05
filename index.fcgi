#!/usr/bin/env python
from simpleweb import WebApplication

def hello(ctx, name):
    if name:
        yield 'Hello %s!\n' % name
    else:
        yield 'Hello World!\n'

urls =  [ ('GET POST',  '/(.*)',    hello)
        ]

app = WebApplication(urls)

if __name__ == '__main__':
    app.run()

