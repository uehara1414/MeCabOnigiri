Unix: [![Unix Build Status](https://img.shields.io/travis/uehara1414/MeCabOnigiri/master.svg)](https://travis-ci.org/uehara1414/MeCabOnigiri) Windows: [![Windows Build Status](https://img.shields.io/appveyor/ci/uehara1414/MeCabOnigiri/master.svg)](https://ci.appveyor.com/project/uehara1414/MeCabOnigiri)<br>Metrics: [![Coverage Status](https://img.shields.io/coveralls/uehara1414/MeCabOnigiri/master.svg)](https://coveralls.io/r/uehara1414/MeCabOnigiri) [![Scrutinizer Code Quality](https://img.shields.io/scrutinizer/g/uehara1414/MeCabOnigiri.svg)](https://scrutinizer-ci.com/g/uehara1414/MeCabOnigiri/?branch=master)<br>Usage: [![PyPI Version](https://img.shields.io/pypi/v/MeCabOnigiri.svg)](https://pypi.python.org/pypi/MeCabOnigiri)

# Overview

mecab-python3 wrapper

# Setup

## Requirements

* Python 3.6+

## Installation

Install MeCabOnigiri with pip:

```sh
$ pip install MeCabOnigiri
```

# Usage

After installation, the package can imported:

```sh
$ python
>>> import MeCabOnigiri
>>> MeCabOnigiri.__version__
```

## Test
```sh
pipenv install --dev
pipenv run nosetests
```
