#!/usr/bin/env python

from distutils.core import setup, Extension


presidents_module = Extension('_presidents',
                           sources=['presidents_wrap.c', 'presidents.c'],
                           )

setup (
    name = 'presidents',
    version = '0.1',
    author      = "John Strickler",
    description = """Simple swig example from docs""",
    ext_modules = [presidents_module],
    py_modules = ["presidents"],
)