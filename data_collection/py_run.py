import os


def main():
	print("Start!")
	directory = "./fin_data"
	for ticker in os.listdir(directory):
		dir1 = directory + "/" + ticker
		print(ticker)
		for _file in os.listdir(dir1):
			print(_file)
			if(_file.endswith(".xlsx")):
				exec_str = "python xlsx2json.py " + _file
				exec(exec_str)
			if(_file.endswith(".json")):
				exec_str = "python json2mongodb.py " + ticker
				exec(exec_str)
if __name__ == '__main__':
	main()
