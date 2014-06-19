#!/usr/bin/env python

# import lxml if installed, otherwise fall back to ElementTree
HAS_LXML = False
try:
    import lxml.etree as ET
    HAS_LXML = True
except ImportError:
    import xml.etree.ElementTree as ET

def main():
    '''Program entry point'''

    pres_root = ET.Element('presidents')

    with open("../DATA/presidents.txt") as fp:
        for rec in fp:
            flds = rec[:-1].split(":")
            add_president(pres_root, flds)

    write_doc(pres_root, '../DATA/presidents.xml')


def write_doc(pres_root, file_name):
    '''Write XML to STDOUT and a file'''
    if HAS_LXML:
        print ET.tostring(pres_root, pretty_print=True)
    else:
        print ET.tostring(pres_root)
    
    pres_doc = ET.ElementTree(pres_root)
    
    if HAS_LXML:
        pres_doc.write(file_name, pretty_print=True)
    else:
        pres_doc.write(file_name)

def TextSubElement(parent, tag, text, attr, **extra):
    '''Add text to a subelement'''
    e = ET.SubElement(parent, tag, attr, **extra)
    e.text = text
    return e
    

def add_president(root, flds):
    '''Add tag and all subtags for one president'''
    (
        f_index, f_lname, f_fname, f_ybirth, f_mbirth, f_dbirth, f_ydeath, 
        f_mdeath, f_ddeath, f_bplace, f_bstate, f_ybegin, f_mbegin, 
        f_dbegin, f_yend, f_mend, f_dend, f_party
    ) = flds

    e_pres = ET.Element('president')
    root.append(e_pres)

    TextSubElement(e_pres, 'index', f_index, {})

    e_name = ET.SubElement(e_pres, 'name', {})
    TextSubElement(e_name, 'last', f_lname, {})
    TextSubElement(e_name, 'first', f_fname, {})

    e_termstart = ET.SubElement(e_pres, 'termstart', {})
    TextSubElement(e_termstart, 'year', f_ybegin, {})
    TextSubElement(e_termstart, 'month', f_mbegin, {})
    TextSubElement(e_termstart, 'day', f_dbegin, {})

    e_termend = ET.SubElement(e_pres, 'termend', {})
    TextSubElement(e_termend, 'year', f_yend, {})
    TextSubElement(e_termend, 'month', f_mend, {})
    TextSubElement(e_termend, 'day', f_dend, {})

    TextSubElement(e_pres, 'birthplace', f_bplace, {})
    TextSubElement(e_pres, 'birthstate', f_bstate, {})

    e_birth = ET.SubElement(e_pres, 'birth', {})
    TextSubElement(e_birth, 'year', f_ybirth, {})
    TextSubElement(e_birth, 'month', f_mbirth, {})
    TextSubElement(e_birth, 'day', f_dbirth, {})

    e_death = ET.SubElement(e_pres, 'death', {})
    TextSubElement(e_death, 'year', f_ydeath, {})
    TextSubElement(e_death, 'month', f_mdeath, {})
    TextSubElement(e_death, 'day', f_ddeath, {})

    TextSubElement(e_pres, 'party', f_party, {})

if __name__ == '__main__':
    main()
