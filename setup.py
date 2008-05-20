# vim:fileencoding=utf-8
# Copyright (c) 2008 gocept gmbh & co. kg
# See also LICENSE.txt
# $Id$
"""Setup for country package.
"""

import os.path

from setuptools import setup, find_packages


setup(
    name='gocept.country',
    version='0.9dev',
    author='Sebastian Wehrmann, Christian Theune',
    author_email='sw@gocept.com',
    description='Zope 3 sources for pycountry databases',
    long_description=open(os.path.join('src', 'gocept', 'country', 'README.txt')
                         ).read(),
    license='ZPL 2.1',
    keywords='country subdivision language currency iso 3166 639 4217 '
             '15924 3166-2 zope',
    zip_safe=False,
    packages=find_packages('src'),
    include_package_data=True,
    package_dir={'':'src'},
    install_requires=['pycountry',
                      'zope.i18nmessageid',
                      'zc.sourcefactory'],
    )
