#program that reads the EmployeePay.csv file and prints out details of each employee

import csv

employee = open('EmployeePay.csv', 'r', newline='')

reader = csv.reader(employee)

next(reader)

for row in reader:
    print('ID:',row[0])
    print('First Name:',row[1])
    print('Last Name:',row[2])
    print('Salary:',row[3])
    print('Bonus:',row[4])
    print('\n')


employee.close()