
from datetime import date

"""
Run a dev-server with:
sphinx-autobuild src/ build/ -c . -a
"""

## Project

project = "STF Documentation"
html_title = "STF Documentation"
description = "Squirrel Transfer Format - A modular file-format for 3D assets"
author = "Mars (https://squirrelbite.com)"
copyright = f"{date.today().year}, stfform.at"
language = "en"
version = "0.0.11"

html_favicon = "theme/favicon.png"

myst_html_meta = {
	"description": "Squirrel Transfer Format - A modular file-format for 3D assets",
	"keywords": "stf, squirrel transfer format, 3d file format, 3d format",
}

html_baseurl = "https://docs.stfform.at"


## Build

exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']
source_suffix = [".rst", ".md"]
master_doc = "index"

## Theme

html_theme = "furo"

html_theme_options = {
	"home_page_in_toc": True,
	"repository_url": "https://codeberg.org/emperorofmars/stf_documentation",
	"repository_branch": "master",
	"path_to_docs": "src",
	"use_repository_button": True,
	"use_edit_page_button": True,
	"use_issues_button": True,
	"navigation_depth": 3,
}

## Extensions

extensions = [
	"myst_parser",
	"sphinxext.opengraph",
	"sphinx_copybutton"
]

myst_enable_extensions = [
	"colon_fence",
	"html_admonition",
	"html_image",
]

ogp_site_url = "https://docs.stfform.at"
