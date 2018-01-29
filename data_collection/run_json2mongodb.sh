echo "Uploading .json to MongoDB!"
for folder in ./fin_data/*
do
	for json in ./$folder/*.json
	do
		IFS="/"
		arr=($folder)
		echo "folder: $folder"
		echo "ticker: ${arr[-1]}"
		echo "json:" $json
		python json2mongodb.py "$json" "${arr[-1]}"		
	done
done
