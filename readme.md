# STF: Documentation
**A modular file-format for 3D assets**\
*Intended for (not only) games-development use-cases.*

This documentation is hosted at <https://docs.stfform.at>

🌰 **[Report Issues](https://codeberg.org/emperorofmars/stf_documentation/issues)**

Made with [Sphinx](https://www.sphinx-doc.org/en/master/) and the following plugins:
* [myst_parser](https://myst-parser.readthedocs.io/en/latest/index.html)
* [sphinx_copybutton](https://sphinx-copybutton.readthedocs.io/en/latest/)
* [sphinx_togglebutton](https://pypi.org/project/sphinx-togglebutton/)
* [sphinx_design](https://sphinx-design.readthedocs.io/en/stable/index.html)
* [sphinxext.opengraph](https://sphinxext-opengraph.readthedocs.io/en/latest/)
* [sphinx-notfound-page](https://github.com/readthedocs/sphinx-notfound-page)

## Contributing
Human made contributions via pull-requests are welcome.\
Please open issues in this repository for changes to the format or any of its resource-types.

### Guidelines
* Any form of LLM contribution is prohibited, this also includes issues and PRs.
* Please open an issue first for larger changes.

### Development
* Use VSCode with the [recommended extensions](./.vscode/extensions.json).
* Use the "Dev Containers" extension to open the project in a container.
* Start a local dev-server:
	```sh
	sphinx-autobuild --watch . src/ _out/ -c . -a
	```

## License
This repository is licensed under **CC-BY-4.0** (<https://creativecommons.org/licenses/by/4.0/>)
