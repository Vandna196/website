from django.db import models
from django.conf import settings
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.
class Header(models.Model):
  brand = models.CharField(max_length=255)
  text = models.CharField(max_length=255)
  link = models.CharField(max_length=255)
  def __str__(self):
      return self.text
    
class Menu(models.Model):
  link = models.CharField(max_length=255)
  title = models.CharField(max_length=255)
  heading = models.CharField(max_length=255)
  subheading = models.CharField(max_length=255)
  isactive = models.BooleanField()
  def __str__(self):
      return self.title
class Service(models.Model):
  img = models.ImageField(upload_to = 'images/')
  title = models.CharField(max_length=255)
  data = models.CharField(max_length=255)
  link = models.CharField(max_length=255)
  text = models.CharField(max_length=255)
  isactive = models.BooleanField()
  def __str__(self):
      return self.title
class Feature(models.Model):
  icon = models.CharField(max_length=255)
  heading = models.CharField(max_length=255)
  data = models.CharField(max_length=255)
  isactive = models.BooleanField()
  def __str__(self):
      return self.data
class Feature_highlight(models.Model):
  img = models.ImageField(upload_to = 'images/')
  heading = models.CharField(max_length=255)
  data = RichTextUploadingField()
  isactive = models.BooleanField()
  def __str__(self):
      return self.data
class Pricing(models.Model):
  title = models.CharField(max_length=255)
  price = models.IntegerField()
  duration = models.CharField(max_length=255)
  link = models.CharField(max_length=255)
  text = models.CharField(max_length=255)
  texta = models.CharField(max_length=255)
  textb = models.CharField(max_length=255)
  isactive = models.BooleanField()
  def __str__(self):
      return self.title
class Single_testimonial(models.Model):
  quote = models.TextField(max_length=255)
  name = models.CharField(max_length=255)
  profile = models.CharField(max_length=255)
  img = models.ImageField(upload_to = 'images/')
  isactive = models.BooleanField()
  def __str__(self):
      return self.quote
class Award(models.Model):
  img = models.ImageField(upload_to = 'images/')
  isactive = models.BooleanField()
class Question(models.Model):
  heading = models.CharField(max_length=255)
  data = models.TextField(max_length=255)
  isactive = models.BooleanField()
  def __str__(self):
      return self.data
class Team(models.Model):
  img = models.ImageField(upload_to = 'images/')
  name = models.CharField(max_length=255)
  profile = models.CharField(max_length=255)
  data = models.TextField(max_length=255)
  isactive = models.BooleanField()
  def __str__(self):
      return self.data
class Icon(models.Model):
  link = models.CharField(max_length=255)
  name = models.CharField(max_length=255)
  clas = models.CharField(max_length=255)
  isactive = models.BooleanField()
  def __str__(self):
      return self.name
class Project(models.Model):
  img = models.ImageField(upload_to = 'images/')
  isactive = models.BooleanField()
class Project_image(models.Model):
  img = models.ImageField(upload_to = 'images/')
  isactive = models.BooleanField()
class Amazing_feature(models.Model):
  name = models.CharField(max_length=255)
  heading = models.CharField(max_length=255)
  data = models.CharField(max_length=255)
  isactive = models.BooleanField()
  def __str__(self):
      return self.data
class Testimonial(models.Model):
  img = models.ImageField(upload_to = 'images/')
  data = models.TextField(max_length=255)
  name = models.CharField(max_length=255)
  profile = models.CharField(max_length=255)
  isactive = models.BooleanField()
  def __str__(self):
      return self.data
class Benefit(models.Model):
  heading = models.CharField(max_length=255)
  data = models.TextField(max_length=255)
  text = models.TextField(max_length=255)
  img = models.ImageField(upload_to = 'images/')
  isactive = models.BooleanField()
  def __str__(self):
      return self.data
class Message_form(models.Model):
    full_name = models.CharField(max_length=255)
    email_address = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=255)
    message = models.TextField(max_length=255)
    def __str_(self):
        return self.full_name
class Contact(models.Model):
  icon = models.CharField(max_length=255)
  text = models.TextField(max_length=255)
  isactive = models.BooleanField()
  def __str__(self):
      return self.text
class Footer_icon(models.Model):
  name = models.CharField(max_length=255)
  isactive = models.BooleanField()
  def __str__(self):
      return self.name
class Left_image(models.Model): 
  img = models.ImageField(upload_to = 'images/')
  text = models.TextField(max_length=255)
  image = models.ImageField(upload_to = 'images/')
  heading = models.CharField(max_length=255)
  imagea = models.ImageField(upload_to = 'images/')
  data = models.TextField(max_length=255)
  isactive = models.BooleanField()
  def __str__(self):
      return self.data
class Left_data(models.Model): 
  heading = models.CharField(max_length=255)
  text = models.TextField(max_length=255)
  office = models.TextField(max_length=255)
  copyrigh = models.TextField(max_length=255)
  isactive = models.BooleanField()
  def __str__(self):
      return self.office
class Subscriber(models.Model): 
  email_address = models.CharField(max_length=255)
  isactive = models.BooleanField(default=True)
 
