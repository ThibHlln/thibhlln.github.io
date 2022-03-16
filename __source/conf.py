# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or classes to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
from datetime import datetime
import os
import sys
sys.path.insert(0, os.path.abspath('..'))


# -- Project information -----------------------------------------------------

project = 'thibhlln.github.io'
author = 'Thibault Hallouin'
copyright = (
    f'2022-{datetime.now().year}, {author}'
    if datetime.now().year != 2022
    else f'2022, {author}'
)


# -- General configuration ---------------------------------------------------

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    'sphinx.ext.doctest',
    'sphinx.ext.autosectionlabel',
    'sphinx.ext.githubpages',
    'sphinx.ext.mathjax',
    'sphinx_panels'
]

# Boolean indicating whether to scan all found documents for
# autosummary directives, and to generate stub pages for each
# (http://sphinx-doc.org/latest/ext/autosummary.html)
autosummary_generate = True

# Both the class’ and the __init__ method’s docstring are concatenated
# and inserted.
autoclass_content = 'both'

# This value selects how automatically documented members are sorted
# (http://sphinx-doc.org/latest/ext/autodoc.html)
autodoc_member_order = 'bysource'
autosummary_member_order = 'bysource'

# This value is a list of autodoc directive flags that should be
# automatically applied to all autodoc
# directives. (http://sphinx-doc.org/latest/ext/autodoc.html)
autodoc_default_flags = ['members', 'inherited-members', 'show-inheritance']

# Add any paths that contain templates here, relative to this directory.
templates_path = ['../__templates']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['Thumbs.db', '.DS_Store']

# The reST default role (used for this markup: `text`) to use for all
# documents.
# default_role = None

# If true, '()' will be appended to :func: etc. cross-reference text.
add_function_parentheses = False

# If true, the current module name will be prepended to all
# description unit titles (such as .. function::).
add_module_names = True

# If true, sectionauthor and moduleauthor directives will be shown in
# the output. They are ignored by default.
show_authors = False

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'
pygments_dark_style = 'monokai'

# The default language to highlight source code
highlight_language = 'python'

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = False

# -- Options for HTML output -------------------------------------------------

html_theme = 'furo'
html_title = 'Thibault Hallouin'
language = 'en'

html_static_path = ['../__static']
html_css_files = ['custom.css']

