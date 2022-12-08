from django.contrib import admin

# Register your models here.


from django.contrib.auth.models import Group
# import user
from django.contrib.auth.models import User
from Adoration.models import Testimonial, Contact, Customer
# Register your models here.

admin.site.unregister(Group)
admin.site.unregister(User)
admin.site.register(Testimonial)
admin.site.register(Contact)
admin.site.register(Customer)


# change the admin site title
admin.site.site_header = "Adoration Admin"
admin.site.site_title = "Adoration Admin Portal"
admin.site.index_title = "Welcome to Adoration Admin Portal"


