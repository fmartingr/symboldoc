SymbolDoc
=========

[![Scrutinizer Code Quality](https://scrutinizer-ci.com/g/fmartingr/symboldoc/badges/quality-score.png?b=master)](https://scrutinizer-ci.com/g/fmartingr/symboldoc/?branch=master)
[![Code Coverage](https://scrutinizer-ci.com/g/fmartingr/symboldoc/badges/coverage.png?b=master)](https://scrutinizer-ci.com/g/fmartingr/symboldoc/?branch=master)
[![Build Status](https://scrutinizer-ci.com/g/fmartingr/symboldoc/badges/build.png?b=master)](https://scrutinizer-ci.com/g/fmartingr/symboldoc/build-status/master)
![Python 3](https://img.shields.io/badge/python-3-blue.svg)

Create a docstring given a module's symbol name.

## Installation

```
pip3 install symboldoc
```

## Usage example

```
$ symboldoc path/to/module.py my_function sphinx
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

## Flavors

| Name | Available |
| ---- | --------- |
| Sphinx | Sort of! |
