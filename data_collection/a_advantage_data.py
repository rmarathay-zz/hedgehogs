from alpha_vantage.timeseries import TimeSeries
import json
import sys
JSON_INDENT = 4
print(type(sys.argv[1]))
print(type(sys.argv[2]))
ts = TimeSeries(key='H0WG63BW6PGFSYEB')
# Get json object with the intraday data and another with the call's metadata
data, meta_data = ts.get_intraday(sys.argv[1],interval = sys.argv[2])
dic = {}
for i,j in data.items():
    dic[i] = {}
    for x,y in j.items():
        dic[i][x.split(".")[1].strip()] = y
data = dic
#print(data)
with open("minute.json", 'w', encoding = 'utf-8') as output_file:
    output_file.write(
        str(
            json.dumps(
                data,
                indent=JSON_INDENT,
# Commented out because str is python3 and accounts for encoding specifications
#                     ensure_ascii=False,
#                     encoding='utf-8'
            )
        )
    )

