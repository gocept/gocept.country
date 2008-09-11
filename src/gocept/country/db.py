import zope.i18nmessageid
import pycountry

iso3166msg = zope.i18nmessageid.MessageFactory('iso3166')
iso3166_2msg = zope.i18nmessageid.MessageFactory('iso3166_2')
iso15924msg = zope.i18nmessageid.MessageFactory('iso15924')
iso4217msg = zope.i18nmessageid.MessageFactory('iso4217')
iso639msg = zope.i18nmessageid.MessageFactory('iso639')


class Data(object):
    """ """

    def __init__(self, token):
        self.token = token

    def __eq__(self, other):
        if not other:
            return False
        if not isinstance(other, self.__class__):
            return False
        return self.token == other.token

    def __reduce__(self):
        return (self.__class__, (self.token, ))

    def __getattr__(self, name):
        return getattr(self._obj, name)

    @property
    def name(self):
        return self._msg(self._obj.name)


class Country(Data):
    """Provides access to pycountry countries (ISO 3166)."""

    _msg = iso3166msg

    @property
    def _obj(self):
        return pycountry.countries.get(alpha2=self.token)


class Subdivision(Data):
    """Provides access to pycountry country subdivisions (ISO 3166-2)."""

    _msg = iso3166_2msg

    @property
    def _obj(self):
        return pycountry.subdivisions.get(code=self.token)


class Script(Data):
    """Provides access to pycountry scripts (ISO 15924)."""

    _msg = iso15924msg

    @property
    def _obj(self):
        return pycountry.scripts.get(alpha4=self.token)


class Currency(Data):
    """Provides access to pycountry currencies (ISO 4217)."""

    _msg = iso4217msg

    @property
    def _obj(self):
        return pycountry.currencies.get(letter=self.token)


class Language(Data):
    """Provides access to pycountry languages (ISO 639-1/2)."""

    _msg = iso639msg

    @property
    def _obj(self):
        return pycountry.languages.get(bibliographic=self.token)
