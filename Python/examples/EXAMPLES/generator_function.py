#!/usr/bin/env python

def main():
    mary = trimmed('../DATA/mary.txt')
    for line in mary:
        print line  # \n is already trimmed, so no double-spacing

def trimmed(file_name):
    '''Generator that yields lines trimmed of the trailing \n '''
    with open(file_name) as FILE:
        for line in FILE:
            yield line[:-1]

if __name__ == '__main__':
    main()

