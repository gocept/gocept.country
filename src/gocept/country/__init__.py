# -*- coding: latin-1 -*-
# Copyright (c) 2008-2009 gocept gmbh & co. kg
# See also LICENSE.txt
# $Id$

import zope.deferredimport

zope.deferredimport.defineFrom(
    'gocept.country.sources',
    'CountrySource',
    'SubdivisionSource',
    'SubdivisionContextualSource',
    'ScriptSource',
    'CurrencySource',
    'LanguageSource',

    'countries',
    'subdivisions',
    'contextual_subdivisions',
    'scripts',
    'currencies',
    'languages',
)
