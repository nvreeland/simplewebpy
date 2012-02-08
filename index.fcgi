#!/usr/bin/env python
import simpleweb as web

class search(web.widget):
    def __init__(self):
        query = web.ctx.cgi.getfirst('q')
        if query:
            self.setValue('Search.Query', query)
            self.setValue('Search.Results',
                          'Displaying results for: {0}'.format(query))

class hello(web.widget):
    def __init__(self, name):
        web.ctx.doc.docTitle('Hello world')
        if name:
            self.setValue('Hello.Name', name)

urls =  [ ('GET',       '/search',  search)
        , ('GET POST',  '/(.*)',    hello)
        ]

app = web.application(urls)

if __name__ == '__main__':
    app.run()
