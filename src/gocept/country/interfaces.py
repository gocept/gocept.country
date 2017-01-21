# -*- coding: latin-1 -*-
# Copyright (c) 2008-2017 gocept gmbh & co. kg

import zope.interface


class ICountry(zope.interface.Interface):
    """A Country (ISO 3166)."""

    name = zope.interface.Attribute("Name of the country.")
    alpha_2 = zope.interface.Attribute("Alpha2 code of the country.")
