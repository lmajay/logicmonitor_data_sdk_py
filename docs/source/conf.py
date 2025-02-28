"""
=======
Copyright, 2021, LogicMonitor, Inc.
This Source Code Form is subject to the terms of the 
Mozilla Public License, v. 2.0. If a copy of the MPL 
was not distributed with this file, You can obtain 
one at https://mozilla.org/MPL/2.0/.
=======
"""

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
import os
import sys

sys.path.insert(0, os.path.abspath('../..'))
sys.setrecursionlimit(1500)

# -- Project information -----------------------------------------------------
_version = {}
with open("../../logicmonitor_data_sdk/version.py") as fp:
  exec(fp.read(), _version)

project = 'LogicMonitor DATA SDK Python'
copyright = '2021, Logicmonitor'
author = 'Logicmonitor'

# The full version, including alpha/beta/rc tags
release = str(_version["__version__"])

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
# extensions = ['rinoh.frontend.sphinx', 'sphinx.ext.autodoc', 'sphinx_markdown_builder']
extensions = ['sphinx.ext.napoleon', 'sphinx.ext.autosectionlabel', ]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']
pdf_documents = [('index', u'rst2pdf', u'Sample rst2pdf doc', u'Your Name'), ]

# Napoleon settings
napoleon_google_docstring = True
napoleon_numpy_docstring = True
napoleon_include_init_with_doc = False
napoleon_include_private_with_doc = False
napoleon_include_special_with_doc = False
napoleon_use_admonition_for_examples = True
napoleon_use_admonition_for_notes = False
napoleon_use_admonition_for_references = True
napoleon_use_ivar = True
napoleon_use_param = True
napoleon_use_rtype = True
napoleon_type_aliases = True
napoleon_attr_annotations = True
