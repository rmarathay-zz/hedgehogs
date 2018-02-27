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



class OrderedDictWithKeyEscaping(collections.OrderedDict):
    def __setitem__(self, key, value, dict_setitem=dict.__setitem__):
        # MongoDB complains when keys contain dots, so we call json.load with
        # a modified OrderedDict class which escapes dots in keys on the fly
        key = key.replace('.', '<DOT>')
        super(OrderedDictWithKeyEscaping, self).__setitem__(key, value, dict_setitem=dict.__setitem__)


def save_to_mongodb(input_file_name,collectionID,usernameID):
    with open(input_file_name) as fp:
        print fp
        json_ = json.load(fp, encoding='utf-8', object_pairs_hook=OrderedDictWithKeyEscaping)


    client = MongoClient(HOST, PORT, username=usernameID, password= '123', authMechanism ='SCRAM-SHA-1')
    #client.admin.authenticate('jgeorge','123',source= 'SEC_EDGAR')
    db = client[DB]
    collection = db[collectionID]
    collection.insert_many(json_)



def main():
    cli_parser = OptionParser(
        usage='usage: %prog <input.json>'
        )
    (options, args) = cli_parser.parse_args()

    # Input file checks
    if len(args) < 2:
        cli_parser.error("You have to supply 2 arguments, USAGE: financialJson Username")
    input_file_name = args[0]
    if not os.path.exists(input_file_name):
        cli_parser.error("The input file %s you supplied does not exist" % input_file_name)

    COLLECTION = sys.argv[1]
    username = sys.argv[2]
    save_to_mongodb(input_file_name,COLLECTION,username)


if __name__ == "__main__":

    main()
