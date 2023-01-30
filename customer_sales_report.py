#program that reads the sales.csv file and creates a new file with the customer ID and calculated total

import csv

sales = open ('sales.csv', 'r', newline='')
sales_report = open('salesreport.csv', 'w', newline='')

reader = csv.reader(sales, delimiter=',')
writer = csv.writer(sales_report, delimiter=',')

header = ['customer |', 'Total']
writer.writerow(header)
next(reader)


total = 0
ids = ''

for x in reader:
    row = [format(ids, '>9'), format(total, '.2f')]
    if x[0] != ids:
        if ids:
            writer.writerow(row)
        total = 0
        ids = x[0]
    subtotal = float(x[3])
    tax = float(x[4])
    freight = float(x[5])
    tot = subtotal + tax + freight
    total += tot
row = [format(ids, '>9'), format(total, '.2f')]
writer.writerow(row)

sales.close()
sales_report.close()