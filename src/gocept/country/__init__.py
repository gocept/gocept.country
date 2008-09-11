import zc.sourcefactory.basic
import pycountry

import gocept.country.db


class BasicSource(zc.sourcefactory.basic.BasicSourceFactory):
    """A basic source for countries, scripts, languages and currencies."""

    def __init__(self, **kw):
        super(BasicSource, self).__init__()
        self.filter = kw

    def __contains__(self, item):
        for token, values in self.filter.items():
            if (getattr(item, token, None) not in values):
                return False
        return True

    def getTitle(self, value):
        return value.name


class CountrySource(BasicSource):
    """Source for the pycountry countries."""

    def getValues(self):
        for country in pycountry.countries:
            if country in self:
                yield gocept.country.db.Country(country.alpha2)

    def getToken(self, value):
        return value.alpha2


class SubdivisionSource(BasicSource):
    """Source for the pycountry country subdivisions."""

    def getValues(self):
        for subdivision in pycountry.subdivisions:
            if subdivision in self:
                yield gocept.country.db.Subdivision(subdivision.code)

    def getToken(self, value):
        return value.code

class ScriptSource(BasicSource):
    """Source for the pycountry scripts."""

    def getValues(self):
        for script in pycountry.scripts:
            if script in self:
                yield gocept.country.db.Script(script.alpha4)

    def getToken(self, value):
        return value.alpha4


class CurrencySource(BasicSource):
    """Source for the pycountry currencies."""

    def getValues(self):
        for currency in pycountry.currencies:
            if currency in self:
                yield gocept.country.db.Currency(currency.letter)

    def getToken(self, value):
        return value.letter


class LanguageSource(BasicSource):
    """Source for the pycountry languages."""

    def getValues(self):
        for language in pycountry.languages:
            if language in self:
                yield gocept.country.db.Language(language.bibliographic)

    def getToken(self, value):
        return value.bibliographic


countries = CountrySource()
subdivisions = SubdivisionSource()
scripts = ScriptSource()
currencies = CurrencySource()
languages = LanguageSource()
