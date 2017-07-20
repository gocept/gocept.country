from __future__ import print_function
import doctest
import gocept.country
import zope.app.wsgi.testlayer
import zope.testing

layer = zope.app.wsgi.testlayer.BrowserLayer(
    gocept.country, allowTearDown=True)


def setUp(test):
    test.globs['print_function'] = print_function


def test_suite():
    suite = doctest.DocFileSuite(
        '../README.txt', optionflags=doctest.ELLIPSIS, setUp=setUp)
    suite.layer = layer
    return suite
