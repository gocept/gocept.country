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

  >>> afghanistan = country_iterator.next()
  >>> afghanistan
  <pycountry.db.Country object at 0x...>


The method getTitle(country) returns the iso 3166 name of a country.
getToken(country) returns the alpha 2 value of the given country.

  >>> country_source.factory.getTitle(afghanistan)
  u'Afghanistan'
  >>> country_source.factory.getToken(afghanistan)
  'AF'


ISO 639 languages
=================

The iso 639 languages are available similar to the countries:

  >>> afar = gocept.country.languages.factory.getValues().next()
  >>> afar
  <pycountry.db.Language object at 0x...>
  >>> gocept.country.languages.factory.getTitle(afar)
  u'Afar'
  >>> gocept.country.languages.factory.getToken(afar)
  'aa'


ISO 15924 scripts
=================

The iso 14924 scripts are available similar to the countries:

  >>> arabic = gocept.country.scripts.factory.getValues().next()
  >>> arabic
  <pycountry.db.Script object at 0x...>
  >>> gocept.country.scripts.factory.getTitle(arabic)
  u'Arabic'
  >>> gocept.country.scripts.factory.getToken(arabic)
  'Arab'


ISO 4217 currencies
===================

The iso 4217 currencies are available similar to the countries:

  >>> dirham = gocept.country.currencies.factory.getValues().next()
  >>> dirham
  <pycountry.db.Currency object at 0x...>
  >>> gocept.country.currencies.factory.getTitle(dirham)
  u'UAE Dirham'
  >>> gocept.country.currencies.factory.getToken(dirham)
  'AED'
