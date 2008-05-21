import zc.sourcefactory.basic
import pycountry

import gocept.country.db

class CountrySource(zc.sourcefactory.basic.BasicSourceFactory):
    """Source for the pycountry countries."""

    def getValues(self):
        for country in pycountry.countries:
            yield gocept.country.db.Country(country.alpha2)

    def getTitle(self, value):
        return value.name

    def getToken(self, value):
        return value.alpha2


class ScriptSource(zc.sourcefactory.basic.BasicSourceFactory):
    """Source for the pycountry scripts."""

    def getValues(self):
        for script in pycountry.scripts:
            yield gocept.country.db.Script(script.alpha4)

    def getTitle(self, value):
        return value.name

    def getToken(self, value):
        return value.alpha4


class CurrencySource(zc.sourcefactory.basic.BasicSourceFactory):
    """Source for the pycountry currencies."""

    def getValues(self):
        for currency in pycountry.currencies:
            yield gocept.country.db.Currency(currency.letter)

    def getTitle(self, value):
        return value.name

    def getToken(self, value):
        return value.letter


class LanguageSource(zc.sourcefactory.basic.BasicSourceFactory):
    """Source for the pycountry languages."""

    def getValues(self):
        for language in pycountry.languages:
            yield gocept.country.db.Language(language.bibliographic)

    def getTitle(self, value):
        return value.name

    def getToken(self, value):
        return value.bibliographic


countries = CountrySource()
scripts = ScriptSource()
currencies = CurrencySource()
languages = LanguageSource()
