#!/usr/bin/env python3
import argparse
import xml.etree.ElementTree as ET
import urllib.request
import file_validator
from item import Item
from const import *

parser = argparse.ArgumentParser()
parser.add_argument("-f", "--file", dest="filepath", required=True,
                    help="path to xml file", metavar="FILE",
                    type=lambda x: file_validator.is_valid_file(parser, x))
parser.add_argument("-o", "--output_dir", dest="outputdir", required=False,
                    help="folder path for saving the images", default='.',
                    type=lambda x: file_validator.is_valid_dir(parser, x))
parser.add_argument("-fc", "--filter_classification_term", dest="classification", required=False,
                    help="pass a classification term to filter by (e.g. 'Fotografie')")
parser.add_argument("-v", "--verbosity", dest="verbose",
                    help="increase output verbosity", action="store_true")

args = parser.parse_args()

item_list = []

if args.verbose:
    print("Downloading all items that have classification term {} to folder {}".format(args.classification, args.outputdir))

def has_term(elem, term):
    term_elements = elem.findall('.//lido:classificationWrap//lido:term', namespaces)
    term_texts    = map(lambda x: x.text, term_elements)

    if term is None:
        return True

    if term in term_texts:
        return True

    return False

if args.verbose:
    print("Filtering items for term: {}".format(args.classification))

# iterating elements and clearing them after usage
# -> allows to start handling elements right away and have low memory impact
for event, elem in ET.iterparse(args.filepath):
    if event == 'end' and elem.tag == '{}lido'.format(namespace_prefix):

        if has_term(elem, args.classification) == False:
            continue

        record_id    = elem.find('.//lido:recordID', namespaces).text
        inventory_no = elem.find('.//lido:workID', namespaces).text
        title        = elem.find('.//lido:titleSet/lido:appellationValue', namespaces).text
        item         = Item(record_id, inventory_no, title)

        if elem.find('.//lido:displayDate', namespaces) is not None:
            item.display_date = elem.find('.//lido:displayDate', namespaces).text

        item_list.append(item)
        elem.clear()


for i in item_list:
    filepath = args.outputdir + i.inventory_no + '.jpg'
    urllib.request.urlretrieve(i.uri, filepath)

    if args.verbose:
        print("Downloading: {}".format(filepath))
