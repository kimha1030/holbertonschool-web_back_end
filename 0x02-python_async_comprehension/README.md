# 0x02. Python - Async Comprehension

## Resources

- [PEP 530 – Asynchronous Comprehensions](https://www.python.org/dev/peps/pep-0530/)
- [What’s New in Python: Asynchronous Comprehensions / Generators](http://www.blog.pythonlibrary.org/2017/02/14/whats-new-in-python-asynchronous-comprehensions-generators/)
- [Type-hints for generators](https://stackoverflow.com/questions/42531143/type-hinting-generator-in-python-3-6)
- [Async IO in Python: A Complete Walkthrough](https://realpython.com/async-io-python/)
- [waiting in asyncio](https://hynek.me/articles/waiting-in-asyncio/)

## Learning Objectives

At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

- How to write an asynchronous generator
- How to use async comprehensions
- How to type-annotate generators

## General requirments

- Allowed editors: vi, vim, emacs
- All your files will be interpreted/compiled on Ubuntu 18.04 LTS using python3 (version 3.7)
- All your files should end with a new line
- The first line of all your files should be exactly #!/usr/bin/env python3
- A README.md file, at the root of the folder of the project, is mandatory
- Your code should use the pycodestyle style (version 2.5.x)
- The length of your files will be tested using wc
- All your modules should have a documentation (python3 -c 'print(**import**("my_module").**doc**)')
- All your functions should have a documentation (python3 -c 'print(**import**("my_module").my_function.**doc**)'
- A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)
- All your functions and coroutines must be type-annotated.

## Tasks:

### [0. Async Generator](./0-async_generator.py)

Write a coroutine called async_generator that takes no arguments.
The coroutine will loop 10 times, each time asynchronously wait 1 second, then yield a random number between 0 and 10. Use the random module.

### [1. Async Comprehensions](./1-async_comprehension.py)

Import async_generator from the previous task and then write a coroutine called async_comprehension that takes no arguments.

The coroutine will collect 10 random numbers using an async comprehensing over async_generator, then return the 10 random numbers.

### [2. Run time for four parallel comprehensions

](./2-measure_runtime.py)
Import async_comprehension from the previous file and write a measure_runtime coroutine that will execute async_comprehension four times in parallel using asyncio.gather. measure_runtime should measure the total runtime and return it.

---

## Author

- **Kimberly Hinostroza** - [kimha1030](https://github.com/kimha1030)
