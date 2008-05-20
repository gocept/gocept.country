from zope.i18nmessageid import MessageFactory
import zc.sourcefactory.basic
import pycountry

iso3166msg = MessageFactory('iso3166')


class CountrySource(zc.sourcefactory.basic.BasicSourceFactory):
    """Source for the pycountry countries."""

    def getValues(self):
        return iter(pycountry.countries)

    def getTitle(self, value):
        return iso3166msg(value.name)

    def getToken(self, value):
        return value.alpha2


class ScriptSource(zc.sourcefactory.basic.BasicSourceFactory):
    """Source for the pycountry scripts."""

    def getValues(self):
        return iter(pycountry.scripts)

    def getTitle(self, value):
        return iso3166msg(value.name)

    def getToken(self, value):
        return value.alpha4


class CurrencySource(zc.sourcefactory.basic.BasicSourceFactory):
    """Source for the pycountry currencies."""

    def getValues(self):
        return iter(pycountry.currencies)

    def getTitle(self, value):
        return iso3166msg(value.name)

    def getToken(self, value):
        return value.letter


class LanguageSource(zc.sourcefactory.basic.BasicSourceFactory):
    """Source for the pycountry languages."""

    def getValues(self):
        return iter(pycountry.languages)

    def getTitle(self, value):
        return iso3166msg(value.name)

    def getToken(self, value):
        return value.alpha2


countries = CountrySource()
scripts = ScriptSource()
currencies = CurrencySource()
languages = LanguageSource()
