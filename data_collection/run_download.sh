# Use this script to download xlsx 

declare -a tickers=('T')

for ticker in "${tickers[@]}"
do
	echo "Downloading xlsx files"
	python xlsxDownloader.py "$ticker"
done
