#Sample usage in terminal: Python main.py your_xls.xls your_csv.csv
import pandas as pd
import csv
from datetime import datetime
import logging
import sys
import argparse


def csv_from_excel(xlsFile, csvFile):
    start = datetime.now()
    logging.basicConfig(filename='logFile.log', level=logging.INFO)

    df = pd.read_excel(xlsFile, dtype={'your_col1':str, 'your_col2':str})
    #replace 'your_col1' with your column name. Delete or add more columns
    #that you want to explicitly specify type. Ex. str, float, int

    df.to_csv(csvFile, index=False, quoting = csv.QUOTE_MINIMAL, header=True)
    #edit above line for quoting and header changes
        #Quoting (4 options): csv.QUOTE_MINIMAL (default), csv.QUOTE_ALL, csv.QUOTE_NONE, csv.QUOTE_NONNUMERIC
        #Header (2 options): True (default), False

    end= datetime.now()
    logging.info('run time:  %s' %(end-start)  )
    logging.info('start:  %s' %start )
    logging.info('end:  %s \n' %end )

try:
    #Create command line parser with two positional arguments
    parser = argparse.ArgumentParser(description = 'xls(x) to csv converter')
    parser.add_argument('your_xls', type = str, nargs=1, help = 'excel file name' )
    parser.add_argument('your_csv', type = str, nargs=1, help = 'csv file name' )
    args = parser.parse_args()

    #call the function with file names receive in command line
    csv_from_excel(args.your_xls[0], args.your_csv[0])

except:
    logging.error('%s \n' %(sys.exc_info()[1]))

    #1. Quoting: default quoting = csv.QUOTE_MINIMAL(line 9)
    #2. Dates: default date format is YYYY-MM-DD
    #3. Numbers: numbers are displayed correctly. (2017 is NOT displayed as 2017.0)
    #4. NULL: NULL is handled correctly. Blank cell will be displayed as ,,
    #5. Trailing/Leading Zeros: This is a non issue. Ex. 000123 and 0.1000 must be stored
    #   as text. (attempting to store 000123 as a number will store 123 instead). Text
    #   is easily processed correctly.
    #6. Headers: default include headers. To omit set header=False(line 9)

