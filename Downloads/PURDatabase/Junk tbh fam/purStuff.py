class Site:
	#MTRS
	meridian = "" 
	township = "" 
	townshipDir = "" 
	siteRange = "" 
	rangeDir = "" 
	section = "" 
	site_id = ""

	def __init__(self, meridian, township, townshipDir, siteRange, rangeDir, section, site_id):
		self.meridian = meridian
		self.township = township
		self.townshipDir = townshipDir
		self.siteRange = siteRange
		self.rangeDir = rangeDir
		self.section = section
		self.site_id = site_id

#use_no, prodno, chem_code, prodchem_pct, lbs_chm_used, lbs_prd_used, #5
#amt_prd_used, unit_of_meas, acre_planted, unit_planted, acre_treated, #10
#unit_treated, applic_cnt, applic_dt, applic_time, county_cd, base_ln_mer, #16
#township, tship_dir, range, range_dir, section, site_loc_id, grower_id,#23
#license_no, planting_seq, aer_gnd_ind, site_code, qualify_cd, #28
#batch_no, document_no, summary_cd, record_id, comtrs, error_flag #34

class Firm:
	name = ""
	address = ""
	city = ""
	state = ""
	zipCode = ""

	siteList = []

	def __init__(self, name, address, city, state, zipCode):
		self.name = name 
		self.address = address
		self.city = city
		self.state = state
		self.zipCode = zipCode

	def printFirm(self):
		print("******************************")
		print("Name:\t", self.name)
		print("Address:\t", self.address)
		print("City:\t", self.city)
		print("State:\t", self.state)
		print("Zip: \t", self.zipCode)
		print("Site List: ")		
		for i in range(0, len(self.siteList)):
			print(self.siteList[i].site_id)

import csv

allFirms = []
existingFirms = []
manualEntryFirms = []

name = ""
address = ""
city = ""
state = ""
zipCode = ""

dataReader = csv.reader(open("udc14_27.txt"), delimiter = ',', 
						quotechar = '"')


for row in dataReader:
	num = row[23]
	if(num == ""):
		continue
	otherReader = csv.reader(open("permits.csv"), delimiter = ',', 
						 quotechar = '"')
	if num not in existingFirms:
		for row in otherReader:
			if num[-7:] == row[0]:
				existingFirms.append(num)
				newFirm = Firm(row[1], row[3], row[4], row[5], row[6])
				allFirms.append(newFirm)
				break
		manualEntryFirms.append(num)
		continue

	index = existingFirms.index(num)
	if row[22] not in allFirms[index].siteList:
		newSite = Site(row[16], row[17], row[18], row[19], row[20], row[21], row[22])
		allFirms[index].siteList.append(newSite)

for i in range(0, len(existingFirms)):
	print("******************************")
	print(existingFirm[i])
	allFirms[i].printFirm()

exit()

