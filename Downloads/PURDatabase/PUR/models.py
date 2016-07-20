from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from django.forms import ModelForm

class Pesticide(models.Model):
    pesticide_name = models.CharField(max_length=90)
    pesticide_id = models.CharField(max_length=20)
    active = models.BooleanField(default=False)
    manufacturer = models.CharField(max_length=50, blank=True, null=True)
    manuAddress = models.CharField(max_length=50, blank=True, null=True)
    dateEntered = models.CharField(max_length=10, blank=True, null=True)

    def __str__(self):
        return self.pesticide_name

class Firm(models.Model):
    # Firm Information
    firm_name = models.CharField(max_length=80)
    firm_address = models.CharField(max_length=80)
    firm_city = models.CharField(max_length=80)
    firm_zip = models.CharField(max_length=11)
    firm_phone = models.CharField(max_length=13)
    firm_id = models.CharField(max_length=8)
    firm_email = models.CharField(max_length=70, default="")
    # Taken From Database
    pesticides = models.ManyToManyField(Pesticide, blank=True, null=True)

    def __str__(self):
        return self.firm_name

class County(models.Model):
    county_name = models.CharField(max_length=30)
    county_number = models.CharField(max_length=30)

    def __str__(self):
        return self.county_name

class Zone(models.Model):
    zone_name = models.CharField(max_length=30, blank=True)
    zone_id = models.CharField(max_length=10)
    zone_section = models.CharField(max_length=10)
    zone_township = models.CharField(max_length=3)
    zone_township_dir = models.CharField(max_length=3)
    zone_range = models.CharField(max_length=3)
    zone_range_dir = models.CharField(max_length=3)
    zone_bm = models.CharField(max_length=1)
    acreage = models.CharField(max_length=10, null=True, blank=True)
    firm = models.ForeignKey(Firm, blank=True, null=True)

    def __str__(self):
        return self.zone_name

    def generateMTRS(self):
        return self.zone_bm + self.zone_township + \
               self.zone_township_dir + self.zone_range + \
               self.zone_range_dir + self.zone_section

class Profile(models.Model):
    user = models.OneToOneField(User)
    is_grower = models.BooleanField(default=False)
    is_county = models.BooleanField(default=True)
    is_manager = models.BooleanField(default=True)
    is_worker = models.BooleanField(default=False)
    firm = models.ManyToManyField(Firm, blank=True, null=True)

    def __str__(self):
        return self.user.username

class Permit(models.Model):
    permit_name = models.CharField(max_length=30)
    permit_agent = models.CharField(max_length=50, blank=True)
    permit_num = models.CharField(max_length=10)
    permit_type = models.CharField(max_length=40, blank=True)
    permit_city = models.CharField(max_length=30)
    permit_state = models.CharField(max_length=14)
    permit_add = models.CharField(max_length=80, blank=True)
    permit_zip = models.CharField(max_length=11)
    permit_county = models.CharField(max_length=40, default="Monterey")
    permit_issue = models.CharField(max_length=12, blank=True)
    permit_expiration = models.CharField(max_length=12, blank=True)
    firm = models.ForeignKey(Firm, blank=True, null=True)
    contacts = models.ManyToManyField(Profile, null=True, blank=True)

    def __str__(self):
        return self.permit_name

class Contact(models.Model):
    contact_id = models.CharField(max_length=6)
    contact_name = models.CharField(max_length=50)
    contact_type = models.CharField(max_length=3)
    contact_permit_num = models.CharField(max_length=12)
    contact_date = models.CharField(max_length=10, null=True, blank=True)
    contact_exp = models.CharField(max_length=10, null=True, blank=True)
    contact_address = models.CharField(max_length=80)
    contact_city = models.CharField(max_length=40)
    contact_state = models.CharField(max_length=2)
    contact_zip = models.CharField(max_length=10)
    contact_phone = models.CharField(max_length=15, null=True, blank=True)
    contact_altPhone = models.CharField(max_length=15, null=True, blank=True)
    contact_fax = models.CharField(max_length=15)
    contact_list = models.ManyToManyField(Permit, null=True, blank=True)

    def __str__(self):
        return self.contact_name


class Commodity(models.Model):
    commodity_name = models.CharField(max_length=40)
    commodity_code = models.CharField(max_length=5)
    qualifier = models.CharField(max_length=2, null=True, blank=True)
    active = models.BooleanField(default=True)
    zone = models.ManyToManyField(Zone, null=True, blank=True)

    def __str__(self):
        return self.commodity_name

