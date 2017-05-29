# vim:fileencoding=utf-8
import doctest
import gocept.country
import zope.app.wsgi.testlayer
import zope.testing

layer = zope.app.wsgi.testlayer.BrowserLayer(
    gocept.country, allowTearDown=True)


def test_suite():
    suite = doctest.DocFileSuite(
        'README.txt', optionflags=doctest.ELLIPSIS)
    suite.layer = layer
    return suite
