from django.shortcuts import render
from .models import *

def company(request):
    view_LatestNews = LatestNews.objects.all()
    view_OurBranches = OurBranches.objects.all()
    view_OurTechnologies = OurTechnologies.objects.all()
    view_Catalogue = Catalogue.objects.all()
    company_context = { 'html_LatestNews':view_LatestNews,
                        'html_OurBranches':view_OurBranches,
                        'html_OurTechnologies':view_OurTechnologies,
                        'html_Catalogue':view_Catalogue}
   
    return render(request,'company_app/cmpny_app.html',company_context)