==============
gocept.country
==============


gocept.country provides Zope 3 sources for the pycountry databases. You can
use it e.g. to get a zope.schema.Choice field with all iso 3166 countries.

  >>> import gocept.country


ISO 3166 countries
==================


For the iso 3166 countries, use the gocept.pycountry.countries sourcefactory:

  >>> country_source = gocept.country.countries
  >>> country_source
  <zc.sourcefactory.source.FactoredSource object at 0x...>


Use the getValues() method to get an countries iterator:

  >>> country_iterator = country_source.factory.getValues()
  >>> country_iterator
  <listiterator object at 0x...>


That iterator can be used to retrieve the countries:

  >>> country= country_iterator.next()
  >>> country
  <pycountry.db.Country object at 0x...>


The method getTitle(country) returns the iso 3166 name of a country.
getToken(country) returns the alpha 2 value of the given country.

  >>> country_source.factory.getTitle(country)
  u'Afghanistan'
  >>> country_source.factory.getToken(country)
  'AF'
