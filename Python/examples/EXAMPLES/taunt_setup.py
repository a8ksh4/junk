#!/usr/bin/env python

from distutils.core import setup, Extension

module1 = Extension('taunt',
                    sources = ['tauntmodule.c'])

setup (name = 'Taunt',
       version = '1.0',
       description = 'This is a demo package',
       ext_modules = [module1])
