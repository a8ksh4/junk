#!/usr/bin/env python
import sys

HAS_LXML = False
try:
    import lxml.etree as ET
    HAS_LXML = True
except ImportError:
    import xml.etree.ElementTree as ET

with open('../DATA/words.txt') as WORDS:
    xwords = [ word[:-1] for word in WORDS if word.startswith('x') ]

root = ET.Element('words')
for word in xwords:
    word_element = ET.Element('word')
    word_element.text = word 
    root.append(word_element)

tree = ET.ElementTree(root)

if HAS_LXML:
    tree.write('xwords.xml', pretty_print=True)
else:
    tree.write('xwords.xml')
