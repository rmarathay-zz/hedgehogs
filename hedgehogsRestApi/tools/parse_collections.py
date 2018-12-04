import csv
import pickle

c_dict = dict()
def save_obj(obj, name ):
    with open(name+'.pkl', 'wb') as f:
        pickle.dump(obj, f, pickle.HIGHEST_PROTOCOL)

def load_obj(name ):
    with open(name + '.pkl', 'rb') as f:
        return pickle.load(f)

def intial_save():
	with open('constituents.csv') as csv_file:
		csv_reader = csv.reader(csv_file, delimiter=',')
		line_count = 0
		for row in csv_reader:
			if line_count == 0:
				line_count += 1
				continue
			else:
				c_dict[row[1].replace('"', '')] = [row[0], row[2]]
				print('\t',row[1], row[0], row[2])
				line_count += 1

	save_obj(c_dict, 'constituents')

intial_save()
print(load_obj('constituents'))
