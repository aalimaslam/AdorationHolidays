from django.shortcuts import render
from Adoration.models import Testimonial, Contact
from django.core.mail import send_mail
# Create your views here.





def Main(request):
    if request.method == 'POST':
        f_name = request.POST['f_name']
        l_name = request.POST['l_name']
        name = f_name + " " + l_name
        email = request.POST['email']
        message = request.POST['message']
        phone = request.POST['phone']
        contact = Contact(name=name,email=email,message=message,phone=phone)
        contact.save()
        print(contact)
        Message_to_send = f'Hello {f_name},\n\nThank you for contacting us. We will get back to you as soon as possible. Be sure you provided the proper information.\n\nName: {name}\nPhone: {phone}\nEmail: {email}\n\nRegards,\nAdoration Team'
        send_mail(
            "Adoration Holidays",
            Message_to_send, #Message to send
            'info@adorationholidays.com',# from email
            [email,], # to email
            fail_silently=False,
        )
        contact.recieved_email = True
        print("recireved email")
        print(contact)
        print(contact.recieved_email)
        contact.save()
        print("saved")
        return render(request,'index.html',{'message':'Message Sent Successfully'})

    tests = Testimonial.objects.all()
    extras = {"tests":tests}
    return render(request,'index.html',extras)



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