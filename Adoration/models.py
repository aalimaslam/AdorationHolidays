from django.db import models

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