#-*- coding: utf-8 -*-
import os
from optparse import OptionParser
from pymongo import MongoClient, bulk
import json
import collections
import sys

HOST = '45.55.48.43'
PORT = 27017
DB = 'SEC_EDGAR'
COLLECTION = sys.argv[1]

class OrderedDictWithKeyEscaping(collections.OrderedDict):
    def __setitem__(self, key, value, dict_setitem=dict.__setitem__):
        # MongoDB complains when keys contain dots, so we call json.load with
        # a modified OrderedDict class which escapes dots in keys on the fly
        key = key.replace('.', '<DOT>')
        super(OrderedDictWithKeyEscaping, self).__setitem__(key, value, dict_setitem=dict.__setitem__)

def save_to_mongodb(input_file_name):
    with open(input_file_name) as fp:
        json_ = json.load(fp, encoding='utf-8', object_pairs_hook=OrderedDictWithKeyEscaping)

    client = MongoClient(HOST, PORT)
    db = client[DB]
    collection = db[COLLECTION]
    collection.insert_many(json_)

def main():
    cli_parser = OptionParser(
        usage='usage: %prog <input.json>'
        )
    (options, args) = cli_parser.parse_args()

    # Input file checks
    if len(args) < 1:
        cli_parser.error("You have to supply 1 argument")
    input_file_name = args[0]
    if not os.path.exists(input_file_name):
        cli_parser.error("The input file %s you supplied does not exist" % input_file_name)

    save_to_mongodb(input_file_name)

if __name__ == "__main__":
    main()
