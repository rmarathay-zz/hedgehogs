from import_hedgehogs import *

def convert_excel_to_csv(excel_file):
    wb = load_workbook(excel_file)
    counter = 0
    for sheet in wb.sheetnames:
        sh = wb[sheet]
        csv_file = open(str(counter)+'.csv', 'w')
        wr = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
        for rows in range(sh.nrows):
            wr.writerow(sh.row_values(rownum))
        csv_file.close()

# def csv_from_excel(excel_file):
#     wb = xlrd.open_workbook(excel_file')
#     sh = wb.sheet_by_name('Sheet1')
#     your_csv_file = open('your_csv_file.csv', 'w')
#     wr = csv.writer(your_csv_file, quoting=csv.QUOTE_ALL)
#     for rownum in range(sh.nrows):
#         wr.writerow(sh.row_values(rownum))
#     your_csv_file.close()
        
def main():
    print("v0.0.1")
    if(len(sys.argv) < 2):
        print("[ERROR] Please provide a filename")
    convert_excel_to_csv(sys.argv[1])

if __name__ == '__main__':
    main()