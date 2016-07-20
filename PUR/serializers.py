from rest_framework import serializers
from PUR.models import County, Permit, Pesticide, Zone, Profile, Firm, Report

class CountySerializer(serializers.Serializer):
    county_name = serializers.CharField(required=True, allow_blank=False, max_length=30)
    county_number = serializers.CharField(required=True, allow_blank=False, max_length=30)

    def create(self, validated_data):
        return County.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.county_name = validated_data.get('county_name', instance.county_name)
        instance.county_number = validated_data.get('county_number', instance.county_number)
        instance.save()
        return instance

class PermitSerializer(serializers.ModelSerializer):
    firm = serializers.StringRelatedField(many=False, read_only=True)
    contacts = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = Permit
        fields = ('permit_name', 'permit_agent', 'permit_num', 'permit_type',
                  'permit_city', 'permit_state', 'permit_add', 'permit_zip',
                  'permit_county', 'permit_issue', 'permit_expiration'
                  'firm', 'contacts')

class PesticideSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pesticide
        fields = ('pesticide_name', 'pesticide_id', 'active', 'manufacturer',
                  'manuAddress', 'dateEntered')

class ZoneSerializer(serializers.ModelSerializer):

    firm = serializers.StringRelatedField(many=False, read_only=True)

    class Meta:
        model = Zone
        fields = ('zone_name', 'zone_id', 'zone_section', 'zone_township_dir', 'zone_range',
                  'zone_bm', 'zone_commodity', 'firm')

class ProfileSerializer(serializers.ModelSerializer):
    User = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = Profile
        fields = ('User', 'Grower', 'Couny', 'Manager', 'Worker')


class FirmSerializer(serializers.ModelSerializer):
    pesticides = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = Firm
        fields = ('firm_name', 'firm_address', 'firm_city', 'firm_zip',
                  'firm_phone', 'firm_id', 'firm_email', 'pesticides')

class ReportSerializer(serializers.ModelSerializer):
    firm = serializers.StringRelatedField(many=False, read_only = True)
    permit = serializers.StringRelatedField(many=False, read_only=True)
    zones = serializers.StringRelatedField(many=True, read_only=True)
    pesticides = serializers.StringRelatedField(many=True, read_only=True)
    creator = serializers.StringRelatedField(many=False, read_only=True)
    reviewer = serializers.StringRelatedField(many=False, read_only=True)

    class Meta:
        model = Report
        fields = ('firm', 'pesticdes', 'permit', 'zones',
                  'date', 'time_of_application',
                  'number_of_applications', 'method_of_application',
                  'total_application', 'block_id', 'status',
                  'dateUpdate', 'creator', 'reviewer',)