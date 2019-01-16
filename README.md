# Python samples

This repository shows some examples of Python code I wrote in order to learn this language. It may not always reflect the best practices, since I built this repo incrementally. I did some refactoring, but I know everything still is not as it should.

## Things to consider

Except when stated otherwise (in comments), the code in this repository is fully functional. Some examples may require you remove comments (i.e. in `functions_use.py`).

One thing I should address some day is to update the structure of the project to have all modules in a specific folder instead of having almost everything in the root folder. This may come sooner or later, but is not my top priority right now.

## Setup

These code samples require a few things:

- Python 3.6+
- pip 9.0+

You can install all dependencies and launch the few tests cases by doing so:

```shell
git clone https://github.com/webmaniak/python-samples.git
cd python-samples/
pip install -r requirements.txt
python3 -m unittest discover -v -p *_test.py
```

## Content Guide

Here's some table of content about what's in this repo:

- [classes](classes/) contains definitions of Classes
  - [animals.py](classes/animal.py) defines a sample 'Animal' class and it's 'Dog' subclass
  - [callable.py](classes/callable.py) features a class that can be (almost) used like a function
  - [custom_exception.py](classes/custom_exception.py) shows how to create a subclass for error handling
  - [timerecorderclass.py](classes/timerecorderclass.py) shows an example of Context Manager implementation
  - [underscores.py](classes/underscores.py) defines a class with various underscores (_) to show how they can be used
- [tests](tests/) contains unit tests for some of the code (especially classes)
- There are other modules in the [root](#) folder too:
  - [datetime_usage.py](datetime_usage.py) shows how to use the datetime API from Python
  - [decorators_use.py](decorators_use.py) demonstrates some use cases of decorators defined in [decorators.py](decorators.py)
  - [decorators.py](decorators.py) defines a few sample decorators
  - [dictionary.py](dictionary.py) shows how to use Python's dictionary structure
  - [exception_handling.py](exception_handling.py) features how to deal with exceptions
  - [files.py](files.py) explains how to interact with files
  - [functions_use.py](functions_use.py) uses `functions.py` and demonstrates how functions can be used
  - [functions.py](functions.py) defines functions in many, many ways
  - [hello.py](hello.py) simply does a few prints (hello world!)
  - [inputs.py](inputs.py) shows how to use the `input` function to get a user's feedback
  - [lists.py](lists.py) shows how to use lists in Python
  - [nulls.py](nulls.py) demonstrates how null (NoneType) values are handled
  - [numbers.py](numbers.py) explains how numbers work and how to deal with them
  - [ordered_dict.py](ordered_dict.py) features the usage of the `OrderedDict` Python structure
  - [pi_digits.py](pi_digits.py) deals with some pi number related stuff
  - [strconcatperf.py](strconcatperf.py) shows how string concatenation can be done and which method is faster
  - [strings.py](strings.py) shows how string concatenation can be done in detail
  - [test.py](test.py) a simple sandbox file (don't mind it)
  - [time_usage.py](time_usage.py) features the `time` functions of Python and how to deal with them
  - [timerecorder.py](timerecorder.py) contains yet another implementation of Context Manager, but as a function (an example of Class implementation can be found in [timerecorderclass.py](classes/timerecorderclass.py))
  - [underscores_use.py](underscores_use.py) demonstrates how we can access (or not) class attributes with underscores (based on [underscores.py](classes/underscores.py))