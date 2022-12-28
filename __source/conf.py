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
            "name": "On Mastodon",
            "url": "https://mas.to/@thibh",
            "html": """
                <svg stroke="currentColor" fill="currentColor" stroke-width="0" viewBox="0 0 512 512">
                    <path fill-rule="evenodd"  d="M256 0c141.284 0 256 114.563 256 256 0 141.284-114.563 256-256 256C114.716 512 0 397.437 0 256 0 114.716 114.563 0 256 0zm134.506 175.487c-4.177-31.049-31.239-55.52-63.32-60.261-5.412-.801-25.918-3.717-73.421-3.717h-.354c-47.516 0-57.709 2.916-63.121 3.717-31.188 4.61-59.669 26.596-66.579 58.014-3.323 15.472-3.678 32.627-3.06 48.361.879 22.566 1.05 45.091 3.101 67.564a317.689 317.689 0 007.395 44.317c6.567 26.924 33.157 49.331 59.208 58.474a158.807 158.807 0 0086.622 4.57 126.28 126.28 0 009.367-2.561c6.988-2.22 15.173-4.701 21.191-9.063a.692.692 0 00.275-.525V362.6a.667.667 0 00-.066-.277.652.652 0 00-.721-.341 240.065 240.065 0 01-56.213 6.569c-32.58 0-41.342-15.46-43.849-21.895a67.833 67.833 0 01-3.812-17.259.611.611 0 01.054-.289.62.62 0 01.441-.361.644.644 0 01.293.006 235.518 235.518 0 0055.293 6.568c4.479 0 8.947 0 13.426-.12 18.732-.524 38.478-1.484 56.907-5.083.461-.091.921-.17 1.314-.288 29.073-5.583 56.739-23.104 59.55-67.472.104-1.748.368-18.296.368-20.108.012-6.16 1.983-43.699-.289-66.763zm-46.057 34.885v77.139H313.88v-74.867c0-15.761-6.569-23.8-19.929-23.8-14.689 0-22.045 9.511-22.045 28.291v40.981h-30.383v-40.981c0-18.78-7.371-28.291-22.058-28.291-13.281 0-19.915 8.039-19.915 23.8v74.867h-30.556v-77.139c0-15.761 4.025-28.283 12.072-37.565 8.303-9.26 19.193-14.014 32.711-14.014 15.645 0 27.468 6.016 35.35 18.033l7.607 12.767 7.62-12.767c7.881-12.017 19.705-18.033 35.323-18.033 13.506 0 24.395 4.754 32.724 14.014 8.041 9.274 12.056 21.796 12.048 37.565z"></path>
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
