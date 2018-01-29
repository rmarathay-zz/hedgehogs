# Use this script to download xlsx 

declare -a tickers=('A' 'AAL' 'AAP' 'AAPL' 'ABBV' 'GOOG' 'TRV' 'TSLA')

for ticker in "${tickers[@]}"
do
	echo "Downloading xlsx files"
	python xlsxDownloader.py "$ticker"
done
