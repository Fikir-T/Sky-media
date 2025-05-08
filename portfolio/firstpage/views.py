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

# def ethiocal(request):
#     if request.method == 'POST':
#         weekdays = ['ሰኞ', 'ማክሰኞ', 'ረቡዕ', 'ሐሙስ', 'ዓርብ', 'ቅዳሜ', 'እሑድ']

#         year = int(request.POST.get('year'))
#         month = int(request.POST.get('month'))
#         day = int(request.POST.get('day'))

#         # Calculate the Ethiopian Julian Day Number
#         julian = 1723856 + 365 * year + (year // 4) + 30 * month + day - 31

#         # Get weekday from Julian number (0 = Monday)
#         weekday_index = julian % 7
#         weekday_name = weekdays[weekday_index]

#         context = {
#             'year': year,
#             'month': month,
#             'day': day,
#             'julian': julian,
#             'weekday': weekday_name
#         }

#         return render(request, 'firstpage/ethiocal.html', context)

#     # If not POST request, just render empty form
#     return render(request, 'firstpage/ethiocal.html')


def ethiocal(request):
    if request.method == 'POST':
        weekdays = ['ሰኞ', 'ማክሰኞ', 'ረቡዕ', 'ሐሙስ', 'ዓርብ', 'ቅዳሜ', 'እሑድ']
        year = int(request.POST.get('year'))
        month = int(request.POST.get('month'))
        day = int(request.POST.get('day'))
        julian =  1723856 + 365 * year + (year // 4) + 30 * month + day - 31
        weekday = julian % 7
        weekday_name =  weekdays[weekday]
        return render(request, 'firstpage/ethiocal.html', {'year': year, 'month': month, 'day': day, 'julian': julian, 'weekday': weekday_name})
    return render(request, 'firstpage/ethiocal.html')