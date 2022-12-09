from django.shortcuts import render
from Adoration.models import Testimonial, Contact, Customer, Package
from django.core.mail import send_mail
# Create your views here.





def Main(request):
    if request.method == 'POST':
        if request.POST.get('type') == 'Quote':
            name = request.POST['name']
            email = request.POST['email']
            phone = request.POST['phone']
            package = request.POST['package']
            Message_to_send = f'Hello {name},\n\nThank you for contacting us. We will get back to you as soon as possible. Be sure you provided the proper information.\n\nName: {name}\nPhone: {phone}\nEmail: {email}\n\nRegards,\nAdoration Team'
            customer = Customer(name=name,email=email,phone=phone,package=package)
            customer.save()
            send_mail(
                "Adoration Holidays",
                Message_to_send, #Message to send
                'info@adorationholidays.com',# from email
                [email,], # to email
                fail_silently=False,
            )
            customer.recieved_email = True
            customer.save()
            return render(request,'index.html',{'message':'Message Sent Successfully'})
        elif request.POST.get('type') == 'contact':
            name = request.POST['name']
            email = request.POST['email']
            phone = request.POST['phone']
            message = request.POST['message']
            Message_to_send = f'Hello {name},\n\nThank you for contacting us. We will get back to you as soon as possible. Be sure you provided the proper information.\n\nName: {name}\nPhone: {phone}\nEmail: {email}\n\nRegards,\nAdoration Team'
            contact = Contact(name=name,email=email,message=message,phone=phone)
            contact.save()
            send_mail(
                "Adoration Holidays",
                Message_to_send, #Message to send
                'info@adorationholidays.com',# from email
                [email,], # to email
                fail_silently=False,
            )
            contact.recieved_email = True
            contact.save()
            return render(request,'index.html',{'message':'Message Sent Successfully'})
    packages = Package.objects.all()
    tests = Testimonial.objects.all()
    extras = {"tests":tests, "packages":packages}
    print()
    return render(request,'index.html',extras)


def packageDetails(request, package):
    if request.method == 'POST':
            name = request.POST['name']
            email = request.POST['email']
            phone = request.POST['phone']
            package = request.POST['package']
            Message_to_send = f'Hello {name},\n\nThank you for contacting us. We will get back to you as soon as possible. Be sure you provided the proper information.\n\nName: {name}\nPhone: {phone}\nEmail: {email}\n\nRegards,\nAdoration Team'
            customer = Customer(name=name,email=email,phone=phone,package=package)
            customer.save()
            send_mail(
                "Adoration Holidays",
                Message_to_send, #Message to send
                'info@adorationholidays.com',# from email
                [email,], # to email
                fail_silently=False,
            )
            customer.recieved_email = True
            customer.save()
            return render(request,'index.html',{'message':'Message Sent Successfully'})
    package = Package.objects.get(name=package)
    extras = {"package":package}
    print(package.inclusions.all())
    return render(request,'product.html', extras)


# error pages
def handler404(request,exception):
    errorCode = exception.__class__.__name__
    return render(request,'errors/404page.html',{"err-code":errorCode})

def handler500(request):
    return render(request,'errors/500page.html')    

def handler403(request,exception):
    errorCode = exception.__class__.__name__
    return render(request,'errors/403page.html',{"err-code":errorCode})

def handler400(request,exception):
    errorCode = exception.__class__.__name__
    return render(request,'errors/400page.html',{"err-code":errorCode})
