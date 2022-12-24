from django.shortcuts import render
from Adoration.models import Testimonial, Contact, Customer, Package
from django.core.mail import send_mail
# Create your views here.


def Main(request):
    packages = Package.objects.all()
    tests = Testimonial.objects.all()
    extras = {"tests":tests, "packages":packages}
    if request.method == 'POST':
        if request.POST.get('type') == 'Quote':
            name = request.POST.get('name','-------')
            email = request.POST.get('email','------')
            phone = request.POST.get('phone','-------')
            package = request.POST.get('package','--------')
            Message_to_send = f'Hello {name},\n\nThank you for contacting us. We will get back to you as soon as possible. Be sure you provided the proper information.\n\nName: {name}\nPhone: {phone}\nEmail: {email}\n\nRegards,\nAdoration Team'
            customer = Customer(name=name,email=email,phone=phone,package=package)
            customer.save()
            send_mail(
                "Adoration Holidays",
                Message_to_send, #Message to send
                'info@adorationholidays.com',# from email
                [email,'adorationholidays@gmail.com'], # to email
                fail_silently=False,
            )
            customer.recieved_email = True
            customer.save()
            return render(request,'index.html',extras)
        elif request.POST.get('type') == 'contact':
            name = request.POST.get('name','-------')
            email = request.POST.get('email','------')
            phone = request.POST.get('phone','-------')
            message = request.POST.get('message','--------')
            Message_to_send = f'Hello {name},\n\nThank you for contacting us. We will get back to you as soon as possible. Be sure you provided the proper information.\n\nName: {name}\nPhone: {phone}\nEmail: {email}\n\nRegards,\nAdoration Team'
            contact = Contact(name=name,email=email,message=message,phone=phone)
            contact.save()
            send_mail(
                "Adoration Holidays",
                Message_to_send, #Message to send
                'info@adorationholidays.com',# from email
                [email,'info@adorationholidays.com','adorationholidays@gmail.com'], # to email
                fail_silently=False,
            )
            contact.recieved_email = True
            contact.save()
            return render(request,'index.html',extras)
    print()
    return render(request,'index.html',extras)


def packageDetails(request, pk):
    packages = Package.objects.all()
    package = Package.objects.get(pk=pk)
    extras = {"package":package,"packages":packages}
    if request.method == 'POST':
            name = request.POST.get('name','-------')
            email = request.POST.get('email','------')
            phone = request.POST.get('phone','-------')
            package = request.POST.get('package','--------')
            Message_to_send = f'Hello {name},\n\nThank you for contacting us. We will get back to you as soon as possible. Be sure you provided the proper information.\n\nName: {name}\nPhone: {phone}\nEmail: {email}\n\nRegards,\nAdoration Team'
            customer = Customer(name=name,email=email,phone=phone,package=package)
            customer.save()
            send_mail(
                "Adoration Holidays",
                Message_to_send, #Message to send
                'info@adorationholidays.com',# from email
                [email,'adorationholidays@gmail.com'], # to email
                fail_silently=False,
            )
            customer.recieved_email = True
            customer.save()
            return render(request,'index.html',extras)
    print(package.inclusions.all())
    return render(request,'product.html', extras)


def SiteMap(request):
    return render(request, 'sitemap.xml')

# error pages
def handler404(request,exception):
    errorCode = exception.__class__.__name__
    return render(request,'errors/404.html',{"err-code":errorCode})

def handler500(request):
    return render(request,'errors/500page.html')    

def handler403(request,exception):
    errorCode = exception.__class__.__name__
    return render(request,'errors/403page.html',{"err-code":errorCode})

def handler400(request,exception):
    errorCode = exception.__class__.__name__
    return render(request,'errors/400page.html',{"err-code":errorCode})
