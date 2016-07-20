"""PURDatabase URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from PUR import views
from django.contrib import admin

urlpatterns = [
    #***********************************************************REST-API*********************************************************************#
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    #Permits
    url(r'^Permits/$', views.PermitList.as_view()),
    url(r'^Permits/(?P<pk>[0-9]+)$', views.PermitDetail.as_view()),
    #Pesticides
    url(r'^Pesticides/$', views.PesticideList.as_view()),
    url(r'^Pesticides/(?P<pk>[0-9]+)$', views.PesticideDetail.as_view()),
    #Counties
    url(r'^Counties/$', views.CountyList.as_view()),
    url(r'^Counties/(?P<pk>[0-9]+)$', views.CountyDetail.as_view()),
    #Zones
    url(r'^Zone/$', views.ZoneList.as_view()),
    url(r'^Zone/(?P<pk>[0-9]+)$', views.ZoneDetail.as_view()),
    #Profiles
    url(r'^Profiles/$', views.ProfileList.as_view()),
    url(r'^Profiles/(?P<pk>[0-9]+)/$', views.ProfileDetail.as_view()),
    #Firms
    url(r'^Firms/$', views.FirmList.as_view()),
    url(r'^Firms/(?P<pk>[0-9]+)$', views.FirmDetail.as_view()),
    url(r'^firm/(?P<firm_num>[0-9]+)/json_sites', views.firmSites),
    #Commodity
    url(r'^Commodities/$', views.CommodityList.as_view()),
    url(r'^Commodities/(?P<pk>[0-9]+)$', views.CommodityDetail.as_view()),
    #Contacts
    url(r'^Contacts/$', views.ContactList.as_view()),
    url(r'^Contacts/(?P<pk>[0-9]+)$', views.ContactDetail.as_view()),
    #Reports
    url(r'^ReportList/$', views.ReportList.as_view()),
    #**************************************************WEB APP**************************************************#
    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/$', views.LoginView),
    url(r'^invalid/$', views.InvalidView),
    url(r'^logout/$', views.logoutView),
    url(r'^authenticate/$', views.AuthView),
    url(r'^home/$', views.HomeView.as_view()),

    url(r'^reportList/$', views.ReportsView.as_view()),
    url(r'^reportList/(?P<report_num>[0-9]+)/$', views.SpecificReportView.as_view()),
    url(r'^reportList/(?P<report_num>[0-9]+)/delete/$', views.deleteReport),
    url(r'^reportList/(?P<report_num>[0-9]+)/update/$', views.updateReport),
    url(r'^reportList/create/$', views.ReportCreate.as_view()),
    url(r'^reportList/(?P<report_num>[0-9]+)/reject/$', views.rejectReport),
    url(r'^reportList/(?P<report_num>[0-9]+)/approve/$', views.approveReport),

    url(r'^permitList/$', views.PermitsView.as_view()),
    url(r'^permitList/(?P<permit_num>[0-9]+)/$', views.SpecificPermitView.as_view()),
    url(r'^permitList/(?P<permit_num>[0-9]+)/delete/$', views.deletePermit),
    url(r'^permitList/(?P<permit_num>[0-9]+)/update/$', views.updatePermit),
    url(r'^permitList/create/$', views.createPermit),

    url(r'^siteList/$', views.SitesView.as_view()),
    url(r'^siteList/(?P<pk>[0-9]+)/$', views.SpecificSiteView.as_view()),
    url(r'^siteList/(?P<pk>[0-9]+)/delete/$', views.deleteSite),
    url(r'^siteList/(?P<pk>[0-9]+)/update/$', views.updateSite),
    url(r'^siteList/create/$', views.createSite),

    url(r'^pesticideList/$', views.PesticidesView.as_view()),
    url(r'^pesticideList/(?P<pk>[0-9]+)/$', views.SpecificPesticideView.as_view()),
    url(r'^pesticideList/(?P<pk>[0-9]+)/delete/$', views.deletePesticide),
    url(r'^pesticideList/(?P<pk>[0-9]+)/update/$', views.updatePesticide),
    url(r'^pesticideList/create/$', views.createPesticide),

    url(r'^firmList/$', views.FirmsView.as_view()),
    url(r'^firmList/(?P<firm_id>[0-9]+)/$', views.SpecificFirmView.as_view()),
    url(r'^firmList/(?P<firm_id>[0-9]+)/delete/$', views.deleteFirm),
    url(r'^firmList/(?P<firm_id>[0-9]+)/update/$', views.updateFirm),

    url(r'^firmList/create/$', views.createFirm),
    #url(r'^firmList/(?P<firm_num>[0-9]+)/firmUpdate/$', views.updateFirm),
]
urlpatterns = format_suffix_patterns(urlpatterns)
