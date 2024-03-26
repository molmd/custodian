"""
pymatgen documentation build configuration file, created by
sphinx-quickstart on Tue Nov 15 00:13:52 2011.

This file is execfile()d with the current directory set to its containing dir.

Note that not all possible configuration values are present in this
autogenerated file.

All configuration values have a default; values that are commented out
serve to show the default.
"""

from __future__ import annotations

from pymatgen.core import __author__

project = "pymatgen"
copyright = "2022, Materials Virtual Lab"
author = __author__


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
# Napoleon is necessary to parse Google style docstrings. Markdown builder allows the generation of markdown output.
extensions = ["sphinx.ext.autodoc", "sphinx.ext.napoleon", "myst_parser", "sphinx_markdown_builder"]
# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]
autoclass_content = "both"

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "alabaster"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]

myst_heading_anchors = 3

autodoc_default_options = {"private-members": False}