class Report(models.Model):
    PRODUCT_USE_CHOICES = (
        ('lb', 'POUNDS'),
        ('oz', 'OUNCES'),
        ('pt', 'PINTS'),
        ('qt', 'QUARTS'),
        ('ga', 'GALLONS'),
    )

    STATUS_CHOICES = (
        ('dr', 'DRAFT'),
        ('sb', 'SUBMITTED'),
        ('re', 'REVIEWING'),
        ('ap', 'APPROVED'),
        ('nr', 'NEEDS REVISION'),

    )

    #PreDefined
    firm = models.ForeignKey(Firm, null=True, blank=True, on_delete=models.SET_NULL)
    firm_name=models.CharField(max_length=80, null=True, blank=True)
    firm_address=models.CharField(max_length=80, null=True, blank=True)
    firm_city=models.CharField(max_length=80, null=True, blank=True)
    firm_zip=models.CharField(max_length=11, null=True, blank=True)
    firm_phone=models.CharField(max_length=13, null=True, blank=True)

    pesticides = models.ManyToManyField(Pesticide, null=True, blank=True)
    pesticide_name=models.CharField(max_length=90, blank=True, null=True)
    pesticide_id = models.CharField(max_length=20, blank=True)
    pesticide_manufacturer = models.CharField(max_length=50, blank=True, null=True)

    permit = models.ForeignKey(Permit, null=True, blank=True, on_delete=models.SET_NULL)
    permit_num=models.CharField(max_length=7, null=True, blank=True)

    zones = models.ManyToManyField(Zone, null=True, blank=True)
    zone_id = models.CharField(max_length=10, blank=True, null=True)
    zone_section = models.CharField(max_length=10, blank=True, null=True)
    zone_township = models.CharField(max_length=3, blank=True, null=True)
    zone_township_dir = models.CharField(max_length=3, blank=True, null=True)
    zone_range = models.CharField(max_length=3, blank=True, null=True)
    zone_range_dir = models.CharField(max_length=3, blank=True, null=True)
    zone_bm = models.CharField(max_length=1, blank=True, null=True)
    zone_acreage=models.CharField(max_length=10, blank=True, null=True)
    #AutoGenerated
    date_filed = models.DateTimeField(editable=False)
    rate_of_application = models.FloatField(default=0.0)
    #Users
    creator = models.ForeignKey(Profile,related_name='Creator', null=True, blank=True, on_delete=models.SET_NULL)
    reviewer = models.ForeignKey(Profile, related_name='Reviewer', null=True, blank=True, on_delete=models.SET_NULL)
    #Pesticide Application
    time_of_application = models.TimeField(auto_now=False, auto_now_add=False)
    date_of_application = models.DateField(auto_now=False, auto_now_add=False, blank=True)
    number_of_applications = models.IntegerField(default=0, blank=True, null=True)

    method_of_application = models.CharField(max_length=2, blank=True, null=True)
    total_application = models.IntegerField(default=0, blank=True, null=True)
    product_measurement = models.CharField(max_length=2, blank=True, null=True)
    #Zone/Site
    block_id = models.CharField(max_length=10, blank=True, null=True)
    #status
    status = models.CharField(max_length = 2, default='dr')
    dateUpdate = models.DateTimeField()
    comment = models.CharField(max_length=400, blank=True, null=True)

    def getDateUpdate(self):
        return str(self.dateUpdate)

    def populateFirm(self):
        self.firm_name = self.firm.firm_name
        self.firm_address = self.firm.firm_address
        self.firm_city = self.firm.firm_city
        self.firm_zip = self.firm.firm_zip
        self.firm_phone=self.firm.firm_phone
        self.save()
        return True

    def populatePermit(self):
        self.permit_num = self.permit.permit_num
        self.save()
        return True

    def populatePesticide(self):
        list = self.pesticides.all()
        pesticide = list[0]
        self.pesticide_name=pesticide.pesticide_name
        self.pesticide_id=pesticide.pesticide_id
        self.pesticide_manufacturer =pesticide.manufacturer
        self.save()

    def populateZone(self):
        list = self.zones.all()
        someZone = list[0]
        self.zone_id=someZone.zone_id
        self.zone_bm = someZone.zone_bm
        self.zone_range = someZone.zone_range
        self.zone_range_dir = someZone.zone_range_dir
        self.zone_section = someZone.zone_section
        self.zone_township = someZone.zone_township
        self.zone_township_dir = someZone.zone_township_dir
        self.zone_acreage = someZone.acreage
        self.save()

    def populateAll(self):
        self.populateFirm()
        self.populatePermit()
        self.populatePesticide()
        self.populateZone()
        self.save()

    def submit(self):
        self.status = 'sb'
        self.save()
        return
    def inReview(self):
        self.status = 're'
        self.save()
        return
    def approve(self):
        self.status = 'ap'
        self.save()
        return
    def revision(self):
        self.status = 'nr'
        self.save()
        return

    def __str__(self):
        return self.firm.firm_name + " " + str(self.pk) + " " + str(self.dateUpdate)

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.date = timezone.now()
        self.dateUpdate = timezone.now()
        return super(Report, self).save(*args, **kwargs)
