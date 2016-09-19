#!/usr/bin/env python3
import argparse
import xml.etree.ElementTree as ET
import file_validator
from item import Item

parser = argparse.ArgumentParser()
parser.add_argument("-f", dest="filepath", required=True,
                    help="path to xml file", metavar="FILE",
                    type=lambda x: file_validator.is_valid_file(parser, x))

# parser.add_argument("echo", help="echo the string you use here")
# parser.add_argument("square", help="echo the string you use here", type=int)
#
# parser.add_argument("-v", "--verbosity", help="increase output verbosity", action="store_true")

args = parser.parse_args()

# print args.echo
#
# if args.verbosity:
#     print "verbosity turned on"

schema_uri       = 'http://www.lido-schema.org'
namespace_prefix = '{' + schema_uri + '}'
namespaces       = {'lido': schema_uri}

item_list = []

# iterating elements and clearing them after usage
# -> allows to start handling elements right away and have low memory impact
for event, elem in ET.iterparse(args.filepath):
    if elem.tag == '{}lido'.format(namespace_prefix) and event == 'end':
        inventory_no = elem.find('.//lido:workID', namespaces).text
        title        = elem.find('.//lido:titleSet/lido:appellationValue', namespaces).text
        item     = Item(inventory_no, title)
        if elem.find('.//lido:displayDate', namespaces) is not None:
            item.display_date = elem.find('.//lido:displayDate', namespaces).text

        item_list.append(item)
        print(item.uri)
        elem.clear()


# for p in portrait_list:
#     print(p)

