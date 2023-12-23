from django.shortcuts import render
from .models import *

def index(request):
    view_MainPagePics = MainPagePics.objects.all()
    view_MainViewPage = MainViewPage.objects.get(id = 1)
    view_SocialMediaLinks = SocialMediaLinks.objects.all()
    view_contactus = ContactUs.objects.all()
    view_Services = Services.objects.all()
    view_AboutUS = AboutUS.objects.get(id = 1)
    index_context = { 'html_MainPagePics':view_MainPagePics,
                    'html_MainViewPage':view_MainViewPage,
                    'html_SocialMediaLinks':view_SocialMediaLinks,
                    'html_contactus':view_contactus,
                    'html_Services':view_Services,
                    'html_AboutUS':view_AboutUS }
    
    return render(request,'main_app/index.html',index_context)



def contact_Us(request):
    if request.method == "POST":
        username = request.POST.get('username')
        user_email = request.POST.get('user_email')
        subject = request.POST.get('subject')
        messageBody = request.POST.get('messageBody')
        phone = request.POST.get('phone')
        data = ContactUs(username=username,
                    user_email=user_email,
                    subject=subject,
                    messageBody=messageBody,
                    phone=phone,
                    )
        data.save()

    return render(request,'main_app/contact_us.html')



























# view_MainViewPage = MainViewPage.objects.all()
# view_AboutViewPage = AboutUS.objects.get(id = 1)
# 'html_AboutViewPage':view_AboutViewPage,

# def company(request):
#     return render(request,'sidalmain/company.html',{})


    # if request.method == "POST":
    #     form=ContactForm(request.POST)
    #     if form.is_valid():
    #         print("form is valid")




# def example(request):
#     # Query Set
#     x10 = Examples.objects.all()
#     y0 = {'exa' : x10.order_by('name')}
#     y5 = {'exa' : str(x10.count())}
#     y6 = {'exa' : x10.exclude(price = 10)}
#     y7 = {'exa' : x10.exclude(category = 'phone')}
#     y8 = {'exa' : x10.filter(name__exact = 'i phone')}
#     y9 = {'exa' : x10.filter(price__exact = 10)}
#     o1 = {'exa' : x10.filter(name__contains = 'i phone')}
#     o2 = {'exa' : x10.filter(price__in=[10, 100, 500])}
#     o3 = {'exa' : x10.filter(name__range=(10, 500))}
        
#     x1 = Examples.objects.get(name='some_exampl')
#     x2 = Examples.objects.get(id=1)
#     x3 = Examples.objects.filter(category='phone')
#     x4 = Examples.objects.all()
    
#     return None



# image on html =>     <img src= " {{ x10.image.url }} "  alt="">   
# affffter creating new object


###########################################################################

# <form method='POST'>
#     {% csrf_token %}
#     <input type='text' name='username' placeholder='username'>
#     <input type='password' name='passwrd' placeholder='password'>
#     <input type='submit' value='save'>
# </form>

# class Login(models.Model):
#     username = forms.CharField(max_length=50)
#     password = forms.CharField(widget=forms.PasswordInput())

# from .models import Login

# def login(request):
#     username = request.POST.get('username')
#     password = request.POST.get('password')

#     data = Login(username =username ,password = password)
#     data.save()



























####################################################################################

# forms.py  File
#_________________

# from django import forms
# class LoginForm(forms.Form):
#     username = forms.CharField(max_length=50)
#     pasword = forms.CharField(max_length=50)





# views.py File
# ______________

# from .forms import LoginForm

# def Login(request):
#     username = request.POST.get('username')
#     password = request.POST.get('password')

#     data = Login(username =username ,password = password)
#     data.save()
#     return render(request,'flan.html',{'loginnform':LoginForm})



# html file form
# <form method='POST'>
#     {% csrf_token %}
#     {{loginnform}}
#     <input type='submit' value='save'>
# </form>



















