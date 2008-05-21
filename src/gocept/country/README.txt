==============
gocept.country
==============


gocept.country provides Zope 3 sources for the pycountry databases. You can
use it e.g. to get a zope.schema.Choice field with all iso 3166 countries.

  >>> import gocept.country
  >>> import gocept.country.db
  >>> import zope.schema


ISO 3166 countries
==================

To get a list of ISO 3166 countries in a webform, you can use the
zope.schema.Choice field and provide the gocept.country.countries as source:

  >>> countries_field = zope.schema.Choice(title=u'Country',
  ...                            source=gocept.country.countries)
  >>> countries_field
  <zope.schema._field.Choice object at 0x...>
  >>> countries = iter(countries_field.source)


The gocept.country.countries sourcefactory returns Country objects as values,
which use the values from pycountry:

  >>> afghanistan = countries.next()
  >>> afghanistan
  <gocept.country.db.Country object at 0x...>
  >>> afghanistan.name
  u'Afghanistan'

Calling the next() method again returns the next country from the source:

  >>> islands = countries.next()
  >>> islands.name
  u'\xc5land Islands'


There are all information available, which you can get from pycountry:

  >>> afghanistan.alpha2
  'AF'
  >>> afghanistan.alpha3
  'AFG'
  >>> afghanistan.numeric
  '004'
  >>> afghanistan.official_name
  'Islamic Republic of Afghanistan'


ISO 15924 Scripts
=================

Scripts are similar to countries:

  >>> scripts_field = zope.schema.Choice(title=u'Script',
  ...                            source=gocept.country.scripts)
  >>> scripts = iter(scripts_field.source)


  >>> arabic = scripts.next()
  >>> arabic.name
  u'Arabic'

  >>> aramaic = scripts.next()
  >>> aramaic.name
  u'Imperial Aramaic'


ISO 4217 Currencies
===================

Currencies are, again, similar to the ones before:

  >>> currencies_field = zope.schema.Choice(title=u'Currency',
  ...                            source=gocept.country.currencies)

  >>> currencies = iter(currencies_field.source)

  >>> dirham = currencies.next()
  >>> dirham.name
  u'UAE Dirham'

  >>> afghani = currencies.next()
  >>> afghani.name
  u'Afghani'


ISO 639 Languages
=================

Languages are similar, too:

  >>> languages_field = zope.schema.Choice(title=u'Language',
  ...                            source=gocept.country.languages)

  >>> languages = iter(languages_field.source)

  >>> afar = languages.next()
  >>> afar.name
  u'Afar'

  >>> abkhazian = languages.next()
  >>> abkhazian.name
  u'Abkhazian'


Translations
============


First we fetch a specific country:

  >>> countries = list(iter(countries_field.source))
  >>> germany = countries[80]
  >>> germany.name
  u'Germany'


The i18n translate method translates 'Germany' into german:

  >>> zope.i18n.translate(germany.name, target_language='de')
  u'Deutschland'
