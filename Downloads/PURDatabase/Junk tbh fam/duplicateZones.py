from PUR.models import Firm, Zone
import csv

numList = []

for firm in Firm.objects.all():
	numList.append(firm.firm_id)

for num in numList:
	zone_id = []
	finalZoneList = []

	firm = Firm.objects.get(firm_id = num)
	zone_list = firm.zone_set.all()
	for zone in zone_list:
		if zone.zone_id not in zone_id:
			zone_id.append(zone.zone_id)
			finalZoneList.append(zone)
		else:
			toDelete = Zone.objects.get(zone_id = zone.zone_id)
			toDelete.delete(keep_parents=True)

	firm.zone_set = finalZoneList
	firm.save()
