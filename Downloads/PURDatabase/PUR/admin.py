from django.contrib import admin
# these lines added:

from django.contrib import admin
from .models import Firm, County, Pesticide, Permit, Zone, Profile, Report, Commodity
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

#Database Entries
class FirmAdmin(admin.ModelAdmin):
    list_display = ['firm_name']
    ordering = ['firm_name']

admin.site.register(Firm, FirmAdmin)

class CountyAdmin(admin.ModelAdmin):
    list_display = ['county_name', 'county_number']
    ordering = ['county_number']

admin.site.register(County, CountyAdmin)

class PesticideAdmin(admin.ModelAdmin):
    list_display = ['pesticide_name', 'pesticide_id', 'active']
    ordering = ['pesticide_name']

admin.site.register(Pesticide, PesticideAdmin)

class PermitAdmin(admin.ModelAdmin):
    list_display = ['permit_name', 'permit_num']
    ordering = ['permit_num']

admin.site.register(Permit, PermitAdmin)

class ZoneAdmin(admin.ModelAdmin):
    list_display = ['zone_name', 'zone_id',
                    'zone_range_dir', 'zone_township_dir',
                    'zone_bm']
    ordering = ['zone_name']

admin.site.register(Zone, ZoneAdmin)

class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user']
    ordering = ['user']

admin.site.register(Profile, ProfileAdmin)

class CommodityAdmin(admin.ModelAdmin):
    list_display = ['commodity_name', 'commodity_code', 'qualifier']
    ordering = ['commodity_code']

admin.site.register(Commodity, CommodityAdmin)
class ReportAdmin(admin.ModelAdmin):
    list_display = ['firm', 'permit', 'dateUpdate', 'status']
    ordering = ['dateUpdate']

admin.site.register(Report, ReportAdmin)