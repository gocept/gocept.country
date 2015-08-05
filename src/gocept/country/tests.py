# vim:fileencoding=utf-8
import doctest
import os.path
import unittest
import zope.app.testing.functional
import zope.testing

layer = zope.app.testing.functional.ZCMLLayer(
    os.path.join(os.path.dirname(__file__), 'ftesting.zcml'),
    __name__, 'gocept.country Layer', allow_teardown=True)


def test_suite():
    suite = unittest.TestSuite()
    test = zope.app.testing.functional.FunctionalDocFileSuite(
        'README.txt', optionflags=doctest.ELLIPSIS)
    test.layer = layer
    suite.addTest(test)
    return suite
