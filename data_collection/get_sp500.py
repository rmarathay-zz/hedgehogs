import json
import requests
import sys

def get_sp500json():
    url = "https://pkgstore.datahub.io/core/s-and-p-500-companies/constituents_json/data/64dd3e9582b936b0352fdd826ecd3c95/constituents_json.json"
    response = json.loads(requests.get(url).text)
    return response

if __name__ == "__main__":
    raw = get_sp500json()
    text_file = open("companies.txt", "w")
    i = 0
    for company in raw:
        text_file.write(company['Symbol'])
        text_file.write('\n')
        i += 1
    text_file.close()