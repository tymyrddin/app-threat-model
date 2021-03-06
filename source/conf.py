# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = 'Application threat model'
copyright = '2022, TyMyrddin'
author = 'TyMyrddin'

# The full version, including alpha/beta/rc tags
release = '0.1'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'myst_parser',
    'sphinx_markdown_tables',
    'sphinx.ext.intersphinx',
]

source_suffix = ['.rst', '.md']

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.

html_theme = 'sphinx_rtd_theme'

html_theme_options = {
    'display_version': True,
    'prev_next_buttons_location': 'bottom',
    'style_external_links': True,
    # Toc options
    'collapse_navigation': True,
    'sticky_navigation': False,
    'navigation_depth': 3,
    'includehidden': True,
    'titles_only': True
}

html_title = "Application threat model"
html_logo = "img/logo.png"
html_favicon = "img/favicon.ico"


# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# These paths are either relative to html_static_path
# or fully qualified paths (eg. https://...)
html_css_files = [
    'css/custom.css',
]

# If true, "Created using Sphinx" is shown in the HTML footer. Default is True.
html_show_sphinx = False

# If true, "(C) Copyright ..." is shown in the HTML footer. Default is True.
html_show_copyright = False

# Intersphinx
intersphinx_mapping = {
    "attack-trees": ("https://tymyrddin.github.io/attack-trees/", None),
    "cheatsheets": ("https://tymyrddin.github.io/cheatsheets/", None),
    "e2ee-threat-model":("https://tymyrddin.github.io/e2ee-threat-model/", None),
    "da-threat-model":("https://tymyrddin.github.io/da-threat-model/", None),
    "se-threat-model":("https://tymyrddin.github.io/se-threat-model/", None),
    "cicd-threat-model":("https://tymyrddin.github.io/cicd-threat-model/", None),
    "linux-pc-mitigations":("https://tymyrddin.github.io/linux-pc-mitigations/", None),
    "linux-server-mitigations":("https://tymyrddin.github.io/linux-server-mitigations/", None),
    "data-mitigations":("https://tymyrddin.github.io/data-mitigations/", None),
    "webserver-mitigations":("https://tymyrddin.github.io/webserver-mitigations/", None),
    "mailserver-mitigations":("https://tymyrddin.github.io/mailserver-mitigations/", None),
    "network-mitigations":("https://tymyrddin.github.io/network-mitigations/", None),
    "app-mitigations": ("https://tymyrddin.github.io/app-mitigations/", None),
}
myst_url_schemes = ["http", "https", ]

