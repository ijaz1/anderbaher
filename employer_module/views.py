import datetime as dt
from time import strftime, time
from django.shortcuts import redirect, render
from datetime import datetime, date, timedelta
from admin_module.models import employerDetails
from django.contrib import messages
from django.http import JsonResponse

from employer_module.models import workStatus

# Create your views here.


def fnEmployerHome(request):
    employer_id = request.session['employer']
    obj_employer_details = employerDetails.objects.get(id=employer_id)
    context = {'employer': obj_employer_details}
    return render(request, 'employerHome.html', context)


def fnEmployerLogOut(request):
    del request.session['employer']
    return redirect('index')


def fnYour_profile(request):
    employer_id = request.session['employer']
    obj_get_employer_details = employerDetails.objects.get(id=employer_id)
    context = {'employer_details': obj_get_employer_details}
    return render(request, 'profile.html', context)


def fnEdit_employer_profile(request):
    if request.method == 'POST':
        first_Name = request.POST['first_Name']
        last_Name = request.POST['last_Name']
        personal_Email = request.POST['personal_Email']
        phone_Number = request.POST['phone_Number']
        address = request.POST['address']
        gender = request.POST['options']
        photo = request.FILES['employer_photo']
        employer_id = request.POST['employer_id']
        employerDetails.objects.filter(id=employer_id).update(first_Name=first_Name, last_Name=last_Name,
                                                              personal_Email=personal_Email, phone_Number=phone_Number, address=address, gender=gender, photo=photo)
        messages.success(request, 'Employer Profile Updated Succesfully')
        return redirect('your_profile')
    else:
        messages.success(request, 'something went wrong')
        return redirect('your_profile')


def work_start(request):
    if request.method == 'POST':
        employer_id = request.session['employer']
        employer = employerDetails.objects.get(id=employer_id)
        current_date = date.today()
        current_time = datetime.now().time().strftime("%I:%M %p")
        print('**old time** ', current_time)
        now = dt.datetime.now()
        delta = dt.timedelta(hours = 8)
        t = now.time()
        a=(dt.datetime.combine(dt.date(1,1,1),t) + delta).time()
        print('qqq',a,'qqq')
        p=a.strftime("%I:%M %p")
        workStatus(employer=employer,current_date=current_date,current_time=t,end_time=a).save()
        return JsonResponse({'start':'Your work started'})

def onLoad(request):
    print('****')
    employer_id=request.session['employer']
    print('****',employer_id)
    obj_work_status=workStatus.objects.get(employer_id=employer_id)
    convert_starting_time=obj_work_status.current_time
    current_time=convert_starting_time.strftime("%I:%M %p")
    print('$$$$',current_time)
    convert_end_time=obj_work_status.end_time
    end_time=convert_end_time.strftime("%I:%M %p")
    print('&&&&',end_time)
    obj_fetch_data=[{'id':obj_work_status.id,'current_date':obj_work_status.current_date,'current_time':current_time,'end_time':end_time}]
    return JsonResponse({'work_data':obj_fetch_data})
