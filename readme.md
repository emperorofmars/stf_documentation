# STF: Documentation
**A modular file-format for 3D assets**\
*Intended for (not only) games-development use-cases.*

This documentation is hosted at <https://docs.stfform.at>

🌰 **[Report Issues](https://codeberg.org/stf_format/stf_documentation/issues)**

Made with [Sphinx](https://www.sphinx-doc.org/en/master/) and the following plugins:
* [myst_parser](https://myst-parser.readthedocs.io/en/latest/index.html)
* [sphinx_copybutton](https://sphinx-copybutton.readthedocs.io/en/latest/)
* [sphinx_togglebutton](https://pypi.org/project/sphinx-togglebutton/)
* [sphinx_design](https://sphinx-design.readthedocs.io/en/stable/index.html)
* [sphinxext.opengraph](https://sphinxext-opengraph.readthedocs.io/en/latest/)
* [sphinx-notfound-page](https://github.com/readthedocs/sphinx-notfound-page)

## Development Setup
* Either:
	* Use the "Dev Containers" extension to open the project in a container.
	* Create a Python 3.14 venv in the repo directory.
		* Inside the venv run:
			``` sh
			pip install -r requirements.txt
			```
* Start a local dev-server:
	```sh
	sphinx-autobuild --watch . src/ _out/ -c . -a
	```

## Contributing
Human made contributions via pull-requests are very welcome.

See [CONTRIBUTING.md](./CONTRIBUTING.md) for guidelines.

## License
This repository is licensed under **CC-BY-4.0** (<https://creativecommons.org/licenses/by/4.0/>)
