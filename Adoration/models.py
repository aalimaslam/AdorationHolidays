from django.db import models
from django.urls import reverse
# Create your models here.





class Testimonial(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')
    description = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    message = models.TextField(max_length=500)
    phone = models.CharField(max_length=100)
    recieved_email = models.BooleanField(default=False)
    Resolved = models.BooleanField(default=False)
    def __str__(self):
        return self.name
    
    

class Customer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=100)
    package = models.CharField(max_length=100)
    recieved_email = models.BooleanField(default=False)
    Resolved = models.BooleanField(default=False)
    def __str__(self):
        return self.name
    
    
    
    

class Package(models.Model):
    name = models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    time = models.CharField(max_length=100, default='1 Day')
    image = models.ImageField(upload_to='images/')
    day_descriptions = models.ManyToManyField('PackageDetails', related_name='day_descriptions')
    inclusions = models.ManyToManyField('inclusion', related_name='inclusions')
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('package_detail', args = [str(self.id)])

class PackageDetails(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    def __str__(self):
        return self.title

class inclusion(models.Model):
    title = models.CharField(max_length=100)
    def __str__(self):
        return self.title
