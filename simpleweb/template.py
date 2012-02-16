#!/usr/bin/env python
from os.path import isfile
import neo_cgi
from neo_util import HDF
from neo_cs import CS
import webapi as web

__all__ = [
    'widget',
    'document',
    ]

class widget(object):
    def setValue(self, name, value):
        if value is None:
            value = ''
        elif not isinstance(value, str):
            value = str(value)
        try:
            self._hdf.setValue(name, value)
        except AttributeError:
            self._hdf = HDF()
            self._hdf.setValue(name, value)
    def render_cs(self, fileType, fileName = None):
        if fileName is None:
            fileName = type(self).__name__
        path = '{0}/templates/{1}.{2}'.format(
                web.ctx.path, fileName, fileType)
        if not isfile(path):
            return None
        cs = CS(self._hdf)
        cs.parseFile(path)
        return cs.render()
    def render(self, fileName = None):
        self.setValue('Script.Name', web.ctx.script_name)
        js = self.render_cs('js', fileName)
        css = self.render_cs('css', fileName)
        html = self.render_cs('html', fileName)
        return (js, css, html)

"""
this class is called by document.render and builds the widget
object the render method returns the proper js, css, and html
for this widget to the document class"""
        

class document(widget):
    def __init__(self, title = None):
        self.title = title
        self.widgets = []
        self.metaCount = 0
    def setMeta(self, equiv = None, name = None, content = None):
        i = self.metaCount
        if equiv:
            self.setValue('Document.Meta.{0}.equiv'.format(i), equiv)
        if name:
            self.setValue('Document.Meta.{0}.name'.format(i), name)
        if content:
            self.setValue('Document.Meta.{0}.content'.format(i), content)
        self.metaCount += 1
    def setTitle(self, title):
        if self.title:
            title = '{0} -- {1}'.format(title, self.title)
        self.setValue('Document.Title', title)
    def render(self):
        self.setValue('Script.Name', web.ctx.script_name)
        for i, w in enumerate(self.widgets):
            (js, css, html) = w.render()
            if js:
                self.setValue('Document.Scripts.{0}'.format(i), js)
            if css:
                self.setValue('Document.Css.{0}'.format(i), css)
            if html:
                self.setValue('Document.Content.{0}'.format(i), html)
        return self.render_cs('html')
""" 
When the init method is called by web.RequestContext, the application builds
the object and returns the proper js, css, and html with the render method"""
