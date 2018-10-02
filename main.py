# import pandas as pd
# import csv
# data_xls = pd.read_excel('C:/Users/hengy/PycharmProjects/noVenv/2011InternationalComparisonProgramresults - Copy.xlsx', 'TABLE R1',)
# data_xls.to_csv('file.csv', encoding='utf-8', quoting=csv.QUOTE_NONNUMERIC)


import xlrd
import csv
from datetime import datetime

def csv_from_excel():
    start = datetime.now()
    xlsFile = 'C:/Users/hengy/Downloads/News_Final.xls'

    wb = xlrd.open_workbook(xlsFile)
    #change sheet name
    sh = wb.sheet_by_index(0)
    # sh = wb.sheet_by_name('News_Final')
    print(sh)

        #newline
        #print runtime
    #general to date, imp
    #xls to csv, then zip csv, not important
    #check if file is too big
    #download excel
    #connect amazon s3, get 90% code
        #find 66MB xls file
        #call helpdesk to download python
    #how it processes dates
    #how fast is the code, n^2, important

    count=0
    with open('file.csv', 'w', newline='') as your_csv_file:
        wr = csv.writer(your_csv_file, quoting=csv.QUOTE_ALL)
        for rownum in range(sh.nrows):
            try:
                count+=1

                #print(rownum, sh.row_values(rownum))
                wr.writerow(sh.row_values(rownum))
            except UnicodeEncodeError:
                pass
                #print('error')

    end = datetime.now()
    print('run time: ', end-start)
    print('start: ', start)
    print('end: ', end)
    print(count)
    your_csv_file.close()

csv_from_excel()