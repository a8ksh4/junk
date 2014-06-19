#!/usr/bin/env python

from distutils.core import setup, Extension


wilma_module = Extension('_wilma',
                           sources=['wilma_wrap.c', 'wilma.c'],
                           )

setup (
    name = 'wilma',
    version = '0.1',
    author      = "John Strickler",
    description = """Simple swig example from docs""",
    ext_modules = [wilma_module],
    py_modules = ["wilma"],
)