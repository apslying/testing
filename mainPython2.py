from __future__ import absolute_import
import pandas as pd
import csv
from datetime import datetime
import logging
import sys

def csv_from_excel(xlsFile, csvFile):
    start = datetime.now()
    logging.basicConfig(filename=u'logFile.log', level=logging.INFO)

    df = pd.read_excel(xlsFile, dtype={u'your_col1':unicode, u'your_col2':unicode})
    #replace 'your_col1' with your column name. Delete or add more columns
    #that you want to explicitly specify type. Ex. str, float, int

    df.to_csv(csvFile, index=False, quoting = csv.QUOTE_MINIMAL, header=True)
    #edit above line for quoting and header changes
        #Quoting (4 options): csv.QUOTE_MINIMAL (default), csv.QUOTE_ALL, csv.QUOTE_NONE, csv.QUOTE_NONNUMERIC
        #Header (2 options): True (default), False

    end= datetime.now()
    logging.info(u'run time:  %s' %(end-start)  )
    logging.info(u'start:  %s' %start )
    logging.info(u'end:  %s' %end )

try:
    csv_from_excel(u'your_xls.xls', u'your_csv.csv')
except:
    logging.error(sys.exc_info()[1])

    #replace 'your_xls.xls' with your xls/xlsx file name. same with csv
    #include full path if not in current directory. change \ to / in path


    #1. Quoting: default quoting = csv.QUOTE_MINIMAL(line 9)
    #2. Dates: default date format is YYYY-MM-DD
    #3. Numbers: numbers are displayed correctly. (2017 is NOT displayed as 2017.0)
    #4. NULL: NULL is handled correctly. Blank cell will be displayed as ,,
    #5. Trailing/Leading Zeros: This is a non issue. Ex. 000123 and 0.1000 must be stored
    #   as text. (attempting to store 000123 as a number will store 123 instead). Text
    #   is easily processed correctly.
    #6. Headers: default include headers. To omit set header=False(line 9)
    #TODO: log file

