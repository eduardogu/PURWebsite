from PUR.models import Permit

import csv

dataReader = csv.reader(open("Businesses.csv"), delimiter = ',',
						quotechar = '"')