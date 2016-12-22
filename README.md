SymbolDoc
=========

[![Codacy Badge](https://api.codacy.com/project/badge/Grade/3760bf0f42404948879c5388254bea52)](https://www.codacy.com/app/fmartingr/symboldoc?utm_source=github.com&utm_medium=referral&utm_content=fmartingr/symboldoc&utm_campaign=badger) ![Python 3](https://img.shields.io/badge/python-3-blue.svg)

Create a docstring given a module's symbol name.

## Installation

```
pip3 install symboldoc
```

## Usage example

```
$ symboldoc path/to/module.py my_function
"""Brief summary for method my_function

The first line is brief explanation, which may be completed with
a longer one.

- **parameters**, **types**, **return** and **return types**::

:param arg1: Description for arg1
:type arg1:
:param arg2: Description for arg2
:type arg2:
:return: return description
:rtype: The return type description
"""
```
