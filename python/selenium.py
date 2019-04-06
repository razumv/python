import csv
from bs4 import BeautifulSoup
import requests


row = ['1', ' LOH', ' PIDR']

with open('people1.csv', 'a') as csvFile:
   	writer = csv.writer(csvFile)
   	writer.writerow(row)

csvFile.close()