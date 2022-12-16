shyft-docs
==========

This repository contains the end-user documentation for the OpenSource hydrological toolbox
[Shyft](https://gitlab.com/shyft-os/shyft).
 
The html documentation content is created using the Python tool [Sphinx](http://www.sphinx-doc.org). All
documentation is written either in documents using [reStructuredText](https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html)
or in [Jupyter notebooks](https://jupyter.org/) using Python.

The resulting Shyft end-user documentation pages are hosted on [Read the docs](http://shyft.readthedocs.io/).

For documentation on coding and development, please check the project's
[GitLab Shyft repository](https://gitlab.com/shyft-os/shyft).


Project structure
-----------------

This project contains the folders:

- publication_sources: Collection of project related publications
- publication_sources/<name>: LaTex documents for a publication
- sphinx: The Sphinx project
- sphinx/content: Actual documentation content
- sphinx/content/project: Information about the Shyft project
- sphinx/content/hydrology: Documentation content for the Shyft package
- sphinx/content/time-series: Documentation content for the shyft.time_series package
- sphinx/content/dashboard: Documentation content for the shyft.dashboard package

Each package documentation will have own sub-section folders, if necessary. In these
folders "code" or "images" can be present, if such are used in that sub-section.


Contributing
------------

If you are reading this page, it assumes you are interested in contributing to the
Shyft end-user documentation which is **strongly** welcomed. Equally welcome are
contributions to the code documentation like doc strings, which are covered in the
[Shyft code repository](https://gitlab.com/shyft-os/shyft) itself.

When contributing, please follow these simple rules:

1. Create a new branch on this repository

```bash
git checkout -b <my-branch-name>
```

2. Each documentation document or notebook must be navigable from the contents tree!
3. Any code example must be written in Python.
4. Any documentation file must be written in reStructureText.
5. If you have example data, please add it to the `shyft-data` repository

```bash
cd shyft-data/contrib
git checkout -b <my-branch-name>
mkdir my-example-data
cp -r ../your_data_source my-example-data
git add my-example-data/*
git commit -m "pushing data for my-example"
```

6. Then create pull requests on github for your branches.


Cloning
-------
Shyft is distributed in three separate code repositories. To contribute to Shyft,
you should clone all three repositories. To make administration easier, clone
them all into a directory "shyft_workspace".

```bash
mkdir shyft_workspace
cd shyft_workspace
git clone https://gitlab.com/shyft-os/shyft.git
git clone https://gitlab.com/shyft-os/shyft-data.git
git clone https://gitlab.com/shyft-os/shyft-doc.git
```


Requirements
------------

This documentation is written in reStructuredText files and in Jupyter notebooks.
In order to process the Jupyter notebooks, the Sphinx extension nbsphinx requires
[Pandoc](https://pandoc.org/installing.html) to be installed on the system.

The file [requirements.txt](requirements.txt) lists the Python packages that are required to build
the documentation help pages. These can be installed either in a Python venv or
an Anaconda/Miniconda environment.

```bash
python -m pip install -r requirements.txt
```


Building
--------

If you have the sphinx and the extensions properly installed on your system, you should be able to run:

```bash
cd sphinx
make html
```

This will generate output in the `_build` directory.

Note that in `conf.py` there are settings controlling whether or not the notebooks will be built with the
sphinx-build run. We have this set to off by default (the notebooks are not built on the readthedocs server).
So, if you have create a new notebook, be sure to run all the code and save it with the output. Then sphinx-build
will pick up the notebook in the state it was saved!


Contributers
------------

Documentation and Notebooks:

All contributors on the main repository https://gitlab.com/shyft-os/shyft, providing doc-strings in c++ code and the 
python interface code.

* John F. Burkhart <john.burkhart@statkraft.com>
* Felix Matt <felix.matt@statkraft.com>
* Olga Sylantieva <olga.sylantieva@gmail.com>
* Yisak Sultan Abdella <YisakSultan.Abdella@statkraft.com>
* Ola Skavhaug <ola@xal.no>
* Eivind Storm Aarnæs <eivind@xal.no>
* Erik Tjøtta <erik.tjotta@statkraft.com>
* Ludovic Pochon-Guerin <ludovic.pochon-guerin@statkraft.com>
* Sigbjørn Helset <sigbjorn.helset@gmail.com>
* Felix Matt <f.n.matt@geo.uio.no>
* Francesc Alted <faltet@gmail.com>
* Alexander Becker <alexander.becker@statkraft.com>


Copyright / Licence
-------------------
Shyft is released under LGPL V.3 See [LICENCE](LICENSE) for details.
