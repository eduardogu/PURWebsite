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

from PUR.models import Firm
firm = Firm()
firm.firm_name = "fakeName"
firm.firm_address = "fakeAddress"
firm.firm_city = "fakeCity"
firm.firm_zip = "fakeZip"
firm.firm_phone="38383838"
firm.firm_id = "fakeid"
firm.save()

from PUR.models import Pesticide
p1 = Pesticide()
p1.pesticide_name = "pesticideName"
p1.pesticide_id = "fakepestid"
p1.pesticide_manufacturer = "fakemanu"
p1.pesticide_manufacturer_num = "33333"
p1.pesticide_manufacturer_add = "fakeddress"
p2 = Pesticide()
p2.pesticide_name = "pesticideName"
p2.pesticide_id = "fakepestid"
p2.pesticide_manufacturer = "fakemanu"
p2.pesticide_manufacturer_num = "33333"
p2.pesticide_manufacturer_add = "fakeddress"
p1.save()
p2.save()

from PUR.models import Permit 
permit = 


#Push Contacts#
from PUR.models import Contact, Permit
import csv

dataReader = csv.reader(open("contacts.csv"), delimiter = ',', 
						quotechar = '"')

permit_numbers = []

for permit in Permit.objects.all():
	permit_numbers.append(permit.permit_num)

for row in dataReader:
	c = Contact()
	c.contact_id = row[0]
	c.contact_name = row[1]
	c.contact_type = row[2]
	c.contact_permit_num = row[3]
	c.contact_date = row[5]
	c.contact_exp = row[6]
	c.contact_address = row[8]
	c.contact_city = row[10]
	c.contact_state = row[11]
	c.contact_zip = row[12]
	c.contact_phone = row[13]
	c.contact_altPhone = row[14]
	c.contact_fax = row[15]
	if c.contact_permit_num in permit_numbers:
		permit = Permit.objects.get(permit_num=c.contact_permit_num)
		permit.contact_set.add(c)
		permit.save()
	c.save()
