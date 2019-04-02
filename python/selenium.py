import csv

row = ['4', ' Danny', ' New York']

with open('people1.csv', 'a') as csvFile:
    writer = csv.writer(csvFile)
    writer.writerow(row)

csvFile.close()