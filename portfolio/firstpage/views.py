from django.shortcuts import render,redirect
from .models import *
from django.utils.timezone import now

# Create your views here.
def success(request):
    return render(request, 'firstpage/success.html')
def index(request):
    if request.method == "POST":
        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone_number')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        contact_us.objects.create(
            full_name=full_name,
            email=email,
            phone_number=phone_number,
            subject=subject,
            message=message
        )
        return redirect ('success')
    return render(request, 'firstpage/index.html')

def orderform(request):
    if request.method =='POST':
        customer_name = request.POST.get('customer_name')
        customer_email = request.POST.get('customer_email')
        ordertype = request.POST.get('ordertype')
        description = request.POST.get('description')


        orders.objects.create(
            customer_name=customer_name,
            customer_email=customer_email,
            ordertype=ordertype,
            description=description,
            order_date = now().date()

        )
        return redirect ('success')
    return render(request, 'firstpage/order.html')


def videos(request):
    return render(request, 'firstpage/video_editing.html')