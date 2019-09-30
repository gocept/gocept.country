# vim:fileencoding=utf-8
import os.path
from setuptools import setup, find_packages


def read(*rnames):
    """Read a file from a path."""
    with open(os.path.join(os.curdir, *rnames)) as f:
        return f.read()

setup(
    name='gocept.country',
    version='2.1',
    author='gocept gmbh & co. kg',
    author_email='mail@gocept.com',
    description='Zope 3 sources for pycountry databases',
    long_description='\n\n'.join([
        read('COPYRIGHT.txt'),
        read('README.rst'),
        read('src', 'gocept', 'country', 'README.txt'),
        read('CHANGES.rst')]),
    license='ZPL 2.1',
    keywords='country subdivision language currency iso 3166 639 4217 '
             '15924 3166-2 zope pycountry',
    zip_safe=False,
    namespace_packages=['gocept'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved',
        'License :: OSI Approved :: Zope Public License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Topic :: Internet :: WWW/HTTP'],
    url='https://github.com/gocept/gocept.country',
    packages=find_packages('src'),
    include_package_data=True,
    package_dir={'': 'src'},
    install_requires=['setuptools',
                      'pycountry >= 16.0',
                      'zope.i18nmessageid',
                      'zc.sourcefactory>=0.3.3',
                      'zope.deferredimport'],
    extras_require=dict(
        test=['zope.testing',
              'zope.app.wsgi[testlayer]',
              'zope.security',
              'zope.schema'])
)
