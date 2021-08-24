Run in project root:

    isort .

    black .

To sort imports and reformat file using PEP8

To build documentation:

    sphinx-quickstart

build and source must be in different folders (use default), and select to include modules in quickstart

    sphinx-apidoc -f -o source ../src/[PROJECT_NAME]/

    make html

Documentation must be inside the [PROJECT_NAME] folder within src.

Then, in the conf.py file change the theme to "spinx_rtd_theme"
