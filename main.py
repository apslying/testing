import xlrd
import csv
from datetime import datetime

def csv_from_excel(xlsFile):
    start = datetime.now()

    wb = xlrd.open_workbook(xlsFile)
    sh = wb.sheet_by_index(0)

    # edit date column data

    # specify date column, add looping
    colnum = 5
    for row in range(1, sh.nrows):
        # TODO: assumes first row header
        cellValue = sh.cell(row, colnum).value
        dt = xlrd.xldate.xldate_as_datetime(cellValue, 0)
        # TODO: import xlwt to write to cells

    with open('file.csv', 'w', newline='') as your_csv_file:
        wr = csv.writer(your_csv_file, quoting=csv.QUOTE_ALL)
        for rownum in range(sh.nrows):
            try:
                wr.writerow(sh.row_values(rownum))
            except UnicodeEncodeError:
                pass
        for rownum in range(sh.nrows):
            try:
                #print(rownum, sh.row_values(rownum))
                wr.writerow(sh.row_values(rownum))
            except UnicodeEncodeError:
                pass

    end = datetime.now()
    # print('run time: ', end-start)
    # print('start: ', start)
    # print('end: ', end)
    your_csv_file.close()

csv_from_excel('C:/Users/hengy/Downloads/News_Final.xls')

