==============
gocept.country
==============


`gocept.country` provides Zope 3 sources for the pycountry databases. You can
use it e.g. to get a ``zope.schema.Choice`` field with all ISO 3166 countries.

  >>> import gocept.country
  >>> import gocept.country.db
  >>> import zope.schema


ISO 3166 Countries
==================

To get a list of ISO 3166 countries in a web form, you can use the
``zope.schema.Choice`` field and provide the gocept.country.countries as
source:

  >>> countries_field = zope.schema.Choice(title=u'Country',
  ...                            source=gocept.country.countries)
  >>> countries_field
  <zope.schema._field.Choice object at 0x...>
  >>> countries = iter(countries_field.source)


The ``gocept.country.countries`` source factory returns Country objects as
values, which use the values from pycountry:

  >>> aruba = next(countries)
  >>> afghanistan = next(countries)
  >>> afghanistan
  <gocept.country.db.Country object at 0x...>
  >>> print(afghanistan.name)
  Afghanistan


Calling ``next()`` again returns the next country from the source:

  >>> angola = next(countries)
  >>> print(angola.name)
  Angola


There are all information available, which you can get from pycountry:

  >>> print(afghanistan.alpha_2)
  AF
  >>> print(afghanistan.alpha_3)
  AFG
  >>> print(afghanistan.numeric)
  004
  >>> print(afghanistan.official_name)
  Islamic Republic of Afghanistan


To reduce the amount of results you can provide a list or tuple of countries
you like to have in your source:

  >>> countries = gocept.country.CountrySource(alpha_2=['DE', 'US'])
  >>> print(*[countries.factory.getTitle(x) for x in countries], sep=', ')
  Germany, United States
  >>> print(*[countries.factory.getToken(x) for x in countries], sep=', ')
  DE, US

Please note, that the result items are sorted by *alpha_2* code. Please also
note, that you can provide alpha_3 and numeric codes and names resp.
official_names to reduce the amount of result items, too:

  >>> len(list(gocept.country.CountrySource())) > 200
  True
  >>> len(list(gocept.country.CountrySource(alpha_2=['DE', 'US', 'GB'])))
  3
  >>> len(list(gocept.country.CountrySource(alpha_3=['DEU', 'USA'])))
  2
  >>> len(list(gocept.country.CountrySource(numeric=['276', ])))
  1
  >>> countries_list = ['Germany', 'Italy', 'Poland', 'France']
  >>> len(list(gocept.country.CountrySource(name=countries_list)))
  4


Providing codes, which are not present, does not result in an exception but
in an empty list:

  >>> len(list(gocept.country.CountrySource(capital=['Berlin', 'Paris'])))
  0

ISO 3166-2 Country subdivisions
===============================

Context free source
-------------------

Country subdivisions are similar to countries:

  >>> subdivisions_field = zope.schema.Choice(
  ...     title=u'Country subdivisions', source=gocept.country.subdivisions)
  >>> subdivisions = iter(subdivisions_field.source)

  >>> canillo = next(subdivisions)
  >>> print(canillo.name)
  Canillo
  >>> print(canillo.code)
  AD-02

  >>> encamp = next(subdivisions)
  >>> print(encamp.name)
  Encamp
  >>> print(encamp.code)
  AD-03
  >>> print(gocept.country.subdivisions.factory.getToken(encamp))
  AD-03

Please note, that the result items are sorted by their *code*. Please
also note, that you can provide names and numeric codes to reduce the
amount of result items, too.

  >>> len(list(gocept.country.SubdivisionSource())) > 4000
  True
  >>> len(list(gocept.country.SubdivisionSource(code=['DE-ST', 'US-WA'])))
  2
  >>> len(list(gocept.country.SubdivisionSource(country_code=['DE'])))
  16
  >>> print(*[x.name
  ...         for x in gocept.country.SubdivisionSource(country_code=['DE'])][3:5],
  ...       sep=', ')
  Bayern, Bremen
  >>> len(list(gocept.country.SubdivisionSource(name=[u'Bayern', u'Bremen'])))
  2

Contextual source
-----------------

There is also a contextual source for country subdivisions which
depends on a country. Let's set up a context object first:

  >>> import zope.interface
  >>> class IAddress(zope.interface.Interface):
  ...     country = zope.interface.Attribute("The country of the address.")
  ...     subdivision = zope.schema.Choice(
  ...         title=u'Country subdivisions',
  ...         source=gocept.country.contextual_subdivisions)

  >>> @zope.interface.implementer(IAddress)
  ... class Address(object):
  ...     pass
  >>> address = Address()
  >>> address.country = gocept.country.db.Country('DE')

The contextual source expects an adapter between the context and
``gocept.country.interfaces.ICountry``:

  >>> import zope.component
  >>> import gocept.country.interfaces
  >>> def get_country(context):
  ...     return context.country
  >>> zope.component.provideAdapter(
  ...    get_country, (IAddress, ), gocept.country.interfaces.ICountry)

  >>> print(gocept.country.interfaces.ICountry(address).name)
  Germany

So the source contains only the country subdivisions belonging to the
country:

  >>> len(list(iter(gocept.country.contextual_subdivisions(address))))
  16
  >>> print(*[x.name
  ...         for x in iter(gocept.country.contextual_subdivisions(address))][3:5],
  ...       sep=', ')
  Bayern, Bremen

