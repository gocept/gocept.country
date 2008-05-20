==============
gocept.country
==============


gocept.country provides Zope 3 sources for the pycountry databases. You can
use it e.g. to get a zope.schema.Choice field with all iso 3166 countries.

  >>> import gocept.pycountry


ISO 3166 countries
==================


For the iso 3166 countries, use the gocept.pycountry.countries iterator:

  >>> gocept.pycountry.countries.getValues()
