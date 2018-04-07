

hedgehogsdata_collection
Name
Last Modified

object_pairs_hook
​
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
    for item in json_:
        collection.insert_one(item)
    # file.close()
def getJsonObj(input_file_name):
    with open(input_file_name) as fp:
        data = fp.read()
        json_ = json.loads(data, encoding='utf-8', object_pairs_hook=OrderedDictWithKeyEscaping)
    return json_
    
    
    
def standardize(obj):
    standardKeys= ["Document Type"
    "Amendment Flag"
    "Document Period End Date"
    "Document Fiscal Year Focus"
    "Document Fiscal Period Focus"
    "Trading Symbol"
    "Entity Registrant Name"
    "Entity Central Index Key"
    "Current Fiscal Year End Date"
    "Entity Filer Category"
    "Entity Common Stock, Shares Outstanding"]
    # delete items from list as you go along ones remaining add to db?
    
    for key in obj[0]:
        ##print(key)
        if key == 'title':
            continue
        newKey = "Document and Entity Information"
        temp = key
        if(newKey!=key):
            obj[0][newKey]=obj[0][key]
            del obj[0][key]
            temp = newKey
        """
        i=0
        for nextKey in obj[0][temp]:
            newKey = standardKeys[i]
            if(newKey!=nextKey):
                obj[0][temp][newKey] =obj[0][temp][nextKey]
                del obj[temp][nextKey]
            i+=1
        """
        break
    return obj
            
            
def json2File(obj):
    with open('data.txt', 'w') as outfile:
         json.dump(obj, outfile, indent = 4,ensure_ascii = False)
        
def get_collection_name(input_file_name):
    data_list = json.load(open(input_file_name))
    data = dict(data_list[0])
    year = "YEAR"
    ticker = "TICKER"