Changing the country changes also the subdivisions:

  >>> address.country = gocept.country.db.Country('CH')
  >>> len(list(iter(gocept.country.contextual_subdivisions(address))))
  26
  >>> print(*[x.name
  ...         for x in iter(gocept.country.contextual_subdivisions(address))],
  ...       sep=', ')
  Aargau, Appenzell Innerrhoden, ...
  >>> print(*[x.code
  ...         for x in iter(gocept.country.contextual_subdivisions(address))],
  ...       sep=', ')
  CH-AG, CH-AI, ...
  >>> print(*[gocept.country.contextual_subdivisions.factory.getToken(address, x)
  ...         for x in iter(gocept.country.contextual_subdivisions(address))],
  ...       sep=', ')
  CH-AG, CH-AI, ...

  >>> print(gocept.country.contextual_subdivisions.factory.getTitle(
  ...     address, gocept.country.db.Subdivision('CH-AG')))
  Aargau

If the country is not set there are no subdivisions:

  >>> address.country = None
  >>> len(list(iter(gocept.country.contextual_subdivisions(address))))
  0
  >>> list(iter(gocept.country.contextual_subdivisions(address)))
  []


ISO 15924 Scripts
=================

Scripts are similar to countries:

  >>> scripts_field = zope.schema.Choice(title=u'Script',
  ...                            source=gocept.country.scripts)
  >>> scripts = iter(scripts_field.source)


  >>> adlam = next(scripts)
  >>> print(adlam.name)
  Adlam

  >>> afaka = next(scripts)
  >>> print(afaka.name)
  Afaka
  >>> print(gocept.country.scripts.factory.getToken(afaka))
  Afak


Please note, that the result items are sorted by *alpha_4* code. Please also
note, that you can provide names and numeric codes to smaller the amount of
result items, too.

  >>> len(list(gocept.country.ScriptSource())) > 130
  True
  >>> len(list(gocept.country.ScriptSource(alpha_4=['Arab', 'Latn'])))
  2
  >>> len(list(gocept.country.ScriptSource(numeric=['215', ])))
  1
  >>> len(list(gocept.country.ScriptSource(name=['Arabic', 'Latin'])))
  2


ISO 4217 Currencies
===================

Currencies are similar to the ones before:

  >>> currencies_field = zope.schema.Choice(title=u'Currency',
  ...                            source=gocept.country.currencies)

  >>> currencies = iter(currencies_field.source)

  >>> dirham = next(currencies)
  >>> print(dirham.name)
  UAE Dirham

  >>> afghani = next(currencies)
  >>> print(afghani.name)
  Afghani
  >>> print(gocept.country.currencies.factory.getToken(afghani))
  AFN

Please note, that the result items are sorted by *alpha_3* code. Please also
note, that you can provide names and numeric codes to reduce the amount of
result items, too.

  >>> len(list(gocept.country.CurrencySource())) >= 170
  True
  >>> len(list(gocept.country.CurrencySource(alpha_3=['ARS', 'AED', 'AFN'])))
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

  >>> ghotuo = next(languages)
  >>> print(ghotuo.name)
  Ghotuo

  >>> alumu_tesu = next(languages)
  >>> print(alumu_tesu.name)
  Alumu-Tesu
  >>> print(gocept.country.languages.factory.getToken(alumu_tesu))
  aab

Please note, that the result items are sorted by *alpha_3*. Please also
note, that you can provide names to reduce the amount of result items, too.

  >>> len(list(gocept.country.LanguageSource())) > 480
  True
  >>> len(list(gocept.country.LanguageSource(alpha_3=['eng', 'deu'])))
  2
  >>> len(list(gocept.country.LanguageSource(name=['English', 'German'])))
  2


Translations
============


First we fetch a specific country:

  >>> countries = list(iter(countries_field.source))
  >>> germany = [x for x in countries if x.name == u'Germany'][0]


The i18n translate method translates 'Germany' into German:

  >>> print(zope.i18n.translate(germany.name, target_language='de'))
  Deutschland


There are also translations for scripts, currencies and languages.


Comparison
==========


Countries, scripts, currencies and languages can be compared to equality. To
test this, we will need another country object ``afghanistan``, which is not
the *same* object as retrieved before:


  >>> afghanistan = next(iter(gocept.country.CountrySource(alpha_2=['AF'])))
  >>> afghanistan2 = next(iter(gocept.country.CountrySource(alpha_2=['AF'])))

  >>> str(afghanistan) == str(afghanistan2)
  False


Comparing them will get the token for each and compare it:

  >>> afghanistan == afghanistan2
  True
  >>> afghanistan != afghanistan2
  False
  >>> afghanistan != germany
  True
  >>> afghanistan == germany
  False


Comparing with an instance of another class always returns False:

  >>> afghanistan == None
  False
  >>> afghanistan != None
  True
  >>> afghanistan == object()
  False
  >>> afghanistan != object()
  True


Pickling and unpickling
=======================


It should be possible to store "proxy objects" in a database (like the ZODB).
Therefore, they have to be pickleable:

  >>> from io import BytesIO
  >>> import pickle
  >>> f = BytesIO(b'')

Pickling a country should never raise an error...

  >>> pickle.dump(afghanistan, f)


... and results in storing the token in the pickle:

  >>> ignored = f.seek(0)
  >>> b'AF' in f.read()
  True


Reading the pickle again will return the same country which was pickled
before:

  >>> ignored = f.seek(0)
  >>> afghanistan2 = pickle.load(f)
  >>> afghanistan2 == afghanistan
  True
  >>> print(afghanistan2.name)
  Afghanistan
