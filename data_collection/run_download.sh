# Use this script to download xlsx 

#!/bin/bash
declare -a tickers=('A' 'AAL' 'AAP' 'AAPL' 'ABBV' 'GOOG' 'TRV' 'TSLA')
echo "Downloading"
for ticker in "${tickers[@]}"
do
	echo "Downloading xlsx files"
	python xlsxDownloader.py "$ticker"
done
