
from datetime import date

"""
Run a dev-server with:
sphinx-autobuild --watch . src/ build/ -c . -a
"""

## Project

version = "0.0.15"
release = version

project = "STF Documentation"
html_title = f"STF Documentation {release}"
description = "Squirrel Transfer Format - A modular file-format for 3D assets"
author = "Mars (https://squirrelbite.com)"
copyright = f"{date.today().year}: stfform.at, This page is licensed under CC-BY-4.0 https://creativecommons.org/licenses/by/4.0/"
language = "en"

html_favicon = "theme/favicon.png"
html_logo = "src/img/stf_logo.png"

myst_html_meta = {
	"description": "Squirrel Transfer Format - A modular file-format for 3D assets",
	"keywords": "stf, squirrel transfer format, 3d file format, 3d format",
	"robots": "noai, noimageai",
}

html_baseurl = "https://docs.stfform.at"


## Build

exclude_patterns = ["_build", "build", "Thumbs.db", ".DS_Store", ".github", ".vscode"]
source_suffix = [".rst", ".md"]
master_doc = "index"
templates_path = ["theme/templates"]


## Theme

html_theme = "furo"

html_theme_options = {
	"source_view_link": "https://codeberg.org/emperorofmars/stf_documentation/src/branch/master/src/{filename}",
	"source_edit_link": "https://codeberg.org/emperorofmars/stf_documentation/_edit/master/src/{filename}",
}

html_static_path = ["theme"]
html_css_files = [
	"stf.css",
]
html_js_files = [
	"stf.js"
]


## Extensions

extensions = [
	"myst_parser",
	"sphinx_copybutton",
	"sphinx_togglebutton",
	"sphinx_design",
	"notfound.extension",
	"sphinxext.opengraph",
]


### myst_parser

myst_enable_extensions = [
	"colon_fence",
	"html_admonition",
	"html_image",
	"attrs_inline",
	"attrs_block",
	"substitution",
]
myst_heading_anchors = 6

myst_substitutions = {
	"version": version,
}

### sphinxext.opengraph

ogp_site_url = "https://docs.stfform.at"
ogp_enable_meta_description = True
ogp_social_cards = {
	"image": "img/stf_logo.png",
	"line_color": "#ff9cac",
}

### notfound.extension

notfound_urls_prefix = None
