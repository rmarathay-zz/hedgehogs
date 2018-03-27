filename="$1"

while read -r ticker
do
	echo "Downloading xlsx files"
	python xlsxDownloader.py "$ticker"  
    for xlsx in ./fin_data/$ticker/*.xlsx
    do
        python xlsx2json.py "$xlsx"
    done
    for xlsx in ./fin_data/$ticker/*.xlsx
    do
        rm "$xlsx"
    done
    # insert script here to send json to mongodb
    # insert script here to delete json
done < "$filename"