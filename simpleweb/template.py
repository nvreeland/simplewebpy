#!/usr/bin/env python
import neo_cgi
from neo_util import HDF
from neo_cs import CS

class template(object):
    def setValue(self, name, value):
        try:
            self._hdf.setValue(name, value)
        except AttributeError:
            self._hdf = HDF()
            self._hdf.setValue(name, value)
    def render(self, fileName = None):
        if fileName is None:
            fileName = type(self).__name__
        try:
            cs = CS(self._hdf)
        except AttributeError:
            cs = CS(HDF())
        cs.parseFile('/var/www/simplewebpy/template/%s.cst' % fileName)
        return cs.render()
