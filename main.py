import xlrd
import csv
import boto3
import botocore
from datetime import datetime

def csv_from_excel(xlsFile):
    start = datetime.now()

    wb = xlrd.open_workbook(xlsFile)
    sh = wb.sheet_by_index(0)
    print(sh.colinfo_map)

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
    print('# of rows: ', count)
    your_csv_file.close()

s3 = boto3.resource('s3')

# Print out bucket names
for bucket in s3.buckets.all():
    print(bucket.name)

BUCKET_NAME = 'my-bucket' # replace with your bucket name
KEY = 'my_image_in_s3.jpg' # replace with your object key

try:
    s3.Bucket(BUCKET_NAME).download_file(KEY, 'my_local_image.jpg')
except botocore.exceptions.ClientError as e:
    if e.response['Error']['Code'] == "404":
        print("The object does not exist.")
    else:
        raise

csv_from_excel('C:/Users/hengy/Downloads/News_Final.xls')

# Upload a file
data = open('file.csv', 'rb')
s3.Bucket('my-bucket').put_object(Key='file.csv', Body=data)