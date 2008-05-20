from zope.i18nmessageid import MessageFactory
import zc.sourcefactory.basic
import pycountry

iso3166msg = MessageFactory('iso3166')


class CountrySource(zc.sourcefactory.basic.BasicSourceFactory):

    def getValues(self):
        return iter(pycountry.countries)

    def getTitle(self, value):
        return iso3166msg(value.name)

    def getToken(self, value):
        return value.alpha2


countries = CountrySource()
