#!/usr/bin/env python3
import argparse
import xml.etree.ElementTree as ET
import urllib.request
import validator
import json
from ComplexEncoder import *
from item import Item
from const import *
import filter
from mkg_lido import *

parser = argparse.ArgumentParser()
parser.add_argument("-f", "--file", dest="filepath", required=True,
                    help="path to xml file", metavar="FILE",
                    type=lambda x: validator.is_valid_file(parser, x))
parser.add_argument("-o", "--output_dir", dest="outputdir", required=False,
                    help="folder path for saving the images", default='.',
                    type=lambda x: validator.is_valid_dir(parser, x))
parser.add_argument("-fc", "--filter_classification_term", dest="classification", required=False,
                    help="pass a classification term to filter by (e.g. 'Fotografie')")
parser.add_argument("-fl", "--filter_license", dest="license", required=False,
                    help="pass a license type to filter by (CC-0, CC-BY, Copyright)",
                    type=lambda x: validator.is_valid_license(parser, x))
parser.add_argument("-v", "--verbosity", dest="verbose",
                    help="increase output verbosity", action="store_true")

args = parser.parse_args()

item_list = []

if args.verbose:
    print("Downloading items")
    print("classification filter: %s" % args.classification)
    print("license filter: %s" % args.license)
    print("output dir: %s" % args.outputdir)

# iterating elements and clearing them after usage
# -> allows to start handling elements right away and have low memory impact
for event, elem in ET.iterparse(args.filepath):
    if event == 'end' and elem.tag == '{}lido'.format(namespace_prefix):

        if filter.has_term(elem, args.classification) == False:
            continue

        if filter.has_license(elem, args.license) == False:
            continue

        record_id    = elem.find('.//lido:recordID', namespaces).text
        inventory_no = elem.find('.//lido:workID', namespaces).text
        title        = elem.find('.//lido:titleSet/lido:appellationValue', namespaces).text
        description  = filter.unwrap_element(elem.find('.//lido:objectDescriptionWrap//lido:descriptiveNoteValue', namespaces))
        date         = EventDate.fromEventWrap(elem, EventType.Herstellung)

        item         = Item(record_id, inventory_no, title, description, date)

        item_list.append(item)
        elem.clear()

if __name__ == "__main__":
    json_filepath = args.outputdir + 'metadata.json'
    with open(json_filepath, 'w') as outfile:
        json.dump(item_list, outfile, cls=ComplexEncoder)

    for i in item_list:
        filepath = args.outputdir + i.inventory_no + '.jpg'
        urllib.request.urlretrieve(i.uri, filepath)

        if args.verbose:
            print("Downloading: %s" % filepath)