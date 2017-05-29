# vim:fileencoding=utf-8
import doctest
import os.path
import zope.app.testing.functional
import zope.testing

layer = zope.app.testing.functional.ZCMLLayer(
    os.path.join(os.path.dirname(__file__), 'ftesting.zcml'),
    __name__, 'gocept.country Layer', allow_teardown=True)


def test_suite():
    suite = zope.app.testing.functional.FunctionalDocFileSuite(
        'README.txt', optionflags=doctest.ELLIPSIS)
    suite.layer = layer
    return suite
