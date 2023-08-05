# Configuration file for the Sphinx documentation builder.

import setuptools_scm

# -- Project information -----------------------------------------------------

project = "Unprompt"
copyright = "2023, Tyler Hughes"
author = "Tyler Hughes"
version = setuptools_scm.get_version("..")

# -- General configuration ---------------------------------------------------

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.doctest",
    "sphinx.ext.duration",
    "sphinx.ext.intersphinx",
    "sphinx.ext.viewcode",
    "sphinx_autodoc_typehints",
    "sphinx_rtd_theme",
]
exclude_patterns = [
    "_build",
    "Thumbs.db",
    ".DS_Store",
]
templates_path = ["_templates"]

# -- Extension configuration -------------------------------------------------

autoclass_content = "both"
autodoc_default_options = {
    "members": True,
    "inherited-members": True,
    "private-members": True,
    "show-inheritance": True,
}
autodoc_default_flags = [
    "members",
    "inherited-members",
    "private-members",
    "special-members",
    "show-inheritance",
]
autodoc_typehints = "description"
autodoc_typehints_format = "short"
autodoc_typehints_description_target = "documented"

autosummary_default_options = {
    "nosignatures": True,
}
autosummary_generate = True

intersphinx_disabled_domains = ["std"]
intersphinx_mapping = {
    "rtd": ("https://docs.readthedocs.io/en/stable/", None),
    "python": ("https://docs.python.org/3/", None),
    "sphinx": ("https://www.sphinx-doc.org/en/master/", None),
}

napoleon_preprocess_types = True
napoleon_use_param = True
napoleon_use_rtype = True

todo_include_todos = True

# -- Options for HTML output -------------------------------------------------

html_theme = "sphinx_rtd_theme"
html_context = {
    "display_github": True,
    "github_user": "tylerh111",
    "github_repo": "unprompt",
    "github_version": version,
}

rst_prolog = """
.. attention::
    This site is under construction
.. role:: bash(code)
    :language: bash
.. role:: python(code)
    :language: python
    :class: highlight
"""
