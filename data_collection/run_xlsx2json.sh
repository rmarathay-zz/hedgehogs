
echo "Converting .xlsx to .json!"
for folder in ./fin_data/*
do
	for xlsx in ./$folder/*.xlsx
	do
		python xlsx2json.py "$xlsx"
	done
done

