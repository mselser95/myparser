.. image:: https://readthedocs.org/projects/myparser/badge/?version=latest
   :target: https://myparser.readthedocs.io/en/latest/?badge=latest
   :alt: Documentation Status


Installation
-----------------

To install this package, run:

    pip install -r requirements.txt


Encode
-----------------

This example allows to generate an encoded file to test the substring count. Usage:

    python3 examples/encode.py


Count
-----------------
The input parameters were defined as follows:

- file: the path to the file to be checked

- encoding: the file encoding. Should be: Should be  utf_32, utf_32_be, utf_32_le, utf_16, utf_16_be, utf_16_le, utf_7, utf_8 or utf_8_sig

- minlen: the minimum number of characters of the substrings


To get the usage help, input

    python3 examples/count.py -h

Then,

    python3 examples/count.py --file [path_to_file] --encoding [encoding] --minlen [min_lenght]

Performance
-----------------

This example provides a simple time comparison between two different ways to do the same thing.

To use:

    python3 examples/performance
