#!/usr/bin/env python
import simpleweb as web

class searchForm(web.template):
    def __init__(self, query = None):
        if query:
            self.setValue('Query', query)

class search(web.template):
    def __init__(self):
        self.query = web.ctx.cgi.getfirst('q')
        self.form = searchForm(self.query)
    def render(self):
        self.setValue('SearchForm', self.form.render())
        if self.query is not None:
            self.setValue('SearchResults', 'You searched for: %s' % self.query)
        return web.template.render(self)

class hello(web.template):
    def __init__(self, name):
        self.setValue('Title', 'Hello World from simplewebpy')
        if name:
            self.setValue('Name', name)
        else:
            self.setValue('Name', 'World')

urls =  [ ('GET',       '/search',  search)
        , ('GET POST',  '/(.*)',    hello)
        ]

app = web.application(urls)

if __name__ == '__main__':
    app.run()
