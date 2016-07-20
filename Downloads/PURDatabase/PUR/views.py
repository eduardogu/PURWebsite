from PUR.models import Pesticide, Permit, County, Firm, Zone, Profile, Report, Commodity, Contact
from rest_framework.views import APIView
from rest_framework import permissions
from PUR.serializers import PesticideSerializer, PermitSerializer, CountySerializer, CommoditySerializer
from PUR.serializers import ProfileSerializer, ReportSerializer, FirmSerializer, ZoneSerializer, ContactSerializer
from rest_framework import generics
from django.views.generic import TemplateView, DetailView, ListView
from django.views.generic.edit import FormView, CreateView
from django.core.context_processors import csrf
from django.shortcuts import render_to_response, render, get_object_or_404
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, Http404, HttpResponse
from django.core import serializers

#********************REST_API_VIEWS***************************#

class PesticideList(generics.ListCreateAPIView):
    queryset = Pesticide.objects.all()
    serializer_class = PesticideSerializer

class PesticideDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = Pesticide.objects.all()
    serializer_class = PesticideSerializer

class PermitList(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = Permit.objects.all()
    serializer_class = PermitSerializer

class PermitDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = Permit.objects.all()
    serializer_class = PermitSerializer

class CountyList(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = County.objects.all()
    serializer_class = CountySerializer

class CountyDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = County.objects.all()
    serializer_class = CountySerializer

class ZoneList(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = Zone.objects.all()
    serializer_class = ZoneSerializer

class ZoneDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = Zone.objects.all()
    serializer_class = ZoneSerializer

class ProfileList(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

class ProfileDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

class FirmList(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = Firm.objects.all()
    serializer_class = FirmSerializer

class FirmDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = Firm.objects.all()
    serializer_class = FirmSerializer

class CommodityList(generics.ListCreateAPIView):
    permission_class = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = Commodity.objects.all()
    serializer_class = CommoditySerializer

class CommodityDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_class = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = Commodity.objects.all()
    serializers_class = CommoditySerializer

class ContactList(generics.ListCreateAPIView):
    permission_class = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

class ContactDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_class = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer



class ReportList(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = Report.objects.all()
    serializer_class = ReportSerializer

class ReportDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = Report.objects.all()
    serializer_class = ReportSerializer

#**********************WEBSITE_VIEWS*********************************#
#Authentication
def LoginView(request):
    c = {}
    c.update(csrf(request))
    return render_to_response('login.html', c)

def AuthView(request):
    username = request.POST.get("username", '')
    password = request.POST.get("password", '')
    user = authenticate(username=username, password=password)

    if user is not None:
        login(request, user)
        return HttpResponseRedirect("/home/")
    else:
        return HttpResponseRedirect("/invalid/")

def InvalidView(request):
    return HttpResponseRedirect("/login/")

def logoutView(request):
    auth.logout(request)
    return HttpResponseRedirect('/login/')

#Home
class HomeView(TemplateView):
    template_name = "home.html"

    def reportsPending(self):
        return Report.objects.all().filter(status="sb").order_by('dateUpdate')[:5]

    def reportsReviewed(self):
        otherList = []
        list = Report.objects.all().filter(status="re").order_by('dateUpdate')
        for report in list:
            if report.reviewer.user == self.request.user:
                otherList.append(report)
            if len(otherList) >= 5:
                break
        return otherList

    def reportsSubmitted(self):
        otherList = []
        list = Report.objects.all().filter(status="ap").order_by('dateUpdate')
        for report in list:
            if report.reviewer.user == self.request.user:
                otherList.append(report)
            if len(otherList) >= 5:
                break
        return otherList

    def reportsOnHold(self):
        otherList = []
        list = Report.objects.all().filter(status="nr").order_by('dateUpdate')
        for report in list:
            if report.reviewer.user == self.request.user:
                otherList.append(report)
            if len(otherList) >= 5:
                break
        return otherList


class ReportsView(ListView):
    model = Report
    template_name = "Lists/reportList.html"
    paginate_by = 30

    def listSize(self):
        return len(Report.objects.all())

class SpecificReportView(DetailView):
    model = Report
    template_name = 'Specifics/reportSpecific.html'
    context_object_name = 'report'

    def get_object(self):
        return get_object_or_404(Report, pk=self.kwargs['report_num'])

    def getZone(self):
        report = Report.objects.get(pk=self.kwargs['report_num'])
        list = report.zones.all()
        return list[0]

    def getPesticide(self):
        report = Report.objects.get(pk=self.kwargs['report_num'])
        list = report.pesticides.all()
        return list[0]

class ReportCreate(CreateView):
    model = Report
    fields = ['firm']
    template_name = 'Create/report_form.html'

    def getFirms(self):
        return Firm.objects.all()
    def getSites(self):
        return Zone.objects.all()
    def getPesticides(self):
        return Pesticide.objects.all()[:10]
    def getPermits(self):
        return Permit.objects.all()

def firmSites(request, firm_num):
    currentFirm = Firm.objects.get(pk=firm_num)
    firm_zones = currentFirm.zone_set.all()
    json_models = serializers.serialize("json", firm_zones)
    return HttpResponse(json_models, content_type="application/javascript")

def deleteReport(request):
    return Http404

def updateReport(request):
    return Http404

def approveReport(request, report_num):
    report = Report.objects.get(pk=report_num)
    report.approve()
    report.reviewer = Profile.objects.get(user=request.user)
    report.save()
    return HttpResponseRedirect("/reportList/" + report_num + "/")

def rejectReport(request, report_num):
    report = Report.objects.get(pk=report_num)
    report.revision()
    report.reviewer = Profile.objects.get(user=request.user)
    report.save()
    return HttpResponseRedirect("/reportList/" + report_num + "/")


class FirmsView(ListView):
    model = Firm
    template_name = "Lists/firmList.html"
    paginate_by = 30

    def listSize(self):
        return len(Firm.objects.all())

class SpecificFirmView(DetailView):
    model = Firm
    template_name = 'specifics/firmSpecific.html'
    context_object_name = 'firm'

    def get_object(self):
        return get_object_or_404(Firm, firm_id=self.kwargs['firm_id'])

    def firmReports(self):
        firm = Firm.objects.get(firm_id=self.kwargs['firm_id'])
        return firm.report_set.all().order_by('dateUpdate')

    def firmSites(self):
        firm = Firm.objects.get(firm_id=self.kwargs['firm_id'])
        return firm.zone_set.all().order_by('zone_id')

    def firmPermit(self):
        firm = Firm.objects.get(firm_id=self.kwargs['firm_id'])
        return firm.permit_set.all()

def createFirm(request):
    c = {}
    c.update(csrf(request))
    return render_to_response('createFirm.html', c)

def updateFirm(request):
    return Http404

def deleteFirm(request):
    return Http404


class PermitsView(ListView):
    model = Permit
    template_name = "Lists/permitList.html"
    paginate_by = 30

    def listSize(self):
        return len(Permit.objects.all())

class SpecificPermitView(DetailView):
    model = Permit
    template_name = 'Specifics/permitSpecific.html'
    context_object_name = 'permit'

    def get_object(self):
        return get_object_or_404(Permit, permit_num=self.kwargs['permit_num'])

def createPermit(request):
    return Http404("Under construction")

def updatePermit(request):
    return Http404("Under construction")

def deletePermit(request):
    return Http404("Under construction")


class SitesView(ListView):
    model = Zone
    template_name = "Lists/zoneList.html"
    paginate_by = 30
    queryset = Zone.objects.order_by('zone_name')

class SpecificSiteView(DetailView):
    model = Zone
    template_name = 'Specifics/siteSpecific.html'
    context_object_name = 'zone'

    def get_object(self):
        return get_object_or_404(Zone, pk=self.kwargs['pk'])

def createSite(request):
    Http404("Under Construction")

def updateSite(request):
    Http404("under construction")

def deleteSite(request):
    Http404("Under Construction")


class PesticidesView(ListView):
    model = Pesticide
    paginate_by = 30
    template_name = 'Lists/pesticideList.html'

class SpecificPesticideView(DetailView):
    model = Pesticide
    template_name = 'Specifics/pesticideSpecific.html'
    context_object_name = 'pesticide'

    def get_object(self):
        return get_object_or_404(Pesticide, pk=self.kwargs['pk'])

def createPesticide(request):
    return Http404("Under Construction")

def updatePesticide(request):
    return Http404("Under Construction")

def deletePesticide(request):
    return Http404("Under construction")