html_theme_options = {
    "light_css_variables": {
        "font-stack": "Open Sans, sans-serif",
        "font-stack--monospace": "JetBrains Mono, monospace",
        "color-brand-primary": "var(--color-foreground-primary)",
        "color-brand-content": "#269fd9",
    },
    "dark_css_variables": {
        "color-code-background": "#18181a",
        "color-brand-primary": "var(--color-foreground-primary)",
        "color-brand-content": "#5ab6e2",
    },
    "footer_icons": [
        {
            "name": "On GitHub",
            "url": "https://github.com/thibhlln",
            "html": """
                <svg stroke="currentColor" fill="currentColor" stroke-width="0" viewBox="0 0 16 16">
                    <path fill-rule="evenodd" d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0 0 16 8c0-4.42-3.58-8-8-8z"></path>
                </svg>
            """,
            "class": ""
        },
        {
            "name": "On Twitter",
            "url": "https://twitter.com/thibhlln",
            "html": """
                <svg stroke="currentColor" fill="currentColor" stroke-width="0" viewBox="0 0 112.2 112.2">
                    <path fill-rule="evenodd"  d="m93.598 34.839c-2.7587 1.2233-5.7262 2.0506-8.8382 2.4201 3.1775-1.9037 5.616-4.916 6.767-8.5112-2.9732 1.7637-6.2678 3.0432-9.7712 3.7329-2.8068-2.9893-6.806-4.8575-11.234-4.8575-8.4963 0-15.387 6.8909-15.387 15.387 0 1.206 0.13656 2.38 0.40049 3.5068-12.788-0.64147-24.127-6.767-31.716-16.079-1.3242 2.2721-2.0839 4.9171-2.0839 7.7366 0 5.3371 2.7185 10.049 6.845 12.808-2.5211-0.07918-4.8953-0.77114-6.9689-1.9267-0.0011 0.06541-0.0011 0.13082-0.0011 0.19508 0 7.4555 5.3062 13.674 12.344 15.087-1.2898 0.35344-2.6519 0.54048-4.0531 0.54048-0.99376 0-1.9565-0.09524-2.8952-0.27426 1.9577 6.1117 7.6391 10.561 14.374 10.686-5.2671 4.1277-11.901 6.5868-19.112 6.5868-1.2393 0-2.4672-0.07229-3.6686-0.21574 6.806 4.3675 14.896 6.9138 23.585 6.9138 28.303 0 43.78-23.446 43.78-43.782 0-0.66671-0.01492-1.3311-0.04475-1.9898 3.0088-2.1688 5.6171-4.8781 7.6792-7.9638zm18.598 21.26a56.098 56.098 0 0 1-56.098 56.098 56.098 56.098 0 0 1-56.098-56.098 56.098 56.098 0 0 1 56.098-56.098 56.098 56.098 0 0 1 56.098 56.098z"></path>
                </svg>
            """,
            "class": ""
        },
        {
            "name": "ORCID",
            "url": "https://orcid.org/0000-0003-0144-2989",
            "html": """
                <svg stroke="currentColor" fill="currentColor" stroke-width="0" viewBox="0 0 24 24">
                    <path fill-rule="evenodd" d="M12 0C5.372 0 0 5.372 0 12s5.372 12 12 12 12-5.372 12-12S18.628 0 12 0zM7.369 4.378c.525 0 .947.431.947.947s-.422.947-.947.947a.95.95 0 0 1-.947-.947c0-.525.422-.947.947-.947zm-.722 3.038h1.444v10.041H6.647V7.416zm3.562 0h3.9c3.712 0 5.344 2.653 5.344 5.025 0 2.578-2.016 5.025-5.325 5.025h-3.919V7.416zm1.444 1.303v7.444h2.297c3.272 0 4.022-2.484 4.022-3.722 0-2.016-1.284-3.722-4.097-3.722h-2.222z"></path>
                </svg>
            """,
            "class": ""
        },
    ],
}

html_sidebars = {}

html_baseurl = 'https://thibhlln.github.io/'

html_logo = '../__images/thibhlln.svg'

html_favicon = '../__images/thibhlln.ico'

html_permalinks_icon = '<span class="fa fa-link">'


# If not '', a 'Last updated on:' timestamp is inserted at every page
# bottom, using the given strftime format.
html_last_updated_fmt = '%b %d, %Y'

# If true, SmartyPants will be used to convert quotes and dashes to
# typographically correct entities.
html_use_smartypants = True

# Additional templates that should be rendered to pages, maps page
# names to template names.
# html_additional_pages = {}

# If false, no module index is generated.
html_domain_indices = True

# If false, no index is generated.
html_use_index = True

# If true, the index is split into individual pages for each letter.
html_split_index = False

html_show_sourcelink = False

html_context = {}

# -- Extension configuration -------------------------------------------------

# -- Options for intersphinx extension ---------------------------------------

intersphinx_mapping = {
    'sphinx': ('https://www.sphinx-doc.org/en/master/',  None),
    'python': ('https://docs.python.org/3', None),
    'numpy': ('https://docs.scipy.org/doc/numpy', None),
    'cfunits': ('https://ncas-cms.github.io/cfunits', None)
}

intersphinx_cache_limit = 5

# -- Options for mathjax extension ---------------------------------------

# to get left alignment of equations
mathjax3_config = {
    "chtml": {
        "displayAlign": "left"
    },
    "options": {
        "ignoreHtmlClass": "tex2jax_ignore",
        "processHtmlClass": "tex2jax_process"
    }
}
