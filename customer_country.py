#program that reads the file customers.csv and produces a new file containing the customer name and country they are from

import csv

# open the csv file in read mode
customers = open('customers.csv','r', newline='')
customer_country = open('customer_country.csv', 'w', newline='')

# the delimiter ',' tells the program how the columns are seperated
reader = csv.reader(customers, delimiter=',')
writer = csv.writer(customer_country, delimiter=',')

# skip the first line in the csv file if it contains a header record
fieldnames = ('FirstName','LastName','Country')
next(reader)
writer.writerow(fieldnames)

# using a for loop you can step through the file, one line at a time
for row in reader:
    FirstName = row[1]
    LastName = row[2]
    Country = row[4]
    new_row = [FirstName,LastName,Country]
    writer.writerow(new_row)


    
customers.close()
customer_country()
