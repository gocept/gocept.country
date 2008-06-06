==============
gocept.country
==============


gocept.country provides Zope 3 sources for the pycountry databases. You can
use it e.g. to get a zope.schema.Choice field with all iso 3166 countries.

  >>> import gocept.country
  >>> import gocept.country.db
  >>> import zope.schema


ISO 3166 Countries
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


To smaller the amount of results you can provide a list or tuple of countries
you like to have in your source:

  >>> countries = iter(gocept.country.CountrySource(alpha2=['DE', 'US']))
  >>> countries.next().name
  u'Germany'
  >>> countries.next().name
  u'United States'
  >>> countries.next().name
  Traceback (most recent call last):
  ...
  StopIteration


Please note, that the result items are sorted by *alpha2* code. Please also
note, that you can provide alpha3 and numeric codes and names resp.
official_names to smaller the amount of result items, too:

  >>> len(list(gocept.country.CountrySource()))
  246
  >>> len(list(gocept.country.CountrySource(alpha2=['DE', 'US', 'GB'])))
  3
  >>> len(list(gocept.country.CountrySource(alpha3=['DEU', 'USA'])))
  2
  >>> len(list(gocept.country.CountrySource(numeric=['276', ])))
  1
  >>> countries_list = ['Germany', 'Italy', 'Poland', 'France']
  >>> len(list(gocept.country.CountrySource(name=countries_list)))
  4


Providing codes, which are not present, does not results in an exception but
in an empty list:

  >>> len(list(gocept.country.CountrySource(capital=['Berlin', 'Paris'])))
  0


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


Please note, that the result items are sorted by *alpha4* code. Please also
note, that you can provide names and numeric codes to smaller the amount of
result items, too.

  >>> len(list(gocept.country.ScriptSource()))
  131
  >>> len(list(gocept.country.ScriptSource(alpha4=['Arab', 'Latn'])))
  2
  >>> len(list(gocept.country.ScriptSource(numeric=['215', ])))
  1
  >>> len(list(gocept.country.ScriptSource(name=['Arabic', 'Latin'])))
  2


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


Please note, that the result items are sorted by *letter* code. Please also
note, that you can provide names and numeric codes to smaller the amount of
result items, too.

  >>> len(list(gocept.country.CurrencySource()))
  183
  >>> len(list(gocept.country.CurrencySource(letter=['ARS', 'AED', 'AFN'])))
  3
  >>> len(list(gocept.country.CurrencySource(numeric=['032', '784'])))
  2
  >>> len(list(gocept.country.CurrencySource(name=['Afghani', ])))
  1


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


Please note, that the result items are sorted by *bibliographic*. Please also
note, that you can provide alpha2 and terminology codes and names to smaller
the amount of result items, too.

  >>> len(list(gocept.country.LanguageSource()))
  486
  >>> len(list(gocept.country.LanguageSource(alpha2=['an', 'en', 'de'])))
  3
  >>> len(list(gocept.country.LanguageSource(bibliographic=['eng', 'ger'])))
  2
  >>> len(list(gocept.country.LanguageSource(terminology=['arg', 'abk'])))
  2
  >>> len(list(gocept.country.LanguageSource(name=['English', 'German'])))
  2


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


Translations are also operating for scripts, currencies and languages.


Comparison
==========


Countries, scripts, currenties and languages can be compared to equality. To
test this, we will need another country object afghanistan, which is not the
*same* object as retrieved before:


  >>> countries = iter(countries_field.source)
  >>> afghanistan = countries.next()
  >>> countries = iter(countries_field.source)
  >>> afghanistan2 = countries.next()

  >>> str(afghanistan) == str(afghanistan2)
  False


Comparing them will get the token for each and compare it:

  >>> afghanistan == afghanistan2
  True


Pickling and unpickling
=======================


It should be possible to store "proxy objects" in a database (like the ZODB).
Therefore, they have to be pickleable:

  >>> import StringIO
  >>> import cPickle
  >>> f = StringIO.StringIO('')
  >>> f.read()
  ''


Pickling a country should never raise an error...

  >>> cPickle.dump(afghanistan, f)


... and results in storing the token in the pickle:

  >>> f.seek(0)
  >>> 'AF' in f.read()
  True


Reading the pickle again will return the same country which was pickled
before:

  >>> f.seek(0)
  >>> afghanistan2 = cPickle.load(f)
  >>> afghanistan2 == afghanistan
  True
  >>> afghanistan2.name
  u'Afghanistan'
