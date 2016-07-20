csv_filepathname = "C:\Users\eduardo\PycharmProjects\PURDatabase\PUR"
PUR_home = "C:\Users\eduardo\PycharProjects\PURDatabase"

import sys, os
sys.path.append(PUR_home)
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'


from PUR.models import Permit
import csv

dataReader = csv.reader(open("Businesses.csv"), delimiter = ',',
						quotechar = '"')

for row in dataReader:
	permit = Permit()
	permit.permit_type = row[0]
	permit.permit_num = row[1]
	permit.permit_name = row[2]
	permit.permit_add = row[3]
	permit.permit_city = row[4]
	permit.permit_state = row[5]
	permit.permit_zip = row[6]
	permit.permit_issue = row[7]
	permit.permit_expiriation = row[8]
	permit.permit_county = row[9]
	permit.save()

dataReader = csv.reader(open("Individuals.csv"), delimiter = ',',
						quotechar = '"')

for row in dataReader:
	permit = Permit()
	permit.permit_type = row[0]
	permit.permit_num = row[1]
	permit.permit_name = row[3] + " " + row[2]
	permit.permit_add = row[4]
	permit.permit_city = row[5]
	permit.permit_state = row[6]
	permit.permit_zip = row[7]
	permit.permit_issue = row[8]
	permit.permit_expiration = row[9]
	permit.permit_county = row[10]
	permit.save()


lineList = []

with open("ayyelmaoWithNoLines.txt", 'r') as file:
	for line in file:
		line = line.strip()
		lineList.append(line)

i = 0

while i < len(lineList):
	flag = True
	x = Pesticide()
	x.pesticide_manufacturer_num = lineList[i]
	i+=1
	x.pesticide_manufacturer = lineList[i]
	i+=1
	x.pesticide_manufacturer_add = lineList[i]
	i+=2
	if i >= len(lineList):
		break
	while(flag):
		if(lineList[i] == "****************************"):
			i+=1
			break
		x.pesticide_name = lineList[i]
		i+=1
		x.pesticide_id = lineList[i]
		i+=1
		x.save()

		x = Pesticide(x.pesticide_manufacturer, 
					  x.pesticide_manufacturer_num, 
					  x.pesticide_manufacturer_add)