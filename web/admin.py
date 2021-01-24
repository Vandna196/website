from django.contrib import admin
from .models import Menu,Header,Service,Feature,Feature_highlight,Pricing,Single_testimonial,Award,Question,Team,Icon,Project,Project_image,Amazing_feature,Testimonial,Benefit,Message_form,Contact,Footer_icon,Left_data,Left_image,Subscriber
# Register your models here.
class MenuAdmin(admin.ModelAdmin):
    list_display = ('link','heading','subheading','isactive')
    fieldsets = [
        (None,{
            'fields':(
                'link','heading','subheading','isactive')})]
admin.site.register(Menu, MenuAdmin)
class HeaderAdmin(admin.ModelAdmin):
    list_display = ('brand','text','link')
    fieldsets = [
        (None,{
            'fields':(
                'brand','text','link')})]
admin.site.register(Header,HeaderAdmin)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('img','title','data','link','isactive')
    fieldsets = [
        (None,{
            'fields':(
                'img','title','data','link','isactive')})]
admin.site.register(Service,ServiceAdmin)
class FeatureAdmin(admin.ModelAdmin):
    list_display = ('icon','heading','data','isactive')
    fieldsets = [
        (None,{
            'fields':(
                'icon','heading','data','isactive')})]
admin.site.register(Feature,FeatureAdmin)
class Feature_hightlightAdmin(admin.ModelAdmin):
    list_display = ('img','heading','data','isactive')
    fieldsets = [
        (None,{
            'fields':(
                'img','heading','data','isactive')})]
admin.site.register(Feature_highlight,Feature_hightlightAdmin)
class PricingAdmin(admin.ModelAdmin):
    list_display = ('title','price','duration','link','text','texta','textb','isactive')
    fieldsets = [
        (None,{
            'fields':(
                'title','price','duration','link','text','texta','textb','isactive')})]
admin.site.register(Pricing,PricingAdmin)
class Single_testimonialAdmin(admin.ModelAdmin):
    list_display = ('quote','img','name','profile','isactive')
    fieldsets = [
        (None,{
            'fields':(
                'quote','img','name','profile','isactive')})]
admin.site.register(Single_testimonial,Single_testimonialAdmin)
class AwardAdmin(admin.ModelAdmin):
    list_display = ('img','isactive')
    fieldsets = [
        (None,{
            'fields':(
                'img','isactive')})]
admin.site.register(Award,AwardAdmin)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('heading','data','isactive')
    fieldsets = [
        (None,{
            'fields':(
                'heading','data','isactive')})]
admin.site.register(Question,QuestionAdmin)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('img','name','profile','data','isactive')
    fieldsets = [
        (None,{
            'fields':(
                'img','name','profile','data','isactive')})]
admin.site.register(Team,TeamAdmin)
class IconAdmin(admin.ModelAdmin):
    list_display = ('link','name','clas','isactive')
    fieldsets = [
        (None,{
            'fields':(
                'link','name','clas','isactive')})]
admin.site.register(Icon,IconAdmin)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('img','isactive')
    fieldsets = [
        (None,{
            'fields':(
                'img','isactive')})]
admin.site.register(Project,ProjectAdmin)
class Project_imageAdmin(admin.ModelAdmin):
    list_display = ('img','isactive')
    fieldsets = [
        (None,{
            'fields':(
                'img','isactive')})]
admin.site.register(Project_image,Project_imageAdmin)
class Amazing_featureAdmin(admin.ModelAdmin):
    list_display = ('name','heading','data','isactive')
    fieldsets = [
        (None,{
            'fields':(
                'name','heading','data','isactive')})]
admin.site.register(Amazing_feature, Amazing_featureAdmin)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('img','data','name','profile','isactive')
    fieldsets = [
        (None,{
            'fields':(
                'img','data','name','profile','isactive')})]
admin.site.register(Testimonial,TestimonialAdmin)
class BenefitAdmin(admin.ModelAdmin):
    list_display = ('heading','data','text','img','isactive')
    fieldsets = [
        (None,{
            'fields':(
                'heading','data','text','img','isactive')})]
admin.site.register(Benefit,BenefitAdmin)
class Message_formAdmin(admin.ModelAdmin):
    list_display = ('full_name','email_address','phone_number','message')
    fieldsets = [
        (None,{
            'fields':(
                'full_name','email_address','phone_number','message')})]
admin.site.register(Message_form,Message_formAdmin)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('icon','text','isactive')
    fieldsets = [
        (None,{
            'fields':(
                'icon','text','isactive')})]
admin.site.register(Contact,ContactAdmin)
class Footer_iconAdmin(admin.ModelAdmin):
    list_display = ('name','isactive')
    fieldsets = [
        (None,{
            'fields':(
                'name','isactive')})]
admin.site.register(Footer_icon,Footer_iconAdmin)
class Left_imageAdmin(admin.ModelAdmin):
    list_display = ('img','text','image','heading','imagea','data','isactive')
    fieldsets = [
        (None,{
            'fields':(
                'img','text','image','heading','imagea','data','isactive')})]
admin.site.register(Left_image,Left_imageAdmin)
class Left_dataAdmin(admin.ModelAdmin):
    list_display = ('heading','text','office','copyrigh','isactive')
    fieldsets = [
        (None,{
            'fields':(
                'heading','text','office','copyrigh','isactive')})]
admin.site.register(Left_data,Left_dataAdmin)
class SubscriberAdmin(admin.ModelAdmin):
    list_display = ('email_address','isactive')
    fieldsets = [
        (None,{
            'fields':(
                'email_address','isactive')})]
admin.site.register(Subscriber,SubscriberAdmin)

#admin header and title modification
admin.site.site_header = "Admin DashBoard"
admin.site.site_title = "Django Admin site"
admin.site.index_title = ''