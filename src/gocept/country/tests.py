# vim:fileencoding=utf-8
# Copyright (c) 2008 gocept gmbh & co. kg
# See also LICENSE.txt
# $Id$
"""Test harness for gocept.country."""

import os.path

from zope.testing import doctest
import zope.app.testing.functional
import unittest

layer = zope.app.testing.functional.ZCMLLayer(
    os.path.join(os.path.dirname(__file__), 'ftesting.zcml'),
    __name__, 'gocept.country Layer', allow_teardown=True)

def test_suite():
    suite = unittest.TestSuite()
    test = zope.app.testing.functional.FunctionalDocFileSuite(
                                       'README.txt',
                                       optionflags=doctest.ELLIPSIS)
    test.layer = layer
    suite.addTest(test)
    return suite
