from django.shortcuts import render,redirect,get_object_or_404,HttpResponseRedirect
from .models import Menu,Header,Service,Feature,Feature_highlight,Pricing,Single_testimonial,Award,Question,Team,Icon,Project,Project_image,Amazing_feature,Testimonial,Benefit,Message_form,Contact,Footer_icon,Left_image,Left_data,Subscriber
from .forms import Form,Newform
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from django.views.generic import View
# Create your views here.
def index(request):#to access all the tables in template
    menu = Menu.objects.all()
    header = Header.objects.all()
    service = Service.objects.all()
    feature = Feature.objects.all()
    feature_highlight = Feature_highlight.objects.all()
    pricing = Pricing.objects.all()
    single_testimonial = Single_testimonial.objects.all()
    award = Award.objects.all()
    question  = Question.objects.all()
    team = Team.objects.all()
    icon = Icon.objects.all()
    project = Project.objects.all()
    project_image = Project_image.objects.all()
    amazing_feature = Amazing_feature.objects.all()
    testimonial = Testimonial.objects.all()
    benefit = Benefit.objects.all()
    form = Form()
    contact = Contact.objects.all()
    footer_icon = Footer_icon.objects.all()
    left_image = Left_image.objects.all()
    left_data = Left_data.objects.all()
    message_form = Message_form.objects.all()
    
    context = {
        'menus':menu,
        'headers':header,
        'services':service,
        'features':feature,
        'feature_highlights':feature_highlight,
        'pricings':pricing,
        'single_testimonial':single_testimonial,
        'awards':award,
        'questions':question,
        'teams':team,
        'icons':icon,
        'projects':project,
        'images':project_image,
        'amazing_features':amazing_feature,
        'testimonials':testimonial,
        'benefits':benefit,
        'form':form,
        'contacts':contact,
        'footer_icons':footer_icon,
        'left_images':left_image,
        'left_datas':left_data,
        'message_forms':message_form
                
        }
    return render(request,"web/index.html",context)


def contact_form(request):#for posting data 
    form = Form(request.POST)
    if form.is_valid():
        print('heellllllllloooooo in form validation')
        full_name = form.cleaned_data.get('full_name')
        email_address = form.cleaned_data.get('email_address')
        phone_number = form.cleaned_data.get('phone_number')
        message = form.cleaned_data.get('message')
        message_form = Message_form(
        full_name = full_name,
        email_address = email_address,
        phone_number = phone_number,
        message = message)
        message_form.save()
    return redirect("/")
def news_letter(request):#for posting method
    form = Newform(request.POST)
    if form.is_valid():
        email_address = form.cleaned_data.get('email_address')
        subscriber = Subscriber(
        email_address = email_address)
        subscriber.save()
    return redirect("/")
  
    