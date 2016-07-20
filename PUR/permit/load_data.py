csv_filepathname = "C:/Users/eduardo/PycharmProjects/PURDatabase/PUR/permit"
PUR_home = "C:/Users/eduardo/PycharProjects/PURDatabase/PUR"

import sys, os
sys.path.append(PUR_home)
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

from PUR.models import Permit
import csv

dataReader = csv.reader(open(csv_filepathname), delimiter = ',',
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
	permit.permit_experiation = row[8]
	permit.permit_date = row[9]
	permit.permit_county = row[10]
	permit.save()
