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
        try:
            self._hdf.setValue(name, value)
        except AttributeError:
            self._hdf = HDF()
            self._hdf.setValue(name, value)
    def render_cs(self, fileType, fileName = None):
        if fileName is None:
            fileName = type(self).__name__
        path = '{0}/templates/{0}.{1}'.format(
                web.ctx.path, fileName, fileType)
        if not isfile(path):
            return None
        try:
            cs = CS(self._hdf)
        except AttributeError:
            cs = CS(HDF())
        cs.parseFile(path)
        return cs.render()
    def render(self, fileName = None):
        js = self.render_cs('js', fileName)
        css = self.render_cs('css', fileName)
        html = self.render_cs('html', fileName)
        return (js, css, html)

class document(widget):
    def __init__(self, title = None):
        self.title = title
        self.widgets = []
    def setTitle(self, title):
        if self.title:
            title = '{0} -- {1}'.format(title, self.title)
        self.setValue('Document.Title', title)
    def render(self):
        for i, w in enumerate(self.widgets):
            (js, css, html) = w.render()
            if js:
                self.setValue('Document.Scripts.{0}'.format(i), js)
            if css:
                self.setValue('Document.Css.{0}'.format(i), css)
            if html:
                self.setValue('Document.Content.{0}'.format(i), html)
        return self.render_cs('html')
