#program that reads the sales.csv file and creates a new file with the customer ID and calculated total

import csv

sales = open ('sales.csv', 'r', newline='')
sales_report = open('salesreport.csv', 'w', newline='')

reader = csv.reader(sales, delimeter=',')
writer = csv.writer(sales_report, delimeter=',')

fieldnames = ['ID', 'Total']
next(reader)
writer.writerow(fieldnames)

sales = [[]*2]
IDs = []

for row in reader:
    ID = row[0]
    Sales = row[3]
    IDSales = [ID, Sales]
    sales.extend(IDSales)
    IDs.extend(ID)

#remove duplicates from IDs
report = [[]*2]

for i in IDs: 
    if i not in report: 
        report.append(i)

#for loop through both lists, if id matches add it to the number