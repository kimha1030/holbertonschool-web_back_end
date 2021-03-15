# 0x00. Python - Variable Annotations

## Resources

- [Python Type Checking (Guide)](https://realpython.com/python-type-checking/)
- [Using Python's Type Annotations](https://dev.to/dstarner/using-pythons-type-annotations-4cfe)
- [Python 3 typing documentation](https://docs.python.org/3/library/typing.html)
- [MyPy cheat sheet](https://mypy.readthedocs.io/en/latest/cheat_sheet_py3.html)
- [TypeVar](https://www.kite.com/python/docs/typing.TypeVar)
- [How to start using Python Type Annotations with Mypy](https://www.stackbuilders.com/tutorials/python/using-types-in-python-with-mypy/)

## General Objectives

At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

- Type annotations in Python 3
- How you can use type annotations to specify function signatures and variable types
- Duck typing
- How to validate your code with mypy

## General Requirements

- Allowed editors: vi, vim, emacs
- All your files will be interpreted/compiled on Ubuntu 18.04 LTS using python3 (version 3.7)
- All your files should end with a new line
- The first line of all your files should be exactly #!/usr/bin/env python3
- A README.md file, at the root of the folder of the project, is mandatory
- Your code should use the pycodestyle style (version 2.5.)
- All your files must be executable
  The length of your files will be tested using wc
- All your modules should have a documentation (python3 -c 'print(**import**("my_module").**doc**)')
- All your classes should have a documentation (python3 -c 'print(**import**("my_module").MyClass.**doc**)')
- All your functions (inside and outside a class) should have a documentation (python3 -c 'print(**import**("my_module").my_function.**doc**)' and python3 -c 'print(**import**("my_module").MyClass.my_function.**doc**)')
- A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)

## Tasks

- [0. Basic annotations - add](./0-add.py)
  Write a type-annotated function add that takes a float a and a float b as arguments and returns their sum as a float.

- [1. Basic annotations - concat](1-concat.py)
  Write a type-annotated function concat that takes a string str1 and a string str2 as arguments and returns a concatenated string

- [2. Basic annotations - floor](./2-floor.py)
  Write a type-annotated function floor which takes a float n as argument and returns the floor of the float.

- [3. Basic annotations - to string](./3-to_str.py)
  Write a type-annotated function to_str that takes a float n as argument and returns the string representation of the float.

- [4. Define variables](./4-define_variables.py)
  Define and annotate the following variables with the specified values:
  a, an integer with a value of 1
  pi, a float with a value of 3.14
  i_understand_annotations, a boolean with a value of True
  school, a string with a value of “Holberton”

- [5. Complex types - list of floats](5-sum_list.py)
  Write a type-annotated function sum_list which takes a list input_list of floats as argument and returns their sum as a float.

- [6. Complex types - mixed list](./6-sum_mixed_list.py)
  Write a type-annotated function sum_mixed_list which takes a list mxd_lst of integers and floats and returns their sum as a float.

- [7. Complex types - string and int/float to tuple](./7-to_kv.py)
  Write a type-annotated function to_kv that takes a string k and an int OR float v as arguments and returns a tuple. The first element of the tuple is the string k. The second element is the square of the int/float v and should be annotated as a float.

- [8. Complex types - functions](./8-make_multiplier.py)
  Write a type-annotated function make_multiplier that takes a float multiplier as argument and returns a function that multiplies a float by multiplier.

- [9. Let's duck type an iterable object](./9-element_length.py)
  Annotate the below function’s parameters and return values with the appropriate types

---

## **Author**

- **Kimberly Hinostroza** - [kimha1030](https://github.com/kimha1030)
