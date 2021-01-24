from django.urls import path
from .import views
from .views import *
urlpatterns = [
    path("",views.index,name="index"),
    path("contact_form",views.contact_form, name="contact_form"),
    path("news_letter",views.news_letter, name="news_letter")
    
    ]

