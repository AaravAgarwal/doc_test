# conf.py for Sphinx

import os
import sys

# -- Path setup --------------------------------------------------------------
# If extensions are in another directory, add these directories to sys.path here.
sys.path.insert(0, os.path.abspath('../'))  # Adjust the path as necessary

# -- Project information -----------------------------------------------------
project = 'Your Project Name'
author = 'Your Name'
release = '0.1.0'

# -- General configuration ---------------------------------------------------
extensions = [
    'sphinx.ext.autodoc',     # For automatic documentation from docstrings
    'sphinx.ext.napoleon',    # Support for NumPy and Google style docstrings
    'sphinx.ext.viewcode',    # Add links to highlighted source code
    'sphinx.ext.autoapi',
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# Paths for autoapi
autoapi_type = 'python'
autoapi_dirs = ['../src']  # Path to the source code directory

# -- Options for HTML output -------------------------------------------------
html_theme = 'sphinx_rtd_theme'  # You can use other themes like 'alabaster', 'classic', etc.
html_static_path = ['_static']   # For custom static files (CSS, JS)

# -- Options for auto-generating API documentation --------------------------
# If using sphinx-autoapi or autodoc:
autodoc_mock_imports = ["your_module_name"]  # Mock imports if you have dependencies

