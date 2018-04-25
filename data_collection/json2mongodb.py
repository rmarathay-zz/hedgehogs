#-*- coding: utf-8 -*-
# import os
# from optparse import OptionParser
# from pymongo import MongoClient, bulk
# import json
# import collections
# import sys

from import_hedgehogs import *

HOST = '45.55.48.43'
PORT = 27017
DB = 'SEC_EDGAR'


class OrderedDictWithKeyEscaping(collections.OrderedDict):
    def __setitem__(self, key, value, dict_setitem=dict.__setitem__):
        # MongoDB complains when keys contain dots, so we call json.load with
        # a modified OrderedDict class which escapes dots in keys on the fly
        key = key.replace('.', '<DOT>')
        super(OrderedDictWithKeyEscaping, self).__setitem__(key, value)#, dict_setitem=dict.__setitem__)
        #super(OrderedDictWithKeyEscaping, self).__setitem__
        #super()

def save_to_mongodb(json_data, collectionID, usernameID, passwordID):
    # with open(input_file_name) as fp:
    #     data = fp.read()
    #     json_ = json.loads(data, encoding='utf-8', object_pairs_hook=OrderedDictWithKeyEscaping)

    client = MongoClient(HOST, PORT, username=usernameID, password=passwordID, authMechanism ='SCRAM-SHA-1')
    # client.admin.authenticate('jgeorge','123',source= 'SEC_EDGAR')
    # print("arguments to function:", input_file_name, usernameID, collectionID)
    db = client[DB]
    collection = db[collectionID]
    # print(type(input_file_name))
    # file = open(input_file_name, "r")
    # data = json.load(file)
    # print(type(data))
    # print(type(file))
    # data = json_util.loads(file.read())
    # print(json_)
    for item in json_data:
        collection.insert_one(item)
    # file.close()

def getJsonObj(input_file_name):
    with open(input_file_name) as fp:
        data = fp.read()
        json_ = json.loads(data, encoding='utf-8', object_pairs_hook=OrderedDictWithKeyEscaping)
    return json_
    
    
    
def standardize(obj):
    """
    standardKeys= [
    "Document Type",
    "Amendment Flag",
    "Document Period End Date",
    "Document Fiscal Year Focus",
    "Document Fiscal Period Focus",
    "Trading Symbol",
    "Entity Registrant Name",
    "Entity Central Index Key",
    "Current Fiscal Year End Date",
    "Entity Filer Category",
    "Entity Common Stock, Shares Outstanding"]
    all flags
    """
    
    standardKeys= [
    "Document Type",
    "Amendment Flag",
    "Document Period End Date",
    "Document Fiscal Year Focus",
    "Document Fiscal Period Focus"]
    
    """
    for key in obj[0]:
        if key == 'title':
            continue
        newKey = "Document And Entity Information"
        temp = key
        if(newKey!=key):
            obj[0][newKey]=obj[0][key]
            del obj[0][key]
            temp = newKey
        
        i=0
        for nextKey in list(obj[0][temp].keys()):
            newKey = standardKeys[i]
            if(newKey!=nextKey):
                obj[0][temp][newKey] =obj[0][temp][nextKey]
                del obj[0][temp][nextKey]
            i+=1
            if(i>=5):
                break
        
        break
        """
    return obj
            
def convert_to_json(obj):
    with open('data.txt', 'w') as outfile:
         json.dump(obj, outfile, indent = 4, ensure_ascii = False)
            
"""
get year function. Has arguments for different formats of each .get argument
so you can pass in Document And Entity Information and Document And Entity Information[Abstract]
"""
def get_year(data_dict,document_entity,document_fiscal_year,value):
    year = data_dict.get(document_entity).get(document_fiscal_year).get(value)
    return year
    
"""
same as above but for quarter
"""
def get_quarter(data_dict,document_entity,document_fiscal_period,value):
    quarter = data_dict.get(document_entity).get(document_fiscal_period).get(value)
    return quarter
    

    
        
def get_collection_name(json_data, input_file):
    document_entity_formats =["Document And Entity Information","Document And Entity Information [Abstract]","Document Information [Line Items]","Document and Entity Information - shares"]
    document_fiscal_year_formats=["Document Fiscal Year Focus"]
    document_fiscal_period_formats=["Document Fiscal Period Focus"]
    value_formats = ["value"]
    ticker_flag = False
    data = dict(json_data[0])
    year = "YEAR"
    ticker = "TICKER"
    quarter = "QUARTER"
    #pp = pprint.PrettyPrinter(indent=1)
    #pp.pprint(json_data)
    try:
        ticker = (str(input_file).split('/'))[2]
        print(ticker)
        #data.get("Document And Entity Information").get("Trading Symbol").get("value")
        # if(len(ticker) > 5):
        #     item = ticker.strip(' ')
        #     items = item.split(',')
        #     ticker = items[0]
    except AttributeError:
        print("[AttributeError] Issues with data")
    except:
        print("[ERROR] Unable to create collection name")
        
    for d_e_format in document_entity_formats:
        for year_format in document_fiscal_year_formats:
            for value in value_formats:
                try:
                    year = get_year(data,d_e_format,year_format,value)
                    print(year)

                except AttributeError:
                    print("[AttributeError] Issues with data")
                except:
                    print("[ERROR] Unable to create collection name")
    
    
    for d_e_format in document_entity_formats:
        for period_format in document_fiscal_period_formats:
            for value in value_formats:
                try:
                    quarter = get_quarter(data,d_e_format,period_format,value)
                    print(year)

                except AttributeError:
                    print("[AttributeError] Issues with data")
                except:
                    print("[ERROR] Unable to create collection name")

    return str(ticker) + "_" + str(year) + "_" + str(quarter)
    
def main():
    cli_parser = OptionParser(
        usage='usage: %prog <input.json> <username> <password>'
        )
    (options, args) = cli_parser.parse_args()

    # Input file checks
    if len(args) < 2:
        cli_parser.error("You have to supply 2 arguments, USAGE: .json username")
    input_file_name = args[0]
    if not os.path.exists(input_file_name):
        cli_parser.error("The input file %s you supplied does not exist" % input_file_name)
    temp_json = getJsonObj(input_file_name)
    # temp_json = standardize(temp_json)
    convert_to_json(temp_json)
    converted_json = temp_json
    #print(type(converted_json))
    # JAROD's FUNCTION
    collection = get_collection_name(converted_json, input_file_name)
    print(collection)
    #collection = (sys.argv[1]).strip('.')
    username = sys.argv[2]
    password = sys.argv[3]
    print("Adding to MongoDB...")   
    save_to_mongodb(converted_json, collection, username, password)

if __name__ == "__main__":
    print("[WARNING] STILL UNDER DEVELOPMENT")
    main()
