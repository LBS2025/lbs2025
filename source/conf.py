# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'LBS Conference 2025'
copyright = 'LBS Conference 2025.'
release = 'v1.0'
author = 'LBS Conference 2025 organizers.'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.mathjax',
    'sphinx.ext.todo',
    'sphinx.builders.linkcheck',
    'sphinx_togglebutton',
    'IPython.sphinxext.ipython_console_highlighting',
    'IPython.sphinxext.ipython_directive',
    'sphinx_design',
    # "sphinx_carousel.carousel",
    # 'myst_nb',
    # 'jupyter_sphinx',
    # 'sphinx_tabs.tabs',
    # "sphinx_inline_tabs",
   # 'sphinx_last_updated_by_git'
]

templates_path = ['_templates']
exclude_patterns = []

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "sphinx_book_theme"
html_logo = "_static/logo-tab.png"
html_title = ""
html_css_files = ["custom.css"]

html_static_path = ['_static']

html_context = {
   "default_mode": "light"
}

# json_url = '_static\switcher.json'
# version_match = "v1.0"

html_theme_options = {
    # "external_links": [],
    # "single_page": False,
    "toc_title": "Contents",
    "logo_only": True,
    "use_download_button": True,
    "show_toc_level": 0,
    "repository_url": "https://github.com/AaltoGIS/LBS2025",
    "repository_branch": "master",
    "path_to_docs": "source/",
    "use_edit_page_button": False,
    "use_repository_button": False,

    # Add 'home page' if needed
    "home_page_in_toc": False,

    #"navbar_end": ["mybutton.html"],

    # Add logos to the bottom left under the TOC
    "extra_navbar": """
    <p><b>Organized by:</b></p>
    <a href='http://lbs.icaci.org/'  target='_blank'> <img src='https://lbs2023.lbsconference.org/wp-content/uploads/2023/01/ica-logo_lbs-commission-300x78.png'> </a>
    <p><br></p>
    <a href='https://www.aalto.fi/en'  target='_blank'> <img src='https://raw.githubusercontent.com/AaltoGIS/lbs2025/master/source/_static/aalto_logo.png'> </a>
    <p><br></p>
    <a href='https://www.maanmittauslaitos.fi/en/research'  target='_blank'> <img src='https://navisp.esa.int/uploads/images/contractor/65129ee279504037723029.png'> </a>
    <p><br><b>Co-sponsored by:</b></p>
    <a href='https://www.maanmittauslaitos.fi/en'  target='_blank'> <img src='https://upload.wikimedia.org/wikipedia/en/thumb/d/d9/National_Land_Survey_of_Finland_logo.svg/1200px-National_Land_Survey_of_Finland_logo.svg.png'> </a>
    """,

    # Possible announcement for the page
    #"announcement": ("📢 All presentations of the accepted papers can now be found under the 'Accepted papers - Short talks' -page. 📢"),
}

html_sidebars = {
    "**": [
        "sidebar-logo.html",
        #"search-field.html",
        #"postcard.html",
        #"recentposts.html",
        #"tagcloud.html",
        #"categories.html",
        #"archives.html",
        "sbt-sidebar-nav.html",
    ]
}