#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Oscar Vargas Torres'
SITENAME = "oscarvarto's blog"
SITEURL = ''

PATH = 'content'

TIMEZONE = 'America/Mexico_City'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Scala-lang.org', 'https://www.scala-lang.org/'),
         ('Python.org', 'https://python.org/'),
         ('Haskell.org', 'https://www.haskell.org/'),)

# Social widget
SOCIAL = (('twitter', 'https://twitter.com/oscarvarto'),
          ('github', 'https://github.com/oscarvarto'),
          ('linkedin', 'https://www.linkedin.com/in/oscar-vargas-torres-32145546'),)

DEFAULT_PAGINATION = 5

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
MARKUP = ('md', 'ipynb', 'org')
IPYNB_USE_METACELL = True
IPYNB_IGNORE_CSS=False
IPYNB_EXTEND_STOP_SUMMARY_TAGS = [('h2', None), ('ol', None), ('ul', None)]
IGNORE_FILES = ['.#*', '__pycache__', '.ipynb_checkpoints']
IPYNB_PREPROCESSORS = ['pre_cite2c.BibTexPreprocessor']

JINJA_ENVIRONMENT = {'extensions': ['jinja2.ext.i18n']}
BOOTSTRAP_THEME = 'cosmo'
THEME = '../pelican-themes/pelican-bootstrap3'
PYGMENTS_STYLE = 'monokai'

MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.codehilite': {'css_class': 'highlight'},
        'markdown.extensions.extra': {},
        'markdown.extensions.meta': {},
    },
    'output_format': 'html5',
}

MATH_JAX = {'color': 'black', 'align': 'left', 'tex_extensions': ['color.js','mhchem.js']}

ORG_READER_EMACS_LOCATION='/usr/bin/emacs'

PLUGIN_PATHS = ['./plugins', '../pelican-plugins/']

PLUGINS = ['render_math', 'i18n_subsites', 'pelican-ipynb.markup', 'pelican-ipynb.liquid', 'liquid_tags.youtube', 'liquid_tags.b64img', "org_reader"]
STATIC_PATHS = ['data', 'images']
