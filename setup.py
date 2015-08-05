# vim:fileencoding=utf-8
import os.path
from setuptools import setup, find_packages


def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()

setup(
    name='gocept.country',
    version='0.6.5',
    author='gocept gmbh & co. kg',
    author_email='mail@gocept.com',
    description='Zope 3 sources for pycountry databases',
    long_description=(read('COPYRIGHT.txt')
                      + '\n\n' +
                      read('README.txt')
                      + '\n\n' +
                      read('src', 'gocept', 'country', 'README.txt')
                      + '\n\n' +
                      read('CHANGES.txt')),
    license='ZPL 2.1',
    keywords='country subdivision language currency iso 3166 639 4217 '
             '15924 3166-2 zope',
    zip_safe=False,
    namespace_packages = ['gocept'],
    classifiers = [
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Zope Public License',
        'Programming Language :: Python',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Topic :: Internet :: WWW/HTTP'],
    url='https://bitbucket.org/gocept/gocept.country',
    packages=find_packages('src'),
    include_package_data=True,
    package_dir={'': 'src'},
    install_requires=['setuptools',
                      'pycountry',
                      'zope.i18nmessageid',
                      'zc.sourcefactory>=0.3.3',
                      'zope.deferredimport'],
    extras_require = dict(
        test=['zope.testing',
              'zope.app.testing',
              'zope.security',
              'zope.schema'])
)
