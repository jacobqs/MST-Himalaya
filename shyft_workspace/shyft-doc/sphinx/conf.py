# -*- coding: utf-8 -*-
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import os
import shutil
import datetime

import sphinx_rtd_theme
from recommonmark.parser import CommonMarkParser


# -- Project information -----------------------------------------------------

project = 'Shyft'
copyright = f'{datetime.date.today().strftime("%Y")}, The Shyft project'
author = 'Alexander Becker, John F. Burkhart, Sarah Dahmen, Sigbjørn Helset, Ola Skavhaug and others'
version = '4.15'
release = '4.12.88'

# -- General configuration ---------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
needs_sphinx = '3.5'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.coverage',
    'sphinx.ext.mathjax',
    'sphinx.ext.ifconfig',
    'sphinx.ext.intersphinx',
    'sphinx.ext.viewcode',
    'sphinx_rtd_theme',
    'nbsphinx',
    'IPython.sphinxext.ipython_console_highlighting'
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store', '**.ipynb_checkpoints']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
# source_suffix = ['.rst', '.md']
source_suffix = ['.rst', '.ipynb']
# Markdown support

source_parsers = {
    '.md': CommonMarkParser,
}

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = False


# -- Extension: nbsphinx ----------------------------------------------

nbsphinx_execute = 'never'
nbsphinx_timeout = 1500
nbsphinx_allow_errors = True


# -- Options for HTML output ----------------------------------------------

# General HTML page settings
# NOTE: the HTML meta tag description is set in index.rst and the below string will be appended to it
html_title = "Documentation"
html_short_title = "Documentation"
html_favicon = '_static/images/favicon.ico'

# The theme to use for HTML and HTML Help pages. See the documentation for
# a list of builtin themes.
html_theme = 'sphinx_rtd_theme'
html_theme_options = {
    'logo_only': False,
    'display_version': True,
    'prev_next_buttons_location': 'bottom',
    'style_external_links': False,
    # Toc options
    'collapse_navigation': True,
    'sticky_navigation': True,
    'navigation_depth': -1,
    'includehidden': True,
    'titles_only': False
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# These paths are either relative to html_static_path
# or fully qualified paths (eg. https://...)
html_css_files = [
    'css/bootstrap.min.css',
    'css/bootstrap-grid.min.css',
    'css/custom.css',
]
html_js_files = [
    'js/bootstrap.min.js',
    'js/bootstrap.bundle.min.js',
    'js/custom.js',
]

# If true, the index is split into individual pages for each letter.
html_split_index = True
