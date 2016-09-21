#!/usr/bin/env python3
import argparse
import xml.etree.ElementTree as ET
import validator
from const import *

parser = argparse.ArgumentParser()
parser.add_argument("-f", "--file", dest="filepath", required=True,
                    help="path to xml file", metavar="FILE",
                    type=lambda x: validator.is_valid_file(parser, x))
args = parser.parse_args()

def get_all_licenses():
    licenses = set()
    for event, elem in ET.iterparse(args.filepath):
        if event == 'end' and elem.tag == '{}rightsResource'.format(namespace_prefix):
            l = elem.find('.//lido:term', namespaces).text
            licenses.add(l)
    return licenses

for l in get_all_licenses():
    print(l)


