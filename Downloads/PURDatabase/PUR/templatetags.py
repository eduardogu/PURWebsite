from PUR.models import Firm
from django import template
register = template.Library()

@register.inclusion_tag('Create/report_form.html')
def firm_site_select():
    firm_list = Firm.objects.all()
    return {'firm_list': firm_list}